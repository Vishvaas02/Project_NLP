from flask import Flask,render_template
from flask import request
import app
import re
import pandas as pd
import os

app=Flask(__name__)
@app.route('/')
def index():
    return render_template("f1.html")
@app.route('/nomalise',methods=['POST','GET'])
def norma():


    prefixes = []
    with open('prefix.txt', encoding="utf8") as my_file:
        prefixes = [i.strip() for i in my_file]
   
    suffixes = []
    my_file1 = open('suffix.txt', encoding="utf8")
    suffixes = [i.split() for i in my_file1]
    #print (suffixes)


    lx = []
    my_file1 = open('lexicon.csv', encoding="utf8")
    lx = [i.split() for i in my_file1]
    f1=request.form['f1']
    f4=open(f1, 'r',encoding='utf8', errors='ignore')
    mn = ''
    w = []
    wd = [i.split() for i in f4]
    f5=open(f1, 'r',encoding='utf8', errors='ignore')
    wqd = [i.split() for i in f5]
    f6=open(f1, 'r',encoding='utf8', errors='ignore')
    wqd1 = [i.split() for i in f6]
    f7=open(f1, 'r',encoding='utf8', errors='ignore')
    wqd2 = [i.split() for i in f7]
    b = open('output.txt','w',encoding = 'utf8')
    for q,w,k,x,l in zip(wd,wqd,wqd1,wqd2,lx):
        temp = ''
        prefix = '-'
        suffix = '-'
        suffix1 = '-'
        temp1 = ''
        temp2=''
        p = ''
        last =''
        temp =''
        temp = w[1]
        flag = 0
        #print (w)
        kp = (0)
        for l in lx:
            if w[1].startswith(tuple(l)) and w[1].endswith(tuple(l)):
                flag = 1
                suffix1 = ",".join(str(item) for item in l[1:])
                b.write ("".join(str(kp))+"\t"+"".join(x[0])+"\t"+"".join(x[1])+"\t"+"".join(prefix)+"\t"+"".join(w[1])+"\t"+"".join(suffix)+"\t"+"".join(suffix1)+"\n")
        if flag == 0:
            for p in prefixes:
                if w[1].startswith(p):
                    m= (1)
                    prefix = ''
                    prefix += p
                    # remove prefix from word
                    temp2 = q[1][len(p):]
                    temp = w[1][len(p):]
                    w[1] = temp
                    b.write ("".join(str(m))+"\t"+"".join(q[0])+"\t" +"".join(q[1])+ "\t"+"".join(prefix) + "\t" + "".join(temp2) + "\t"+"".join("-")+"\n")
   
            for s in suffixes:
                if w[1].endswith(tuple(s)):
                    mm = (2)
                    #print (s)
                    suffix = ""
                    suffix = s[0]
                    suffix1 =",".join(str(item) for item in s[1:])
                    last = s[-1]
                    # remove suffix from word
                    temp1 = k[1][:-len(s[0 ])]
                    temp = w[1][:-len(s[0])]
                    b.write ("".join(str(mm))+"\t"+"".join(k[0])+"\t" +"".join(k[1])+"\t"+"".join("-")+"\t"+"".join(temp1) + "\t" +"".join(suffix)+"\t"+"".join(suffix1)+"\t"+"".join(last)+"\n")
           
            k=(3)
            b.write ("".join(str(k))+"\t"+"".join(x[0])+"\t"+"".join(x[1])+"\t"+"".join(prefix)+"\t"+"".join(temp)+"\t"+"".join(suffix)+"\t"+"".join(suffix1)+"\t"+"".join(last)+"\n")
    b.close()
    lines_seen = set() # holds lines already seen
    outfile = open("stemmeroutput.txt", "w",encoding='utf8')
    for line in open("output.txt", "r",encoding='utf8'):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
    return render_template('f1.html')
        

    
if __name__=="__main__":
    app.run()
               
                                        
                                
                       
           
    
                                    
