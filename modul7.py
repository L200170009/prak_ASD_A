import re

#nomor 1
a = open('Indonesia.txt', 'r')
teks = a.read()
a.close()
b = r"me\w+"
kata = re.findall(b, teks)
print(kata)

#nomor 2
a = open('Indonesia.txt', 'r', encoding='latin1')
teks = a.read()
a.close()
b = r"di\w+"
kata = re.findall(b, teks)
print(kata)

#nomor 3
a = open('Indonesia.txt', 'r', encoding='latin1')
teks = a.read()
a.close()
b = r"di\s\w+"
kata = re.findall(b, teks)
print(kata)

#nomor 4 a
a = open('KEI.html', 'r', encoding = 'latin')
teks = a.read()
a.close()
pola = r'(\w+)</a></td>'
muncul = re.findall(pola, teks)
print(muncul)

#nomor 4 b
a = open('KEI.html','r', encoding='latin')
teks4 = a.read()
a.close()
string=re.findall(r'title="([\w+]+)">',teks4)
string=re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>',teks4)
b=[]
for i in string:
    b.append((i[0], float(i[1])))
print(b)

