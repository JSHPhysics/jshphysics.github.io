#!/usr/bin/env python3
"""Intervention codes and encrypted student plans.

A student's plan is never committed as readable HTML. It is encrypted with a key
made from the student's code, and stored under a file name that is also made from
the code, so the repository holds only unreadable files with meaningless names.

Usage:
  python3 intervention/tools/intervention.py new-code
      Print one new random code. Keep codes OUT of this repository.

  python3 intervention/tools/intervention.py encrypt <plan.html> <CODE>
      Write intervention/data/<id>.enc for that code and print the file name.

  python3 intervention/tools/intervention.py check <plan.html> <CODE>
      Decrypt the stored file for that code and confirm it matches the plan.

The four constants below must match intervention/index.html exactly.
"""
import hashlib
import os
import re
import secrets
import sys

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

SALT_TEXT = "jshphysics-intervention-v1"
ITERATIONS = 600000
CODE_LENGTH = 12
# No I, O, 0 or 1, so a code cannot be misread when it is written down.
ALPHABET = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
# The plan page's own localStorage key; each student gets their own so two plans never share saved answers.
PLAN_STORE_KEY = '"physics-plan-v1"'


def normalise(raw):
    """Upper case, letters and digits only (dashes and spaces are for reading)."""
    return re.sub(r"[^A-Z0-9]", "", raw.upper())


def new_code():
    """Twelve random characters, shown in three groups of four."""
    characters = []
    for _ in range(CODE_LENGTH):
        characters.append(secrets.choice(ALPHABET))
    joined = "".join(characters)
    return joined[0:4] + "-" + joined[4:8] + "-" + joined[8:12]


def derive(code):
    """Return (file id, AES key) for a code, the same way the web page does."""
    clean = normalise(code)
    if len(clean) != CODE_LENGTH:
        raise SystemExit("A code must have %d letters and numbers." % CODE_LENGTH)
    material = hashlib.pbkdf2_hmac("sha256", clean.encode("utf-8"), SALT_TEXT.encode("utf-8"), ITERATIONS, dklen=48)
    file_id = material[0:16].hex()
    key = material[16:48]
    return file_id, key


def prepare(html, file_id):
    """Give the plan its own storage key so saved answers stay with this student."""
    count = html.count(PLAN_STORE_KEY)
    if count != 1:
        raise SystemExit("Expected the plan's storage key exactly once, found %d." % count)
    return html.replace(PLAN_STORE_KEY, '"jsh-plan-' + file_id[0:12] + '"')


def encrypt(plan_path, code):
    file_id, key = derive(code)
    with open(plan_path, "r", encoding="utf-8") as handle:
        html = handle.read()
    prepared = prepare(html, file_id)
    iv = secrets.token_bytes(12)
    ciphertext = AESGCM(key).encrypt(iv, prepared.encode("utf-8"), None)
    os.makedirs(DATA_DIR, exist_ok=True)
    out_path = os.path.join(DATA_DIR, file_id + ".enc")
    with open(out_path, "wb") as handle:
        handle.write(iv + ciphertext)
    print("wrote", os.path.relpath(out_path), "(%d KB)" % (os.path.getsize(out_path) // 1024))


def check(plan_path, code):
    file_id, key = derive(code)
    path = os.path.join(DATA_DIR, file_id + ".enc")
    with open(path, "rb") as handle:
        blob = handle.read()
    plain = AESGCM(key).decrypt(blob[0:12], blob[12:], None).decode("utf-8")
    with open(plan_path, "r", encoding="utf-8") as handle:
        expected = prepare(handle.read(), file_id)
    if plain != expected:
        raise SystemExit("MISMATCH: the stored file does not decrypt to this plan.")
    print("ok: the stored file decrypts to this plan")


def main():
    if len(sys.argv) == 2 and sys.argv[1] == "new-code":
        print(new_code())
        return
    if len(sys.argv) == 4 and sys.argv[1] == "encrypt":
        encrypt(sys.argv[2], sys.argv[3])
        return
    if len(sys.argv) == 4 and sys.argv[1] == "check":
        check(sys.argv[2], sys.argv[3])
        return
    print(__doc__)


if __name__ == "__main__":
    main()
