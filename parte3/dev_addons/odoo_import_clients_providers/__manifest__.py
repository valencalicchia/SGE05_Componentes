{
    'name': "Importar CSV",
    'version': '1.0',
    'author': "Valentina Calicchia",
    'summary': 'Importa contactos desde CSV y los clasifica como clientes/proveedores',
    'depends': ['base', 'contacts'],
    'data': [
        'data/contact_category.xml',
        'views/contact_import_wizard_view.xml',
    ],
    'installable': True,
    'application': True,
}