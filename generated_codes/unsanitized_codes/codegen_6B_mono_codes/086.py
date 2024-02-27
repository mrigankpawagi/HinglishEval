
def anti_shuffle(s):
    """
    Ek function likho jo ek string leta hai aur uska ordered version return karta hai.
    Ordered version of string, woh string hoti hai jahan saare words (space se separated)
    ko ek naye word se replace kiya jata hai jahan saare characters ko 
    unke ascii value ke basis pe ascending order mein arrange kiya jata hai.
    Dhyan do: Aapko words aur blank spaces ki order sentence mein maintain karni chahiye.

    Jaise ki:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello!!!Wdlor'
    """
    s = s.lower().strip().split()
    result = ""
    for i in range(len(s)):
        result += s[i][-int(i%2==1)-1]+s[i][-int(i%2==0)-1]
    return result

#-----------------------------------------------------------------------

## 22. Generate a random number between 1-6, and ask to guess it. Use a while loop and if else 
## statement to perform this task, but without the use of random module.

