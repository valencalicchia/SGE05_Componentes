import xmlrpc.client
import csv
import re
from html import unescape


class OdooStockManager:
    """
    Clase para la gestión completa de inventario en Odoo mediante XML-RPC.
    
    Proporciona funcionalidades para:
    - Conexión con servidor Odoo
    - Consulta de productos
    - Obtención de detalles de productos
    - Exportación de datos a CSV
    - Interfaz de menú interactivo
    
    Atributos:
        url (str): URL del servidor Odoo
        db (str): Nombre de la base de datos
        user (str): Usuario para autenticación
        password (str): Contraseña para autenticación
        uid (int): ID de usuario autenticado
        api (ServerProxy): Objeto para llamadas API XML-RPC
    """
    
    def __init__(self, url="http://localhost:8069", db="valen", user="valen@gmail.com", password="admin"):
        """
        Inicializa el gestor de stock con parámetros de conexión.
        
        Parámetros:
            url (str): URL del servidor Odoo (default: "http://localhost:8069")
            db (str): Nombre de la base de datos (default: "valen")
            user (str): Email del usuario (default: "valen@gmail.com")
            password (str): Contraseña (default: "admin")
        """
        # Configuración de conexión
        self.url = url      # URL base del servidor Odoo
        self.db = db        # Nombre de la base de datos
        self.user = user    # Usuario para autenticación
        self.password = password  # Contraseña para autenticación
        self.uid = None     # User ID (se establece al conectar)
        self.api = None     # Objeto API (se establece al conectar)
        
        # Conectar automáticamente al inicializar
        self._connect()
    
    def _connect(self):
        """
        Establece conexión con el servidor Odoo mediante XML-RPC.
        
        Realiza:
        1. Autenticación con las credenciales proporcionadas
        2. Configuración del proxy para llamadas a la API
        
        Excepciones:
            ValueError: Si las credenciales son inválidas
            Exception: Para otros errores de conexión
        """
        try:
            # Conexión al endpoint común de Odoo
            common = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/common")
            
            # Autenticación y obtención del UID
            self.uid = common.authenticate(self.db, self.user, self.password, {})
            
            if not self.uid:
                raise ValueError("Credenciales inválidas")
                
            # Configuración del proxy para llamadas a objetos
            self.api = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/object")
            
        except Exception as e:
            print(f"Error de conexión: {e}")
            # Nota: En producción sería mejor manejar esto con logging y excepciones específicas
    
    def get_products(self):
        """
        Obtiene todos los productos del inventario desde Odoo.
        
        Returns:
            list: Lista de diccionarios con información de productos o lista vacía en caso de error
            
        Campos incluidos:
            - id: Identificador único del producto
            - default_code: Código de referencia
            - name: Nombre del producto
            - qty_available: Cantidad disponible en stock
        """
        try:
            return self.api.execute_kw(
                self.db, self.uid, self.password,
                "product.template",          # Modelo Odoo
                "search_read",               # Método
                [[]],                        # Dominio (vacío para todos)
                {"fields": ["id", "default_code", "name", "qty_available"]}  # Campos a recuperar
            )
        except Exception as e:
            print(f"Error obteniendo productos: {e}")
            return []  # Retorna lista vacía para manejo elegante de errores
    
    def get_product_details(self, product_id):
        """
        Obtiene información detallada de un producto específico.
        
        Parámetros:
            product_id (int): ID del producto a consultar
            
        Returns:
            dict: Diccionario con los detalles del producto o None si no se encuentra
        """
        try:
            data = self.api.execute_kw(
                self.db, self.uid, self.password,
                "product.template",
                "search_read",
                [[["id", "=", product_id]]],  # Filtro por ID específico
                {"fields": ["id", "default_code", "name", "qty_available"]}
            )
            return data[0] if data else None  # Retorna el primer resultado o None
        except Exception as e:
            print(f"Error obteniendo detalle del producto: {e}")
            return None
    
    def save_stock_to_csv(self, filename="stock_list_cinco.csv"):
        """
        Exporta el listado de stock actual a un archivo CSV.
        
        Parámetros:
            filename (str): Nombre del archivo CSV a generar (default: "stock_list_cinco.csv")
            
        Proceso:
        1. Obtiene todos los productos
        2. Ordena alfabéticamente por nombre
        3. Limpia formato HTML de los nombres
        4. Genera CSV con columnas: Código, Nombre, Stock
        """
        try:
            products = self.get_products()
            with open(filename, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=["Código", "Nombre", "Stock"])
                writer.writeheader()
                
                # Procesa cada producto: ordena, limpia HTML y escribe en CSV
                for product in sorted(products, key=lambda x: x["name"].lower()):
                    writer.writerow({
                        "Código": product["default_code"] or "N/A",  # Maneja valores nulos
                        "Nombre": unescape(re.sub(r'<[^>]+>', '', product["name"])),  # Limpia HTML
                        "Stock": product["qty_available"]  # Cantidad disponible
                    })
            print(f"Archivo CSV generado: {filename}")
        except Exception as e:
            print(f"Error generando CSV: {e}")
    
    def run_menu(self):
        """
        Ejecuta el menú interactivo principal con las siguientes opciones:
        
        1. Mostrar productos: Lista todos los productos con ID y nombre
        2. Ver detalles de producto: Muestra información detallada de un producto específico
        3. Exportar stock a CSV: Genera archivo CSV con el inventario actual
        4. Salir: Termina la ejecución del programa
        """
        while True:
            print("\nMenú de Gestión de Stock")
            print("1. Mostrar productos")
            print("2. Ver detalles de un producto")
            print("3. Exportar stock a CSV")
            print("4. Salir")
            choice = input("Seleccione una opción: ")
            
            if choice == "1":
                # Opción 1: Listar todos los productos
                print("\nListado de Productos:")
                for product in self.get_products():
                    print(f"{product['id']}: {product['name']}")
                    
            elif choice == "2":
                # Opción 2: Detalles de producto específico
                try:
                    product_id = int(input("Ingrese el ID del producto: "))
                    details = self.get_product_details(product_id)
                    
                    if details:
                        print("\nDetalles del Producto:")
                        print(f"Código: {details['default_code']}")
                        print(f"Nombre: {details['name']}")
                        print(f"Stock disponible: {details['qty_available']}")
                    else:
                        print("Producto no encontrado.")
                        
                except ValueError:
                    print("Error: Debe ingresar un ID numérico válido.")
                    
            elif choice == "3":
                # Opción 3: Exportar a CSV
                self.save_stock_to_csv()
                print("Exportación completada.")
                
            elif choice == "4":
                # Opción 4: Salir
                print("Saliendo del sistema...")
                break
                
            else:
                print("Opción inválida, por favor intente de nuevo.")


if __name__ == "__main__":
    # Punto de entrada principal - solo se ejecuta al llamar directamente al script
    print("Iniciando Gestor de Stock Odoo...")
    manager = OdooStockManager()  # Crea instancia del gestor
    manager.run_menu()           # Inicia el menú interactivo