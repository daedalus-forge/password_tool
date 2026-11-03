# Password Tool

A command-line password generator and strength checker, written in Python as a hands-on project for learning the language from scratch.

## Features

- **Interactive menu:** generate a password, check a password's strength, or quit
- **Password generator:**
  - Random passwords between **8 and 64 characters** long
  - Uses uppercase and lowercase letters, digits and symbols
  - Uses Python's [`secrets`](https://docs.python.org/3/library/secrets.html) module, which is cryptographically secure, rather than `random`, which is predictable and unsuitable for passwords
  - Every generated password is rated automatically
- **Strength checker:**
  - Scores a password out of 7 on length and character variety
  - Rates it **Weak**, **Moderate** or **Strong**
  - Hides the password as you type it (via `getpass`), and never prints it back to the screen
- **Input validation:** rejects non-numbers, out-of-range lengths and invalid menu choices, and keeps asking until it gets a valid answer

## Usage

Requires Python 3.10+. No external packages needed.

```bash
git clone https://github.com/daedalus-forge/password-tool.git
cd password-tool
python3 password_tool.py
```

Example:

```
===Password Tool===
1. Generate a password
2. Check password strength
3. Quit
Choose an option: 1
How long should the password be? 16
Password: k#7Qz!pR2vX@m9Lw
Rating: Strong (7/7)

===Password Tool===
1. Generate a password
2. Check password strength
3. Quit
Choose an option: 2
Enter a password to check:
Rating: Moderate (5/7)
```

## How passwords are scored

| Check | Points |
|---|---|
| At least 8 characters | +1 |
| At least 12 characters | +1 |
| At least 16 characters | +1 |
| Contains an uppercase letter | +1 |
| Contains a lowercase letter | +1 |
| Contains a digit | +1 |
| Contains a symbol | +1 |

| Score | Rating |
|---|---|
| 0–3 | Weak |
| 4–5 | Moderate |
| 6–7 | Strong |

**Limitation:** the score only looks at length and character types, so a predictable password like `Password123!` still scores well. A common-passwords check is next on the roadmap to fix this.

## Roadmap

- [x] Random password generation
- [x] Input validation and error handling
- [x] Refactor into functions
- [x] Password strength checker (length, character variety)
- [x] Interactive menu
- [x] Hidden password input (`getpass`)
- [ ] Check against a common-passwords wordlist
- [ ] Command-line arguments (`argparse`)
- [ ] Passphrase generation
- [ ] Entropy estimate
- [ ] Breach check via the Have I Been Pwned k-anonymity API
- [ ] Unit tests with `pytest`

## What I've learned so far

- **Python basics:** variables, data types (strings, integers, booleans), type conversion and f-strings
- **Control flow:** `if`/`elif`/`else`, `for` and `while` loops, `break`/`continue`
- **Error handling:** `try`/`except`, and reading tracebacks
- **Functions:** parameters, return values (including returning several), and scope
- **Code design:** refactoring, DRY (Don't Repeat Yourself), separation of concerns and PEP 8 style
- **Standard library:** `secrets`, `string`, `getpass`
- **Tooling:** VS Code, the terminal, Git and GitHub

## Disclaimer

This is a learning project. For real-world use, a well-established password manager is recommended.
