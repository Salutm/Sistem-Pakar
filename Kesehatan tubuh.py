gejala_penyakit = {
    "1" : "Deman tinggi",
    "2" : "Demam rendah",
    "3" : "Pilek",
    "4" : "Batuk",
    "5" : "Sesak nafas",
    "6" : "Sakit kepala",
    "7" : "Nyeri otot",
}

penyakit = {
    "P1" : "Flu",
    "P2" : "Covid-19",
    "P3" : "Demam Berdarah",
    "P4" : "Perlu pemeriksaan lebih lanjut",
    "P5" : "Demam biasa",
}

def diagnosa_penyakit():
    print ("Pilih gejala yang Anda alami:")
    for key, value in gejala_penyakit.items():
        print(f"{key}, {value}")

    pilihan = input ("Masukkan nomor gejala yang Anda alami ( contoh: 1, 2, 3 ): ")
    pilihan_user = set(pilihan.replace(" ", "").split(","))

    print("\n<------------------->")
    print("\nHasil diagnosa:")
    print("\n<------------------->")

    if pilihan_user == {"2", "3", "4"}:
        hasil = penyakit["P1"]
        
    elif pilihan_user == {"1", "4", "5"}:
        hasil = penyakit["P2"]

    elif pilihan_user == {"1", "6", "7"}:
        hasil = penyakit["P3"]

    elif pilihan_user == {"1"}:
        hasil = penyakit["P5"]

    else:
        hasil = penyakit["P4"]

    print("\n<----------------------------------->")
    print(f"\nAnda kemungkinan besar mengalami {hasil}")
    print("\n<----------------------------------->")
diagnosa_penyakit()
