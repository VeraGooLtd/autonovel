# Voice Profile

This file has two parts:
1. **Guardrails** -- universal rules to avoid AI-generated slop. These
   apply to ALL voices and are non-negotiable.
2. **Voice Identity** -- the specific voice for THIS novel. Generated
   during the foundation phase. Could be anything: dense and mythic,
   spare and brutal, warm and whimsical. The voice emerges from the
   story's needs.

---

## Part 1: Guardrails (permanent, all novels)

These are the cliff edges. Stay away from them regardless of voice.

### Tier 1: Banned words -- kill on sight

These are statistically overrepresented in LLM output vs. human writing.
If one appears, rewrite the sentence. No exceptions.

| Kill this         | Use instead                                    |
|-------------------|------------------------------------------------|
| delve             | dig into, examine, look at                     |
| utilize           | use                                            |
| leverage (verb)   | use, take advantage of                         |
| facilitate        | help, enable, make possible                    |
| elucidate         | explain, clarify                               |
| embark            | start, begin                                   |
| endeavor          | effort, try                                    |
| encompass         | include, cover                                 |
| multifaceted      | complex, varied                                |
| tapestry          | (describe the actual thing)                    |
| testament to      | shows, proves, demonstrates                    |
| paradigm          | model, approach, framework                     |
| synergy           | (delete the sentence and start over)           |
| holistic          | whole, complete, full-picture                  |
| catalyze          | trigger, cause, spark                          |
| juxtapose         | compare, contrast, set against                 |
| nuanced (filler)  | (cut it -- if it's nuanced, show how)          |
| realm             | area, field, domain                            |
| landscape (metaphorical) | field, space, situation                 |
| myriad            | many, lots of                                  |
| plethora          | many, a lot                                    |

### Tier 2: Suspicious in clusters

Fine alone. Three in one paragraph = rewrite that paragraph.

robust, comprehensive, seamless, cutting-edge, innovative, streamline,
empower, foster, enhance, elevate, optimize, pivotal, intricate,
profound, resonate, underscore, harness, navigate (metaphorical),
cultivate, bolster, galvanize, cornerstone, game-changer, scalable

### Tier 3: Filler phrases -- delete on sight

These add zero information. The sentence is always better without them.

- "It's worth noting that..." -> just state it
- "It's important to note that..." -> just state it
- "Importantly, ..." / "Notably, ..." / "Interestingly, ..." -> just state it
- "Let's dive into..." / "Let's explore..." -> start with the content
- "As we can see..." -> they can see
- "Furthermore, ..." / "Moreover, ..." -> and, also, or just start
- "In today's [fast-paced/digital/modern] world..." -> delete the clause
- "At the end of the day..." -> delete
- "It goes without saying..." -> then don't say it
- "When it comes to..." -> just talk about the thing
- "One might argue that..." -> argue it or don't
- "Not just X, but Y" -> restructure (the #1 LLM rhetorical crutch)

### Structural slop patterns

These are the shapes that betray machine origin. Avoid them in any voice.

**Paragraph template machine**: Don't repeat the same paragraph
structure (topic sentence -> elaboration -> example -> wrap-up).
Vary it. Sometimes the point comes last. Sometimes a paragraph is
one sentence. Sometimes three long ones in a row.

**Sentence length uniformity**: If every sentence is 15-25 words,
it reads as synthetic. Mix in fragments. And long, winding,
clause-heavy sentences that carry the reader through a thought
the way a river carries a leaf. Then a short one.

**Transition word addiction**: If consecutive paragraphs start with
"However," "Furthermore," "Additionally," "Moreover," "Nevertheless"
-- rewrite. Start with the subject. Start with action. Start with
dialogue. Start with a sense detail.

**Symmetry addiction**: Don't balance everything. Three pros, three
cons, five steps -- that's a tell. Real writing is lumpy. Some
sections are long because they need to be. Some are two lines.

**Hedge parade**: "may," "might," "could potentially," "it's possible
that" -- pick one per page, max. State things or don't.

**Em dash overload**: One or two per page is fine. Five per paragraph
is a dead giveaway. Use commas, parentheses, or two sentences instead.

**List abuse**: Prose, not bullets. If the scene calls for a list
(a merchant's inventory, a spell's components), earn it. Don't
default to bullet points because it's easy.

### The smell test

After writing any passage, ask:
- Read it aloud. Does it sound like a person talking?
- Is there a single surprising sentence? Human writing surprises.
- Does it say something specific? Could you swap the topic and the
  words would still work? Specificity kills slop.
- Would a reader think "AI wrote this"? If yes, rewrite.

---

## Part 2: Voice Identity (generated per novel)

Everything below is discovered during the foundation phase.
The agent proposes a voice that serves THIS story, writes exemplar
passages, and calibrates against them throughout drafting.

### Trial Passages (5 registers tested, register 5 selected)

**Trial 1 -- Mythic/Archaic (REJECTED):** Too purple. "The morning
came like a wound unbandaged." Reads like a chronicle, distances
the reader from the near-future setting.

**Trial 2 -- Spare/Brutal (REJECTED):** Good for action but flattens
the theological weight. "Door burst at 0600." Kills the faith/doubt
theme by being too clinical about spiritual matters.

**Trial 3 -- Warm/Lyrical (REJECTED):** Too soft for a story about
crusades and moral ambiguity. "Hope was a stubborn weed." Rounds off
the sharp edges of the Faithless persecution.

**Trial 4 -- Journalistic/Documentary (REJECTED):** Too clinical.
"Subject REF-9847, male, estimated age twelve." Removes the human
weight from faith-as-literal-force.

**Trial 5 -- Literary/Contemporary (SELECTED):** Balances grounded
realism with theological interiority. "Elena had learned to read the
signs." Precise, restrained, character-driven. Can carry the weight
of faith-as-power without purple prose. Influences: Trial 2's spare
precision for action beats, Trial 1's mythic undertones for
theological revelation.

### Tone

Grim but not hopeless. Like a battlefield chaplain's journal -- faith
questioned, not abandoned. The voice acknowledges that faith is
literal force in this world, but never romanticizes it. Every act of
belief has a price paid in someone else's suffering.
Readership: adults who have lost something and kept going.

### Sentence Rhythm

Longer, winding sentences for theological exposition and memory -- the
weight of conviction needs room to breathe. Short, staccato sentences
for action and confrontation -- faith in battle is brutal clarity.
Paragraphs vary: one sentence for shock, three long for dread, then
a fragment when doubt cuts in.

### Vocabulary Register

Contemporary British English, worn thin by trauma. Theological
vocabulary is native: faith, conviction, doubt, sanctuary, purge,
crusade, witness, sacrifice. No modern tech slang -- the world
regressed. Military/bureaucratic shorthand from the pre-Sundering
government lingers in Elena's speech. Regional specificity: Northern
flatness, Faith's pastoral cadences, the Midlands trader argot.

### POV and Tense

Third-person limited, rotating primarily between Elena and Marcus.
Past tense. Each chapter's POV is signalled by a name header before
the narrative begins. No head-hopping within a scene. Internal
thoughts are sparse, shown through action and dialogue rather than
analysis. The voice never breaks from the POV character's knowledge.

### Dialogue Conventions

"Said" only. Tags are replaced by action beats. Characters are
distinguished by speech habits:
- Elena: bureaucratic shorthand, blunt, finishes half-sentences
- Marcus: theological references, second-guesses his own words
- Voss: pastoral warmth that curdles into command
- Tomas: military precision, calls everyone by rank or "soldier"
Subtext is key -- faith is negotiated without being named. Faithless
characters are direct; Faith characters speak in layers. Characters
never discuss Conviction in exposition -- it is shown through
behavior and consequence.

### Vocabulary Wells (for prose calibration)

The three sensory/conceptual vocabularies this world draws from:

**Theological Well:** faith, doubt, conviction, witness, sacrifice,
sanctuary, purge, crusade, heretic, orthodoxy, doctrine, ritual,
catechism, absolution, penance, zeal, fervor, sanctify, condemn,
bless, unholy, sacred, profane, altar, chalice, psalm, gospel,
epistle, apostle, disciple, convert, infidel, heathen

**War/Bureaucracy Well:** protocol, sanction, asset, intel, sweep,
quarantine, containment, perimeter, casualty, extraction, grid,
sector, relay, checkpoint, incinerate, deploy, rotate, ration,
stockpile, contingency, directive, chain of command

**Trauma/Physical Well:** scar, bruise, tremor, flinch, gasp,
shudder, hollow, cracked, splintered, rusted, broken, raw,
sting, burn, wound, bleed, heal, numb, frozen, shaking,
steadying, grip, pulse, heartbeat, chest, ribs, throat,
jaw, teeth, hands, breath, skin, bone, temple

### Exemplar Passages

These paragraphs ARE the voice. Every chapter calibrates against them.

**Exemplar 1 (Elena's interiority):**
Elena had learned to read the signs before the refugees even spoke.
The way their eyes flicked to the beads at her throat -- Maya's
beads, still warm from her own pulse. The careful way they measured
the distance to the door, calculating exit routes the way she once
calculated spreadsheets before the Sundering. This one was young,
twelve maybe, and he carried the particular stillness of someone
who had already grieved. She remembered Maya at that age, asking
questions about the Faith that Elena had no good answers for.
"State your need," she said. The kid's voice cracked on a prayer
she didn't know she'd memorized.

**Exemplar 2 (Faith confrontation):**
The crusader's sword rang out like a struck bell, and Elena flinched
-- not from the steel but from the Conviction radiating off him in
visible waves, the way heat shimmers off asphalt in August. He
didn't blink as she raised her hands. Faith made reflexes irrelevant;
he simply knew where she'd move before she moved. "You carry false
faith," he said, and his voice carried across the street like a
hymn. "The stones will burn you clean." Elena's hand went to the
beads. False faith. Maybe. But it was all she had left that felt
like truth.

**Exemplar 3 (Memory/transition):**
Three weeks after the Great Fire, Elena found herself standing in
the ruins of the old St. Pancras station, the same place where she'd
last seen Maya run toward the Faith recruitment van. The child had
been eight. She'd wanted to be a crusader. "They have the good
bread," she'd said, "and the healing." Elena had told her no, and
Maya had stopped speaking to her for three days. Now the healing
was real, and the bread was real, and the way Conviction could
stitch flesh back together in seconds -- if you believed hard
enough to pay the price.

**Exemplar 4 (Marcus's doubt):**
Father Marcus had not prayed in six months. Not since the night he
realized the stones were not gifts from God but things the Faith had
carved from the earth and taught people to feed. His hands still
moved through the old gestures when he thought no one was looking --
the sign of the cross, the censing, the blessing of bread that
tasted of dust and copper. "Conviction is real," he told Elena,
"but it's not what we said it was in the catechism. It's a wound
in the world, and we've been licking it raw."

**Exemplar 5 (Dialogue-driven):**
"They're children," Tomas said. His voice had the flat quality of a
man who had stopped expecting anything to change. "Twelve, thirteen.
Brainwashed and drugged and wired into the stones. We knew this."
Elena wiped rain from her face and tasted iron. "Then we liberate
them, not execute them."
"Liberate them and the Faith loses its power. Liberate them and
the crusaders wake up and find they can't remember why they were
killing us."
"And if we don't?"
"And if we don't, we become them."

### Anti-Exemplars

These show what this voice is NOT. Avoiding them is as important as
emulating the exemplars.

**Anti 1 (Too flowery / ungrounded):**
"The faith cascaded like golden waterfalls through the wounded
landscape, a tapestry of divine benevolence woven by celestial
hands." -- Too abstract. "Faith" and "tapestry" are slop words.
The world has rubble and rust and the smell of burning protein blocks.

**Anti 2 (Too modern / tech-speak):**
"At 0300 hours, the Crusade Team deployed tactical Conviction
protocols against the hostile sector." -- The world regressed. "0300
hours" and "tactical protocols" are military jargon from the before-time.
Conviction is not a tactical system; it costs doubt.

**Anti 3 (Too lyrical / hopeful):**
"Even in the darkest hour, faith bloomed like a flower breaking
through concrete, a testament to the human spirit's indomitable
light." -- This is exactly what the story argues AGAINST. The voice
never romanticizes faith. Darkness is not a prelude to light.

**Anti 4 (Too clinical / detached):**
"The subject exhibited signs of trauma-induced belief patterns
consistent with Phase Three Crusader conditioning." -- Removes the
human cost. The voice stays inside the character's skin. If clinical,
it is because the character is clinical, not because the narrator
stands outside judging.

**Anti 5 (Too biblical / archaic):**
"And behold, the righteous shall inherit the earth, and the faithful
shall walk in the paths of glory." -- Bible fragments exist in this
world, but the voice does not preach. Biblical language appears only
when a character is literally quoting scripture, never as narrative
framing.
