import os

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    """
    Contiene la lógica principal del restaurante.
    """

    def __init__(self):
        base_dir = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        self.ruta_productos = os.path.join(
            base_dir, "datos", "productos.json"
        )

        self.ruta_usuarios = os.path.join(
            base_dir, "datos", "usuarios.json"
        )

    # -------------------------------------------------
    # PRODUCTOS
    # -------------------------------------------------

    def obtener_productos(self):
        """
        Obtiene todos los productos almacenados.
        """
        datos = ArchivoServicio.leer_json(self.ruta_productos)

        return [
            Producto.from_dict(item)
            for item in datos
        ]

    def guardar_productos(self, productos):
        """
        Guarda la lista completa de productos.
        """
        datos = [
            producto.to_dict()
            for producto in productos
        ]

        ArchivoServicio.guardar_json(
            self.ruta_productos,
            datos
        )

    def obtener_siguiente_id(self):
        """
        Genera automáticamente el siguiente ID.
        """
        productos = self.obtener_productos()

        if not productos:
            return 1

        return max(producto.id for producto in productos) + 1

    def agregar_producto(
        self,
        nombre,
        categoria,
        precio,
        stock
    ):
        """
        Agrega un nuevo producto.
        """
        productos = self.obtener_productos()

        nuevo_producto = Producto(
            self.obtener_siguiente_id(),
            nombre,
            categoria,
            precio,
            stock
        )

        productos.append(nuevo_producto)
        self.guardar_productos(productos)

        return nuevo_producto

    def actualizar_producto(
        self,
        id_producto,
        nombre,
        categoria,
        precio,
        stock
    ):
        """
        Actualiza un producto existente.
        """
        productos = self.obtener_productos()

        for producto in productos:
            if producto.id == id_producto:
                producto.nombre = nombre
                producto.categoria = categoria
                producto.precio = float(precio)
                producto.stock = int(stock)

                self.guardar_productos(productos)
                return True

        return False

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto mediante su ID.
        """
        productos = self.obtener_productos()

        productos_filtrados = [
            producto
            for producto in productos
            if producto.id != id_producto
        ]

        if len(productos_filtrados) == len(productos):
            return False

        self.guardar_productos(productos_filtrados)

        return True

    # -------------------------------------------------
    # USUARIOS
    # -------------------------------------------------

    def validar_usuario(self, usuario, password):
        """
        Verifica las credenciales del usuario.
        """
        datos = ArchivoServicio.leer_json(
            self.ruta_usuarios
        )

        usuarios = [
            Usuario.from_dict(item)
            for item in datos
        ]

        for user in usuarios:
            if (
                user.usuario == usuario
                and user.password == password
            ):
                return user

        return None
