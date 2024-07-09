def odd_count(lst):
    return [
        "input ki string {} mein odd elements ki sankhya {}.".format(
            sum(int(i) % 2 for i in s),
            s.count("1") + s.count("3") + s.count("5") + s.count("7") + s.count("9"),
        )
        for s in lst
    ]
