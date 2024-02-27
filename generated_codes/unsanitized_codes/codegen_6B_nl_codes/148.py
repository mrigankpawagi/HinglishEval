
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
    orbit1, orbit2, planet1, planet2 = input().split(',')
    if not planet1 in {'Mercury', 'Mars', 'Earth', 'Jupiter', 'Saturn', 'Venus', 'Uranus', 'Neptune'}:
        print("Bol ke dikhao ki aap ka doosain koi planet par khone hi nahi hai")
        return -1
    elif planet2 not in {'Mercury', 'Mars', 'Earth', 'Jupiter', 'Saturn', 'Venus', 'Uranus', 'Neptune'}:
        print("Bol ke dikhao ki aap ka doosain koi planet par khone hi nahi hai")
        return -1

    elif orbit1 == "Earth": # Planet Jupiter
        orbits = orbit2.split("")
        for i in range