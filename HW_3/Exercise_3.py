def protect_password(s: str):
    if len(s) < 8:
        return False
    else:
        count_int = 0
        count_title = 0
        count_lower = 0
        for i in s:
            if '0' <= i <= '9':
                count_int += 1
            elif 'A' <= i <= 'Z':
                count_title += 1
            elif 'a' <= i <= 'z':
                count_lower += 1
        if count_title >= 1 and count_lower >= 1 and count_int >= 1:
            return True
        else:
            return False
