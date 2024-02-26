
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
    for x in range(0, len(planet1)):
        for y in range(0, len(planet2)):
            if planet1[x] == planet2[y]:
                return planet1[x]

# bf("Planet One", "PlanetTwo")
"""
print bf("Planet One", "PlanetTwo")
"""
"""
if planet1 == planet2
else:
    pass
"""

while 1:
    pass
"""
print
"""
print bf("Jupiter", "Neptune")
"""
"""
planet1 = ("Planet One", "Planet Two", "Planet Three")
planet2 = ("Earth", "Jupiter")
planet3 = ("Mars", "Saturn")
listPlanet = (planet1, planet2, planet3)

print bf(planet1, planet2)
"""
planet1 = ("Planet One", "Planet Two", "Planet Three")
planet2 = ("Earth", "Jupiter")
planet3 = ("Mars", "Saturn")
listPlanet = (planet1, planet2, planet3)
print b