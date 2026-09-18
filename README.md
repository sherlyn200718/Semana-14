# RESTAURANTE APP

Aplicación gráfica desarrollada en Python utilizando Tkinter para la
gestión básica de productos de un restaurante.

## 1. Objetivo

El proyecto tiene como objetivo aplicar los fundamentos de interfaces
gráficas estudiados durante la Semana 14:

- Componentes gráficos.
- Contenedores.
- Formularios.
- Tablas.
- Controles de acción.
- Validación básica.
- Separación modular del proyecto.

La aplicación permite iniciar sesión y administrar los productos
registrados en un archivo JSON.

---

## 2. Tecnologías utilizadas

- Python 3
- Tkinter
- ttk
- JSON
- Programación orientada a objetos

Tkinter forma parte de la instalación estándar de Python, por lo que
normalmente no es necesario instalar paquetes adicionales.

---

## 3. Estructura del proyecto

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── assets/
├── main.py
└── README.md

4. Funcionalidades
Inicio de sesión
La aplicación dispone de una pantalla de inicio de sesión.

Usuarios de prueba:

Usuario: admin
Contraseña: 1234

También puede utilizarse:

Usuario: mesero
Contraseña: 1234

Gestión de productos
La ventana principal permite:

Visualizar productos.

Registrar productos.

Editar productos.

Eliminar productos.

Limpiar el formulario.

Cerrar sesión.

5. Formulario
El formulario contiene los siguientes campos:

ID.

Nombre.

Categoría.

Precio.

Stock.

La categoría se selecciona mediante un componente Combobox.

El ID se genera automáticamente.

6. Tabla
Los productos se muestran mediante un componente Treeview.

La tabla contiene:

ID

Nombre

Categoría

Precio

Stock

Al seleccionar un producto de la tabla, sus datos se cargan en
el formulario para poder editarlos.

7. Contenedores utilizados
Se utilizan diferentes contenedores para organizar la interfaz:

Frame
Se utiliza para agrupar componentes relacionados.

LabelFrame
Se utiliza para crear secciones visuales:

Datos del producto.

Listado de productos.

Inicio de sesión.

8. Componentes utilizados
La aplicación utiliza:

Label

Entry

Button

Combobox

Treeview

Scrollbar

Frame

LabelFrame

9. Persistencia
Los productos se almacenan en:

datos/productos.json

Los usuarios se almacenan en:

datos/usuarios.json

La clase ArchivoServicio se encarga de realizar la lectura y escritura
de los archivos JSON.

10. Arquitectura
El proyecto mantiene una arquitectura modular.

modelos/
Contiene las clases que representan los datos.

servicios/
Contiene la lógica relacionada con archivos y operaciones del restaurante.

ui/
Contiene las ventanas y componentes de la interfaz gráfica.

datos/
Contiene los archivos JSON utilizados para almacenar la información.

main.py
Es el punto de entrada de la aplicación.

11. Ejecución
Abrir una terminal dentro de la carpeta del proyecto:

cd restaurante_app

Ejecutar:

python main.py

En algunos sistemas puede ser necesario utilizar:

python3 main.py

12. Flujo de funcionamiento
Se ejecuta main.py.

Se muestra la pantalla de inicio de sesión.

El usuario introduce sus credenciales.

El sistema valida los datos mediante RestauranteServicio.

Si las credenciales son correctas, se abre la ventana principal.

Los productos se cargan desde productos.json.

El usuario puede registrar, editar o eliminar productos.

Los cambios se almacenan nuevamente en productos.json.

El usuario puede cerrar sesión y regresar al formulario de acceso.

13. Validaciones
La aplicación realiza validaciones básicas:

El nombre es obligatorio.

La categoría es obligatoria.

El precio debe ser numérico.

El precio debe ser mayor que cero.

El stock debe ser un número entero.

El stock no puede ser negativo.

Para editar se debe seleccionar un producto.

Para eliminar se debe seleccionar un producto.

14. Conclusión
El proyecto aplica los fundamentos de interfaces gráficas mediante
componentes y contenedores, manteniendo una arquitectura modular.

La interfaz permite demostrar el uso de formularios, tablas y controles
de acción dentro de una aplicación práctica para la administración de
productos de un restaurante.


## 15. ¿Qué puntos de la actividad quedan cubiertos?

Con este proyecto tienes una correspondencia bastante directa con lo solicitado:

| Requisito | Implementación |
|---|---|
| Arquitectura modular | `modelos`, `servicios`, `ui`, `datos` |
| Componentes | `Label`, `Entry`, `Button`, `Combobox`, `Treeview` |
| Contenedores | `Frame` y `LabelFrame` |
| Formularios | Login y formulario de productos |
| Tablas | `ttk.Treeview` |
| Controles de acción | Nuevo, Guardar, Editar, Eliminar, Limpiar, Cerrar sesión |
| Datos | Archivos JSON |
| Modelo | `Producto` y `Usuario` |
| Servicios | `ArchivoServicio` y `RestauranteServicio` |
| Punto de entrada | `main.py` |
| Persistencia | Lectura/escritura de `productos.json` |
| Validación | Formulario de productos y login |
| README | Incluido |
| Eventos avanzados | No son necesarios |

### Para ejecutarlo

Crea exactamente las carpetas y archivos anteriores, copia cada código en su archivo correspondiente y finalmente ejecuta:

```bash
python main.py

Credenciales de prueba: admin / 1234.
