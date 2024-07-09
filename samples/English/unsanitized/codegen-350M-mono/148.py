
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
    planet1 = planet1.lower()
    planet2 = planet2.lower()

    if planet1 =='saturn':
        sun = 'neptune'
    elif planet1 =='venus':
        sun = 'jupiter'
    elif planet1 == 'earth':
        sun ='mercury'
    else:
        print('Error')
        sys.exit(0)

    if planet2 =='sun':
        if sun == 'jupiter':
            if planet2 =='mars':
                return ('mars', 'jupiter')
            elif planet2 =='venus':
                return ('venus', 'earth','mars')
            elif planet2 == 'neptune':
                return ('neptune','sun')
        elif sun =='mars':
            if planet2 == 'earth':
                return ('earth', 'jupiter','mars') 
            elif planet2 =='venus':
                return ('venus', 'neptune','mars')
            elif planet2 =='mercury':
                return ('mercury','venus', 'jupiter')
        elif sun =='venus':
            if planet