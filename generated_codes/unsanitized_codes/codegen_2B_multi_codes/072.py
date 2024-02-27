
def will_it_fly(q,w):
    """
    Ek function likho jo True return kare agar object q udega, aur False otherwise.
    Object q tabhi udega jab vo balanced ho (yani ki ek palindromic list ho) aur uske elements ka sum maximum possible weight w se kam ya barabar ho.

    Udaharan:
    will_it_fly([1, 2], 5) ➞ False 
    # 1+2 maximum possible weight se kam hai, lekin ye balanced nahi hai.

    will_it_fly([3, 2, 3], 1) ➞ False
    # ye balanced hai, lekin 3+2+3 maximum possible weight se jyada hai.

    will_it_fly([3, 2, 3], 9) ➞ True
    # 3+2+3 maximum possible weight se kam hai, aur ye balanced hai.

    will_it_fly([3], 5) ➞ True
    # 3 maximum possible weight se kam hai, aur ye balanced hai.
    """
    return all(e in q if len([n for n in (q+[w]) if n > 0]) <= len(q) and len([n for n in (q+[w]) if n > 0]) == len(q))
                
# This solution will be more difficult.
if __name__ == "__main__":
    # Read the file containing the sequence of numbers to be searched for in
    # from the command line if provided else from the console.
    s = read_input() if len(sys.argv) > 1 else input().split()
    # Now search through the file for every combination of the numbers in the list.
    c = []
    for w in range(1, max_weight):
        for j in range(s[0]-1, len(s)):
            if w <= j:
                # Get the number of elements to the right and the left of the number 
                # in the combination.
                x = j - s[j] + 1
                y = s[j+1] - s[x] - 1
                # Check the if the number