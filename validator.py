from dcvalidator import is_nationalcode

# Example usage
national_code = "1234567890"
result = is_nationalcode(national_code)

if result:
    print("National Code is valid.")
else:
    print("National Code is invalid.")