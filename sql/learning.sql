-- Learning tracker database
-- Run: python -m sqlite3 learning.db < sql/learning.sql

CREATE TABLE stages (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    stage INTEGER,
    done INTEGER DEFAULT 0
);

INSERT INTO stages (name) VALUES
    ('Foundations'),
    ('Python'),
    ('Claude API');

INSERT INTO tasks (title, stage, done) VALUES
    ('Learn Git', 1, 1),
    ('Learn SQL', 1, 1),
    ('Protect API key', 1, 1),
    ('Python JSON and requests', 2, 0);

-- Tasks per stage
SELECT stages.name, COUNT(*)
FROM tasks
JOIN stages ON tasks.stage = stages.id
GROUP BY stages.name;