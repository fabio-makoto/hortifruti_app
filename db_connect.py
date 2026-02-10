import mysql.connector
import configparser


class DataBaseConnection:
    def __init__(self):
        self.config = configparser.ConfigParser()
        # file_path = "/home/makoto/Desktop/crochet_app/crochet_app/dbconfig.ini"
        self.config.read("db/dbconfig.ini")
        
    
    def connectDb(self):
        try:
            self.conn = mysql.connector.connect(
                user=self.config.get("DB", "user"),
                password=self.config.get("DB", "password"),
                host=self.config.get("DB", "host"),
                database=self.config.get("DB", "database")
            )

        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Há algo de errado com seu usuário e senha.")
            
            else:
                print(f"Erro: {err}")
        
        else:
            print("Conexão feita")
            return self.conn

    
    def closeDb(self, conn, cursor):
        conn.close()
        cursor.close()
        print("Conexão e cursor fechado.")
