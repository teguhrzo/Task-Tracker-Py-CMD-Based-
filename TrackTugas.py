import csv
import pandas as pd
import os

column = ["Tugas", "Tenggat", "Comment"]
field = {"Tugas":[], "Tenggat":[], "Comment":[]}
def show():
    try:
        f = open("Tugas.csv", 'r')
        isi = []
        baca = csv.DictReader(f)
        for data in baca:
            isi.append(data)
        # print(f"No. \t Tugas \t\t Tenggat \t Comment")
        # print(50*"=")
        if(len(isi)<1):
            print("Tidak ada tugas!")
            return
        # else:
        #     for row in isi:
        #         print(f"{row['No']} \t ", end='')
        #         if(len(row['Tugas'])>5):
        #             print(f"{row['Tugas']} \t ", end='')
        #         else:
        #             print(f"{row['Tugas']} \t\t ", end='')
        #         if(len(row['Tenggat'])>5):
        #             print(f"{row['Tenggat']} \t ", end='')
        #         else:
        #             print(f"{row['Tenggat']} \t\t ", end='')
        #         print(f"{row['Comment']} \t ", end='')
        #         print()
        # print("="*50)
        # f.close()
        read = pd.read_csv("Tugas.csv")
        read.index+=1
        print(read)
    except:
        print("File tugas belum ada!")
        print("Buat file pada menu (2)!\n")
        

def tambah():
    data = []
    try:
        f = open("Tugas.csv", 'r')
        baca = csv.DictReader(f)
        for row in baca:
            data.append(row)
        no = len(data)+1
        f.close()       
    except:
        f= open("Tugas.csv", 'w')
        tulis = csv.DictWriter(f, fieldnames=column)
        tulis.writeheader()
        f.close()
    # no = len(data)+1
    try:
        f = open("Tugas.csv", 'a')
        tulis = csv.DictWriter(f, fieldnames=column)
        task = input("Tugas: ")
        time = input("Tenggat: ")
        komen = input("Comment: ")
        tulis.writerow({"Tugas":task, "Tenggat":time, "Comment":komen})
        print("Tugas berhasil dimasukan ke dalam list!")
        f.close()
    except:
        print("Terjadi kesalahan koneksi databatase!")
    os.system("pause")
    menu()

def hapus():
    try:
        f = open("Tugas.csv", 'r')
        isi = []
        baca = csv.DictReader(f)
        for data in baca:
            isi.append(data)
        if(len(isi)<1):
            print("Tidak ada tugas dalam daftar!")
            return
        show()
        f.close()
        Hapus = int(input("Pilih nomor yang ingin dihapus: "))
        isi.pop(Hapus-1)
        f = open("Tugas.csv", 'w')
        tulis = csv.DictWriter(f, fieldnames=column)
        tulis.writeheader()
        no = 1
        for row in isi:
            tulis.writerow({"Tugas":row['Tugas'], 'Tenggat':row["Tenggat"], 'Comment':row['Comment']})
            no+=1
        f.close()
        print("Data berhasil dihapus!")
    except:
        print("Belum ada tugas apapun!")
        print("Buat file pada menu (2)!\n")
    
    os.system("Pause")
    menu()

def mark():
    try:
        f = open("Tugas.csv", 'r')
        isi = []
        baca = csv.DictReader(f)
        for data in baca:
            isi.append(data)
        if(len(isi)<1):
            print("Tidak ada tugas dalam daftar!")
            return
        show()
        pilih = int(input("Pilih nomor tugas yang sudah selesai: "))
        isi[pilih-1]['Comment'] = "Selesai"
        f = open("Tugas.csv", 'w')
        tulis = csv.DictWriter(f, fieldnames=column)
        tulis.writeheader()
        no = 1
        for row in isi:
            tulis.writerow({"Tugas":row['Tugas'], 'Tenggat':row["Tenggat"], 'Comment':row['Comment']})
            no+=1
        f.close()
        print("Data berhasil ditandai!")
        
    except:
        print("Belum ada tugas apapun!")
        print("Buat file pada menu (2)!\n")

    os.system("Pause")
    menu()



def menu():
    os.system("CLS")
    print("="*32)
    print(f"\tTRACK TUGAS")
    print("="*32)
    print("""1. Lihat Tugas
2. Tambah Tugas
3. Tandai tugas telah selesai
4. Hapus tugas dari daftar
5. Keluar program""")
    print("="*32)
    pilih = int(input("Pilih menu: "))
    if(pilih==1):
        show()
        os.system("Pause")
        menu()
    elif pilih==2:
        tambah()
    elif pilih ==3:
        mark()
    elif pilih==4:
        hapus()
    else:
        exit()
        

menu()