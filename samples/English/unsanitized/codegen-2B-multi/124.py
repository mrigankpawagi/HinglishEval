
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
    if not (len(date) and "-" in date and len(date) > 31):
        return False
    elif (date[1] not in range(1,13) or (date[2] not in range(31,30) and date[2]!= 2) or date[2] == 2 and (date[4] not in range(1,30) and date[4]!= 1) or (date[4] == 1 and date[5] not in range(29,30))):
        return False
    elif (date[0] == "5" and date[3] not in range(19,30)):
        return False
    elif date[2] <= 0 or date[3] <= 0 or date[4] <= 0 or date[5] <= 0 or date[6] <= 0 or date[7] <= 0 or date[8] <= 0:
        return False
    else:
        return True

#TODO: fix the way of writing the code.
