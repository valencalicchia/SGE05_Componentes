import re

def validar_nombre_usuario(username):
    if len(username) < 6:
        return 1, "El nombre de usuario debe contener al menos 6 caracteres"
    if len(username) > 12:
        return 2, "El nombre de usuario no puede contener más de 12 caracteres"
    if not re.match(r"^[a-zA-Z0-9]*$", username):
        return 3, "El nombre de usuario puede contener solo letras y números"
    return 0, "El nombre de usuario es válido"