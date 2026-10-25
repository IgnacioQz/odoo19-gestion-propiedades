# Módulo de práctica: Gestión de Propiedades (Odoo 19)

Módulo a medida desarrollado como práctica, en una VM Ubuntu con Docker Compose (Odoo 19 + PostgreSQL 16).

## Qué incluye
- Modelo `cb.propiedad` con campo calculado (`@api.depends`) y validaciones (`@api.constrains`)
- Permisos por grupo (`ir.model.access.csv`)
- Vistas de lista, formulario y búsqueda, acción y menú
- Botones de estado: disponible → reservada → vendida
- Herencia de `res.partner` (`_inherit`) y de su vista (`xpath`)

## Cómo levantarlo
    docker compose up -d
    # http://localhost:8069 -> crear base de datos -> Apps -> instalar "Gestión de Propiedades"

Credenciales del compose: solo para uso local de práctica.
