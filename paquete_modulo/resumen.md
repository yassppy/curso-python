# Paquete y Módulo

## Paquete

Es una carpeta que Python reconoce como importable (accesible desde `sys.path`, ya sea directamente o como subpaquete de algo que sí lo está).

- Si tiene `__init__.py`, se llama **paquete tradicional** (regular package), y `__file__` apunta a ese `__init__.py`.
- Si no tiene `__init__.py`, es un **namespace package** (PEP 420). En este caso `__file__` no existe o es `None`, según la versión de Python. Un namespace package ni siquiera necesita contener archivos `.py` para existir — una carpeta vacía reconocida en el path también puede funcionar como uno.
- Al comprobar con `__file__` (o su ausencia), se puede determinar si es un paquete tradicional o un namespace package.

## Módulo

- Es cualquier archivo `.py`, esté suelto o dentro de un paquete.
- Al comprobar con `__file__`, imprime la ruta directa del archivo `.py` correspondiente.

## Resumen

```
app/
├── funcion_directa/  --> PAQUETE (Namespace, sin __init__.py)
│   └── despedida.py  --> MÓDULO dentro de un paquete
├── paquete/          --> PAQUETE (Tradicional)
│   ├── __init__.py
│   └── saludo.py     --> MÓDULO dentro de un paquete
├── main.py           --> MÓDULO suelto (Archivo principal)
└── validador_email.py--> MÓDULO suelto (Módulo raíz)
```

### Notas clave

- **Paquete tradicional**: `__file__` → ruta al `__init__.py`.
- **Namespace package**: sin `__file__` real (o `None`), y no requiere contener módulos `.py` para existir.
- **Módulo**: `__file__` → ruta directa al archivo `.py`.
