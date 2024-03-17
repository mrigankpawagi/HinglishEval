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
    # your code here
    return [letter_grade(gpa) for gpa in grades]


def letter_grade(gpa):
    """
    Returns the letter grade corresponding to the given GPA.
    """
    # your code here
    if gpa >= 4.0:
        return "A+"
    elif gpa >= 3.7:
        return "A"
    elif gpa >= 3.3:
        return "A-"
    elif gpa >= 3.0:
        return "B+"
    elif gpa >= 2.7:
        return "B"
    elif gpa >= 2.3:
        return "B-"
    elif gpa >= 2.0:
        return "C+"
    elif gpa >= 1.7:
        return "C"
    elif gpa >= 1.3:
        return "C-"
    elif gpa >= 1.0:
        return "D+"
    elif gpa >= 0.7:
        return "D"
    elif gpa >= 0.0:
        return "D-"
    else:
        return "E"
