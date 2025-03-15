import re

def validar_contrasena(password):
    if len(password) < 8 or ' ' in password:
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not re.search(r'[^a-zA-Z0-9]', password):
        return False
    return True