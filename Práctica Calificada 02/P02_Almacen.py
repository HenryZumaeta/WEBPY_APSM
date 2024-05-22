import sqlite3
from datetime import datetime

class AlmacenDB:
    def __init__(self, db_name="almacen.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS producto (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                marca TEXT,
                fecha_creacion TEXT,
                stock INTEGER,
                precio REAL
            )
        ''')
        self.conn.commit()

    def agregar_producto(self, nombre, descripcion, marca, stock, precio):
        fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute('''
            INSERT INTO producto (nombre, descripcion, marca, fecha_creacion, stock, precio)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (nombre, descripcion, marca, fecha_creacion, stock, precio))
        self.conn.commit()

    def actualizar_producto(self, producto_id, nombre=None, descripcion=None):
        if nombre:
            self.cursor.execute('''
                UPDATE producto
                SET nombre = ?
                WHERE id = ?
            ''', (nombre, producto_id))
        if descripcion:
            self.cursor.execute('''
                UPDATE producto
                SET descripcion = ?
                WHERE id = ?
            ''', (descripcion, producto_id))
        self.conn.commit()

    def eliminar_producto(self, producto_id):
        self.cursor.execute('''
            DELETE FROM producto
            WHERE id = ?
        ''', (producto_id,))
        self.conn.commit()

    def filtrar_por_marca(self, marca):
        self.cursor.execute('''
            SELECT * FROM producto
            WHERE marca = ?
        ''', (marca,))
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()

# Ejemplo de uso:
almacen = AlmacenDB()

# Agregar productos
almacen.agregar_producto("Producto 1", "Descripción del producto 1", "Marca A", 10, 19.99)
almacen.agregar_producto("Producto 2", "Descripción del producto 2", "Marca B", 5, 29.99)

# Actualizar producto
almacen.actualizar_producto(1, nombre="Producto 1 Actualizado")

# Eliminar producto
almacen.eliminar_producto(2)

# Filtrar productos por marca
productos_marca_a = almacen.filtrar_por_marca("Marca A")
print(productos_marca_a)
