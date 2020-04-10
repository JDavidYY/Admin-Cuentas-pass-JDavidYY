import sqlite3
from sqlite3 import Error

#---- Creamos la función de la creación con la BD----------
def crear_conexion(dbFile):
    conn = None
    try:
        conn = sqlite3.connect(dbFile)
    except Error as e:
        print(e)
    return conn

def crear_tabla(conn, tabla):
    try:
        c= conn.cursor()
        c.execute(tabla)
    except Error as e:
        print(e)

def db():
 
    sql_tabla_cuenta = """ CREATE TABLE IF NOT EXISTS cuenta (
                                        id integer PRIMARY KEY,
                                        nombre text NOT NULL,
                                        pagina text NOT NULL,
                                        correo text NOT NULL,
                                        contraseña text NOT NULL
                                    ); """
 

#----------Creamos la conexión con la base de datos----------
    conn = crear_conexion("database")
    
    # --------creamos las tablas------------
    if conn is not None:
        # creamos la tabla cuenta
        crear_tabla(conn, sql_tabla_cuenta)
 
    else:
        print("Error! No se pudo crear la conexión.")
 
 
if __name__ == '__main__':
    db()