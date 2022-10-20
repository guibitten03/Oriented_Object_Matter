
def string_compare(string_1, string_2):
    if len(string_1) == len(string_2):
        for i in range(len(string_1)):
            if not (string_1[i] == string_2[i]):
                return "Its not equal."
    
    else:
        return "Its not equal."
    return "Its equal."


if __name__ == "__main__":
    string_1 = "a"
    string_2 = 45

    try:
        print(string_compare(string_1, string_2))
    except:
        exit("Its not a string")