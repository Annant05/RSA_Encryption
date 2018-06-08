from MainPrint import start_decrypt, encrypt_it

while 1:
    ch = int(raw_input("1-Encrypt  2-Decrypt 0-Exit Choice : "))
    if ch == 1:
        encrypt_it()
    elif ch == 2:
        start_decrypt()
    elif ch == 0:
        exit(0)
