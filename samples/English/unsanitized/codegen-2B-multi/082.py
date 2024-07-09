
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    is_prime = True
    count_max = prime_length_method(string, 2, 10)
    """I didn't want to do this with for-loops. However I didn't have another
     chance to write a function that took string as input and returns True"""
    for n in range(2, abs(count_max)):
        for d in range(2, n):
            is_prime = is_prime and prime_length_method(string, d, n) #this works for
                                                                        #testing the
                                                                        #method to ensure
                                                                        #that any prime
                                                                        #was less than
                                                                        #the end of
                                                                        #calculating
        if is_prime: #return the true for the is prime
            return True
    return False

tasks = [('Primes.', prime_length), ]

for input_task_name, input_task_function in tasks:
    #check if the question exists
    if (not questions_exist(input_task_name)):
        print('Question not found!')
        continue
     #if the task exists and is not already completed
    if (question_is_completed(input_task_name)):
        print('Task Has Been Completed!')
        continue
    else:
        continue
    q_id = get_question_id(input_task_name)
    if (len(get_answers(q_id)) == 0):
        #add user an answer
        add_answer(q_id, 1)
    for i in range(1000):
        print(input_task_function(get_answers(q_id)[i], input_task_name))
