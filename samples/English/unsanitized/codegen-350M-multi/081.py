
def numerical_letter_grade(grades):
    """It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of GPAs for some students and you have to write 
    a function that can output a list of letter grades using the following table:
             GPA       |    Letter grade
              4.0                A+
            > 3.7                A 
            > 3.3                A- 
            > 3.0                B+
            > 2.7                B 
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+ 
            > 0.7                D 
            > 0.0                D-
              0.0                E
    

    Example:
    grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
    """
    return(grade_grade(grades, 'A') + grade_grade(grades, 'B') + grade_grade(grades, 'C-E'))


##
# It will output your result in csv format.
#
# Example:
# grade_equation([4.0, 3, 1.5, 2.7]) ==> 4, A, A-G, A+G

#
# Example for a non-terminating equation with a non-terminating sum operation:
# grade_equation([1.0, 1.5, 2.0, 2.7]) ==> 4, A, A+G 

#
# An alternative to using these functions to show a list of the grade of a grade.
# grade_grade(grades, letter) ==> print(letter_grade(grades))

