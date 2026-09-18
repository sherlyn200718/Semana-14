import tkinter as tk
from tkinter import ttk, messagebox


class MainView:
    """
    Ventana principal de la aplicación.
    """

    def __init__(self, root, usuario, on_logout):

        self.root = root
        self.usuario = usuario
        self.on_logout = on_logout

        from servicios.restaurante_servicio import RestauranteServicio

        self.servicio = RestauranteServicio()

        self.producto_seleccionado = None

        self.root.title(
            "Restaurante App - Gestión de productos"
        )

        self.root.geometry("950x650")
        self.root.minsize(850, 550)

        self.crear_estilos()
        self.crear_interfaz()
        self.cargar_productos()

    # =================================================
    # ESTILOS
    # =================================================

    def crear_estilos(self):

        estilo = ttk.Style()

        try:
            estilo.theme_use("clam")
        except tk.TclError:
            pass

        estilo.configure(
            "Titulo.TLabel",
            font=("Arial", 22, "bold")
        )

        estilo.configure(
            "Subtitulo.TLabel",
            font=("Arial", 11)
        )

        estilo.configure(
            "Accion.TButton",
            padding=8
        )

    # =================================================
    # INTERFAZ
    # =================================================

    def crear_interfaz(self):

        # ---------------------------------------------
        # CONTENEDOR PRINCIPAL
        # ---------------------------------------------

        contenedor_principal = ttk.Frame(
            self.root,
            padding=15
        )

        contenedor_principal.pack(
            fill="both",
            expand=True
        )

        # ---------------------------------------------
        # ENCABEZADO
        # ---------------------------------------------

        encabezado = ttk.Frame(
            contenedor_principal
        )

        encabezado.pack(
            fill="x",
            pady=(0, 15)
        )

        ttk.Label(
            encabezado,
            text="Gestión de Productos",
            style="Titulo.TLabel"
        ).pack(
            side="left"
        )

        info_usuario = ttk.Label(
            encabezado,
            text=f"Usuario: {self.usuario.nombre}"
        )

        info_usuario.pack(
            side="right",
            padx=10
        )

        boton_salir = ttk.Button(
            encabezado,
            text="Cerrar sesión",
            command=self.cerrar_sesion
        )

        boton_salir.pack(
            side="right"
        )

        # ---------------------------------------------
        # FORMULARIO
        # ---------------------------------------------

        formulario = ttk.LabelFrame(
            contenedor_principal,
            text="Datos del producto",
            padding=15
        )

        formulario.pack(
            fill="x",
            pady=(0, 15)
        )

        # ID

        ttk.Label(
            formulario,
            text="ID:"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )

        self.id_entry = ttk.Entry(
            formulario,
            width=12,
            state="readonly"
        )

        self.id_entry.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        # Nombre

        ttk.Label(
            formulario,
            text="Nombre:"
        ).grid(
            row=0,
            column=2,
            sticky="w",
            padx=5,
            pady=5
        )

        self.nombre_entry = ttk.Entry(
            formulario,
            width=30
        )

        self.nombre_entry.grid(
            row=0,
            column=3,
            padx=5,
            pady=5
        )

        # Categoría

        ttk.Label(
            formulario,
            text="Categoría:"
        ).grid(
            row=0,
            column=4,
            sticky="w",
            padx=5,
            pady=5
        )

        self.categoria_combo = ttk.Combobox(
            formulario,
            width=20,
            state="readonly",
            values=[
                "Hamburguesas",
                "Pizzas",
                "Ensaladas",
                "Bebidas",
                "Postres",
                "Otros"
            ]
        )

        self.categoria_combo.grid(
            row=0,
            column=5,
            padx=5,
            pady=5
        )

        # Precio

        ttk.Label(
            formulario,
            text="Precio:"
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )

        self.precio_entry = ttk.Entry(
            formulario,
            width=12
        )

        self.precio_entry.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        # Stock

        ttk.Label(
            formulario,
            text="Stock:"
        ).grid(
            row=1,
            column=2,
            sticky="w",
            padx=5,
            pady=5
        )

        self.stock_entry = ttk.Entry(
            formulario,
            width=12
        )

        self.stock_entry.grid(
            row=1,
            column=3,
            padx=5,
            pady=5,
            sticky="w"
        )

        # ---------------------------------------------
        # BOTONES DEL FORMULARIO
        # ---------------------------------------------

        botones_formulario = ttk.Frame(
            formulario
        )

        botones_formulario.grid(
            row=1,
            column=4,
            columnspan=2,
            padx=5,
            pady=5
        )

        ttk.Button(
            botones_formulario,
            text="Nuevo",
            style="Accion.TButton",
            command=self.nuevo_producto
        ).pack(
            side="left",
            padx=3
        )

        ttk.Button(
            botones_formulario,
            text="Guardar",
            style="Accion.TButton",
            command=self.guardar_producto
        ).pack(
            side="left",
            padx=3
        )

        ttk.Button(
            botones_formulario,
            text="Editar",
            style="Accion.TButton",
            command=self.editar_producto
        ).pack(
            side="left",
            padx=3
        )

        # ---------------------------------------------
        # TABLA
        # ---------------------------------------------

        tabla_frame = ttk.LabelFrame(
            contenedor_principal,
            text="Listado de productos",
            padding=10
        )

        tabla_frame.pack(
            fill="both",
            expand=True
        )

        columnas = (
            "id",
            "nombre",
            "categoria",
            "precio",
            "stock"
        )

        self.tabla = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings",
            selectmode="browse"
        )

        self.tabla.heading(
            "id",
            text="ID"
        )

        self.tabla.heading(
            "nombre",
            text="Nombre"
        )

        self.tabla.heading(
            "categoria",
            text="Categoría"
        )

        self.tabla.heading(
            "precio",
            text="Precio"
        )

        self.tabla.heading(
            "stock",
            text="Stock"
        )

        self.tabla.column(
            "id",
            width=60,
            anchor="center"
        )

        self.tabla.column(
            "nombre",
            width=280
        )

        self.tabla.column(
            "categoria",
            width=180
        )

        self.tabla.column(
            "precio",
            width=100,
            anchor="center"
        )

        self.tabla.column(
            "stock",
            width=100,
            anchor="center"
        )

        scroll_vertical = ttk.Scrollbar(
            tabla_frame,
            orient="vertical",
            command=self.tabla.yview
        )

        self.tabla.configure(
            yscrollcommand=scroll_vertical.set
        )

        self.tabla.pack(
            side="left",
            fill="both",
            expand=True
        )

        scroll_vertical.pack(
            side="right",
            fill="y"
        )

        self.tabla.bind(
            "<<TreeviewSelect>>",
            self.seleccionar_producto
        )

        # ---------------------------------------------
        # CONTROLES INFERIORES
        # ---------------------------------------------

        controles = ttk.Frame(
            contenedor_principal
        )

        controles.pack(
            fill="x",
            pady=(10, 0)
        )

        ttk.Button(
            controles,
            text="Eliminar seleccionado",
            command=self.eliminar_producto
        ).pack(
            side="left"
        )

        ttk.Button(
            controles,
            text="Limpiar formulario",
            command=self.limpiar_formulario
        ).pack(
            side="left",
            padx=10
        )

        self.estado_label = ttk.Label(
            controles,
            text="Productos cargados: 0"
        )

        self.estado_label.pack(
            side="right"
        )

    # =================================================
    # PRODUCTOS
    # =================================================

    def cargar_productos(self):

        for item in self.tabla.get_children():
            self.tabla.delete(item)

        productos = self.servicio.obtener_productos()

        for producto in productos:

            self.tabla.insert(
                "",
                "end",
                values=(
                    producto.id,
                    producto.nombre,
                    producto.categoria,
                    f"${producto.precio:.2f}",
                    producto.stock
                )
            )

        self.estado_label.config(
            text=f"Productos cargados: {len(productos)}"
        )

    def seleccionar_producto(self, event=None):

        seleccion = self.tabla.selection()

        if not seleccion:
            return

        valores = self.tabla.item(
            seleccion[0],
            "values"
        )

        if not valores:
            return

        self.producto_seleccionado = int(
            valores[0]
        )

        self.id_entry.config(
            state="normal"
        )

        self.id_entry.delete(
            0,
            tk.END
        )

        self.id_entry.insert(
            0,
            valores[0]
        )

        self.id_entry.config(
            state="readonly"
        )

        self.nombre_entry.delete(
            0,
            tk.END
        )

        self.nombre_entry.insert(
            0,
            valores[1]
        )

        self.categoria_combo.set(
            valores[2]
        )

        self.precio_entry.delete(
            0,
            tk.END
        )

        self.precio_entry.insert(
            0,
            valores[3].replace("$", "")
        )

        self.stock_entry.delete(
            0,
            tk.END
        )

        self.stock_entry.insert(
            0,
            valores[4]
        )

    # =================================================
    # VALIDACIÓN
    # =================================================

    def obtener_datos_formulario(self):

        nombre = self.nombre_entry.get().strip()
        categoria = self.categoria_combo.get().strip()
        precio = self.precio_entry.get().strip()
        stock = self.stock_entry.get().strip()

        if not nombre:
            messagebox.showwarning(
                "Validación",
                "Ingrese el nombre del producto."
            )
            return None

        if not categoria:
            messagebox.showwarning(
                "Validación",
                "Seleccione una categoría."
            )
            return None

        try:
            precio_numero = float(precio)

            if precio_numero <= 0:
                raise ValueError

        except ValueError:

            messagebox.showwarning(
                "Validación",
                "El precio debe ser un número mayor que cero."
            )

            return None

        try:
            stock_numero = int(stock)

            if stock_numero < 0:
                raise ValueError

        except ValueError:

            messagebox.showwarning(
                "Validación",
                "El stock debe ser un número entero mayor o igual a cero."
            )

            return None

        return (
            nombre,
            categoria,
            precio_numero,
            stock_numero
        )

    # =================================================
    # NUEVO
    # =================================================

    def nuevo_producto(self):

        self.limpiar_formulario()

        nuevo_id = self.servicio.obtener_siguiente_id()

        self.id_entry.config(
            state="normal"
        )

        self.id_entry.insert(
            0,
            str(nuevo_id)
        )

        self.id_entry.config(
            state="readonly"
        )

        self.nombre_entry.focus()

    # =================================================
    # GUARDAR
    # =================================================

    def guardar_producto(self):

        datos = self.obtener_datos_formulario()

        if datos is None:
            return

        nombre, categoria, precio, stock = datos

        try:

            producto = self.servicio.agregar_producto(
                nombre,
                categoria,
                precio,
                stock
            )

            messagebox.showinfo(
                "Producto guardado",
                f"El producto '{producto.nombre}' fue registrado correctamente."
            )

            self.cargar_productos()
            self.limpiar_formulario()

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"No fue posible guardar el producto.\n{error}"
            )

    # =================================================
    # EDITAR
    # =================================================

    def editar_producto(self):

        if self.producto_seleccionado is None:

            messagebox.showwarning(
                "Editar",
                "Seleccione un producto de la tabla."
            )

            return

        datos = self.obtener_datos_formulario()

        if datos is None:
            return

        nombre, categoria, precio, stock = datos

        actualizado = self.servicio.actualizar_producto(
            self.producto_seleccionado,
            nombre,
            categoria,
            precio,
            stock
        )

        if actualizado:

            messagebox.showinfo(
                "Producto actualizado",
                "El producto fue actualizado correctamente."
            )

            self.cargar_productos()
            self.limpiar_formulario()

        else:

            messagebox.showerror(
                "Error",
                "No se encontró el producto."
            )

    # =================================================
    # ELIMINAR
    # =================================================

    def eliminar_producto(self):

        seleccion = self.tabla.selection()

        if not seleccion:

            messagebox.showwarning(
                "Eliminar",
                "Seleccione un producto de la tabla."
            )

            return

        valores = self.tabla.item(
            seleccion[0],
            "values"
        )

        id_producto = int(
            valores[0]
        )

        nombre_producto = valores[1]

        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Desea eliminar '{nombre_producto}'?"
        )

        if not confirmar:
            return

        eliminado = self.servicio.eliminar_producto(
            id_producto
        )

        if eliminado:

            messagebox.showinfo(
                "Producto eliminado",
                "El producto fue eliminado correctamente."
            )

            self.cargar_productos()
            self.limpiar_formulario()

        else:

            messagebox.showerror(
                "Error",
                "No fue posible eliminar el producto."
            )

    # =================================================
    # LIMPIAR
    # =================================================

    def limpiar_formulario(self):

        self.producto_seleccionado = None

        self.id_entry.config(
            state="normal"
        )

        self.id_entry.delete(
            0,
            tk.END
        )

        self.id_entry.config(
            state="readonly"
        )

        self.nombre_entry.delete(
            0,
            tk.END
        )

        self.categoria_combo.set("")

        self.precio_entry.delete(
            0,
            tk.END
        )

        self.stock_entry.delete(
            0,
            tk.END
        )

        for item in self.tabla.selection():
            self.tabla.selection_remove(item)

    # =================================================
    # CERRAR SESIÓN
    # =================================================

    def cerrar_sesion(self):

        confirmar = messagebox.askyesno(
            "Cerrar sesión",
            "¿Desea cerrar la sesión?"
        )

        if confirmar:

            self.root.destroy()

            self.on_logout()
