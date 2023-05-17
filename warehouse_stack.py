stack = []

def add_item(stack, new_item):
    stack.append(new_item)
    print(f"{new_item} Berhasil ditambahkan ke dalam stack.")

def remove_last_item(stack):
    if len(stack)==0:
        print("Stack Kosong, tidak ada barang yang dapat dihapus.")
    else:
        last_item = stack.pop()
        print(f"{last_item} berhasil dihapus dari stack.")

def show_top_item(stack):
    if len(stack)==0:
        print("Stack kosong, tidak ada barang yang ditampilkan.")
    else:
        top_item = stack[-1]
        print(f"Barang teratas di dalam stack adalah {top_item}")

while True:
    print(f"\nGudang saat ini : {stack}")
    print("Menu:")
    print("1.Tambah Barang")
    print("2.Hapus Barang Terakhir")
    print("3.Tampilkan Barang Teratas")
    print("4.Keluar")

    pilihan = input("Masukan Pilihan Anda (1/2/3/4):")

    if pilihan == "1" :
        new_item = input("Masukan barang yang akan ditambahkan: ")
        add_item1(stack, new_item)
    if pilihan == "2" :
        remove_last_item(stack)
    if pilihan == "3" :
        show_top_item(stack)
    elif pilihan == "4" :
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("pilihan tidak valid. Silakan masukkan pilihan yang benar")

