CREATE TABLE IF NOT EXISTS sightings (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  sighted_at DATE,
  reported_at DATE,
  location_city VARCHAR(100),
  location_state VARCHAR(100),
  shape VARCHAR(10),
  duration VARCHAR(10),
  description TEXT,
  lat FLOAT(10, 6),
  lon FLOAT(10, 6)
) ENGINE = MYISAM CHARACTER SET utf8 COLLATE utf8_general_ci;
LOAD DATA LOCAL INFILE 'sightings-city-state.tsv' INTO TABLE sightings FIELDS TERMINATED BY '\t' ENCLOSED BY '"' LINES TERMINATED BY '\n';
