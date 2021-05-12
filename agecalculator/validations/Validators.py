def name_validity_checker(name):
    if len(name) >= 5:
        return True
    return False


def age_validity_checker(age):
    if age >= 0:
        return True
    return False