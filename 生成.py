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
def strQ2B(ustring):
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 12288:
            inside_code = 32  
        elif (inside_code >= 65281 and inside_code <= 65374): 
            inside_code -= 65248
 
        rstring += unichr(inside_code)
    return rstring
    
def strB2Q(ustring):
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 32:    
            inside_code = 12288
        elif inside_code >= 32 and inside_code <= 126:    
            inside_code += 65248
 
        rstring += chr(inside_code)
    return rstring


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
f = open('资料/拆分表.txt', encoding = 'utf-8', mode = 'r')
l = [x.strip('\r\n').split('\t') for x in f]
f.close()
f = open('资料/简码表.txt', encoding = 'utf-8', mode = 'r')
b = [x.strip('\r\n').split('\t') for x in f]
f.close()
f = open('资料/映射表.txt', encoding = 'utf-8', mode = 'r')
d = {x.strip('\r\n').split('\t')[0]:x.strip('\r\n').split('\t')[1] for x in f}
f.close()
f = open('资料/映射表.txt', encoding = 'utf-8', mode = 'r')
s = {x.strip('\r\n').split('\t')[0]:x.strip('\r\n').split('\t')[2] for x in f}
for i in s:
    if s[i] == '':
        s[i] = i
f.close()
f = open('资料/特码表.txt', encoding = 'utf-8', mode = 'r')
t = [x.strip('\r\n').split('\t') for x in f]
f.close()
u = [(x[0], (s[x[1]]+s[x[2]]+s[x[3]]+strB2Q(x[4].upper()))[:3]) for x in l if x[5] == '0']
q = [(x[0], (d[x[1]]+d[x[2]]+d[x[3]]+x[4])[:3]) for x in l if x[5] == '0']
qq = [(x[0], (d[x[1]]+d[x[2]]+d[x[3]]+x[4])[:3]) for x in l]
f = open('输出/其他/全码表.txt', encoding = 'utf-8', mode = 'w')
for i in q:
    f.write(i[0] + '\t' + i[1] + '\n')
f.close()
qd = {x[0]:x[1] for x in q}
f = open('输出/c_42.dict.yaml', encoding = 'utf-8', mode = 'w')
f.write(c_42_meta)
for i in b:
    f.write(i[0] + '\t' + i[1] + '\n')
    f.write('　' + '\t' + i[1] + '\n')
f.close()
key = 'abcdefghijklmnopqrstuvwxyz;'
a = [x + y + z for x in key for y in key for z in key]
f = open('输出/c_42a.dict.yaml', encoding = 'utf-8', mode = 'w')
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
a = [[],[],[]]
f = open('输出/opencc/brevity.txt', encoding = 'utf-8', mode = 'w')
for i in c:
    if i[1] != qd[i[0]][:2]:
        if i[1][-1] in ',./':
            f.write(i[0] + '\t~' + i[1] + '\n')
            a[0].append(i)
        else:
            f.write(i[0] + '\t~~' + i[1] + '\n')
            a[1].append(i)
    else:
        f.write(i[0] + '\t' + i[1] + '\n')
f.close()
w = [(x[0], x[1]) for x in b if len(x[0]) == 2]
f = open('输出/opencc/brevity2.txt', encoding = 'utf-8', mode = 'w')
for i in w:
    f.write(i[0] + '\t' + i[1] + '\n')
    a[2].append(i)
f.close()
f = open('输出/opencc/division.txt', encoding = 'utf-8', mode = 'w')
for i in u:
    f.write(i[0] + '\t' + i[1] + '\n')
f.close()
f = open('输出/其他/选重、无理码和简词集锦.txt', encoding = 'utf-8', mode = 'w')
f.write('选重：\n\n')
for i in a[0]:
    f.write(i[0] + '\t' + i[1] + '\n')
f.write('\n无理：\n\n')
for i in a[1]:
    f.write(i[0] + '\t' + i[1] + '\n')
f.write('\n简词：\n')
for i in a[2]:
    f.write(i[0] + '\t' + i[1] + '\n')
f.close()
