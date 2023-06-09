import os

trasaksi = [
  {
    'no_sku': None,
    'jumlah_beli': None,
    'sub_total': None
  }
]
barang = []

class Barang:
    def __init__(self, no_sku, nama, harga, stok):
        self.no_sku = no_sku
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, no_sku, nama, harga, stok):
        barang = Barang(no_sku, nama, harga, stok)
        if self.root is None:
            self.root = barang
        else:
            self.insert_barang(self.root, barang)

    def insert_barang(self, current_node, barang):
        if barang.no_sku < current_node.no_sku:
            if current_node.left is None:
                current_node.left = barang
            else:
                self.insert_barang(current_node.left, barang)
        else:
            if current_node.right is None:
                current_node.right = barang
            else:
                self.insert_barang(current_node.right, barang)

    def display(self):
        self.display_recursive(self.root)

    def display_recursive(self, current_node):
        if current_node:
            self.display_recursive(current_node.left)
            print("No SKU:", current_node.no_sku)
            print("Nama:", current_node.nama)
            print("Harga:", current_node.harga)
            print("Stok:", current_node.stok)
            print("----------------------")
            self.display_recursive(current_node.right)

def menu():
  print('='*50)
  print('\tSISTEM INFORMASI STOK DAN TRANSAKSI')
  print('='*50)
  print('MENU:\n1. Kelola Stok Barang\n2. Kelola Transaksi Konsumen')
  
def sub_menu1():
  os.system('cls')
  print('PIIH:\n1. Input Data Stok Barang\n2. Restok Barang')
  
def sub_menu2():
  os.system('cls')
  print('PIIH:\n1. Input Data Transaksi Baru\n2. Lihat Data Seluruh Transaksi\n3. Lihat Data Seluruh Transaksi berdasarkan subtotal')

def main_sub_menu_1():
  os.system('cls')
  sub_menu1()
  while True:
    try:
      choice = int(input('Pilih: '))
      if choice == 1:
        input_barang()
      elif choice == 2:
        restok_barang()
    except:
      print('An exception occurred')
      
def main_sub_menu_2():
  os.system('cls')
  sub_menu1()
  while True:
    try:
      choice = int(input('Pilih: '))
      if choice == 1:
        input_transaksi()
      elif choice == 2:
        lihat_semua_data_transaksi()
      elif choice == 3:
        lihat_data_transaksi_by_subtotal()
    except:
      print('An exception occurred')
  
def main_menu():
  menu()
  while True:
    try:
      choice = int(input('Masukan pulihan: '))
      if choice == 1:
        main_sub_menu_1()
      elif choice == 2:
        main_sub_menu_2()
    except:
      print('An exception occurred')

def input_barang():
  bst = BinarySearchTree()
  while True:
    try:
        no_sku = int(input('masukan no sku barang: '))
        nama = input('masukan nama barang: ')
        harga = int(input('masukan harga barang: '))
        jumlah = int(input('masukan jumlah barang: '))
        bst.insert(no_sku=no_sku,nama=nama,harga=harga,stok=jumlah)
        print('berhasil input data')
        os.system('cls')
        bst.display()
        again = input('ingin input lagi? (y/n): ')
        if again == 'y':
          return input_barang()
        else:
          return main_menu()
    except:
      print('An exception occurred')
      
main_menu()
  










# Contoh penggunaan BST untuk pengelolaan data barang
# bst = BinarySearchTree()

# # Menambahkan barang ke dalam BST
# bst.insert(1001, "Barang A", 50, 10)
# bst.insert(1002, "Barang B", 75, 5)
# bst.insert(1003, "Barang C", 100, 15)
# bst.insert(1004, "Barang D", 200, 8)

# # Menampilkan data barang dalam BST
# bst.display()
