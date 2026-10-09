-- SQLite-Schema für die Demo-App
-- Achtung: Beim Ausführen werden alle bestehenden Tabellen und Daten gelöscht!

-- Reihenfolge beachten: Tabellen mit Fremdschlüsseln zuerst löschen
DROP TABLE IF EXISTS tier;
DROP TABLE IF EXISTS tierart;
DROP TABLE IF EXISTS besitzer;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(250) NOT NULL UNIQUE,
    password VARCHAR(250) NOT NULL
);

CREATE TABLE besitzer(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vorname VARCHAR(100) NOT NULL,
    nachname VARCHAR(100) NOT NULL,
    adresse VARCHAR(250),
    telefon VARCHAR(20)
);

CREATE TABLE tierart(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bezeichnung VARCHAR(100) NOT NULL
);

CREATE TABLE tier (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tiername VARCHAR(100) NOT NULL,
    tierart_id INTEGER NOT NULL,
    besitzer_id INTEGER NOT NULL,
    FOREIGN KEY (tierart_id) REFERENCES tierart(id),
    FOREIGN KEY (besitzer_id) REFERENCES besitzer(id)
);

-- Insert sample data
-- Beachten Sie, dass die Primary Keys automatisch generiert werden
INSERT INTO besitzer (vorname, nachname, adresse, telefon) VALUES
('Geralt', 'Example', 'Musterstrasse 1, 8000 Zürich', '01234567890'),
('Cirilla', 'Beispiel', 'Beispielweg 2, 8400 Winterthur', '09876543210');

INSERT INTO tierart (bezeichnung) VALUES
('Hund'),
('Katze'),
('Pferd');

INSERT INTO tier (tiername, tierart_id, besitzer_id) VALUES
('Rex', 1, 1),
('Miezi', 2, 2),
('Ploetze', 3, 1);
