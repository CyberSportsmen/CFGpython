# CFGpython

Context-Free Grammars implementation in Python.

This project demonstrates the use of a context-free grammar (CFG) to:

- Define a simple grammar for the language aⁿbⁿ (e.g., `ab`, `aabb`, `aaabbb`, ...).
- Generate valid strings from the grammar.
- Derive strings step-by-step using leftmost derivation.
- Test whether a given string belongs to the language.

## Features

- **Grammar definition** using Python dictionaries.
- **String generation** based on CFG rules.
- **Derivation visualization** showing how strings are formed.
- **Membership testing** for the aⁿbⁿ language.

## How to Run

1. Make sure you have Python 3 installed.
2. Save the script to a `.py` file, e.g., `cfg_script.py`.
3. Run the script with:
4. (optional) If you want to change the settings of the script, change the variables (stringuri_pentru_derivare and stringuri_de_testat).

```bash
python cfg_script.py
```

## Example output

```
Definitia CFG-ului:
Non-terminale: ['S']
Terminale: ['a', 'b']
Simbol de Start: S
Reguli de Productie: {'S': [['a', 'S', 'b'], ['']]}

Generator de String-uri:
String-uri generate:
ε
aabb
aaabbb
ab

Derivare:
Incercare derivare pentru: 'aabb'
S -> aSb -> aaSbb -> aabb

Incercare derivare pentru: 'ab'
S -> aSb -> ab

Incercare derivare pentru: 'ε'
S -> ε

Incercare derivare pentru: 'aab'
String-ul 'aab' nu respecta structura a^n b^n sau nu este in limbaj.


Testare Apartenenta:
String-ul 'aabb' este membru? True
String-ul 'ab' este membru? True
String-ul 'ε' este membru? True
String-ul 'aab' este membru? False
String-ul 'bba' este membru? False
String-ul 'aaabbb' este membru? True
String-ul 'aaaaabbbbba' este membru? False
```
