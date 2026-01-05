# password-chekcer
A small program, that  checks how strong a password is based on a specific criteria.
# Password Strength Checker

A small command-line project for evaluating password strength. The folder contains three simple scripts you can run to test or compare password-strength heuristics.

## Files
- `main.py` — A modular implementation with functions for length, character types, and common-pattern checks. Run with `python main.py`.
- `mymian.py` — A quick script with a different scoring approach and decorative output. Run with `python mymian.py`.
- `testing.py` — A more refactored and constant-driven version with clearer output and basic validation. Run with `python testing.py`.

## Requirements
- Python 3.9+ (no external packages required)

## Quick start
1. Open a terminal in this folder.
2. Run one of the scripts, for example:
   - `python main.py`
   - `python mymian.py`
   - `python testing.py`
3. Enter a password when prompted and read the strength evaluation printed to the console.

## Notes
- Each script uses a simple points-based heuristic and prints a strength label (e.g., Weak, Medium, Strong).
- These are example programs intended for learning and experimentation, not for production security checks.
