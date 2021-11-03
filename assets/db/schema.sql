DROP TABLE IF EXISTS domains;

CREATE TABLE IF NOT EXISTS domains (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    deleted_at DATETIME DEFAULT null
);

DROP TABLE IF EXISTS subjects;

CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    deleted_at DATETIME DEFAULT null 
);

DROP TABLE IF EXISTS subject_attributes;

CREATE TABLE IF NOT EXISTS subject_attributes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id INTEGER NOT NULL,
    name text NOT NULL,
    value text NOT NULL,
    deleted_at DATETIME DEFAULT null 
);

DROP TABLE IF EXISTS subjects;

CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    domain_id INTEGER NOT NULL,
    deleted_at DATETIME default null
);

DROP TABLE IF EXISTS temporals;

CREATE TABLE IF NOT EXISTS temporals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mapname text NOT NULL,
    temporal_type INTEGER NOT NULL,
    deleted_at DATETIME default null
);