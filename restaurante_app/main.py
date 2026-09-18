import tkinter as tk

from ui.login_view import LoginView
from ui.main_view import MainView


class RestauranteApp:
    """
    Controlador principal de la aplicación.
    """

    def __init__(self):

        self.root = tk.Tk()

        self.mostrar_login()

        self.root.mainloop()

    def mostrar_login(self):

        # Limpiar ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.deiconify()

        LoginView(
            self.root,
            self.iniciar_aplicacion
        )

    def iniciar_aplicacion(self, usuario):

        self.abrir_ventana_principal(
            usuario
        )

    def abrir_ventana_principal(self, usuario):

        # Crear nueva ventana principal
        ventana_principal = tk.Toplevel(
            self.root
        )

        # Ocultar ventana raíz
        self.root.withdraw()

        MainView(
            ventana_principal,
            usuario,
            self.regresar_login
        )

    def regresar_login(self):

        self.mostrar_login()


if __name__ == "__main__":
    RestauranteApp()
