{
    "name": "Importación de Clientes",
    "version": "1.0",
    "depends": ["base"],
    "category": "Tools",
    "author": "Valentina Alessandra",
    "summary": "Importar clientes desde un archivo CSV",
    "description": "Permite importar clientes desde un archivo CSV a Odoo.",
    "data": [
        "security/ir.model.access.csv",
        "views/import_clientes_view.xml",
    ],
    "installable": True,
    "application": True,
}
