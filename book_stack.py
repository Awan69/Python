book = []
author = []


def add_book(book, author, new_book):
    book.append(new_book)
    print(f"{new_book} Berhasil ditambahkan ke dalam Rak Buku.")
    author.append(new_author)
    print(f"{new_author} berhasil ditambahkan.")


def remove_last_book(book, author):
    if len(book) == 0:
        print("Rak buku Kosong, tidak ada buku yang dapat dihapus.")
    else:
        last_book = book.pop()
        print(f"{last_book} berhasil dihapus dari rak buku.")
        last_author = author.pop()


def show_top_book(book, author):
    if len(book) == 0:
        print("Rak buku kosong, tidak ada buku yang ditampilkan.")
    else:
        top_book = book[-1]
        print(f"Buku teratas di Rak buku adalah {top_book}")
        top_author = author[-1]
        print(f"Authornya adalah {top_author}")


while True:
    print(f"\nRak Buku : {book}")
    print(f"Author : {author}")
    print("Menu:")
    print("1.Tambah Buku")
    print("2.Hapus Buku Terakhir")
    print("3.Tampilkan Buku Teratas")
    print("4.Keluar")

    pilihan = input("Masukan Pilihan Anda (1/2/3/4):")

    if pilihan == "1":
        new_book = input("Masukan buku yang akan ditambahkan: ")
        new_author = input("Masukan nama authornya: ")
        add_book(book, author, new_book)
    if pilihan == "2":
        remove_last_book(book, author)
    if pilihan == "3":
        show_top_book(book, author)
    elif pilihan == "4":
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("pilihan tidak valid. Silakan masukkan pilihan yang benar")
