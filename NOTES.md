# Python Learning Notes

Project: [password-tool](https://github.com/daedalus-forge/password-tool), a CLI password generator and strength checker.

---

## Setup
- **Python:** popular object-oriented programming language which can be used for everything from simple scripting and automation to complex data science and graphic generation. It is the program (the interpreter) that interprets the code and runs it line by line.
- **Terminal:** where commands are typed and run, e.g. running scripts or creating and navigating directories.
- **VS Code:** code editor. Helps lay out and format code and manage the tools (extensions) needed to write it. It doesn't run the code itself.
- **Running a script:** `python3 file.py`, run from inside the file's folder. Check where I am with `pwd`.
- **VS Code profile "Python":** keeps my extensions separate from other languages.

## Variables & data types
- **Variable:** a name attached to a value. `length = 16` means "store 16, call it `length`".
- **`str` vs `int`:** `"16"` is text and `16` is a number. `16 * 2` gives `32`, but `"16" * 2` gives `"1616"` (repeats the text).
- **Converting:** `int("16")` gives `16`, and `str(16)` gives `"16"`. `int("abc")` crashes with a `ValueError`.
- **Check a type:** `type(x)`.
- **Boolean (`bool`):** `True` or `False`. Capital first letter, no quotes. Comparisons like `10 > 5` produce one.
- **Constants:** values that never change, written in CAPITALS: `CHARACTERS = ...`.

## Reading errors (tracebacks)
- Read **from the bottom up**. The last line gives the error type and the reason. Above that are the file and line number.
- Multi-level tracebacks show the chain of calls. The real cause is at the **bottom**.
- `ValueError`: right type, bad value (`int("abc")`).
- `TypeError`: wrong types mixed together (`"Length: " + 16`).
- `NameError`: Python doesn't recognise the name (a typo, or a scope problem).
- `UnboundLocalError`: a variable is used before it's been given a value in that function.

## Input
- `input("Question? ")` waits for the user and **always returns a string**. Wrap it in `int()` for a number.
- `getpass("Password: ")` works like `input()` but **hides what's typed**. Use it for passwords. (`from getpass import getpass`)

## Imports
- `import secrets` loads a module, used as `secrets.choice()`.
- `from getpass import getpass` imports one tool directly, used as `getpass()`.

## Strings
- Join with `+`: `"ab" + "cd"` gives `"abcd"`. Build up with `+=`.
- `len(s)` gives the length.
- **Methods** (called with a dot): `.isupper()`, `.islower()`, `.isdigit()`, each returning `True`/`False`.
- `x in s` checks whether `x` appears inside `s`: `"#" in string.punctuation` gives `True`.
- `string.ascii_letters`, `string.digits`, `string.punctuation` are ready-made character sets.
- `\n` is a newline character.

## f-strings
- Put `f` before the quotes and variables in `{}`: `f"{length} characters"`.
- Values are converted to text automatically, so there are no type errors.
- Expressions work inside: `f"{len(password) * 2}"`.
- Forgetting the `f` prints `{name}` literally.

## Loops
- **`for`:** repeats a set number of times. `for i in range(5):` runs 5 times, `i` from 0 to 4.
- **Loop over a string:** `for char in password:` gives one character at a time.
- **`_` as loop variable:** `for _ in range(n):` when the variable isn't used.
- **`while True`:** repeats until stopped. `break` exits, and `continue` jumps back to the top.
- **Ctrl+C** force-stops a stuck program.
- **Indentation** (4 spaces) after a `:` defines the block: what's inside the loop, `if` or function.

## Conditionals
- `if` / `elif` / `else`: checks in order and runs the **first** `True` branch only.
- `=` assigns (`x = 5`). `==` compares (`x == 5`).
- Comparisons: `==`  `!=`  `<`  `>`  `<=`  `>=`
- Booleans work directly as conditions: `if has_upper:` (same as `== True`).
- **`elif` vs separate `if`s:**
  - `elif` when only **one** option can apply ("which category is this?")
  - separate `if`s when conditions **overlap** and each should count ("which of these are true?"). For example, length ≥8 *and* ≥12 *and* ≥16 each earn a point.

## Patterns
- **Running total:** `score = 0`, then `score += 1` for each thing that's true.
- **Building a string:** `password = ""`, then `password += char` in a loop.
- **Flag pattern:** set `has_upper = False` **before** the loop, flip it to `True` inside the loop if found, and check it after.
- **Ask until valid:** `while True` + `try`/`except` + `continue` on bad input + `return`/`break` on good input.
- **Menu:** `while True`, show options, `input()`, `if`/`elif` per choice, `break` on Quit. Compare against `"1"` (a string), so bad input can't crash it.

## Error handling
- `try:` runs code that might fail.
- `except ValueError:` handles that specific error instead of crashing. Catch specific errors, not everything.
- `else:` runs only if no error happened.

## Functions
- `def name(param):` defines it. It only runs when **called**: `name(value)`.
- **Parameter:** the input the function receives.
- **`return`:** sends a value back **and ends the function immediately**.
- **`return` vs `print`:** `print` just shows something on screen. `return` gives a value the code can keep using.
- **Return multiple values:** `return rating, score`, caught with `rating, score = check_strength(pw)`.
- `return` goes **inside** the function doing the work. Where you call it, you **catch** the values; you don't `return` there.
- **Scope:** variables created inside a function only exist inside it. To get them out, `return` them.
- Defining a function doesn't run it, so it must be called.

## Code design
- **File layout:** imports → constants → functions → `main()` → call `main()` at the bottom.
- **Refactoring:** restructuring code without changing what it does.
- **DRY (Don't Repeat Yourself):** the same code in two places is a hint it should be a function. Change it once, and it updates everywhere.
- **Separation of concerns:** keep "work things out" (`check_strength` returns) separate from "show the user" (`show_strength` prints).
- **Order matters:** Python runs top to bottom, so get the input *before* using it.
- **Comments explain *why*, not *what*.** Keep them accurate, because a wrong comment is worse than none.
- **PEP 8 style:** `print(` with no space before the bracket, spaces around `==`, two blank lines between functions, `snake_case` names.

## Security points
- **`secrets`, not `random`**, for passwords, tokens and keys. `random` is predictable.
- **Never echo passwords** back to the screen. Use `getpass` for input.
- **Never commit** secrets, API keys or work material. Use `.gitignore` (including `.env`).
- **OPSEC:** keep my employer, clearance and work details out of public repos.
- **Boundary testing:** test edge values (7, 8, 64, 65), because bugs hide at the edges.
- **Silent bugs** (wrong answer, no crash) are more dangerous than crashes.

## Git & GitHub
- **Git** tracks changes locally. **GitHub** hosts repos online (backup and portfolio).
- **Repo:** a tracked folder. **Staging (`git add`):** choosing what goes into the next snapshot. **Commit:** a saved snapshot with a message. **Push:** upload to GitHub.
- **Routine:** `git status` → `git add .` → `git commit -m "..."` → `git push`.
- Commit every time something works. Write messages like commands: "Add…", "Fix…", "Refactor…".
- **Prompt symbols:** `?` untracked files, `+` staged, `!` tracked file modified.
- `.gitignore` lists files Git should never track (`.DS_Store`, `__pycache__/`, `.env`, `scratch.py`).
- Press **q** to exit the pager when you see `(END)`.

## Terminal & VS Code shortcuts
- `cd` changes folder, `pwd` shows where I am, `ls -a` lists all files, `mkdir` makes a folder.
- **Tab** auto-completes names. **↑** recalls the last command.
- `code .` opens the folder in VS Code. `code file.md` creates and opens a file.
- `reset` fixes a terminal with hidden typing (type it blind).
- VS Code: **Ctrl+`** terminal · **Cmd+Shift+P** Command Palette · **Cmd+P** open a file · **Cmd+Shift+X** extensions · **Option+↑/↓** move a line · **Tab / Shift+Tab** indent/unindent · **Cmd+Shift+V** Markdown preview.

---

## Mistakes I made (and fixes)
- **Ran the script from the wrong folder** → `can't open file`. Fix: `cd` into the project, check with `pwd`, open the project folder itself in VS Code.
- **Indentation put my code under `except`** → valid input did nothing. Fix: line up `try` / `except` / `else` at the same level.
- **Indented `print` inside the loop** → printed every pass. Indentation decides what's inside a loop.
- **Used `score` outside the function** → `NameError`. Fix: `return` it, then catch it.
- **`return "Weak"` inside the `if`** → the function ended before returning the score. Fix: store `rating`, then `return rating, score` at the end.
- **Wrote `return` in `main()`** to get values out of `check_strength` → wrong. Fix: catch them with `rating, score = check_strength(pw)`.
- **Checked the password before asking for it** → `UnboundLocalError`, or silently checked the old password. Fix: `input` first, then check.
- **Forgot to save before running** → "I fixed it but it still breaks". Fix: **Cmd+S**. A white dot on the tab means unsaved.
- **Ctrl+C during `getpass`** → terminal stopped showing typing. Fix: `reset`.
- **Put `/7` on the rating instead of the score** → read the output carefully when testing.
