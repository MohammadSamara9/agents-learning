# Learning Log

## 2026-10-10 — Git basics
- git init, add, commit, status, log
- .gitignore to protect .env (API keys)
- Connected to GitHub: remote, origin, push -u
- Branches: switch -c, merge




## 2026-10-14 — SQL basics
- SQLite via python -m sqlite3
- CREATE TABLE, INSERT, SELECT, WHERE, ORDER BY
- UPDATE, DELETE (always with WHERE!)
- JOIN two tables, COUNT, GROUP BY
- .db files go in .gitignore; commit the .sql instead

## 2026-10-18 — Claude 101
- Completed the Claude 101 course on Claude Academy
- Badge saved in [certificates/](certificates/claude-101-badge.pdf)

## 2026-10-23 — Prompt engineering practice
- A good prompt = setting the stage + defining the task + specifying the rules
- Practiced rewriting vague prompts into clear ones
- Decided to keep improving prompts inside real projects, not only exercises

## 2026-11-10 — Python lab course finished (chapters 7 to 10)
- Chapter 7: variables, types, strings, lists, tuples, dicts, conditions, loops, files
- Chapter 8: functions, modules, `pip`, data structures, recursion, regex
- Chapter 9: classes, inheritance, polymorphism, abstract classes, data hiding, exceptions with `raise`
- Chapter 10: NumPy arrays and a simple Matplotlib plot (SciPy skipped, not needed for agents)
- HackerRank: first problems solved without AI, first star earned
- Next: JSON, HTTP requests and `.env` with `os`, then my first small project with the Claude API

## 2026-11-17 — Python gaps for agents
- `venv`: create, activate, `pip install`, `requirements.txt`, and why `.venv` is never committed
- `.env` with `python-dotenv` and `os.getenv`; a missing key returns `None`, so I check it
- JSON: `dumps` / `loads` for strings, `dump` / `load` for files
- `requests`: `get`, `status_code`, `.json()`
- What an API is: the road between two programs, and JSON is what travels on it
- Mistakes I learned from: running in `System32`, `cmd` vs PowerShell activation, typos in file names, and never naming a file `requests.py`
- Exercises saved in [python/](python)

## 2026-11-17 — Claude API: first look
- Opened my Claude Console account (credits, keys, models)
- Shape of a request: `model`, `max_tokens`, `messages`
- Next: add a small amount of credit, create a key, and send my first request
