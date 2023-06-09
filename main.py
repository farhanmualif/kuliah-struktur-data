import os
from termcolor import cprint

list_trasaksi = []
list_barang = []

class Barang:
    def __init__(self, no_sku, nama, harga, stok):
        self.no_sku = no_sku
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.left = None
        self.right = None
    def __str__(self):
        return f"Barang: {self.nama}\nNo SKU: {self.no_sku}\nHarga: {self.harga}\nStok: {self.stok}"
      

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
                
    def search(self, no_sku):
        return self.search_recursive(self.root, no_sku)

    def search_recursive(self, current_node, no_sku):
        if current_node is None or current_node.no_sku == no_sku:
            return current_node
        if no_sku < current_node.no_sku:
            return self.search_recursive(current_node.left, no_sku)
        return self.search_recursive(current_node.right, no_sku)

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
  os.system('cls')
  print('='*50)
  print('\tSISTEM INFORMASI STOK DAN TRANSAKSI')
  print('='*50)
  print('MENU:\n1. Kelola Stok Barang\n2. Kelola Transaksi Konsumen\n3. Exit')
  
def sub_menu1():
  os.system('cls')
  print('PIIH:\n1. Input Data Stok Barang\n2. Restok Barang\n3. kembali...')
  
def sub_menu2():
  os.system('cls')
  print('PIIH:\n1. Input Data Transaksi Baru\n2. Lihat Data Seluruh Transaksi\n3. Lihat Data Seluruh Transaksi berdasarkan subtotal\n4. kembali...')

def main_sub_menu_1():
  sub_menu1()
  while True:
    try:
      choice = int(input('Pilih: '))
      if choice == 1:
        input_barang()
      elif choice == 2:
        restok_barang()
      elif choice == 3:
        return main_menu()
    except:
      cprint('An exception occurred','red')
      
def main_sub_menu_2():
  sub_menu2()
  while True:
    try:
      choice = int(input('Pilih: '))
      if choice == 1:
        input_transaksi()
      elif choice == 2:
        lihat_semua_data_transaksi()
      elif choice == 3:
        lihat_data_transaksi_by_subtotal()
      elif choice == 4:
        return main_menu()
    except:
      cprint('An exception occurred','red')
  
def main_menu():
  menu()
  while True:
    try:
      choice = int(input('Masukan pulihan: '))
      if choice == 1:
        main_sub_menu_1()
      elif choice == 2:
        main_sub_menu_2()
      elif choice == 3:
        cprint('Terima kasih 😄','blue')
        break
    except:
      cprint('An exception occurred','red')

# fungsi input barang
bst = BinarySearchTree()
def input_barang():
  while True:
    try:
        no_sku = int(input('masukan no sku barang: '))
        nama = input('masukan nama barang: ')
        harga = int(input('masukan harga barang: '))
        stok = int(input('masukan jumlah barang: '))
        
        # cek apakah no sku sudah ada dalam list?
        for i in list_barang:
          if no_sku == i['no_sku']:
            cprint('no sku sudah ada','red')
            print('-'*20)
            return input_barang()
        
        barang = {
         'no_sku':no_sku,
         'nama': nama,
         'harga': harga,
          'stok': stok
        }
        
        bst.insert(no_sku=barang['no_sku'],nama=barang['nama'],harga=barang['harga'],stok=barang['stok'])
        os.system('cls')
        cprint('berhasil input data','green')
        list_barang.append(barang)

        bst.display()
        again = input('ingin input lagi? (y/n): ')
        if again == 'y':
          os.system('cls')
          return input_barang()
        else:
          os.system('cls')
          return main_menu()
    except:
      cprint('An exception occurred','red')

# fungsi restok barang
def restok_barang():
  no_sku = int(input('masukan no sku barang yang akan di update: '))
  old_stok = None
  index = None
  
  for i, item in enumerate(list_barang):
    if item['no_sku'] == no_sku:
      index =+ i
      print(list_barang[index])
      old_stok =+ item['stok']
      break
    else:
      cprint(f'barang dengan kode ${no_sku} tidak ada','red')
      break
  
  if index is not None:
    new_stok = int(input('masukan stok baru: '))
    stok = old_stok+new_stok
    list_barang[index]['sku']=stok
    print(list_barang[index])
  

def input_transaksi():
  nama = input('input nama customer: ')
  while True:
    no_sku = int(input('masukan no sku barang: '))
    index = None
    for i, item in enumerate(list_barang):
      if item['no_sku'] == no_sku:
        index = i
        break
    # cek apakah barang dengan sku taersedia?
    if index is None:
        cprint('No. SKU yang diinputkan belum terdaftar','red')
        confirm = input('Apakah ingin melanjutkan transaksi (Y/N)?: ')
        if confirm == 'y':
          continue
        else:
          return main_sub_menu_2()
    sisa_stok = list_barang[index]['stok']
    jumlah_dibeli = int(input('masukan jumlah barang yang dibeli: '))
    # cek apakah input jumlah beli lebih dari sisa stok
    if jumlah_dibeli > sisa_stok:
      cprint('Jumlah Stok No.SKU yang Anda beli tidak mencukup','red')
      confirm = input('Apakah ingin melanjutkan transaksi (Y/N)?: ')
      if confirm == 'y':
        continue
      else:
        return main_sub_menu_2()
    # get harga barang
    harga = list_barang[index]['harga']
    # update stok barang
    barang = bst.search(no_sku=no_sku)
    if barang is not None:
      barang.stok -=jumlah_dibeli
    # tampung data
    data_transaksi = {
      'nama_konsumen': nama,
      'no_sku': no_sku,
      'jumlah_dibeli': jumlah_dibeli,
      'subtotal': jumlah_dibeli*harga
    } # 246, 642
    list_trasaksi.append(data_transaksi)
    cprint('Data Transaksi Konsumen Berhasil Diinputkan','green')
    print(list_trasaksi)
    confirm = input('Apakah ingin menambahkan data pembelian (Y/N)?: ')
    if confirm == 'y':
        continue
    else:
        return main_sub_menu_2()
    
def lihat_semua_data_transaksi():
  for i in list_trasaksi:
    print('nama konsumen: ',i['nama_konsumen'])
    print('no sku: ',i['no_sku'])
    print('jumlah barang yang dibeli: ',i['jumlah_dibeli'])
    print('subtotal: ',i['subtotal'])
    print('-'*50)

def bubble_sort_subtotal(transaksi_list):
    n = len(transaksi_list)
    for i in range(n-1):
        for j in range(n-i-1):
            if transaksi_list[j]['subtotal'] > transaksi_list[j+1]['subtotal']:
                transaksi_list[j], transaksi_list[j+1] = transaksi_list[j+1], transaksi_list[j]
                
def lihat_data_transaksi_by_subtotal():
    subtotal_threshold = int(input('Masukkan batas subtotal: '))
    filtered_transactions = [transaksi for transaksi in list_trasaksi if transaksi['subtotal'] >= subtotal_threshold]
    
    bubble_sort_subtotal(filtered_transactions)
    
    for transaksi in filtered_transactions:
        print('Nama Konsumen:', transaksi['nama_konsumen'])
        print('No. SKU:', transaksi['no_sku'])
        print('Jumlah Barang yang Dibeli:', transaksi['jumlah_dibeli'])
        print('Subtotal:', transaksi['subtotal'])
        print('----------------------')


  
main_menu()
# bst = BinarySearchTree()
# bst.display()

  










# Contoh penggunaan BST untuk pengelolaan data barang
# bst = BinarySearchTree()

# # Menambahkan barang ke dalam BST
# bst.insert(1001, "Barang A", 50, 10)
# bst.insert(1002, "Barang B", 75, 5)
# bst.insert(1003, "Barang C", 100, 15)
# bst.insert(1004, "Barang D", 200, 8)

# # Menampilkan data barang dalam BST
# bst.display()
