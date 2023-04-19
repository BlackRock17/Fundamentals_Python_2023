def pass_valid(passw):
    is_valid = True
    counter = 0
    if len(passw) < 6 or len(passw) > 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not passw.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False
    for el in passw:
        if el.isdigit():
            counter += 1
    if counter < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    return is_valid


password = input()

if pass_valid(password):
    print("Password is valid")
