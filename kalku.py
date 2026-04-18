#kalkulator sederhana

angka_pertama = int(input("Masukan angka pertama = "))
operator = input("Operator (+,-,x,/) = ")
angka_kedua = int(input("Masukan angka kedua = "))

if operator == "+":
    angka = (angka_pertama + angka_kedua)
    print(f"Hasil = {angka}")
elif operator == "-":
    angka = (angka_pertama - angka_kedua)
    print(f"Hasil = {angka}")
elif operator == "*" or operator == "x":
    angka = (angka_pertama * angka_kedua)
    print(f"Hasil = {angka}")
elif operator == "/":
    angka = (angka_pertama / angka_kedua)
    print(f"Hasil = {angka}")