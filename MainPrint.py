from RawData import keyAtoZ

numFunc = keyAtoZ()


def enter_message():
    message = raw_input(" Your message to Encrypt : ")
    return (message.upper()).replace(" ", "_")


def encrypt_it():
    gotString = enter_message()
    list_of_string = []
    for i in gotString:
        list_of_string.append((numFunc.charToNum(i) ** 29) % 31)
    print list_of_string


def decrypt_it(list_str):
    list_of_st = []
    for i in list_str:
        newNumber = (i ** 29) % 31
        list_of_st.append((numFunc.getKeyFormValue(newNumber)))
    return list_of_st


def start_decrypt():
    lis = [1, 20L, 20L, 1, 20L, 14L]
    list_st = ''.join(decrypt_it(lis))
    print list_st.replace("_", " ")

#
# myString =
# print("You entered : " + myString)
#
# listStr = to_list_num(myString)
# print listStr
#
# newstr = listStr
# print("".join(str(listStr))).replace(", ", "")
#
# listSt = ''.join(decrypt_it(newstr))
# print listSt.replace("_", " ")
