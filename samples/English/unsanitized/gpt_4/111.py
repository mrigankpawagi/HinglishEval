def histogram(test):
    test = test.split()
    hist = {i: test.count(i) for i in test}
    max_val = max(hist.values()) if hist else 0
    return {k: v for k, v in hist.items() if v == max_val}