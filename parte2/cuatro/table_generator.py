import csv

class GestionTabla:
    """
    Clase para gestionar una tabla de datos de personas con operaciones CRUD básicas
    y persistencia en archivos CSV.
    
    Atributos:
        datos (list): Lista que almacena diccionarios con la información de las personas
    """
    
    def __init__(self):
        """Inicializa la clase con una lista vacía para almacenar los datos."""
        self.datos = []  # Lista para almacenar los registros de personas

    def solicitar_datos(self):
        """
        Solicita al usuario los datos de una persona y los almacena en la lista.
        
        Campos solicitados:
        - Nombre
        - Apellido
        - Fecha de nacimiento (formato YYYY-MM-DD)
        - Dirección
        - Contraseña (en texto claro, sin encriptar)
        """
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
        direccion = input("Ingrese la dirección: ")
        contrasena = input("Ingrese la contraseña: ")

        # Añade un nuevo diccionario con los datos a la lista
        self.datos.append({
            "Nombre": nombre,
            "Apellido": apellido,
            "Fecha Nacimiento": fecha_nacimiento,
            "Dirección": direccion,
            "Contraseña": contrasena  # Nota: En producción debería encriptarse
        })
        print("Datos almacenados con éxito!\n")

    def buscar_datos(self):
        """
        Busca registros por nombre o apellido y muestra los resultados.
        
        Realiza una búsqueda exacta (case-sensitive) en los campos Nombre y Apellido.
        Muestra todos los registros que coincidan con el criterio de búsqueda.
        """
        criterio = input("Ingrese el nombre o apellido a buscar: ")
        # List comprehension para filtrar los datos
        resultados = [dato for dato in self.datos 
                     if dato["Nombre"] == criterio or dato["Apellido"] == criterio]
        
        if resultados:
            print("\nResultados encontrados:")
            for resultado in resultados:
                print(resultado)
        else:
            print("No se encontraron coincidencias.\n")

    def guardar_csv(self, archivo="datos_cuatro.csv"):
        """
        Guarda los datos actuales en un archivo CSV.
        
        Parámetros:
            archivo (str): Nombre del archivo CSV (default: 'datos_cuatro.csv')
            
        Crea el archivo si no existe, lo sobrescribe si ya existe.
        """
        campos = list(self.datos[0].keys())

        with open(archivo, mode='w', newline='', encoding='utf-8') as f:
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(self.datos)

        print(f"Datos guardados en '{archivo}'!\n")

    def cargar_csv(self, archivo="datos_cuatro.csv"):
        """
        Carga datos desde un archivo CSV a la lista interna.
        
        Parámetros:
            archivo (str): Nombre del archivo CSV a cargar (default: 'datos_cuatro.csv')
            
        Si el archivo no existe, muestra un mensaje de error sin interrumpir el programa.
        """
        try:
            with open(archivo, mode='r', encoding='utf-8') as f:
                lector = csv.DictReader(f)
                self.datos.extend(lector)  # Añade los datos cargados a los existentes
            print(f"Datos cargados desde '{archivo}'!\n")
        except FileNotFoundError:
            print(f"El archivo '{archivo}' no existe.\n")

    def menu(self):
        """
        Muestra un menú interactivo con las operaciones disponibles.
        
        Opciones:
        1. Solicitar datos - Añade un nuevo registro
        2. Buscar datos - Busca registros por nombre/apellido
        3. Guardar en CSV - Exporta los datos a archivo
        4. Cargar desde CSV - Importa datos desde archivo
        5. Salir - Termina la ejecución del programa
        """
        while True:
            print("\nMenú de Gestión de Datos:")
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
    # Punto de entrada principal del programa
    app = GestionTabla()  # Crea una instancia de la clase
    app.menu()  # Inicia el menú interactivo