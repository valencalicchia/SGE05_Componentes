from validador_usuario import validar_nombre_usuario
from validador_contrasena import validar_contrasena

def solicitar_y_validar_credenciales():
    """
    Función principal que solicita y valida credenciales de usuario de forma interactiva.
    
    Flujo:
    1. Solicita nombre de usuario y lo valida
    2. Si el nombre es válido, solicita contraseña
    3. Valida la contraseña según los requisitos
    4. Informa al usuario si las credenciales son válidas o muestra mensajes de error
    """
    # Solicitar nombre de usuario
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    
    # Validar nombre de usuario (asume que validar_nombre_usuario retorna (codigo, mensaje))
    codigo, mensaje = validar_nombre_usuario(nombre_usuario)
    
    # Si hay error en el nombre de usuario, mostrar y terminar
    if codigo != 0:
        print(f"Error: {mensaje}")
        return  # Termina la función si el nombre no es válido
    
    # Solicitar contraseña solo si el nombre es válido
    contraseña = input("Ingrese su contraseña: ")
    
    # Validar contraseña (asume que validar_contrasena retorna True/False)
    if validar_contrasena(contraseña):
        print("¡Credenciales válidas! Bienvenido.")
    else:
        print("Error: La contraseña no es válida. Asegúrese de que cumpla con los requisitos.")

def probar_casos_ejemplo():
    """
    Función de prueba que ejecuta varios casos de ejemplo para validar el sistema.
    
    Casos incluidos:
    - Combinaciones de nombres de usuario válidos e inválidos
    - Combinaciones de contraseñas válidas e inválidas
    - Casos extremos y valores límite
    """
    # Lista de casos de prueba
    casos = [
        # Caso 1: Todo válido
        {"usuario": "Usuario123", "contraseña": "Passw0rd!"},
        
        # Caso 2: Nombre de usuario inválido (menos de 6 caracteres)
        {"usuario": "User", "contraseña": "Passw0rd!"},
        
        # Caso 3: Nombre de usuario inválido (más de 12 caracteres)
        {"usuario": "UsuarioConMasDe12Caracteres", "contraseña": "Passw0rd!"},
        
        # Caso 4: Nombre de usuario inválido (caracteres no alfanuméricos)
        {"usuario": "Usuario@123", "contraseña": "Passw0rd!"},
        
        # Caso 5: Contraseña inválida (menos de 8 caracteres)
        {"usuario": "Usuario123", "contraseña": "Pwd1!"},
        
        # Caso 6: Contraseña inválida (sin letras mayúsculas)
        {"usuario": "Usuario123", "contraseña": "passw0rd!"},
        
        # Caso 7: Contraseña inválida (sin números)
        {"usuario": "Usuario123", "contraseña": "Password!"},
        
        # Caso 8: Contraseña inválida (sin caracteres especiales)
        {"usuario": "Usuario123", "contraseña": "Password1"},
        
        # Caso 9: Contraseña inválida (con espacios)
        {"usuario": "Usuario123", "contraseña": "Passw 0rd!"},
    ]
    
    # Probar cada caso
    for caso in casos:
        print(f"\nProbando caso: Usuario: {caso['usuario']}, Contraseña: {caso['contraseña']}")
        
        # Validar nombre de usuario
        codigo, mensaje = validar_nombre_usuario(caso["usuario"])
        
        if codigo != 0:
            print(f"Error en nombre de usuario: {mensaje}")
        else:
            # Validar contraseña solo si el nombre es válido
            if validar_contrasena(caso["contraseña"]):
                print("¡Credenciales válidas! Bienvenido.")
            else:
                print("Error: La contraseña no es válida. Asegúrese de que cumpla con los requisitos.")

if __name__ == "__main__":
    """
    Punto de entrada principal del programa.
    
    Ejecuta:
    1. Modo interactivo (solicita credenciales al usuario)
    2. Opcionalmente, modo de prueba con casos predefinidos
    """
    print("=== Modo interactivo ===")
    solicitar_y_validar_credenciales()
    
    # Descomentar para ejecutar casos de prueba
    # print("\n=== Casos de ejemplo ===")
    # probar_casos_ejemplo()