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
    a_tuple = (planet1[0], planet1[1]), (planet2[0], planet2[1])
    a_dict = dict(a_tuple)
    b_tuple_list = []
    for key, value in a_dict.items():
        b_tuple = (value[0], value[1]), (
            str(a_dict[key + "_0"])[:-1] + "_1",
            str(a_dict[key + "_0"])[:-1] + "_2",
        )
        b_tuple_list.append(b_tuple)
    return b_tuple_list
