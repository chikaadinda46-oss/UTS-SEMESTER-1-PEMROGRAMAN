kalimat = input ("MASUKKAN KALIMAT :")
huruf = ""

kalimat = kalimat.lower()

jumlah = 0

for karakter in kalimat:
    if karakter:
        jumlah += 1

print (f"jumlah teks dalam teks adalah: {jumlah}")