def bf(planet1, planet2):
    """
    Hamare solar system mein aath grah hain: sabse paas Suraj ke Mercury hai, uske baad Venus, phir Earth, Mars, Jupiter, Saturn, Uranus, Neptune.
    Ek function likho jo do grahon ke naam planet1 aur planet2 ko strings ke roop mein leta hai.
    Function ko ek tuple return karna chahiye jisme saare grah hain jinke orbits planet1 aur planet2 ke orbit ke beech mein hote hain, Suraj ke nazdeek hone ke hisaab se sort kiye gaye.
    Agar planet1 ya planet2 sahi grah ke naam nahi hain to function ko ek khali tuple return karna chahiye.
    Udaharan
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    """
    planets = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune",
    ]
    if planet1 not in planets or planet2 not in planets:
        return ()
    index1 = planets.index(planet1)
    index2 = planets.index(planet2)
    if index1 > index2:
        index1, index2 = index2, index1
    return tuple(planets[index1 + 1 : index2])
