
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
    
    def calculate_letter_grade(grade):
        if not 1 <= grade <= 100:
            return "Invalid value!" 
        else:
            return 'C'
        
    def check_letter_grade(grade):
        if grade not in ['A+', 'B', 'C-', 'C', 'A-', 'D', 'D', "E"]:
            return "Invalid value!"
        else:
            return grade
    
    if grades.count(Numerical_letter_grade(grades)) == len(grades):
        return grades
    else:
        grades = [Numerical_letter_grade(grade) for grade in grades]
        grades = [grade for grade in grades if grade]
        grades.sort(key = lambda grade: (-float(grade), grade))
        
        best_grade = calculate_letter_grade(grade)
        students_correct = grades.count(best_grade)
        grades_in_group = grades.count(best_grade)
        grades_