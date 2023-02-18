#program membuat phonebook dengan requirement create, read, update, delete

daftar={}
import json

def tambah():
    file=open("listkontak.txt","a")
    nama=input("Masukkan nama kontak: ")
    nomor=input("Masukkan nomor telepon: ")
    daftar[nama]=nomor
    pb="{}: {}\n".format(nama,nomor)
    file.write(pb)
    file.close()
    print("kontak sudah ditambahkan")

def semua():
    file=open("listkontak.txt")
    file.seek(0)
    lines=file.readlines()
    for line in lines:
        print(line)

def cari():
    nama=input("Masukkan nama yang ingin dicari: ")
    file=open("listkontak.txt","r")
    for isi in file:
        if nama in isi:
            print("Kontak yang dicari:\n"+isi)
            return 
    print("\nKontak yang dicari tidak ada")    
    file.close()

def ubah():
    nama=input("Masukkan nama kontak yang ingin diperbarui: ")
    file=open("listkontak.txt","r")
    simpan={}
    i=0
    data=file.readline()
    dnama=data.split(": ")
    while data:
        if dnama[0]==nama:
            del(data)
        else:
            simpan[i]=data
            i+=1
        data=file.readline()
        dnama=data.split(": ")
    file.close()

    file=open("listkontak.txt","w")
    for x in simpan:
        file.write(simpan[x])
    file.close()
    
    file=open("listkontak.txt","a")
    nomor=input("Masukkan nomor baru: ")
    daftar[nama]=nomor
    pb="{}: {}\n".format(nama,nomor)
    file.write(pb)
    file.close()
    print("kontak sudah diperbarui")

def hapus():
    nama=input("Masukkan nama yang ingin dihapus: ")
    file=open("listkontak.txt","r")
    simpan={}
    i=0
    data=file.readline()
    dnama=data.split(": ")
    while data:
        if dnama[0]==nama:
            del(data)
        else:
            simpan[i]=data
            i+=1
        data=file.readline()
        dnama=data.split(": ")
    file.close
    file=open("listkontak.txt","w")
    for x in simpan:
        file.write(simpan[x])
    file.close()
    print("kontak sudah dihapus")

while True:
    print("\n--------PHONEBOOK--------") 
    print("1. Tambah kontak baru")
    print("2. Perbarui kontak")
    print("3. Hapus kontak")
    print("4. Cari kontak")
    print("5. Tampilkan semua kontak")
    print("6. Keluar")
    print("-------------------------")
    pilihan=int(input("Pilih opsi: "))

    if pilihan==1:
        tambah()
    elif pilihan==2:
        ubah()
    elif pilihan==3:
        hapus()
    elif pilihan==4:
        cari()
    elif pilihan==5:
        semua()    
    elif pilihan==6:
        break
    else:
        print("opsi tidak valid")
print("byee!")
