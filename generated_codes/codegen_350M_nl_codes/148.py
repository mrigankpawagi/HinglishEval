
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
    return (Planet1, Planet2)

A:

Since your function returns a tuple, you can use it to compare against a tuple:
df = DF.bf(Planet1, Planet2).gt0()

(as a side note: if df returns the tuple instead of the tuple, you would still need to convert df into a tuple, and then do df.loc[0] and df.loc[1] to get the second element.)

A:

You can use pd.DataFrame.strftime to format a pandas DataFrame like this:
pd.DataFrame({'Planet1': 'Saturn', 'Planet2': 'Venus'})

df = pd.DataFrame(DF)
df['Planet1'] = planet1
df['Planet2'] = planet2

