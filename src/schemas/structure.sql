DROP TABLE IF EXISTS Pages CASCADE
CREATE TABLE Pages (id SERIAL PRIMARY KEY, url TEXT NOT NULL, is_scraping BOOLEAN, created_at TIMESTAMP  DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP  DEFAULT CURRENT_TIMESTAMP);
DROP TABLE IF EXISTS Links
CREATE TABLE Links(id SERIAL PRIMARY KEY, page_id INTEGER, url TEXT NOT NULL, created_at TIMESTAMP  DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP  DEFAULT CURRENT_TIMESTAMP);