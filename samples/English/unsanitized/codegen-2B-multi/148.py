
def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''
    # First, check if planet1 is a planet
    if planet1 not in planets_list:
        return None

    # Second, check if planet2 is a planet
    if planet2 not in planets_list:
        return None

    # Third, check if planet2 is closer to planet1
    d_t = get_distance(planet1, planet2)  # distance to planet1
    for planet in planets_list:  # check the rest
        if planet == planet1 or planet == planet2:
            continue
        if planet is not None:
            if d_t < get_distance(planet1, planet):
                return None
    return planets_list[:]


