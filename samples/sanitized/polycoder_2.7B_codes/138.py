def is_equal_to_sum_even(n):
    """
    Evaluate karo ki diya gaya number n kya exactly 4 positive even numbers ka sum ho sakta hai
    Udaharan
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # n = 3
    # d[s] <- [[[0.8, 0.6, 0.4],[ 0.2, 0.7, 0.5]],
    #         [[0.7, 0.8, 0.6],[ 0.5, 0.4, 0.3]],
    #         [[0.5, 0.5, 0.4],[ 0.6, 0.4, 0.3]],]
    # k = [[-1.2, -0.8, 0], [-0.7, -0.6, 0.2], [-0.4, -0.2, 0.4]]
    # s = [[], [], [], []]
    d = np.array([[0.8, 0.6, 0.4], [0.2, 0.7, 0.5], [0.5, 0.5, 0.4], [0.6, 0.4, 0.3]])
    k = [[4], [4], [6], []]  # s, x_array, y_array
    s = []
    k_sum = 4  # s, x_array, y_array
    sum_even = np.array([0.8, 0.6, 0.4, 0.7])

    is_true_sum = is_equal_to_
