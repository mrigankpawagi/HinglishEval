
def order_by_points(nums):
    """
    Ek function likho jo diye gaye integers ki list ko unke digits ka sum ke hisaab se ascending order mein sort kare.
    Dhyan do: agar kuch items ke digits ka sum similar ho, 
    toh unhe original list ke index ke basis par order karo.

    Jaise ki:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

    temp = []
    list_with_points = []
    # list_with_points.sort(key=lambda x: sum(int (i) for i in str(x)))
    #return list_with_points


        
    for x in nums:
        str_x = str(x)
        print("str_x", str_x)
        #list_with_points.sort(key=lambda x: sum(int (i) for i in str(x)))
        list_with_points.append(str_x)







if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n\nALL TESTS PASSED! NOW DO THESE EXERCISES ON PAPER!\n\n")
