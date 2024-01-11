def password_validate(p):
    if len(p) >= 4 and len(p) <= 20:
        return "valid password"
    else:
        return "Password must be between 4 and 20 characters!"