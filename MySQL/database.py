import pymysql
from pymysql import Connection as MysqlConn


class Database:
    def __init__(self, db: str | None = None, host: str = "localhost", user: str = "root", password: str = "") -> None:
        """
        Initializing database.
        """
        self.host: str = host
        self.user: str = user
        self.password: str = password
        self.db: str = db

    def Conn(self) -> MysqlConn:
        """
        Setting up connection to the mysql server.
        """
        conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.db)
        return conn

    def Exec(self, sql: str) -> bool:
        """
        Executing the sql command.
        """
        ok = False
        try:
            conn = self.Conn()
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            ok = True
        except pymysql.connect.Error as error:
            print("MYSQL Run Error: {}".format(error))
        finally:
            if conn.ping():
                cur.close()
                conn.close()
        return ok

    def getArray(self, sql: str) -> list[tuple]:
        """
        Getting data from database.
        """
        conn = self.Conn()
        cur = conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        conn.close()
        return res
