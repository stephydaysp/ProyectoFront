# ProyectoFront — Proyecto 1 Asignatura Back End

Pequeño proyecto base en **Django** (proyecto `proyectofront` + app `Pfront`) con una vista inicial y template.

## Requisitos
- Python 3.10+ (probado con 3.13)
- Git

## Cómo clonar e instalar

### macOS / Linux
```bash
git clone https://github.com/stephydaysp/ProyectoFront.git
cd ProyectoFront
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

### Windows (PowerShell)
```powershell
git clone https://github.com/stephydaysp/ProyectoFront.git
cd ProyectoFront
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## Instrucciones para clonar y probar Actividad 2

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/stephydaysp/ProyectoFront.git
   cd ProyectoFront
2. Crear entorno virtual y activarlo:

En macOS / Linux:
python3 -m venv .venv
source .venv/bin/activate

En Windows (PowerShell):
python -m venv .venv
.venv\Scripts\Activate

3. Instalar dependencias:
pip install -r requirements.txt

4. Aplicar migraciones:
python manage.py makemigrations
python manage.py migrate

5. Crear superusuario (usuario/clave: inacap):
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('inacap','inacap@example.com','inacap')"

6. Levantar el servidor y entrar a:
http://127.0.0.1:8000/admin/
Usuario: inacap
Clave: inacap


