---
name: teaching-format
description: Formatting standard for step-by-step instruction in this repo. Use whenever walking the owner through a task, explaining a concept they will act on, teaching a library or language feature, or giving any sequence of instructions to follow. Applies to the mentor role defined in CLAUDE.md.
---

# Teaching format

## Why this exists

The owner reads your response on one monitor and works in the editor on another, glancing back and forth mid-step. **Optimize for re-acquiring your place at a glance**, not for reading top to bottom.

The failure mode is looking back at the response and having to re-read prose to work out where you were. Length is not the problem — undifferentiated text is. A long response with strong visual anchors beats a short one without them.

## The three visual objects

Every teaching response is built from exactly three kinds of block. They must look different from each other on screen.

### 1. Step banner — a boxed block

Each step opens with a fenced block containing a box. **No language tag** — that is what distinguishes a banner from code.

````
```
┌────────────────────────────────────────────────────┐
│  STEP 3 of 6  —  Walk the whole tree                │
└────────────────────────────────────────────────────┘
```
````

Rules:

- Box interior is 52 characters wide. Two leading spaces, then the title, then spaces to pad.
- Always include `of M` so position in the sequence is visible without scrolling.
- Titles are imperative and concrete: `Run the test and read the failure`, never `Next` or `Continue`.
- Keep titles short enough to fit the box. If a title does not fit, the title is too long — shorten it, do not widen the box.

### 2. Response-needed block — a blockquote

When you need the owner to answer, decide, or report back, it goes at the very end in a blockquote. This is the only blockquote in the response, so its shape means one thing.

````
> ## ▶ YOUR TURN
> Work through steps 1–5, then make the fix in step 6.
>
> Then: which of these should a `domain/` file be allowed to import?
````

Rules:

- One per response, always last.
- Never put a question anywhere else. Questions scattered mid-explanation get missed.
- If there is nothing to ask, still close with what to do next and what to report back.

### 3. Code — a fenced block with a caption

Every code block gets a **bold caption on its own line directly above it**, and a language tag. Three captions, used exactly as written:

- `**▶ Run this**` — paste and execute. Language tag `bash`, `python`, etc.
- `**✓ Expected output**` — what should come back. Language tag `text`, so it renders without syntax coloring and reads as inert.
- `**○ Illustration — do not run**` — demonstrates a concept. Real language tag.

Rules:

- No code in prose. If the owner would have to retype something out of a sentence, it belongs in a block.
- One shell command per block, paste-ready, `uv run` prefix already included.
- Never a complete solution to the task at hand (see the mentor role in CLAUDE.md). Illustrations stay small and obviously partial.

## Writing the steps

- **One action per step.** Two verbs in a step ("read X, then change Y") means two steps.
- **Action first, explanation after.** State what to do in one sentence, then explain why. Acting must not require reading the rationale first.
- **Stable numbering.** Once issued, step 3 is step 3 for the rest of the conversation. Follow-ups insert as "Step 3a" — never renumber.
- **Name the file and line** in any step that touches the project, as `tests/test_architecture.py:5`.
- **Define unfamiliar names on every first appearance** — one plain sentence on what it is and whether it is standard library, a dependency to install, or a term of art.
- **Close ambiguous steps with a checkpoint**: one line on what success looks like, so a step can be verified before moving on.
- Open the response with a short paragraph on what you are doing and why. Keep that background out of the steps.

## Worked example

````markdown
We're turning each file's text into a list of imported module names. Working in
the REPL first, on throwaway strings, before touching your test file.

```
┌────────────────────────────────────────────────────┐
│  STEP 1 of 2  —  Open a Python REPL                 │
└────────────────────────────────────────────────────┘
```

**▶ Run this**

```bash
uv run python
```

`uv run` puts you inside the project's virtual environment. Keep this session
open for the whole walkthrough.

```
┌────────────────────────────────────────────────────┐
│  STEP 2 of 2  —  Parse one import and dump it       │
└────────────────────────────────────────────────────┘
```

**▶ Run this**

```python
import ast
print(ast.dump(ast.parse("import json"), indent=2))
```

**✓ Expected output**

```text
Module(
  body=[
    Import(
      names=[
        alias(name='json')])])
```

`ast` is a standard-library module — nothing to install. `ast.parse` runs the
same parser Python uses to read your code, but hands back a tree instead of
executing anything.

> ## ▶ YOUR TURN
> Run both steps, then tell me what `ast.dump` shows for
> `from . import unit`. One field differs from the example above in a way
> that will matter later.
````
