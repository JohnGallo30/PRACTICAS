def is_armstrong_number(number):
    number_text= str(number)
    potencia = len(number_text)
    suma = 0

    for caracter in number_text:
        digito= int (caracter)
        suma += digito ** potencia

    return suma == number
        
