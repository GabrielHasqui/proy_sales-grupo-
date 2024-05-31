from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex=r'^\d{9,15}$', message="El número de teléfono debe contener entre 9 y 15 dígitos.")
 
def valida_cedula(value):
    cedula = str(value)
    if not cedula.isdigit():
        raise ValidationError('La cédula debe contener solo números.')

    longitud = len(cedula)
    if longitud != 10:
        raise ValidationError('La cédula debe tener 10 dígitos.')

    coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
    total = 0
    for i in range(9):
        digito = int(cedula[i])
        coeficiente = coeficientes[i]
        producto = digito * coeficiente
        if producto > 9:
            producto -= 9
        total += producto

    digito_verificador = (total * 9) % 10
    if digito_verificador != int(cedula[9]):
        raise ValidationError('La cédula no es válida.')


def valida_decimal(value):
    numero = str(value)
    # Verifica si el valor tiene un solo punto decimal y el resto son dígitos
    if numero.count('.') > 1 or not numero.replace('.', '', 1).isdigit():
        raise ValidationError('El valor debe ser un número decimal válido.')

    return float(numero)  # Devuelve el número como float

def valida_numero(value):
    numero = str(value)
    
    # Verifica si el valor contiene solo dígitos
    if not numero.isdigit():
        raise ValidationError('El valor debe contener solo números.')
    
    return int(numero)  # Devuelve el número como entero

def valida_letras(value):
    letras = str(value)
    
    # Verifica si el valor contiene solo letras
    if not letras.isalpha():
        raise ValidationError('El valor debe contener solo letras.')

    return letras

