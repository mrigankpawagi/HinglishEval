
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

    planet1 = str(planet1)
    planet2 = str(planet2)
    planet_dict = {planet1: planet2 for v in range(1,5)}
    while len(planet_dict)!= 0:
        first_name = getFirstName(planet1)
        if first_name not in planet_dict:
            planet_dict[first_name] = planet2
        else:
            for v in range(1,5):
                second_name = getSecondName(planet1[v-1])
                if (v+1) not in planet_dict and second_name not in planet_dict:
                    planet_dict[