
def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example: 
    valid_date('03-11-2000') => True

    valid_date('15-01-2012') => False

    valid_date('04-0-2040') => False

    valid_date('06-04-2020') => True

    valid_date('06/04/2020') => False
    """
    for element in date:
        if element in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("The element %s can not be a space" % element)
            return False

    date = date.replace('/','-')
    date = date.replace('\D','')
    month = date[2:4]
    day = date[4:6]
    year = date[6:10]

    if int(day) > 31:
        return False
    elif day > 1:
        if int(month) is 12 or int(month) is 1: 
            if day > 30:
                return False
        else:
            if day > 29:
                return False
    else:
        return False
    if int(day) == 1 and int(month) is 3 or int(month) is 10:  
        if year == '1200':
            return False
    elif int(day) == 1 and int(month) is 4 or int(month) is 6