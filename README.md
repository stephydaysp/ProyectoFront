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

