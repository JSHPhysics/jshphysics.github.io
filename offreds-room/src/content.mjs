// Everything the page says about the room lives here.
// The drawing, the panel, the chips, the readout and the playback all read from this one file.
//
// Wording rule: the page never reproduces passages from the novel.
// It tells students where to look and asks them to find and copy the words themselves.

// The chapters a class can set the page to, in reading order.
export const CHAPTERS = [2, 9, 10, 29];

// One entry per thing in the room.
// "layers" are in reading order: each one unlocks when the class has reached that chapter.
export const OBJECTS = [
  {
    id: "chair",
    name: "The chair",
    layers: [
      {
        chapter: 2,
        discuss: "The chapter opens by listing three plain pieces of furniture and nothing else. Before any feeling or event is mentioned, what impression does a bare list like that give you of the room and of the person describing it?",
        find: "Chapter 2, the first sentence. Copy it exactly, with its punctuation.",
        closer: [
          "The sentence has no verb. What is missing from a room where nothing happens in the sentence that describes it?",
          "Why might Atwood begin with the things Offred is given, before the things that have been taken away?",
          "A chair is for sitting and waiting. Keep a tally of how often Offred waits in this room as you read on.",
        ],
        zoom: "Look at the section titles of the novel. How many of them are about waiting, resting or night?",
      },
    ],
  },
  {
    id: "table",
    name: "The table",
    layers: [
      {
        chapter: 2,
        discuss: "The narrator names the table and moves straight on. What do you usually keep on a bedroom table that a Handmaid would not be allowed to have?",
        find: "Chapter 2, first sentence again. Where does the table come in the list, and does she ever return to it?",
        closer: [
          "Handmaids are forbidden to read or write. How does that change what a table is for?",
          "She gives the table no detail at all, yet she comments at length on the rug. What decides how much attention an object gets from this narrator?",
        ],
        zoom: "Find out what Gilead allows women to read. Then look at the signs on the shops in chapter 5.",
      },
    ],
  },
  {
    id: "lamp",
    name: "The lamp",
    layers: [
      {
        chapter: 2,
        discuss: "A lamp is the one light she lists. A different light fitting has been taken out of this room. Why might a regime allow one kind of light and remove another?",
        find: "Chapter 2, opening paragraph. Find the sentence that says what has been removed. What reason does it imply?",
        closer: [
          "Compare the lamp with the missing light fitting. From the regime's point of view, what is the difference between them?",
          "She says who removed things with a single pronoun. Which pronoun, and why doesn't she name them?",
        ],
        zoom: "Track every use of that pronoun in chapter 2. Who does she mean by it?",
      },
    ],
  },
  {
    id: "ceiling",
    name: "The ceiling wreath",
    layers: [
      {
        chapter: 2,
        discuss: "Look up. There is a plaster wreath on the ceiling and its centre has been filled in and smoothed over. What do you think used to be there, and why would someone take it away?",
        find: "Chapter 2, opening paragraph. Find the simile she uses for the blank space in the middle of the wreath.",
        closer: [
          "The simile turns the ceiling into a face. What has happened to that face? What does that suggest about how she sees the room, or how the room sees her?",
          "A wreath can stand for celebration or for mourning. Which reading fits this ceiling?",
          "Switch the model to 'What was removed'. Does seeing the fitting change how you read the opening paragraph?",
        ],
        zoom: "Start a list of every eye in the novel, and of every time someone is watched. This one goes first.",
      },
      {
        chapter: 29,
        discuss: "In chapter 29 Offred asks the Commander what became of the Handmaid who had this room before her. What clues has this ceiling been giving you since chapter 2?",
        find: "Chapter 29, the end of the conversation in the study. Find the Commander's answer, and what he says was done about the light fitting afterwards.",
        closer: [
          "Reread the opening paragraph of chapter 2. Which phrases now carry a second meaning?",
          "In chapter 2 Offred already knew why the fitting had gone, and she did not dwell on it. Find where she tells us she is trying not to think. Why does the narrator hold back what she knows?",
          "What does Offred realise about why the Commander has been inviting her to the study?",
        ],
        zoom: "Atwood plants the answer 27 chapters before the question is asked. How does chapter 2 read the second time?",
      },
    ],
  },
  {
    id: "window",
    name: "The window and curtains",
    layers: [
      {
        chapter: 2,
        discuss: "The window opens only a little way and the glass cannot be broken. What do you think the authorities are afraid of?",
        find: "Chapter 2. Find where she says what they are not afraid of, and the phrase she uses for what they are afraid of.",
        closer: [
          "She says it is not running away they fear. Why is the other kind of escape a particular threat to Gilead? Think about what a Handmaid is for.",
          "Two white curtains move when the air comes in. Why include a detail that gentle in a paragraph about confinement?",
          "The glass keeps her safe and it keeps her in. Which of those is it there for?",
        ],
        zoom: "Compare with Aunt Lydia on the two kinds of freedom in chapter 5. Which kind is this window?",
      },
    ],
  },
  {
    id: "windowseat",
    name: "The window seat and cushion",
    layers: [
      {
        chapter: 2,
        discuss: "Under the window there is a seat with one small cushion. A window seat is made for looking out. What can Offred do with what she sees from it, and what can she not do?",
        find: "Chapter 2. Find the short sentence that mentions the window seat. How much does she tell us about the cushion at this point?",
        closer: [
          "In chapter 2 the cushion is only 'little'. She is holding something back about it. Make a note to come back here after chapter 10.",
          "Sitting at a window and watching is one of the few things she is free to do. Is watching a form of power in this novel?",
        ],
        zoom: "Who watches whom in Gilead? Add the window seat to your list of eyes.",
      },
      {
        chapter: 10,
        discuss: "In chapter 10 she finally tells us what is stitched on the cushion: a single word, FAITH. Why is one embroidered word remarkable in this house?",
        find: "Chapter 10. Find what she says about being given this to read, and what she wonders happened to the cushions that once went with it.",
        closer: [
          "She is forbidden to read, and here is a word. Is looking at the cushion a small act of rebellion, or exactly what the regime intends?",
          "Faith was once one of a set of three. Which two words are missing from her room, and why does it matter that those are the two that have gone?",
          "She can spend a long time looking at one word. What does that tell you about her life before?",
        ],
        zoom: "Collect every act of reading or writing in the novel. So far you have the cushion and the cupboard.",
      },
    ],
  },
  {
    id: "floor",
    name: "The floor and the sunlight",
    layers: [
      {
        chapter: 2,
        discuss: "Sunlight falls on a polished wooden floor and she can smell the polish. Why would a place of confinement be made to look and smell pleasant?",
        find: "Chapter 2. Find the sentence about the sunlight and the floor. Which senses does she use?",
        closer: [
          "Somebody polishes this floor. Who does the housework in the Commander's house, and what colour do they wear?",
          "List every sense used in chapter 2. Which sense is used least, and what might that tell you?",
          "The room is clean and sunny. Does that make her situation better or worse?",
        ],
        zoom: "Gilead keeps its houses comfortable. Find other places in the novel where comfort is used to control people.",
      },
    ],
  },
  {
    id: "rug",
    name: "The rug",
    layers: [
      {
        chapter: 2,
        discuss: "The rug is an oval, braided by hand out of rags. What might a regime like Gilead find to admire in a handmade object like that?",
        find: "Chapter 2. Find where she explains the kind of touch 'they' like. Then find the two sayings that follow, and the question she ends on.",
        closer: [
          "She describes the rug as women's work made from things nobody needs any more. Who else in Gilead is valued only for their use?",
          "She turns a proverb about waste into a question about wanting. What does the double meaning of 'want' do here?",
          "She gives the rug more commentary than the chair, the table and the lamp put together. Why does the rug get so much?",
        ],
        zoom: "'Traditional values' was a political slogan in the 1980s, when Atwood was writing. Find out who used it.",
      },
    ],
  },
  {
    id: "picture",
    name: "The picture",
    layers: [
      {
        chapter: 2,
        discuss: "On the wall is a framed print of flowers, and the frame has no glass in it. Why would anyone take the glass out of a picture frame?",
        find: "Chapter 2. Find the flower and its colour. Then find the two-word question she asks about whether every Handmaid has the same room.",
        closer: [
          "She says flowers are 'still allowed'. What does the word 'still' imply about everything else?",
          "Aunt Lydia compares this life to being in the army. If that is right, what kind of room is this?",
          "She comes back to this picture later in the chapter to explain the missing glass. Why does she describe it first and explain it afterwards?",
        ],
        zoom: "Flowers keep coming back in this novel. Start a tracker with these irises, then add Serena Joy's garden when you reach it.",
      },
    ],
  },
  {
    id: "bed",
    name: "The bed",
    layers: [
      {
        chapter: 2,
        discuss: "A single bed with a white cover. She tells us that only one thing takes place in it. What does it suggest that she feels the need to say so?",
        find: "Chapter 2. Find her remark about what takes place in the bed, and the short correction she adds straight after it.",
        closer: [
          "The bed is single, with a white cover and a medium-hard mattress. Which parts of an adult life have been kept out of this room?",
          "The correction after the semicolon is typical of this narrator. Find two more places in chapter 2 where she revises what she has just said.",
          "She says she tries not to think too much. Why would thinking be dangerous?",
        ],
        zoom: "The Ceremony does not happen in this room. When you reach chapter 16, ask why it matters where it takes place.",
      },
    ],
  },
  {
    id: "gloves",
    name: "The red gloves",
    layers: [
      {
        chapter: 2,
        discuss: "A pair of red gloves lies on the bed. Everything she wears is red apart from the white wings around her face. What does red make you think of?",
        find: "Chapter 2. Find what she says red is the colour of, and the verb she uses for what it does to the Handmaids.",
        closer: [
          "List three things red can stand for. Which does Gilead intend, and which does Offred feel?",
          "The wings stop her from seeing and from being seen. Link them to the window that only opens partly.",
          "The gloves are the only strong colour in this drawing. What is the only strong colour in the room she describes?",
        ],
        zoom: "Gilead sorts women by colour. Find the colours worn by Wives, Marthas, Aunts and Econowives.",
      },
    ],
  },
  {
    id: "door",
    name: "The door",
    layers: [
      {
        chapter: 2,
        discuss: "The door of this room is not locked. In fact it will not even shut properly. Is that a kind of freedom?",
        find: "Chapter 2. Find the word she refuses to use about this room, and the reason she gives.",
        closer: [
          "A door that will not shut lets her out. Who else does it let in?",
          "She refuses a single small word. Why does a pronoun matter so much to her? Come back at chapter 9 and see whether she still refuses it.",
          "Outside, on the hall wall, hangs the one mirror she passes. Find the simile she uses for it and what she sees of herself.",
        ],
        zoom: "Bentham's panopticon was a prison designed so that inmates behave because they might be watched at any moment. Look it up and decide whether it fits this house.",
      },
    ],
  },
  {
    id: "cupboard",
    name: "The cupboard",
    layers: [
      {
        chapter: 2,
        unmentioned: true,
        discuss: "Offred walks us round the whole room in chapter 2 and never mentions the cupboard. Why might a narrator leave something out of a description?",
        find: "Chapter 2. Check for yourself: read the chapter again and list every object she names. Is the cupboard there?",
        closer: [
          "She chose what to describe. What does this gap tell you about treating her inventory as complete?",
          "Run the narrator's-eye playback. Which other parts of the room does her attention pass over?",
        ],
        zoom: "Keep a list of things Offred tells us late, or tells us twice in different ways.",
      },
      {
        chapter: 9,
        discuss: "In chapter 9 Offred searches the room slowly, one section at a time, and in the cupboard she finds something left by the woman who lived here before her. If you were that woman, what would you leave for the next person?",
        find: "Chapter 9. Find where in the cupboard the message is, what she thinks it was written with, and copy the message exactly.",
        closer: [
          "She cannot translate it, yet it pleases her. Why does a message you cannot read still count as a message?",
          "The regime approves of the rug, which is women's handiwork put on show. The message is women's writing, and it is hidden. Why does one count as acceptable and the other not?",
          "Chapter 9 opens with her using the word she refused in chapter 2. What has changed?",
        ],
        zoom: "Atwood uses the word 'palimpsest' in chapter 1. Look it up, then list the traces of earlier people that this room keeps.",
      },
      {
        chapter: 29,
        discuss: "In chapter 29 Offred asks the Commander what the scratched words mean. Who do you now think the message was written for?",
        find: "Chapter 29. Find the Commander's translation, and where he says the phrase comes from.",
        closer: [
          "The phrase turns out to be a schoolboy joke that belonged to the Commander. Is it still a message of resistance now you know that?",
          "How did the woman before her come to know those words? What does that tell Offred about her own evenings in the study?",
        ],
        zoom: "Who in this novel is allowed to play with words?",
      },
    ],
  },
  {
    id: "clock",
    name: "The missing clock",
    absent: true,
    layers: [
      {
        chapter: 2,
        discuss: "There is no clock in this room. A bell somewhere in the house tells her the time. What changes for a person when someone else keeps the time?",
        find: "Chapter 2. Find the sentence about the bell, and the kind of place she compares this house to.",
        closer: [
          "She does not choose when to get up, eat or go out. List the things in chapter 2 that are decided for her.",
          "The clock is in the drawing because an ordinary bedroom would have one. The novel does not say a clock was taken away. What does the text tell us, and what are we assuming?",
        ],
        zoom: "Track how Offred tells the time across the novel. Start with the bell.",
      },
    ],
  },
  {
    id: "mirror",
    name: "The missing mirror",
    absent: true,
    layers: [
      {
        chapter: 2,
        discuss: "There is no mirror in this room, and very few in the house. What does a person lose when they can no longer see themselves?",
        find: "Chapter 2. Find the comparison to a nunnery, and the two things she says a nunnery and this house have in common.",
        closer: [
          "Vanity is one reason to remove a mirror. Look again at what has been done to the picture and the window. What other reason is there?",
          "The mirror is in the drawing because an ordinary bedroom would have one. The text only tells us mirrors are few. Why is it worth separating what the text states from what we infer?",
          "When she does see herself, in the hall, how does she describe the figure in the glass?",
        ],
        zoom: "Offred is not her real name. Track the ways the regime takes away a person's sense of who they are.",
      },
    ],
  },
];

// The order in which the narrator's attention moves in chapter 2.
// "object" is the thing that lights up. A step with no object is something she hears or does.
export const TOUR = [
  { object: "chair", say: "She starts with a chair." },
  { object: "table", say: "Then a table." },
  { object: "lamp", say: "Then a lamp. Three nouns and no verb." },
  { object: "ceiling", say: "Her eyes go up to the plaster wreath and its blank centre." },
  { object: "window", say: "She looks across to the window and its two white curtains." },
  { object: "windowseat", say: "Her eyes drop to the window seat and its little cushion." },
  { object: "floor", say: "Sunlight falls on the polished floor, and she can smell the polish." },
  { object: "rug", say: "She lingers on the braided rug and comments on it." },
  { object: "picture", say: "Her eyes go up to the picture, flowers in a frame with no glass." },
  { object: "bed", say: "Next is the single bed, where she says only one thing takes place." },
  { object: "picture", say: "She goes back to the picture and explains the missing glass." },
  { object: "window", say: "She goes back to the window and explains why it barely opens." },
  { object: null, say: "A bell rings. Bells mark the time in this house." },
  { object: "gloves", say: "She stands. Her red gloves are lying on the bed." },
  { object: "door", say: "She leaves by a door that does not lock, or even shut." },
];

// What the model does when a chapter button is pressed.
// Each chapter is a short list of beats. A beat moves the camera to "focus" (object ids, or null for
// the whole room), shows "say" under the model and waits "hold" milliseconds before the next beat.
// "light: true" lets the missing light fitting show for that beat.
export const SCENES = {
  2: [{ focus: null, say: "Chapter 2. This is the room as she first describes it.", hold: 2600 }],
  9: [
    {
      focus: ["cupboard"],
      say: "Chapter 9. She searches the room and opens the cupboard. Something is scratched on its floor.",
      hold: 6200,
    },
  ],
  10: [{ focus: ["windowseat"], say: "Chapter 10. She tells us the word stitched on the cushion.", hold: 4800 }],
  29: [
    { focus: ["cupboard"], say: "Chapter 29. She asks the Commander what the scratched words mean.", hold: 4600 },
    {
      focus: ["ceiling"],
      say: "He also tells her what used to hang from this ceiling, and why it was taken down.",
      hold: 5600,
      light: true,
    },
  ],
};

// Shown when a chapter's beats have finished.
export const SCENE_END = "The objects outlined in red have new questions. Click one.";

// The three views of the room. "line" shows under the model when the view is chosen.
// "heading", "about" and "questions" fill the panel while no object is selected.
export const VIEWS = {
  ordinary: {
    label: "An ordinary bedroom",
    readout: "an ordinary bedroom",
    line: "The dashed objects are things a bedroom usually has. None of them is in Offred's room.",
    heading: "An ordinary bedroom",
    about: "The dashed objects are a ceiling light, a mirror, glass in the picture frame, a window that opens wide, a clock, family photographs, books and paper, a plant, scatter cushions and a key in the door. They are here for comparison. The novel does not list them.",
    questions: [
      "Sort the dashed objects into three groups: comforts, luxuries, and things that make a room your own. Which group has she lost most of?",
      "She is left a bed, a chair, a table and a rug. Why would a regime keep those and leave out a book or a photograph?",
      "Nothing here shows who lives in this room. What does it do to a person to live somewhere with no trace of themselves?",
      "How does taking away small comforts make someone easier to control?",
    ],
  },
  now: {
    label: "Offred's room",
    readout: "Offred's room",
    line: "This is what Offred's room contains.",
  },
  removed: {
    label: "What was removed",
    readout: "what was removed",
    line: "Chapter 2 says one thing was taken out of this room: the light fitting.",
    heading: "What was removed",
    about: "Most of what an ordinary bedroom has was never given to her. Chapter 2 names one thing that was there and was taken out: the light fitting in the middle of the ceiling wreath.",
    questions: [
      "Find the sentence that says so. Who does she say removed it, and what else did they remove?",
      "Later in the chapter she says she knows why the picture has no glass. Does the glass belong in this view too? Argue it both ways.",
      "Is there a difference between having something taken away and never being given it? Which is worse for her?",
    ],
  },
};
