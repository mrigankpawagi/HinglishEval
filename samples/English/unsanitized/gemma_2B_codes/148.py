
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
    planets = []
    planets.extend(planetlist(planet1))
    planets.extend(planetlist(planet2))
    planets = sorted(planets)
    return tuple(planets[planet_index(planets[i], planets[i+1]) : planet_index(planets[i+1], planets[i])])
    
def planetlist(planet):
    planetlist = []
    for i in range(0, 9):
        if planet == 'Mercury' or planet == 'Mars' or planet == 'Venus' or planet == 'Earth' or planet == 'Jupiter' or planet == 'Saturn':
            if i == 0:
                planetlist.append(planet)
            else:
                n = int(i)
                planetlist.append(str(n))
                return planetlist
        elif planet == 'Neptune' or planet == 'Uranus' or planet == 'Sun':
            planetlist.append(planet)                
    return planetlist
    
def planet_index(planet1, planet2):
    c = 0
    planets = planetlist(planet2)
    while c < len(planets):
        if planet2 == planets[c]:
            return c
        c += 1
    return c
