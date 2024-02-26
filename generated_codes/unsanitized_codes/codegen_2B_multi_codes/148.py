
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
    def bf1(planet1, planet2, orbits):
        if planet1 == "" or planet2 == "":
            return orbits
        else:
            for p in orbits:
                if p.name == planet1:
                    return orbits
                for p2 in orbits:
                    if p.name!= planet1 and p2.name!= planet2 and p2 in planet1.orbit[p] \
                    or p2.name!= planet2 and p.name!= planet2 and p2 in planet2.orbit[p]:
                        return orbits
    return bf1

