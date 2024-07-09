def closest_integer(value):
    float_value = float(value)
    if float_value >= 0:
        return int(float_value) if float_value - int(float_value) < 0.5 else int(float_value) + 1
    else:
        return int(float_value) if int(float_value) - float_value < 0.5 else int(float_value) - 1