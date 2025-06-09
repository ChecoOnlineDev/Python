# -*- coding: utf-8 -*-
"""
Este es un código de prueba para conectar Python a una base de datos SQLite.
No se requiere instalación adicional para SQLite, ya que está integrado con Python.
"""

import sqlite3

def test_sqlite_connection(db_name="test_database.db"):
    """
    Intenta conectar a una base de datos SQLite, crear una tabla,
    insertar datos y leerlos.
    """
    print(f"--- Iniciando prueba de conexión a SQLite: {db_name} ---")
    conn = None # Inicializamos la conexión a None
    try:
        # Paso 1: Conectar a la base de datos SQLite.
        # Si el archivo no existe, SQLite lo creará automáticamente.
        conn = sqlite3.connect(db_name)
        print(f"Conexión exitosa a la base de datos: {db_name}")

        # Paso 2: Crear un objeto cursor.
        # El cursor permite ejecutar comandos SQL.
        cursor = conn.cursor()
        print("Cursor creado.")

        # Paso 3: Crear una tabla (si no existe).
        # Usamos 'IF NOT EXISTS' para evitar un error si la tabla ya existe.
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mensajes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contenido TEXT NOT NULL,
                fecha_creacion TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        # Confirmar los cambios en la base de datos (necesario para CREATE, INSERT, UPDATE, DELETE)
        conn.commit()
        print("Tabla 'mensajes' verificada/creada.")

        # Paso 4: Insertar algunos datos.
        # Usamos IGNORE para evitar errores si el ID ya existe en futuras ejecuciones de la prueba.
        # En una aplicación real, usarías INSERT INTO sin IGNORE para nuevos registros.
        cursor.execute("INSERT OR IGNORE INTO mensajes (id, contenido) VALUES (1, 'Hola, mundo desde Python!')")
        cursor.execute("INSERT OR IGNORE INTO mensajes (id, contenido) VALUES (2, 'Esta es una prueba de conexión.')")
        conn.commit()
        print("Datos insertados o actualizados.")

        # Paso 5: Leer los datos.
        print("Leyendo datos de la tabla 'mensajes':")
        cursor.execute("SELECT id, contenido, fecha_creacion FROM mensajes")
        # 'fetchall()' obtiene todas las filas del resultado de la consulta.
        filas = cursor.fetchall()

        if filas:
            for fila in filas:
                print(f"ID: {fila[0]}, Contenido: '{fila[1]}', Fecha: {fila[2]}")
        else:
            print("No se encontraron mensajes en la base de datos.")

    except sqlite3.Error as e:
        # Paso 6: Manejo de errores.
        print(f"Ocurrió un error de SQLite: {e}")
    finally:
        # Paso 7: Cerrar la conexión.
        # Es crucial cerrar la conexión para liberar los recursos.
        if conn:
            conn.close()
            print("Conexión a la base de datos cerrada.")

# Ejecutar la función de prueba si el script se ejecuta directamente.
if __name__ == "__main__":
    test_sqlite_connection()
