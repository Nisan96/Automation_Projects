def phone_validate(ph):
    try:
        if type(int(ph)) == int:
            if len(ph) <= 32 and len(ph) >= 3:
                return "valid phone number"
            else:
                return "Telephone must be between 3 and 32 characters!"
    except Exception as e:
        return "It's Invalid phone number"