value1 = 1
value2 = 2
value3 = 3

def compare_values_alike(v1, v2, v3):
    if v1 == v2 == v3:
        print("All values are equal.")

def compare_values_different(v1, v2, v3):
    if v1 != v2 and v1 != v3 and v2 != v3:
        print("All values are different.")

compare_values_alike(value1, value2, value3)
compare_values_different(value1, value2, value3)