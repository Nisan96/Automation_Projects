def char1_validate(char1,email):
    list_char1 = []
    count = 0
    for c in email:
        count += 1
        if c == char1:
            i = count-1
            list_char1.append(i)
        else:
            continue
    return list_char1

def char2_validate(char2,email):
    list_char2 = []
    count = 0
    for c in email:
        count += 1
        if c == char2:
            i = count-1
            list_char2.append(i)
        else:
            continue
    return list_char2

def position_validate(c,at, dt):
    for a in at:
        for d in dt:
            if d == 0:
                return "E-Mail Address does not appear to be valid!"
            elif d == a + 1:
                return "'.' used at wrong position in this email"
            elif d == a - 1:
                return "E-Mail Address does not appear to be valid!"
            else:
                continue
    if dt[-1] > at[0]:
        if dt[-1] == len(c) - 1:
            return "'.' used at wrong position in this email"
        elif len(dt) > 1:
            x = 1
            for q in dt:
                if q == dt[x] - 1:
                    return "'.' used at wrong position in this email"
                else:
                    if dt[x] == dt[-1]:
                        return "valid email"
                    x += 1
                    continue
        else:
            return "valid email"
    else:
        return "E-Mail Address does not appear to be valid!"

