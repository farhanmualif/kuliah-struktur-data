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

# Contoh penggunaan BST untuk pengelolaan data barang
bst = BST()

# Menambahkan barang ke dalam BST
bst.insert(1001, "Barang A", 50, 10)
bst.insert(1002, "Barang B", 75, 5)
bst.insert(1003, "Barang C", 100, 15)
bst.insert(1004, "Barang D", 200, 8)

# Menampilkan data barang dalam BST
bst.display()

# Mencari barang berdasarkan no_sku
search_result = bst.search(1002)
if search_result:
    print("Barang ditemukan:")
    print("No SKU:", search_result.no_sku)
    print("Nama:", search_result.nama)
    print("Harga:", search_result.harga)
    print("Stok:", search_result.stok)
else:
    print("Barang tidak ditemukan.")
