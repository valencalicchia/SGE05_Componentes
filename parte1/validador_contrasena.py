import re

def validar_contrasena(password):
    """
    Valida si una contraseña cumple con los requisitos de seguridad básicos.
    
    Requisitos:
    1. Longitud mínima de 8 caracteres
    2. No debe contener espacios
    3. Debe contener al menos una letra minúscula
    4. Debe contener al menos una letra mayúscula
    5. Debe contener al menos un dígito numérico
    6. Debe contener al menos un carácter especial (no alfanumérico)
    
    Parámetros:
        password (str): La contraseña a validar
        
    Retorna:
        bool: True si la contraseña es válida, False si no cumple con los requisitos
    """
    
    # Validación 1: Longitud mínima de 8 caracteres y sin espacios
    if len(password) < 8 or ' ' in password:
        return False  # No cumple con el tamaño mínimo o contiene espacios
    
    # Validación 2: Al menos una letra minúscula
    if not any(c.islower() for c in password):
        return False  # Falta letra minúscula
    
    # Validación 3: Al menos una letra mayúscula
    if not any(c.isupper() for c in password):
        return False  # Falta letra mayúscula
    
    # Validación 4: Al menos un dígito numérico
    if not any(c.isdigit() for c in password):
        return False  # Falta número
    
    # Validación 5: Al menos un carácter especial (no alfanumérico)
    if not re.search(r'[^a-zA-Z0-9]', password):
        return False  # Falta carácter especial
    
    # Si pasa todas las validaciones, la contraseña es válida
    return True