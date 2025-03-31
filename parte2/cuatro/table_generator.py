import csv

class GestionTabla:
    def __init__(self):
        self.datos = []

    def solicitar_datos(self):
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
        direccion = input("Ingrese la dirección: ")
        contrasena = input("Ingrese la contraseña: ")

        self.datos.append({
            "Nombre": nombre,
            "Apellido": apellido,
            "Fecha Nacimiento": fecha_nacimiento,
            "Dirección": direccion,
            "Contraseña": contrasena
        })
        print("Datos almacenados con éxito!\n")

    def buscar_datos(self):
        criterio = input("Ingrese el nombre o apellido a buscar: ")
        resultados = [dato for dato in self.datos if dato["Nombre"] == criterio or dato["Apellido"] == criterio]
        
        if resultados:
            for resultado in resultados:
                print(resultado)
        else:
            print("No se encontraron coincidencias.\n")

    def guardar_csv(self, archivo="datos.csv"):
        with open(archivo, mode='w', newline='', encoding='utf-8') as f:
            campos = ["Nombre", "Apellido", "Fecha Nacimiento", "Dirección", "Contraseña"]
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(self.datos)
        print("Datos guardados en CSV!\n")

    def cargar_csv(self, archivo="datos.csv"):
        try:
            with open(archivo, mode='r', encoding='utf-8') as f:
                lector = csv.DictReader(f)
                self.datos.extend(lector)
            print("Datos cargados desde 'datos.csv'!\n")
        except FileNotFoundError:
            print("El archivo 'datos.csv' no existe.\n")

    def menu(self):
        while True:
            print("Menú:")
            print("1. Solicitar datos")
            print("2. Buscar datos")
            print("3. Guardar en CSV")
            print("4. Cargar desde CSV")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.solicitar_datos()
            elif opcion == "2":
                self.buscar_datos()
            elif opcion == "3":
                self.guardar_csv()
            elif opcion == "4":
                self.cargar_csv()
            elif opcion == "5":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida, intente de nuevo.\n")

if __name__ == "__main__":
    app = GestionTabla()
    app.menu()
