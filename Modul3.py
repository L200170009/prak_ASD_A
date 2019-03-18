m1 = [[4,1],[9,3]]
m2 = [[6,17],[3,7]]

##NOMER 1
#A
def tesmatrik(matrix):
    """memastikan type data Integer"""
    jumlah = len(matrix)
    hasil = ""
    for a in matrix:
        for i in a:
            assert isinstance(i, int),"Harus Integer"
        return True
#B
def Ukur(matrix):
    """Mengambil ukuran matriks"""
    return("Ukuran Matrix = "+str(len(matrix))+" x "+str(len(matrix[0])))
#C
def Jum(matrix1,matrix2):
    """Penjumlahan 2 Matrix"""
    if Ukuran(matrix1) == Ukuran(matrix2):
        for a in range(0, len(matrix1)):
            for b in range(0, len(matrix1[0])):
                print(matrix1[a][b] + matrix2[a][b], end=' '),
            print()
    else:
        print("Matriks Tidak Sesuai")
#D
def Kali(matrix1,matrix2):
    """Perkalian 2 Matrix"""
    mat3 = []
    if Ukuran(matrix1) == Ukuran(matrix2):
        for a in range(0, len(matrix1)):
            row = []
            for b in range(0, len(matrix1[0])):
                total = 0
                for c in range(0, len(matrix1)):
                    total = total + (matrix1[a][c] * matrix2[c][b])
                row.append(total)
            mat3.append(row)

        for  in range(0, len(mat3)):
            for b in range(0, len(mat3[0])):
                print(mat3[a][b], end=' ')
            print()
    else:
        print("Matriks Tidak Sesuai")
def determinan(matrix):
    """Menghitung Determinan Matrix"""
    if len(matrix) == len(matrix[0]):
        bil = [a for a in range(len(matrix))]
        jum = 0
        for i in range(len(matrix)):
            total = 1
            for a in range(len(matrix)):
                total *= matrix[a][bil[a]]
            bil += [bil.pop(0)]
            jum += total
        bil2 = [a for a in range(len(matrix))]
        bil.reverse()
        jum2 = 0
        for i in range(len(matrix)):
            total2 = 1
            for a in range(len(matrix)):
                total2 *= matrix[a][bil2[a]]
            bil2 += [bil2.pop()]
            jum2 += total2
        print(total-total2)
        return ""
    else:
        print("Matriks Harus Bujursangkar")

#Run Nomer 1
print(tesmatrik(m1))
print(Ukur(m1))
Juml(m1,m2)
Kali(m1,m2)
print(determinan(m1))

##NOMER 2
#A
def buatNol(m, n):
    """Menggunakan dua input"""
    matrix = [[0 for a in range(m)] for i in range(n)]
    print(matrix)

def buatNol2(m):
    """Menggunakan satu input"""
    n = m
    matrix = [[0 for a in range(m)] for i in range(n)]
    print(matrix)

#B
def buatIdentitas(m):
    n = m
    matrix = [[1 if j == i else 0 for j in range(m)]for i in range(n)]
    print(matrix)

#Run Nomer 2
buatNol(5,9)
buatNol2(4)
buatIdentitas(9)

#NOMER 3
class Node():
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode
    def cetak(head):
        curr = head
        while curr != None:
            print(curr.data)
            curr = curr.nextNode

    def cari(head, cari):
        curr = head
        while curr != None:
            if curr.data == cari:
                print("Data ditemukan!")
            else:
                print("Check data!")
            curr = curr.nextNode
    def tambahDepan(head):
        newNode = Node(1)
        newNode.nextNode = head
        head = newNode
        return head
    def tambahAkhir(head):
        curr = head
        while curr is not None:
            if curr.nextNode == None:
                newNode = Node(25)
                curr.nextNode = newNode
                return curr
            else:
                pass
            curr = curr.nextNode
        return curr
    def tambah(head, posisi):
        newNode = Node(8)
        newNode.nextNode = posisi.nextNode
        posisi.nextNode = newNode
        head.head = posisi
        return head
    def hapus(head, posisi):
        curr = head
        while curr != None:
            if curr.nextNode.data == posisi:
                curr.nextNode = curr.nextNode.nextNode
                return curr
            else:
                pass
            curr = curr.nextNode
        return curr

#NOMER 4
class doubly_linked():
    def __init__(self, Data, Next=None, Prev=None):
        self.Data = Data
        self.Next = Next
        self.Prev = Prev

    def mencetak():
        curr = head
        while curr != None:
            print(curr.Data)
            if curr.Next == None:
                curr = curr
                break
            else:
                curr = curr.Next
        print("\n")
        while curr != None:
            print(curr.Data)
            curr = curr.Prev
    def simpulAwal(head):
        newNode = doubly_linked(25)
        newNode.Next = head
        head.Prev = newNode
        head =newNode
        return head

    def simpulAkhir(head):
        curr = head
        while curr != None:
            if curr.Next == None:
                newNode = doubly_linked(365)
                curr.Next = newNode
                newNode.Prev = curr
                return curr
            else:
                pass
            curr = curr.Next
        return curr
