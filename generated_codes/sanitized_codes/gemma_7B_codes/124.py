
def valid_date(date):
    """
    Aapko ek function likhna hai jo diye gaye date string ko validate karta hai aur
    agar date valid hai to True return karta hai, nahi to False.
    Date tabhi valid hogi jab niche diye gaye saare rules satisfy ho:
    1. Date string khali nahi honi chahiye.
    2. Dinon ki sankhya 1 se kam ya 31 se adhik na ho mahino 1,3,5,7,8,10,12 ke liye. Aur dinon ki sankhya 1 se kam ya 30 se adhik na ho mahino 4,6,9,11 ke liye. Aur, dinon ki sankhya 1 se kam ya 29 se adhik na ho mahine 2 ke liye.
    3. Mahine ki sankhya 1 se kam ya 12 se adhik na ho.
    4. Date ka format aisa hona chahiye: mm-dd-yyyy

    jaise ki: 
    valid_date('03-11-2000') => True

    valid_date('15-01-2012') => False

    valid_date('04-0-2040') => False

    valid_date('06-04-2020') => True

    valid_date('06/04/2020') => False
    """
    # Your code here
    if date == "":
        return False
    else:
        date = date.split("-")
        if len(date) != 3:
            return False
        else:
            if int(date[0]) < 1 or int(date[0]) > 12:
                return False
            else:
                if int(date[1]) < 1 or int(date[1]) > 31:
                    return False
                else:
                    if int(date[2]) < 1 or int(date[2]) > 9999:
                        return False
                    else:
                        if int(date[0]) == 2:
                            if int(date[1]) > 29:
                                return False
                        elif int(date[0]) in [1, 3, 5, 7, 8, 10, 12]:
                            if int(date[1]) > 31:
                                return False
                        elif int(date[0]) in [4, 6, 9, 11]:
                            if int(date[1]) > 30:
                                return False
                        else:
                            return True
