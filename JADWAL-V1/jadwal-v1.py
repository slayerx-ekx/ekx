while True :
    import random

    def kata():
        import random
        with open("C:/Users/dettl/OneDrive/Dokumen/VSCODE belajar massse/beljar python/wordlist.txt", "r") as file: 
            allText = file.read() 
            words = list(map(str, allText.split()))  
            print(random.choice(words)) 

    
    def waktu():
        print ("Senin	07:00 - 12:00")
        print ("Selasa	07:00 - 12:00")
        print ("Rabu	07:00 - 12:00")
        print ("Kamis	07:00 - 12:00")
        print ("Jumat	07:00 - 12:00")    
    
    def senin():
        print ("===jadwal hari senin===")
        print ("==> BAHASA JAWA")
        print ("==> MATEMATIKA")
        print ("==> PKK")

    def selasa():
        print ("===jadwal hari senin===")
        print ("==> BAHASA INGGRIS")
        print ("==> PRODUKTIF PAK ARYA")
     

    def rabu():
        print ("===jadwal hari senin===")
        print ("==> PRODUKTIF BU AS")
        print ("==> PPKN")
        print ("==> SEJARAH")
        print ("==> BAHASA INGGRIS")    

    def kamis():
        print ("===jadwal hari senin===")
        print ("==> MAPEL PILIHAN")
        print ("==> BAHASA INDONESIA")
        print ("==> AGAMA")   

    def jumat():
        print ("===jadwal hari senin===")
        print ("==> PJOK")
        print ("==> PRODUKTIF PAK HADI")
        print ("==> BAHASA JEPANG")    
    
    print ("=========== >     INI ADALAH JADWAL SEKOLAH LENGKAP SENIN SAMPAI JUMAT    < ===========")
    print ("=========== >   masukkan perintah sesuai dengan apa yang di suruh hehe :) < ===========")

    print ("1.HARI SENIN   ")
    print ("2.HARI SELASA  ")
    print ("3.HARI RABU    ")
    print ("4.HARI KAMIS   ")
    print ("5.HARI JUMAT   ")

    hari = int(input("pilih nomor untuk harinya :"))

    if hari == 1 :
        
        waktu()
        senin()
        kata()

    elif hari == 2:
        waktu()
        selasa()
        kata()

    elif hari == 3:
        waktu()
        rabu()
        kata()

    elif hari == 4:
        waktu()
        kamis()
        kata()

    elif hari == 5:
        waktu()
        jumat()
        kata()

    else :
        print ("====>>>SALAH PILIH HARI PILIH DENGAN MENGGUNAKAN ANGKA BUKAN HURUH<<<===")
    