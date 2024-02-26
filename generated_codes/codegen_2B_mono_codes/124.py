
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
    dates = {
            '01': 31,
            '03': 31,
            '04': 30,
            '05': 31,
            '08': 31,
            '09': 30,
            '10': 31,
            '11': 30,
            '12': 31
            }
    if not isinstance(date, str):
        return False 
    
    date = date.split()
    if len(date)!= 3:
        return False
    
    date[0] = date[0].lower().strip()
    date[1] = int(date[1].strip().replace('-', ''))
    date[2] = int(date[2].strip())
    check_date = {'01':1, '03':1, '04':30, '05':31, '08':31, '09