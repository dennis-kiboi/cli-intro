def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18.")
    return "Access granted"

try:
    check_age(26)
except ValueError as e:
    print(f"Exception: {e}")

print("End of execution")