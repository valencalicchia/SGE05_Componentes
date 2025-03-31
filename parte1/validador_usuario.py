import re

def validar_nombre_usuario(username):
    """
    Valida un nombre de usuario según los siguientes criterios:
    
    1. Longitud entre 6 y 12 caracteres
    2. Solo caracteres alfanuméricos (letras y números)
    3. Sin espacios ni caracteres especiales
    
    Parámetros:
        username (str): Nombre de usuario a validar
        
    Retorna:
        tuple: (código, mensaje) donde:
               - código: 0 si es válido, 1-3 para errores específicos
               - mensaje: Descripción del resultado de validación
    """
    
    # Validación 1: Longitud mínima de 6 caracteres
    if len(username) < 6:
        return 1, "El nombre de usuario debe contener al menos 6 caracteres"
    
    # Validación 2: Longitud máxima de 12 caracteres
    if len(username) > 12:
        return 2, "El nombre de usuario no puede contener más de 12 caracteres"
    
    # Validación 3: Solo caracteres alfanuméricos (expresión regular)
    if not re.match(r"^[a-zA-Z0-9]*$", username):
        return 3, "El nombre de usuario puede contener solo letras y números"
    
    # Si pasa todas las validaciones
    return 0, "El nombre de usuario es válido"