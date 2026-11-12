// ---------------- Touch screens (iPad in landscape) ----------------

// A finger swiping up or down scrolls the page, so it cannot also tilt a model.
// Each 3D figure therefore gets two round buttons that tilt it instead.
// tiltBy(step) is given the change in elevation, in degrees.
function addTiltButtons(stage, tiltBy) {
  const holder = document.createElement("div");
  holder.className = "hd-tilt";
  const choices = [
    { label: "Tilt the model up", mark: "▲", step: 8 },
    { label: "Tilt the model down", mark: "▼", step: -8 },
  ];
  for (const choice of choices) {
    const button = document.createElement("button");
    button.type = "button";
    button.setAttribute("aria-label", choice.label);
    button.textContent = choice.mark;
    // A press on the button must not start a drag of the model underneath it.
    button.addEventListener("pointerdown", (event) => {
      event.stopPropagation();
    });
    // Keys pressed on the button belong to the button, not to the figure's own shortcuts.
    button.addEventListener("keydown", (event) => {
      event.stopPropagation();
    });
    button.addEventListener("click", () => {
      tiltBy(choice.step);
    });
    holder.appendChild(button);
  }
  stage.appendChild(holder);
}

// Shrink the drawings in one figure card until the whole card (drawing and controls) fits on screen.
function fitPlate(plate, available) {
  const drawings = Array.from(plate.querySelectorAll(".iso-svg"));
  // Start from the natural size.
  for (const drawing of drawings) {
    drawing.style.maxHeight = "";
  }
  if (plate.offsetHeight <= available) {
    return;
  }
  const natural = drawings.map((drawing) => drawing.getBoundingClientRect().height);
  const apply = (scale) => {
    drawings.forEach((drawing, index) => {
      drawing.style.maxHeight = Math.round(natural[index] * scale) + "px";
    });
  };
  // Search for the largest scale that fits. Never go below 45%, or the labels become unreadable.
  let fits = 0.45;
  let tooBig = 1;
  for (let round = 0; round < 7; round += 1) {
    const middle = (fits + tooBig) / 2;
    apply(middle);
    if (plate.offsetHeight <= available) {
      fits = middle;
    } else {
      tooBig = middle;
    }
  }
  apply(fits);
}

function fitAllPlates() {
  const plates = document.querySelectorAll(".iso-plate");
  // Phones stack everything in a narrow column, where the cards are already short.
  const wideEnough = window.innerWidth >= 700;
  const available = window.innerHeight - 12;
  for (const plate of plates) {
    if (wideEnough) {
      fitPlate(plate, available);
    } else {
      for (const drawing of plate.querySelectorAll(".iso-svg")) {
        drawing.style.maxHeight = "";
      }
    }
  }
}

{
  let waiting = false;
  const refit = () => {
    if (waiting) {
      return;
    }
    waiting = true;
    requestAnimationFrame(() => {
      waiting = false;
      fitAllPlates();
    });
  };
  window.addEventListener("resize", refit);
  window.addEventListener("orientationchange", refit);
  // Fonts arriving late change the height of the controls.
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(refit);
  }
  fitAllPlates();
}
