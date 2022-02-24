def protect_password(s: str):
    if len(s) < 8:
        return False
    else:
        count_int = 0
        count_title = 0
        count_lower = 0
        for i in s:
            if i in '123456789':
                count_int +=1
            elif i == i.title():
                count_title +=1
            else:
                count_lower +=1
        if count_title >= 1 and count_lower >= 1 and count_int >= 1:
            return True
        else:
            return False
