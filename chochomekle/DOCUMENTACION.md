# Proyecto Chochomekle

## Descripción
Sistema Django para reservar espacios de coworking. Incluye interfaz web y API REST.

## Cómo ejecutar

1. Instalar dependencias:
pip install -r requirements.txt

2. Ejecutar migraciones:
python manage.py migrate

3. Crear superusuario:
python manage.py createsuperuser

4. Iniciar servidor:
python manage.py runserver

## API REST

- `GET /api/espacios/` — Listar espacios disponibles
- `GET /api/reservas/?cliente=Juan` — Filtrar reservas por cliente
- `POST /api/reservas/nueva/` — Crear reserva
- `GET /api/clientes/<id>/` — Detalles del cliente
- `PUT /api/reservas/<id>/actualizar/` — Actualizar estado
