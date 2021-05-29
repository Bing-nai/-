txt=open('C:\\Users\\戴尔\\Desktop\\iepa_srow.txt','r')#分句文本
file=open('C:\\Users\\戴尔\\Desktop\\iepa_sn.txt','a')#空白文本
for i in range(173):#分句文本行数
    A=txt.readline()
    arr=A.split()
    l=len(arr)
    #print(l)
    file.writelines(str(l)+"\n")
txt.close()
file.close()
