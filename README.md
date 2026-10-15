# 🤖 Agents Learning

> ✍️ Created by **Mohammed Samara**

My hands-on journey learning **AI agents** and **multi-agent systems**, from the foundations up to building agents with the **Claude API**.

I learn by doing: every step has small practical exercises, and I write what I learned in the [Learning Log](LEARNING_LOG.md).

---

## 🗺️ Roadmap

| Stage | Topics | Status |
|---|---|---|
| 1. Foundations | Git & GitHub, SQL basics, protecting API keys | ✅ Done |
| 2. Python | JSON, HTTP requests, working with APIs | 🔄 In progress |
| 3. Claude API | Messages API, prompts, tool use | ⏳ Next |
| 4. AI Agents | Agent loop, tools, memory | ⏳ Planned |
| 5. Multi-Agent Systems | Several agents working together | ⏳ Planned |

---

## 📂 Structure

| Path | What's inside |
|---|---|
| [`LEARNING_LOG.md`](LEARNING_LOG.md) | What I learned each day |
| [`sql/learning.sql`](sql/learning.sql) | A small SQLite database that tracks my learning tasks |

---

## ▶️ Run the SQL example

```bash
python -m sqlite3 learning.db < sql/learning.sql
```

---

## 🔒 Security

API keys are kept in a `.env` file, which is listed in `.gitignore` so it is never pushed to GitHub.
