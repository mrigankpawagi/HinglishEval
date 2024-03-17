
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
    grades_list = list(grades)
    grades_list.sort(reverse=True)
    result = []
    
    try:
        letter_grade = []
        grad_range = range(3, 4.1, 0.1)
        
        # Gives the result of the calculation based on grades list
        for g in grad_range:
            # Gives percentage 
            grades_ratio = float(g)/5
            grades_list.append(grades_ratio)
            
            # Gets the letter grade string based on the calculated percentage
            for a in grades_list:
                if int(a) > 1:
                    letter_grade = 'B-'
                elif int(a) > 1.3:
                    letter_grade = 'C-'
                elif int(a) > 1