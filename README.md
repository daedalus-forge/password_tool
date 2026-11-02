# Password Tool

A command-line password generator, written in Python as a hands-on project for learning the language from scratch. A password strength checker is next on the roadmap.

## Features

- Generates random passwords between **8 and 64 characters** long
- Uses uppercase and lowercase letters, digits and symbols
- Uses Python's [`secrets`](https://docs.python.org/3/library/secrets.html) module, which is cryptographically secure, rather than `random`, which is predictable and unsuitable for passwords
- Validates input: it rejects non-numbers and out-of-range lengths, and keeps asking until it gets a valid answer

## Usage

Requires Python 3.10+. No external packages needed.

```bash
git clone https://github.com/daedalus-forge/password-tool.git
cd password-tool
python3 password_tool.py
```

Example:

```
How long should the password be? abc
That is not a valid number. Please enter a whole number between 8 and 64.
How long should the password be? 20
Your 20-character password is: xpBcHr;/^e{?>xKnQZ!x
```

## Roadmap

- [x] Random password generation
- [x] Input validation and error handling
- [x] Refactor into functions
- [ ] Password strength checker (length, character variety)
- [ ] Check against a common-passwords wordlist
- [ ] Menu / command-line arguments (`argparse`)
- [ ] Passphrase generation
- [ ] Entropy estimate
- [ ] Breach check via the Have I Been Pwned k-anonymity API
- [ ] Unit tests with `pytest`

## What I've learned so far

Variables and data types, type conversion, user input, `for` and `while` loops, `if`/`elif`/`else`, `try`/`except` error handling, f-strings, functions, the standard library (`secrets`, `string`), and Git and GitHub workflows.

## Disclaimer

This is a learning project. For real-world use, a well-established password manager is recommended.