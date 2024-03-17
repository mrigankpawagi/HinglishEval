
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
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 in planets and planet2 in planets:
        planets.remove(planet1)
        planets.remove(planet2)
        planets.sort()
        return planets
    else:
        return ()


# Question 2
def is_prime(n):
    """
    Ek function likho jo ek integer n ko input le aur uske liye ek boolean return kare.
    Function true return karega agar n prime hai, aur false return karega agar n prime nahi hai.
    Udaharan
    is_prime(1) ==> False
    is_prime(2) ==> True
    is_prime(3) ==> True
    is_prime(4) ==> False
    is_prime(5) ==> True
    is_prime(6) ==> False
    is_prime(7) ==> True
    is_prime(8) ==> False
    is_prime(9) ==> False
    is_prime(10) ==> False
    is_prime(11) ==> True
    is_prime(12) ==> False
    is_prime(13) ==> True
    is_prime(14) ==> False
    is_prime(15) ==> False
    is_prime(16) ==> False
    is_prime(17) ==> True
    is_prime(18) ==> False
    is_prime(19) ==> True
    is_prime(20) ==> False
    is_prime(21) ==> False
    is_prime(22) ==> False
    is_prime(23) ==> True
    is_prime(24) ==> False
    is_prime(25) ==> False
    is_prime(26) ==> False
    is_prime(27) ==> False
    is_prime(28) ==> False
    is_prime(29) ==> True
    is_prime(30) ==> False
    is_prime(31) ==> True
    is_prime(32) ==> False
    is_prime(33) ==> False
    is_prime(34) ==> False
    