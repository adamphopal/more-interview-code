def case_insenseitive_compare(str_1, str_2):
    if len(str_1) != len(str_2):
        return True
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    dict_1 = dict.fromkeys(list(alphabet), 0)
    dict_2 = dict.fromkeys(list(alphabet), 0)

    for i in range(len(str_1)):
        dict_1[str_1[i]] = 1
        dict_2[str_2[i]] = 1
    return dict_1 == dict_2


# Is case senseitive compare
print(case_insenseitive_compare("abc", "ABC"))
print(case_insenseitive_compare("abc", "def"))
print(case_insenseitive_compare("abc", "ABCD"))
print(case_insenseitive_compare("abc", "AC"))

#https://www.youtube.com/watch?v=wyu6VRmtCmE&list=PL_557Q1uZ7gIzDxN_rH_Vi6Egh0ID7un2&index=52
