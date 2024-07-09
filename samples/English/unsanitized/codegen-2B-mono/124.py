
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
    assert valid_string(date)
    if date == None:
        return False
    date = date.split("-")
    months = {1: 31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31,\
    11:30, 12:31}
    if int(date[0]) > 10 or int(date[0]) <= 0:
        return False
    if int(date[1]) > 31 or int(date[1]) <= 0:
        return False
    if int(date[2]) > 2020 or int(date[2]) <=0:
        return False
    if int(date[0]) > 11 or int(date[0]) <= 1: 
        return False
    if int(date[0]) % 2 == 1:
        return False
    return True

@pytest.mark.parametrize("date,expected",[
    ('03-11-2000', True),
    ('15-01-2012', False),
    ('04-