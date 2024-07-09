
def numerical_letter_grade(grades):
    """
    Yeh semester ka aakhri week hai aur teacher ko students ko grades dena hai.
    Teacher ne apna khud ka algorithm banaya hai grading ke liye.
    Sirf ek problem hai, unhone jo code use kiya tha grading ke liye, woh kho gaya hai.
    Unhone aapko kuch students ke GPAs ki list di hai aur aapko ek function likhna hai 
    jo letter grades ki list output kar sake, neeche diye gaye table ke hisaab se:
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
    validate_list_grades(grades)

    # for every grade in the order of the grade
    for grade in grades:
        # if grade is equal to 1.0
        if grade == 0.0:
            # replace 1.0 with 'A'
            grade = 'A'
        # if grade is great than 1.0,
        elif grade >= 2.0:
            # replace 1.0 with "B" + add '-+' character to grade
            grade = "B" + "-" + str(round(0.5 + grade - 2.0, 1))
        elif grade >= 1.0:
            # replace 1.0 with "C" + add '---' character to grade
            grade = "C" + "-" + str(round(0.5 + grade - 1.0,