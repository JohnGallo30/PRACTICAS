
def eat_ghost(power_pellet_active, touching_ghost):
    
        
    
    """Devuelve true si pac-man se comió el fantasma """
    return power_pellet_active and touching_ghost
    


def score(touching_power_pellet, touching_dot):

    
    """Devuelve true, si suma puntos

    """
    return touching_power_pellet or touching_dot




def lose(power_pellet_active, touching_ghost):

    
    """Devuelve true si pierde
    """
    return touching_ghost and not power_pellet_active
    


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    
    
    """Devuelve true si gana
    """
    return has_eaten_all_dots and not lose (power_pellet_active, touching_ghost)