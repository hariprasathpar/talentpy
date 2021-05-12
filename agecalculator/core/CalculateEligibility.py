from validations.Validators import name_validity_checker, age_validity_checker
def compute_eligibility(name, age):
    name_check = name_validity_checker(name)
    if name_check == False:
        return "Username is invalid"
    else:
        age_check = age_validity_checker
        if age_check == False:
            return "Age is invalid"
        else:
            if age > 18:
                return "Yes"
            else:
                return "No"
