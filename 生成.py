##import xlrd
##f = open('GBK.txt', encoding = 'utf-8', mode = 'r')
##l = [x.strip('\r\n') for x in f]
##f.close()
##data = xlrd.open_workbook('拆分表.xlsx')
##table = data.sheets()[0]
##c = table.col_values(16)
##i = [x for x in c if x not in l and x != '' and x[0] != '<']
##f = open('o.txt', encoding = 'utf-8', mode = 'w')
##for x in i:
##    f.write(x + '\n')
##f.close()
c_42_meta = '''# Rime dictionary: c_42
# encoding: utf-8

---
name: c_42
version: "1"
sort: original
columns:
  - text
  - code
...
'''
c_42a_meta = '''# Rime dictionary: c_42a
# encoding: utf-8

---
name: c_42a
version: "1"
sort: original
columns:
  - text
  - code
...
'''
##char = table.col_values(0)[2:]
##code = table.col_values(8)[2:]
##word = table.col_values(13)[1:]
##wcode = table.col_values(14)[1:]
##cc = [(char[n], code[n]) for n in range(len(char))]
##ww = [(word[n], wcode[n]) for n in range(len(word))]
##w2 = [x for x in ww if len(x[1]) == 2]
##c2 = [x for x in cc if len(x[1]) == 2]
##c3 = [x for x in cc if len(x[1]) == 3]
f = open('拆分表.txt', encoding = 'utf-8', mode = 'r')
l = [x.strip('\r\n').split('\t') for x in f]
f.close()
f = open('简码表.txt', encoding = 'utf-8', mode = 'r')
b = [x.strip('\r\n').split('\t') for x in f]
f.close()
f = open('映射表.txt', encoding = 'utf-8', mode = 'r')
d = {x.strip('\r\n').split('\t')[0]:x.strip('\r\n').split('\t')[1] for x in f}
f.close()
f = open('特码表.txt', encoding = 'utf-8', mode = 'r')
t = [x.strip('\r\n').split('\t') for x in f]

q = [(x[0], (d[x[1]]+d[x[2]]+d[x[3]]+x[4])[:3]) for x in l if x[5] == '0']
qd = {x[0]:x[1] for x in q}
f = open('c_42.dict.yaml', encoding = 'utf-8', mode = 'w')
f.write(c_42_meta)
for i in b:
    f.write(i[0] + '\t' + i[1] + '\n')
    f.write('　' + '\t' + i[1] + '\n')
f.close()
key = 'abcdefghijklmnopqrstuvwxyz;'
key2 = key + ',./'
a = [x + y + z for x in key for y in key2 for z in key]
f = open('c_42a.dict.yaml', encoding = 'utf-8', mode = 'w')
f.write(c_42a_meta)
c3 = []
bc = [i[0] for i in b]
for i in q:
    c3.append(i[1])
    if i[0] in bc:
        f.write(i[0] + '\t~' + i[1] + '\n')
    else:
        f.write(i[0] + '\t' + i[1] + '\n')
for i in [x for x in a if x not in c3]:
    f.write('　' + '\t~' + i + '\n')
for i in t:
    f.write(i[0] + '\t' + i[1] + '\n')
f.close()
c = [(x[0], x[1]) for x in b if len(x[0]) == 1 and x[0] != '　']
f = open('brevity.txt', encoding = 'utf-8', mode = 'w')
for i in c:
    if i[1] != qd[i[0]][:2]:
        if i[1][-1] in ',./':
            f.write(i[0] + '\t~' + i[1] + '\n')
        else:
            f.write(i[0] + '\t~~' + i[1] + '\n')
    else:
        f.write(i[0] + '\t' + i[1] + '\n')
f.close()
w = [(x[0], x[1]) for x in b if len(x[0]) == 2]
f = open('brevity2.txt', encoding = 'utf-8', mode = 'w')
for i in w:
    f.write(i[0] + '\t' + i[1] + '\n')
f.close()
