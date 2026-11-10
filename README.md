# 🤖 Agents Learning

> ✍️ Created by **Mohammed Samara**

My hands-on journey learning **AI agents** and **multi-agent systems**, from the foundations up to building agents with the **Claude API**.

I learn by doing: every step has small practical exercises, and I write what I learned in the [Learning Log](LEARNING_LOG.md).

---

## 🗺️ Roadmap

| Stage | Topics | Status |
|---|---|---|
| 1. Foundations | Git & GitHub, SQL basics, protecting API keys, Claude 101, prompt engineering basics | ✅ Done |
| 2. Python | Basics, functions, modules, data structures, recursion, regex ✅ · OOP & exceptions 🔄 · JSON & HTTP requests ⏳ | 🔄 In progress |
| 3. Claude API | Messages API, structured outputs, cost | ⏳ Next |
| 4. AI Agents | Agent loop, tool use, error handling, memory, RAG | ⏳ Planned |
| 5. Multi-Agent Systems | Manager + workers, passing tasks between agents | ⏳ Planned |
| 6. Testing & Safety | Evaluating agents, human approval, prompt injection | ⏳ Planned |
| 7. Deployment | Docker, FastAPI | ⏳ Later |

---

## 🎯 Where I am now

I finished the foundations and I am learning Python alongside my university lab course.

Next up is object-oriented programming and exception handling, then JSON and HTTP requests, and after that my first small project with the Claude API.

## 🧩 How I learn

- One small project for every topic, pushed to this repo
- I write the core of each exercise myself first, and use AI only to review and debug
- One practice problem on HackerRank for each new Python topic, solved without AI
- During exam and project weeks, the university comes first and my learning pauses without guilt

---

## 🎓 Certificates

| Course | Issuer | Date | Certificate |
|---|---|---|---|
| Claude 101 | Claude Academy (Anthropic) | Oct 2026 | [PDF](certificates/claude-101-badge.pdf) · [Verify](https://academy.claude.com/verify/b0de2c3808f48a5303c4142cd1417cfe) |

---

## 📂 Structure

| Path | What's inside |
|---|---|
| [`LEARNING_LOG.md`](LEARNING_LOG.md) | What I learned each day |
| [`sql/learning.sql`](sql/learning.sql) | A small SQLite database that tracks my learning tasks |
| [`certificates/`](certificates) | Course certificates and badges |

---

## ▶️ Run the SQL example

```bash
python -m sqlite3 learning.db < sql/learning.sql
```

---

## 🔒 Security

API keys are kept in a `.env` file, which is listed in `.gitignore` so it is never pushed to GitHub.
