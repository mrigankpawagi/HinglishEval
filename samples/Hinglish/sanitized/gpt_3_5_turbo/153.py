def Strongest_Extension(class_name, extensions):
    strengths = []
    for extension in extensions:
        cap_count = sum(1 for char in extension if char.isupper())
        sm_count = sum(1 for char in extension if char.islower())
        strength = cap_count - sm_count
        strengths.append(strength)
    max_strength = max(strengths)
    max_index = strengths.index(max_strength)
    return class_name + "." + extensions[max_index]
