# Python for agents

Small exercises I wrote while filling the Python gaps I need before the Claude API.

Setup used for all of them:

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install python-dotenv requests
pip freeze > requirements.txt
```

| File | Question | What it practices |
|---|---|---|
| [`01_env_check.py`](exercises/01_env_check.py) | Read a key from `.env` and check it exists | `os.getenv`, `load_dotenv`, `is None` |
| [`02_json_strings.py`](exercises/02_json_strings.py) | Convert a dict to JSON text and back | `json.dumps`, `json.loads` |
| [`03_json_files.py`](exercises/03_json_files.py) | Write and read a JSON file | `json.dump`, `json.load`, `with open` |
| [`04_students.py`](exercises/04_students.py) | Save 3 students to a file, read them, print names | lists of dicts, `for` loop |
| [`05_requests_get.py`](exercises/05_requests_get.py) | First GET request to a public API | `requests.get`, `status_code`, `.json()` |
| [`06_users_request.py`](exercises/06_users_request.py) | Print a user's name and email only on status 200 | `if`/`else` on the status code |

Exercises 04 and 06 were solved on my own, without AI.

The `.env` file and the `.venv` folder are never committed (see `.gitignore`).
