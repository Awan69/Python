from queue import Queue


class Customer:
    def __init__(self, name, transaction_type):
        self.name = name
        self.transaction_type = transaction_type


class TransactionQueue:
    def __init__(self):
        self.queue = Queue()

    def is_empty(self):
        return self.queue.empty()

    def enqueue(self, customer):
        self.queue.put(customer)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.get()

    def display_all_transaction(self):
        if self.is_empty():
            print("Tidak Ada transaksi Dalam Antrian.")
        else:
            print("Seluruh Antrian Transaksi: ")
            i = 1
            for customer in self.queue.queue:
                print(
                    f"------------------Transaksi Ke-{i}-----------------------")
                print(f"Nama Pelanggan : {customer.name}")
                print(f"Jenis Transaksi : {customer.transaction_type}")
                i += 1

    def remove_completed_transaction(self):
        if self.is_empty():
            print("Tidak Ada Transaksi Dalam Antrian.")
        else:
            completed_customer = self.queue.get()
            print("Untuk Pelanggan:", completed_customer.name)
            print("Jenis Transaksi:", completed_customer.transaction_type)


if __name__ == "__main__":
    transaction_queue = TransactionQueue()

    while True:
        print("\n1. Tambah Transaksi ke Antrian.")
        print("2. Tampilkan Seluruh Antrian Transaksi.")
        print("3. Layani Transaksi Dan Hapus.")
        print("4. Keluar.")

        choice = input("Pilih menu (1/2/3/4): ")

        if choice == "1":
            name = input("Masukkan Nama Pelanggan: ")
            transaction_type = input("Masukkan Jenis Transaksi: ")
            customer = Customer(name, transaction_type)
            transaction_queue.enqueue(customer)
            print("Transaksi berhasil ditambahkan ke dalam antrian.")

        elif choice == "2":
            transaction_queue.display_all_transaction()

        elif choice == "3":
            transaction_queue.remove_completed_transaction()
            print("Transaksi Selesai.")

        elif choice == "4":
            print("Terima Kasih Telah Menggunakan Program Ini.")
            break

        else:
            print("Pilihan Tidak Valid. Silakan Masukkan Pilihan Yang Benar")
