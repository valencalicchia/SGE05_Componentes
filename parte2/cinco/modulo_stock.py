import xmlrpc.client
import csv
import re
from html import unescape


class OdooConnector:
    """
    Clase encargada de gestionar la conexión con el servidor Odoo.
    """
    def __init__(self, url="http://localhost:8069", db="valen", user="valen@gmail.com", password="admin"):
        self.url = url
        self.db = db
        self.user = user
        self.password = password
        self.uid = None
        self.api = None
        self.connect()

    def connect(self):
        try:
            common = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/common")
            self.uid = common.authenticate(self.db, self.user, self.password, {})
            if not self.uid:
                raise ValueError("Credenciales inválidas")
            self.api = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/object")
        except Exception as e:
            print(f"Error de conexión: {e}")


class StockManager:
    """
    Clase para la gestión del stock en Odoo.
    """
    def __init__(self, connector):
        self.connector = connector

    def get_products(self):
        try:
            return self.connector.api.execute_kw(
                self.connector.db, self.connector.uid, self.connector.password,
                "product.template", "search_read", [[]],
                {"fields": ["id", "default_code", "name", "qty_available"]}
            )
        except Exception as e:
            print(f"Error obteniendo productos: {e}")
            return []

    def get_product_details(self, product_id):
        try:
            data = self.connector.api.execute_kw(
                self.connector.db, self.connector.uid, self.connector.password,
                "product.template", "search_read", [[[ "id", "=", product_id ]]],
                {"fields": ["id", "default_code", "name", "qty_available"]}
            )
            return data[0] if data else None
        except Exception as e:
            print(f"Error obteniendo detalle del producto: {e}")
            return None

    def save_stock_to_csv(self, filename="stock_list.csv"):
        try:
            products = self.get_products()
            with open(filename, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=["Código", "Nombre", "Stock"])
                writer.writeheader()
                for product in sorted(products, key=lambda x: x["name"].lower()):
                    writer.writerow({
                        "Código": product["default_code"] or "N/A",
                        "Nombre": unescape(re.sub(r'<[^>]+>', '', product["name"])),
                        "Stock": product["qty_available"]
                    })
            print(f"Archivo CSV generado: {filename}")
        except Exception as e:
            print(f"Error generando CSV: {e}")


if __name__ == "__main__":
    connection = OdooConnector()
    stock_manager = StockManager(connection)
    while True:
        print("\nMenú de Gestión de Stock")
        print("1. Mostrar productos")
        print("2. Ver detalles de un producto")
        print("3. Exportar stock a CSV")
        print("4. Salir")
        choice = input("Seleccione una opción: ")
        if choice == "1":
            for product in stock_manager.get_products():
                print(f"{product['id']}: {product['name']}")
        elif choice == "2":
            try:
                product_id = int(input("Ingrese el ID del producto: "))
                details = stock_manager.get_product_details(product_id)
                if details:
                    print(f"Código: {details['default_code']}, Nombre: {details['name']}, Stock: {details['qty_available']}")
                else:
                    print("Producto no encontrado.")
            except ValueError:
                print("ID inválido.")
        elif choice == "3":
            stock_manager.save_stock_to_csv()
        elif choice == "4":
            break
        else:
            print("Opción inválida, intente de nuevo.")


