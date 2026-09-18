import tkinter as tk
from tkinter import ttk, messagebox

from servicios.restaurante_servicio import RestauranteServicio


class LoginView:
    """
    Ventana de inicio de sesión.
    """

    def __init__(self, root, on_login):
        self.root = root
        self.on_login = on_login

        self.servicio = RestauranteServicio()

        self.root.title("Restaurante App - Inicio de sesión")
        self.root.geometry("420x320")
        self.root.resizable(False, False)

        self.crear_interfaz()

    def crear_interfaz(self):

        # ---------------------------------------------
        # CONTENEDOR PRINCIPAL
        # ---------------------------------------------

        contenedor = ttk.Frame(
            self.root,
            padding=30
        )

        contenedor.pack(
            fill="both",
            expand=True
        )

        # ---------------------------------------------
        # TÍTULO
        # ---------------------------------------------

        titulo = ttk.Label(
            contenedor,
            text="RESTAURANTE APP",
            font=("Arial", 20, "bold")
        )

        titulo.pack(pady=(10, 5))

        subtitulo = ttk.Label(
            contenedor,
            text="Sistema de gestión de productos"
        )

        subtitulo.pack(pady=(0, 20))

        # ---------------------------------------------
        # FORMULARIO
        # ---------------------------------------------

        formulario = ttk.LabelFrame(
            contenedor,
            text="Inicio de sesión",
            padding=20
        )

        formulario.pack(
            fill="x"
        )

        ttk.Label(
            formulario,
            text="Usuario:"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=5,
            pady=8
        )

        self.usuario_entry = ttk.Entry(
            formulario,
            width=30
        )

        self.usuario_entry.grid(
            row=0,
            column=1,
            padx=5,
            pady=8
        )

        ttk.Label(
            formulario,
            text="Contraseña:"
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=5,
            pady=8
        )

        self.password_entry = ttk.Entry(
            formulario,
            width=30,
            show="*"
        )

        self.password_entry.grid(
            row=1,
            column=1,
            padx=5,
            pady=8
        )

        # ---------------------------------------------
        # BOTÓN
        # ---------------------------------------------

        boton = ttk.Button(
            formulario,
            text="Ingresar",
            command=self.iniciar_sesion
        )

        boton.grid(
            row=2,
            column=0,
            columnspan=2,
            pady=15
        )

        self.root.bind(
            "<Return>",
            lambda event: self.iniciar_sesion()
        )

        self.usuario_entry.focus()

    def iniciar_sesion(self):

        usuario = self.usuario_entry.get().strip()
        password = self.password_entry.get().strip()

        if not usuario or not password:
            messagebox.showwarning(
                "Campos requeridos",
                "Ingrese usuario y contraseña."
            )
            return

        usuario_obj = self.servicio.validar_usuario(
            usuario,
            password
        )

        if usuario_obj:

            self.root.withdraw()

            self.on_login(usuario_obj)

        else:

            messagebox.showerror(
                "Error",
                "Usuario o contraseña incorrectos."
            )
