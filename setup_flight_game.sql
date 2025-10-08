CREATE DATABASE IF NOT EXISTS flight_game CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE flight_game;

CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(64) NOT NULL UNIQUE,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  location VARCHAR(10) NOT NULL DEFAULT 'EFHK',
  battery INT NOT NULL DEFAULT 100,
  KM DOUBLE NOT NULL DEFAULT 0,
  membership VARCHAR(20) NOT NULL DEFAULT 'Silver',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS airport (
  ident VARCHAR(10) PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  iso_country CHAR(2) NOT NULL,
  continent CHAR(2),
  municipality VARCHAR(100),
  latitude_deg DOUBLE,
  longitude_deg DOUBLE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT IGNORE INTO airport (ident, name, iso_country, continent, municipality, latitude_deg, longitude_deg) VALUES
('EFHK','Helsinki Vantaa','FI','EU','Vantaa',60.3172,24.9633),
('EGLL','London Heathrow','GB','EU','London',51.4700,-0.4543),
('KJFK','John F Kennedy Intl','US','NA','New York',40.6413,-73.7781),
('KLAX','Los Angeles Intl','US','NA','Los Angeles',33.9416,-118.4085);
