"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate):
    
    """Calcula el valor de la moneda cambiada.

    :param budget: float - cantidad de dinero a cambiar.
    :param exchange_rate: float - precio de una unidad de moneda extranjera.
    :return: float - valor obtenido en la nueva moneda.
    """

    return budget / exchange_rate

    pass


def get_change(budget, exchanging_value):
    
    """Calcula la cantidad devuelta del presupuesto original.

    :param budget: float - cantidad inicial antes del cambio.
    :param exchanging_value: float - dinero tomado para cambiar.
    :return: float - dinero restante del presupuesto.
    """
    
   

    return budget - exchanging_value

    pass


def get_value_of_bills(denomination, number_of_bills):
    
    """Calcula el valor total de un número de billetes.

    :param denomination: int - valor de un solo billete.
    :param number_of_bills: int - número total de billetes.
    :return: int - valor total del conjunto de billetes.
    """
    
    
    return denomination * number_of_bills

    pass


def get_number_of_bills(amount, denomination):
    
    """Calcula el número de billetes completos que se pueden obtener.

    :param amount: float - cantidad de dinero recibida.
    :param denomination: int - valor de cada billete.
    :return: int - número entero de billetes.
    """
    
    
    return int (amount// denomination)
    pass


def get_leftover_of_bills(amount, denomination):
    
    """Calcula la cantidad sobrante que no cabe en billetes completos.

    :param amount: float - cantidad de dinero a convertir.
    :param denomination: int - valor de cada billete.
    :return: float - residuo sobrante.
    """
    
   
    return amount % denomination
    pass


def exchangeable_value(budget, exchange_rate, spread, denomination):
    
    """Calcula el valor máximo intercambiable en billetes enteros considerando comisiones.

    :param budget: float - presupuesto a cambiar.
    :param exchange_rate: float - tasa de cambio base.
    :param spread: int - porcentaje de comisión.
    :param denomination: int - valor de los billetes entregados.
    :return: int - valor máximo recibido en billetes enteros.
    """
    
    
    actual_rate = exchange_rate * (1+ (spread/100))
    exchanged_amount = exchange_money(budget, actual_rate)
    number_of_bills = get_number_of_bills(exchanged_amount, denomination)

    return get_value_of_bills (denomination, number_of_bills)
    pass
