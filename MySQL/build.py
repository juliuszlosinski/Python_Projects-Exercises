from database import Database
import db_configuration as db_conf

conn = Database(
    host=db_conf.HOST,
    user=db_conf.USER,
    password=db_conf.PASSWORD
)
conn.Exec(f"DROP DATABASE IF EXISTS {db_conf.DB_NAME};")
conn.Exec(f"CREATE DATABASE {db_conf.DB_NAME};")
conn.db = db_conf.DB_NAME
conn.Exec("""
    CREATE TABLE devices 
    (
      id INT UNSIGNED NOT NULL UNIQUE AUTO_INCREMENT,
      uid CHAR(24) NOT NULL,
      name VARCHAR(255),
      measurement_interval INT UNSIGNED NOT NULL DEFAULT 5,
      transceive_interval INT UNSIGNED NOT NULL DEFAULT 60,
      PRIMARY KEY (id)
    );             
""")

conn.Exec("""
    CREATE TABLE data 
    (
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
""")

conn.Exec("""
    INSERT INTO devices
    VALUES (NULL, "000000000000000000000000", "Test Device", 1, 5);
""")
