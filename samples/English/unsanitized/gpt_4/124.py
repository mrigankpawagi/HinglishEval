def valid_date(date):
    if date == "":
        return False
    if len(date.split("-")) != 3:
        return False
    month, day, year = map(int, date.split("-"))
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if month in [4, 6, 9, 11] and day > 30:
        return False
    if month == 2 and day > 29:
        return False
    return True