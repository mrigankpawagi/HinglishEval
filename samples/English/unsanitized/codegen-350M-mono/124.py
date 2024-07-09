
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
    # TODO: Write your function
    d = date
    d = d.split("-")
    if not d or len(d[0])<1:
        return False
    if len(d[0])==1 or len(d[0])>=2 and not d[1].isdigit() or d[1].isdigit() and not d[2].isdigit():
        return False
    if not d[1].isdigit() and len(d[1])>=1 and d[1].isalnum():
        
        m = ['M','MM','MMM','MMM','MMM']
        if d[1].isnumeric() or d[1] in m:
            if len(d[2])>=1 and \
                not d[2].isnumeric() and d[2].isalnum():
                return False
            return True
    if len(d[2])>=10 and d[2].isnumeric() and \
            not d[2].isnumeric() and len(d[2])>=30:
        