
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
    assert ( planet1, planet2 )
    #print "the planets"
    planet1 = astropy.core.extent.bbox2str(planet1)
    #print "the bbox of planet 1"
    planet2 = astropy.core.extent.bbox2str(planet2)
    #print "the bbox of planet 2"
    planets = ( planet1[0]- planet2[0])**2+\
              ( planet1[1]- planet2[1])**2
    result = []
    is_equal = False
    while len(result) < 8: 
        if ( planet1[2] - planet2[2] )**2 + \
           (planet1[0] - planet2[0])**2 + \
           (planet1[1] - planet2[1])**2 / planets
