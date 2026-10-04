EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calcula el tiempo de horneado restante.

    :param elapsed_bake_time: int - tiempo que la lasaña lleva horneándose.
    :return: int - tiempo restante de horneado (en minutos).
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calcula el tiempo total de preparación según el número de capas.

    :param number_of_layers: int - número de capas de la lasaña.
    :return: int - tiempo total de preparación en minutos.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calcula el tiempo total transcurrido cocinando.

    :param number_of_layers: int - número de capas.
    :param elapsed_bake_time: int - tiempo transcurrido en el horno.
    :return: int - tiempo total en minutos.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    
    
