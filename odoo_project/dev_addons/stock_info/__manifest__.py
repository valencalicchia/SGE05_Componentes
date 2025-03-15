{
    'name': 'Stock Information',
    'version': '1.0',
    'summary': 'Módulo para consultar y exportar información de stock',
    'description': 'Permite consultar productos y exportar su stock a un archivo CSV.',
    'author': 'Tu Nombre',
    'depends': ['base', 'stock'],
    'data': [
        'views/stock_info_views.xml',
    ],
    'installable': True,
    'application': True,
}