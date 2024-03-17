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
    if planet1 is planet2:
        return planet1
    m1 = re.search("^([A-Za-z]+)$", planet1.lower())
    m2 = re.search("^([A-Za-z]+)$", planet2.lower())
    if m1 and m2:
        return tuple(
            m1.group(1) for m1 in bf_khanda(m1.groups() + [planet1] + m2.groups())
        )
    elif not m1 and not m2:
        return planet1