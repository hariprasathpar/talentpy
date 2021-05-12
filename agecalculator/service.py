from core.CalculateEligibility import compute_eligibility
def compute_result():
    name = "Hariprasath"
    age = 19
    result = compute_eligibility(name, age)
    return result


print(compute_result())