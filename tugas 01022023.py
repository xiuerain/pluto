print ('''ˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉ
\tSelamat Datang di Kopsis Moklet
ˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍ''')
print ('''\nNama barang

1. pensil
2. rautan
3. penghapus
4. isolasi
5. bulpen
6. tipex''')

a = ["pensil", "rautan", "penghapus", "isolasi", "bulpen", "tipex"]
b = ["2000", "1500", "2000", "2500", "2500", "3000"]
c = input("\nMasukan nama barang yang ingin di cek harga: ")

for i in range (len(a)):
    if c == a[i]:
        print (a[i]+" Rp."+b[i])

print ('''\nIngin melanjutkan transaksi?
\tyes
\tnay
\t\t*ketik y/n untuk melanjutkan transaksi''')
d = ["y", "n"]
e = input("\nPilihan anda: ")
if e=="y":
    f =input("\nmasukkan pesanan anda: ")
    for i in range (len(a)):
        if f == a[i]:
            print ("\nTotal anda: "+b[i])
            print ("Tolong memakai uang pas yaa~ Have a nice day!!")
if e=="n":
    print ("\nTerima kasih!! Have a nice day~")
