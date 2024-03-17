
def is_equal_to_sum_even(n):
    """
    Evaluate karo ki diya gaya number n kya exactly 4 positive even numbers ka sum ho sakta hai
    Udaharan
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    def find_square(n):
        return n.square_if_squared(n)
    def calculate(karo, ki):
        """
                Evaluate karo ki diya gaya number n kya exactly 4 positive odd numbers ka sakta hai
                Udaharan
                calculate_square( 4 ) == True
                calculate_square( 6 ) == True
                calculate_square( 8 ) == True
                calculate_square( 12 ) == True
                calculate_square( 16 ) == True
                calculate_square( 20 ) == True
                calculate_square( 21 ) == True
                calculate_square( 22 ) == True
                calculate_square( 24 ) == True
                calculate_square( 28 ) == True
                calculate_square( 0 ) == True