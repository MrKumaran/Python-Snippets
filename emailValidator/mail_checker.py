def has_invalid_characters(string):
    valid = "abcdefghijklmnopqrstuvwxyz0123456789."
    for i in string:
        if i not in valid:
            return True
    return False


def is_valid(email):
    if email.count("@") == 1:
        usr_name = email.split("@")
        if len(usr_name[0]) == 0:
            return False
        else:
            if has_invalid_characters(usr_name[0]):
                return False
            elif usr_name[1].count(".") == 1:
                domain = usr_name[1].split(".")
                if len(domain[0]) == 0:
                    return False
                else:
                    if len(domain[1]) == 0:
                        return False
                    else:
                        if has_invalid_characters(domain[0]):
                            return False
                        elif has_invalid_characters(domain[1]):
                            return False
                        else:
                            return True
            else:
                return False
    else:
        return False
