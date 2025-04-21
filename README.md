# 🛡️ Sistema de Gestión de Riesgos – Backend

¡Bienvenido al backend del **Sistema de Gestión de Riesgos Laborales**!  
Este proyecto está construido con **Django** + **Django REST Framework**, y forma parte de una solución integral para la gestión de empleados, documentos y riesgos laborales en organizaciones.

---

## 📦 Tecnologías utilizadas

- 🐍 **Python 3.10+**
- 🌐 **Django** y **Django REST Framework**
- 🗂️ Modularización profesional por apps (`apps/`)
- 🔐 **JWT Authentication**
- 🗃️ **MariaDB / MySQL compatible**
- 📂 Gestión de documentos con `FileField` y estructura organizada por tipo/fecha

---

## ⚙️ Instalación del proyecto

```bash
# 1️⃣ Clona el repositorio
git clone https://github.com/xxkfjfredxx/sgr_backend.git
cd sgr_backend

# 2️⃣ Crea un entorno virtual
python -m venv venv
venv\Scripts\activate      # (En Windows)
# source venv/bin/activate  # (En Linux/macOS)

# 3️⃣ Instala las dependencias
pip install -r requirements.txt

# 4️⃣ Aplica migraciones
python manage.py migrate

# 5️⃣ Crea un superusuario (opcional)
python manage.py createsuperuser

# 6️⃣ Ejecuta el servidor
python manage.py runserver
