from termcolor import cprint
class Barang:
    def __init__(self, no_sku, nama, harga, stok):
        self.no_sku = no_sku
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, no_sku, nama, harga, stok):
        barang = Barang(no_sku, nama, harga, stok)
        if self.root is None:
            self.root = barang
        else:
            self._insert_recursive(self.root, barang)

    def _insert_recursive(self, current_node, barang):
        if barang.no_sku < current_node.no_sku:
            if current_node.left is None:
                current_node.left = barang
            else:
                self._insert_recursive(current_node.left, barang)
        else:
            if current_node.right is None:
                current_node.right = barang
            else:
                self._insert_recursive(current_node.right, barang)

    def search(self, no_sku):
        return self._search_recursive(self.root, no_sku)

    def _search_recursive(self, current_node, no_sku):
        if current_node is None or current_node.no_sku == no_sku:
            return current_node
        if no_sku < current_node.no_sku:
            return self._search_recursive(current_node.left, no_sku)
        return self._search_recursive(current_node.right, no_sku)

    def display(self):
        self._display_recursive(self.root)

    def _display_recursive(self, current_node):
        if current_node:
            self._display_recursive(current_node.left)
            print("No SKU:", current_node.no_sku)
            print("Nama:", current_node.nama)
            print("Harga:", current_node.harga)
            print("Stok:", current_node.stok)
            print("----------------------")
            self._display_recursive(current_node.right)

# # Contoh penggunaan BST untuk pengelolaan data barang
# bst = BST()

# # Menambahkan barang ke dalam BST
# bst.insert(1001, "Barang A", 50, 10)
# bst.insert(1002, "Barang B", 75, 5)
# bst.insert(1003, "Barang C", 100, 15)
# bst.insert(1004, "Barang D", 200, 8)

# # Menampilkan data barang dalam BST
# bst.display()

# # Mencari barang berdasarkan no_sku
# search_result = bst.search(1002)
# if search_result:
#     print("Barang ditemukan:")
#     print("No SKU:", search_result.no_sku)
#     print("Nama:", search_result.nama)
#     print("Harga:", search_result.harga)
#     print("Stok:", search_result.stok)
# else:
    # print("Barang tidak ditemukan.")
    
list_barang = []
list_transaksi = []
def input_barang():
  while True:
    try:
        no_sku = int(input('masukan no sku barang: '))
        nama = input('masukan nama barang: ')
        harga = int(input('masukan harga barang: '))
        jumlah = int(input('masukan jumlah barang: '))
        data = {
            'no_sku':no_sku,
            'nama':nama,
            'harga':harga,
            'jumlah':jumlah
        }
        list_barang.append(data)
        print('berhasil input data')
        print(list_barang)
        # for i in list_barang:
        #     print(i['no_sku'])
        #     print(i['nama'])
        #     print(i['harga'])
        again = input('ingin input lagi? (y/n): ')
        if again == 'y':
          return input_barang()
        else:
            return dua()
    except:
      print('An exception occurred')
      
def dua():
    nama = input('nama: ')
    no_sku = int(input('no sku: '))
    for i, item in enumerate(list_barang):
        if no_sku == item['no_sku']:
            index=i
            print(index)
            jumlah_barang = int(input('jumlah barang: '))
            
            old_stok = list_barang[index]['stok']
            harga = list_barang[index]['harga']
    
            if old_stok < jumlah_barang:
                cprint('Jumlah Stok No.SKU yang Anda beli tidak mencukupi','red')
            
            # data_barang = bst.search(no_sku=no_sku)
            # if data_barang is not None:
            #     data_barang.stok -= jumlah_barang
            
            data_transaksi = {
            'nama_cusromer': nama,
            'no_sku': no_sku,
            'jumlah_beli': jumlah_barang,
            'subtotal': jumlah_barang*harga
            }
            list_transaksi.append(data_transaksi)
            print(list_transaksi)
            break
        else:
            print('tidak ada')
        
# choice = int(input('pilih: 1 / 2'))
# if choice == 1:
#   input_barang()
# elif choice == 2:
#   dua()

data = [
    {
        'id':1,
        'nama': 'farhan',
    },
    {
        'id':2,
        'nama': 'alip',
    },
    {
        'id':3,
        'nama': 'al',
    },
]
index = None
for i, item in enumerate(data):
    if item['id'] == 3:
        index = i
        
print(data[index]['nama'])
