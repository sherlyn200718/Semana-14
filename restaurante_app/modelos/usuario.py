class Usuario:
    """
    Modelo que representa un usuario del sistema.
    """

    def __init__(self, usuario, password, nombre):
        self.usuario = usuario
        self.password = password
        self.nombre = nombre

    def to_dict(self):
        return {
            "usuario": self.usuario,
            "password": self.password,
            "nombre": self.nombre
        }

    @staticmethod
    def from_dict(data):
        return Usuario(
            data["usuario"],
            data["password"],
            data["nombre"]
        )
