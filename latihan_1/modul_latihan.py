from unittest import result


def calculator(a,b,operation):
    if(type(a,b) == int or type(a,b) == float):
        if operation == '+':
            result = a + b
        elif operation == '-':
            result = a - b
        elif operation == '*':
            result = a * b
        elif operation == '/':
            result = a / b
        else:
            result="Operasi Tidak Dikenal"
    else:
        result = "Inputan Harus Angka"
    print(result)

def is_palyndrome(kata):
    if(kata == kata[::-1]):
        return True
    else:
        return False

def guess_number():
    import random
    guess = random.randint(0,9)
    print(guess)
    for i in range(1,3):
        user_guess = int(input("Masukkan Angka : "))
        if(user_guess == guess):
            print("Selamat Anda Benar")
            break
        elif(user_guess > guess):
            print("Angka Terlalu Besar")
        else:
            print("Angka Terlalu Kecil")
        print("Anda Sudah Memasukkan {} kali".format(i))
    print("Game Over")

