"""
en este codigo crearemos la conexion a una base de datos mysql ya existente
con el usuario : root 
contraseña: 151107
local host : 3306
una localinstance mysql 80
el nombre de la base de datos es:  holamundo
e imprimiremos el contenido de una tabla especifica llamada animales
#         # Paso 7: Cerrar la conexión.

"""
import mysql.connector
def test_mysql_connection():
    """
    Intenta conectar a una base de datos MySQL, leer datos de una tabla específica
    y manejar errores de conexión.
    """
    print("--- Iniciando prueba de conexión a MySQL ---")
    
    try:
        # Paso 1: Conectar a la base de datos MySQL.
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='151107',
            database='holamundo'
        )
        print("Conexión exitosa a la base de datos MySQL.")
        # Paso 2: Crear un cursor.
        cursor = conexion.cursor()
        print("Cursor creado.")
        # Paso 3: Leer datos de la tabla 'animales'.
        print("Leyendo datos de la tabla 'animales':")
        cursor.execute("SELECT id, estado, tipo FROM animales")
        filas = cursor.fetchall()
        
        if filas:
            for fila in filas:
                print(f"ID: {fila[0]}, Nombre: '{fila[1]}', Especie: {fila[2]}")
        else:
            print("No se encontraron animales en la base de datos.")
    except mysql.connector.Error as e:
        # Paso 4: Manejo de errores.
        print(f"Ocurrió un error de MySQL: {e}")
    finally:
        # Paso 5: Cerrar la conexión.
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión a MySQL cerrada.")
# Ejecutar la prueba de conexión
if __name__ == "__main__":
    test_mysql_connection()
# Este código establece una conexión a una base de datos MySQL, lee datos de una tabla específica llamada 'animales' y maneja posibles errores de conexión.
# Asegúrate de tener el paquete mysql-connector-python instalado:


