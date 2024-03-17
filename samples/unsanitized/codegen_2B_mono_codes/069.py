
def search(lst):
    """
    Aapko ek non-empty list di gayi hai positive integers ki. Return karo sabse bada integer jo zero se bada ho, 
    aur uska frequency us integer ke value ke barabar ya usse zyada ho. 
    Ek integer ka frequency uski list mein kitni baar aane ki sankhya hoti hai.
    Agar aisa koi value nahi hai, to -1 return karo.
    Udaharan:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    """
    
    #if lst == None or len(lst) == 0:
    #    return -1
    count = -1
    m = 0
    for i in lst:
        if i < 0:
            return -1

    return count


if __name__ == "__main__":
    lst = get_input(11, "list.txt")
    print(f"Enter length of integers:\t {12}")
    for i in lst:
        print(f"Enter numbers for list:\t {i}", end= "\t")
    print()
    s1=time.time()
    # print(print_output())
    output = search(lst)
    print(f"Total output from solution {s1}", f"Time taken to code {time.time() - s1}\n {output}")
