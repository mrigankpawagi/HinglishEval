
def fruit_distribution(s,n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for examble:
    fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
    """
    
    def distribute(s, n):

    	total_size = n

    	for apple in string.printable:
     		for orange in string.printable:
     			if apple == orange and n < total_size:
     				apple_value = apple_or_orange(n - str(total_size - apple_total_size[n])
     				total_size += apple_value
					break

     		return total_size
        
    		return 0

    	return -1

    	def apple_or_orange(n):
		if n >= 50:
        		return 10
		if n >= 40:
        		return 5
		if n >= 30:
			return 3
		return 0

	def string.printable(s):
    	return set(string.ascii_lowercase +
   