
def iscube(a):
    """
    Ek function likho jo ek integer a leta hai aur True return karta hai 
    agar yeh integer kisi integer number ka cube hai.
    Dhyan de: aap maan sakte ho ki input hamesha valid hoga.
    Udaharan:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    """
    if(0<a<=100):
        return(True)
    return(False)
#%%
"""
9. Create a function “cube_generator” that takes two parameters x & y and computes the x,y-th cube. 
Hint: This can be done in a single line using a built-in function like np.power(x,y).
Test this using some of the examples given for you below.
"""
#%%
"""
10. Create a function “prime_generator” which takes 3 parameters and returns a list of all the numbers 
	from the lowest prime to the highest prime (inclusive). For example, if the parameters are (1,100,5) then you 
	should return [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]. If the 3 
	parameter is set to (1,1,5), then you should return only the list [2,3,5]
"""
#%%
"""
11. Create a list from 1 to 100 with 4 steps between each element. 
Note: Create it manually.
"""
#%%
"""
12. Create a list from 1 to 100 and, in the middle, create a sublist which will increase the middle number by one. 
Hint:
"""
#%%
from copy import deepcopy
