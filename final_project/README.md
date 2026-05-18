# 🗓️ Administrador de Eventos - Flask + MySQL

Este proyecto permite gestionar eventos donde **organizadores** pueden crear y administrar eventos, y **participantes** pueden visualizarlos. Además, los **administradores** pueden gestionar usuarios y roles. Es el Proyecto 4 dentro de una colección de 11 proyectos desarrollados como práctica final para los estudiantes.

## 🚀 Tecnologías utilizadas

- **Flask** – Framework backend en Python
- **Flask-Login** – Sistema de autenticación
- **MySQL** – Base de datos relacional
- **SQLAlchemy** – ORM para la base de datos
- **Bootstrap 5** – Framework CSS responsivo
- **Jinja2** – Motor de plantillas para HTML

---

## 📂 Estructura del proyecto

| Archivo / Carpeta | Descripción |
| ------------------------------------------------ | -------------------------------------------------------------------------- |
| `create_demo_users.py` | Script para crear usuarios iniciales con roles y contraseñas |
| `config.py` | Configuración de Flask (DB URI, claves, etc.) |
| `README.md` | Este archivo de documentación del proyecto |
| `requirements.txt` | Lista de paquetes Python requeridos |
| `run.py` | Punto de entrada para ejecutar el servidor Flask |
| `app/__init__.py` | Inicializa la aplicación Flask y carga la configuración |
| `app/models.py` | Contiene los modelos SQLAlchemy: User, Role, Evento |
| `app/forms.py` | Formularios de Flask-WTF usados en login, registro, eventos, contraseñas |
| `app/routes.py` | Rutas principales del proyecto (dashboard, eventos, cambiar contraseña) |
| `app/auth_routes.py` | Rutas para autenticación (login, registro, logout) |
| `app/test_routes.py` | Rutas para pruebas de los endpoints del CRUD |
| `app/templates/layout.html` | Plantilla base HTML con barra de navegación |
| `app/templates/index.html` | Página de inicio pública del sitio |
| `app/templates/login.html` | Formulario de inicio de sesión |
| `app/templates/register.html` | Formulario de registro con selección de rol |
| `app/templates/dashboard.html` | Panel principal del usuario autenticado |
| `app/templates/evento_form.html` | Formulario de creación/edición de eventos |
| `app/templates/usuarios.html` | Listado de usuarios con sus roles (solo para admins) |
| `app/templates/cambiar_password.html` | Formulario para cambiar la contraseña del usuario |
| `database_schema/04_eventos.sql` | SQL para crear la base de datos y tablas del proyecto |
| `pruebas/` | Archivos .rest para probar los endpoints del CRUD |

---

## 🧪 Requisitos previos

- Python 3.8 o superior
- MySQL Server corriendo localmente (`localhost:3306`)
- Un entorno virtual activo (opcional, pero recomendado)

---

## ⚙️ Instalación del proyecto

1. **Clonar el repositorio**

```bash
   git clone https://github.com/bonillaylen-7/comp2052.git
   cd comp2052/final_project
```

2. **Instalar dependencias**

```bash
   pip install -r requirements.txt
```

3. **Crear la base de datos en MySQL**

```bash
   mysql -u root -p < database_schema/04_eventos.sql
```

4. **Crear usuarios de prueba**

```bash
   python create_demo_users.py
```

5. **Ejecutar la aplicación**

```bash
   python run.py
```

   Luego abre en tu navegador: `http://127.0.0.1:5000`

---

## 👤 Credenciales de prueba

| Rol | Usuario | Email | Contraseña |
| ------------ | ----------------- | ------------------------- | --------------- |
| Admin | admin_demo | admin@eventos.com | admin123 |
| Organizador | organizador_demo | organizador@eventos.com | organizador123 |
| Participante | participante_demo | participante@eventos.com | participante123 |

---

## 🧠 Licencia

Este proyecto es de uso académico y puede ser reutilizado con fines educativos indicando las referencias correspondientes. Este proyecto y la lista de proyectos son creaciones originales del profesor Javier A. Dastas de Ciencias de Computadoras.