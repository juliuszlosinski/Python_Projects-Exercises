from database import Database
from datetime import datetime
import db_configuration as db_conf
import random
from time import sleep

conn = Database(
    host=db_conf.HOST,
    user=db_conf.USER,
    password=db_conf.PASSWORD
)
conn.db = db_conf.DB_NAME

MEASUREMENT_TIME = db_conf.MEASUREMENT_TIME
INSERT_TIME = db_conf.INSERT_TIME

temp, humi, volts = 20, 50, 4
n = int(INSERT_TIME / MEASUREMENT_TIME)
i = 0

while True:
    starting_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sql = f"INSERT INTO data VALUES " \
          f"(NULL, {db_conf.DEVICE_ID}, '{starting_time}', {temp}, {humi}, {volts}),"
    i += 1
    if i >= n:
        i = 0
        sql = sql.rstrip(",") + ";"
        print(sql)
        conn.Exec(sql)
        sql = f"INSERT INTO data VALUES"
    temp += random.uniform(-0.5, 0.5)
    humi += random.uniform(-1.0, 1.0)
    volts += random.uniform(-0.01, 0)
    sleep(MEASUREMENT_TIME)
