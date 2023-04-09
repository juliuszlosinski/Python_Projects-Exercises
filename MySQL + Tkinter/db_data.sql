CREATE TABLE devices (
  id INT UNSIGNED NOT NULL UNIQUE AUTO_INCREMENT,
  uid CHAR(24) NOT NULL,
  name VARCHAR(255),
  measurement_interval INT UNSIGNED NOT NULL DEFAULT 5,
  transceive_interval INT UNSIGNED NOT NULL DEFAULT 60,
  PRIMARY KEY (id)
);

CREATE TABLE data (
  id INT UNSIGNED NOT NULL UNIQUE AUTO_INCREMENT,
  device_id INT UNSIGNED NOT NULL,
  time DATETIME NOT NULL,
  temperature FLOAT,
  humidity FLOAT,
  voltage FLOAT,
  PRIMARY KEY (id),
  FOREIGN KEY (device_id) REFERENCES devices(id),
  INDEX device_time (device_id, time)
);

INSERT INTO devices (uid, name)
VALUES ('000000000000000000000000', 'Test Device');

INSERT INTO devices
VALUES (NULL, '000000000000000000000000', 'Test Device', 1, 5);