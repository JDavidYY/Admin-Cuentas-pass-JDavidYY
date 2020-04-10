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
#----------Creamos la función para crear tablas-------------
def crear_tabla(conn, tabla):
    try:
        c= conn.cursor()
        c.execute(tabla)
    except Error as e:
        print(e)

#----------Creamos la función para insertar datos en las tablas-----

def actualizar_tabla(conn,tabla):
    try:
        c = conn.cursor()
        c.execute(tabla)
        conn.commit()
    except Error as e:
        print(e)
    return c

#------------Creamos la función para arrancar la base de datos inicial
def db():
 
    sql_tabla_cuenta = """ CREATE TABLE IF NOT EXISTS cuenta (
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