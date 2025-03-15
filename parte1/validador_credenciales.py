# credential_validator.py

# Importar los módulos de validación de username y password
from validador_usuario import validar_nombre_usuario
from validador_contrasena import validar_contrasena


def solicitar_y_validar_credenciales():
    # Solicitar nombre de usuario
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    codigo, mensaje = validar_nombre_usuario(nombre_usuario)
    
    # Validar nombre de usuario
    if codigo != 0:
        print(f"Error: {mensaje}")
        return
    
    # Solicitar contraseña
    contraseña = input("Ingrese su contraseña: ")
    
    # Validar contraseña
    if validar_contrasena(contraseña):
        print("¡Credenciales válidas! Bienvenido.")
    else:
        print("Error: La contraseña no es válida. Asegúrese de que cumpla con los requisitos.")

def probar_casos_ejemplo():
    # Casos de ejemplo para nombres de usuario y contraseñas
    casos = [
        # Nombre de usuario válido, contraseña válida
        {"usuario": "Usuario123", "contraseña": "Passw0rd!"},
        
        # Nombre de usuario inválido (menos de 6 caracteres)
        {"usuario": "User", "contraseña": "Passw0rd!"},
        
        # Nombre de usuario inválido (más de 12 caracteres)
        {"usuario": "UsuarioConMasDe12Caracteres", "contraseña": "Passw0rd!"},
        
        # Nombre de usuario inválido (caracteres no alfanuméricos)
        {"usuario": "Usuario@123", "contraseña": "Passw0rd!"},
        
        # Contraseña inválida (menos de 8 caracteres)
        {"usuario": "Usuario123", "contraseña": "Pwd1!"},
        
        # Contraseña inválida (sin letras mayúsculas)
        {"usuario": "Usuario123", "contraseña": "passw0rd!"},
        
        # Contraseña inválida (sin números)
        {"usuario": "Usuario123", "contraseña": "Password!"},
        
        # Contraseña inválida (sin caracteres no alfanuméricos)
        {"usuario": "Usuario123", "contraseña": "Password1"},
        
        # Contraseña inválida (con espacios en blanco)
        {"usuario": "Usuario123", "contraseña": "Passw 0rd!"},
    ]
    
    # Probar cada caso
    for caso in casos:
        print(f"\nProbando caso: Usuario: {caso['usuario']}, Contraseña: {caso['contraseña']}")
        codigo, mensaje = validar_nombre_usuario(caso["usuario"])
        if codigo != 0:
            print(f"Error en nombre de usuario: {mensaje}")
        else:
            if validar_contrasena(caso["contraseña"]):
                print("¡Credenciales válidas! Bienvenido.")
            else:
                print("Error: La contraseña no es válida. Asegúrese de que cumpla con los requisitos.")

# Ejecutar el programa
if __name__ == "__main__":
    print("=== Modo interactivo ===")
    solicitar_y_validar_credenciales()
    
    # print("\n=== Casos de ejemplo ===")
    # probar_casos_ejemplo()