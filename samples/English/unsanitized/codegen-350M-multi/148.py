
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
    
    # This part just allows me to write this logic in Python by 
    # hand.
    # For reference I wrote this myself in the previous comment to the
    # program, and that means a full code. This is what the answer 
    # to the comment is.
    _a1 = "Jupiter"
    _b1 = "Jupiter"
    _b2 = "Jupiter"
    _a2 = "Neptune"
    _c1 = "Uranus"
    _b1c = "Uranus"
    # Make two lists. The one with Jupiter is the list. The one with
    # Mercury, then Uranus. Then the two lists that are then compared. 
    # Then for the planets from Mercury to Uranus, return the list of 
    # the planets, sorted by proximity to the planet. 
    
    # If either planet name does not identify its Jupiter and
    # Uranus, then return an empty list of the planets.
    if _b1!= _b2:
        _list1 = bf(_a1, _b1)
        _list2 = bf(_b1c, _b2)
     
        # Get the planets with the right orbits.
