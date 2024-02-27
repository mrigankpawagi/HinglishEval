
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
    #return planet1, planet2
    if planet1 == "Sol":
        return planet2
    elif planet2 == "Sun":
        return "Sun"
    elif (planet1[0][1] == "J" and planet1[0][2] == "R" and planet1[0][3] == "H" and planet2[0][1] == "J" and planet2[0][2] == "R" and planet2[0][3] == "H" and planet2[0][4] == "S") or (planet1[0][1] == "J" and planet1[0][2] == "R" and planet1[0][3] == "A" and planet1[0][4] == "N") or (planet2[0][1] == "J" and planet2[0][2] == "R" and planet2[0][3] == "A" and planet2[0][4] == "N") or (planet1[0][1] == "E" and planet1[0][2] == "S"