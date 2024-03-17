def sorted_list_sum(lst):
    # Filter out strings with odd length
    filtered_list = [word for word in lst if len(word) % 2 == 0]
    # Sort the list based on length of strings and then alphabetically
    sorted_list = sorted(filtered_list, key=lambda x: (len(x), x))
    return sorted_list
