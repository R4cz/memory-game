import sqlite3

class Connection:

    def open( self):
        connection = sqlite3.connect( "d:/Oscar/Progamación/Portfolio/Hola Mundo/Ejercicio 3/JuegoDeMemoria.db")
        return connection
    
    def add_to_ranking(self, data):
        con = self.open()
        cursor = con.cursor()
        sql = f"insert into MemoramaRanking( nombre,edad,tiempo,errores) values {data}"
        cursor.execute(sql)
        con.commit()
        con.close()

    def recover_ranking(self):
        try:
            con = self.open()
            cursor = con.cursor()
            sql = "select nombre,edad,tiempo,errores from MemoramaRanking"
            cursor.execute( sql)
            return cursor.fetchall()
        finally:
            con.close()