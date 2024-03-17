def file_name_check(file_name):
    if file_name.count(".") != 1:
        return "No"
    name, ext = file_name.split(".")
    if len(name) - len(name.translate(str.maketrans("", "", "0123456789"))) > 2:
        return "No"
    if not name[0].isalpha():
        return "No"
    if ext not in ["txt", "exe", "dll"]:
        return "No"
    return "Yes"
