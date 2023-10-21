from flask import Flask,render_template
from flask import request
from flask import Flask,render_template,redirect,url_for,flash,request 
import app
import re
import pandas as pd
import os
from forms import NounForm,VerbForm,OtherForm
import numpy as np
import itertools


app=Flask(__name__)
app.config['SECRET_KEY']='e80221527ae2691b4130960d62e5843b'


@app.route('/')
def index():
    return render_template("main_page.html")

    
@app.route('/Tokenization')
def Tokenization():
    return render_template("Tokenization.html")

    
@app.route('/Tokenization',methods=['POST','GET'])
def Tokenization1():
    
    f1=request.form['f1']
    f4=open(f1, 'r',encoding='utf-8-sig', errors='ignore')
    roots = f4.read()
    roots = roots.split()
    out_file = f1.split(".")[0].split("_")[0]+"_"+'Tokenout.txt'
    g =  open(out_file, 'w',encoding='utf8', errors='ignore')
    out_file = f1.split(".")[0].split("_")[0]+"_"+'ViewTokenout.txt'
    gl =  open(out_file, 'w',encoding='utf8', errors='ignore')
    gl.write("TOKEN_NO"+"\t"+"TOKENS"+"\n")
    kpl=(1)
    for line in roots:
        g.write(line+"\n")
        gl.write(str(kpl)+"\t"+line+"\n")
        kpl=kpl+1
    g.close()
    
    return render_template('Tokenview.html')

    
@app.route('/Tokenview/')
def Token():
    return render_template("Tokenview.html")


@app.route('/Normalization')
def Normalization():
    return render_template("Normalization.html")

    
@app.route('/Normalization',methods=['POST','GET'])
def Normalization1():
    
    f1=request.form['f1']
    f4=open(f1, 'r',encoding='utf-8-sig', errors='ignore')
    roots = f4.readlines()
    mylist =list(dict.fromkeys(roots))
    mk = (1)
    out_file = f1.split(".")[0].split("_")[0]+"_"+'Normunqtokenout.txt'
    a =  open(out_file, 'w',encoding='utf8', errors='ignore')
    out_file = f1.split(".")[0].split("_")[0]+"_"+'ViewNormunqtokenout.txt'
    gl =  open(out_file, 'w',encoding='utf8', errors='ignore')
    gl.write("TOKEN_NO"+"\t"+"TOKENS"+"\n")
    for word in mylist:
        rangeStart = r"\u0C80"
        rangeEnd = r"\u0CFF"
        pattern = rangeStart + '-' + rangeEnd
        if re.match('^[' + pattern + ']+$',word) != None:
            a.write(str (mk)+"\t"+"".join(word))
            gl.write(str (mk)+"\t"+"".join(word))
            mk = mk + 1
    a.close()
    mk = (1)
    out_file = f1.split(".")[0].split("_")[0]+"_"+'ViewNormtokenout.txt'
    a =  open(out_file, 'w',encoding='utf8', errors='ignore')
    for word in roots:
        rangeStart = r"\u0C80"
        rangeEnd = r"\u0CFF"
        pattern = rangeStart + '-' + rangeEnd
        if re.match('^[' + pattern + ']+$',word) != None:
            a.write(str (mk)+"\t"+"".join(word))
            mk = mk + 1
    a.close()
    
    return render_template('Normalizationview.html')

    
@app.route('/Normalizationview/')
def Normal():
    return render_template("Normalizationview.html")


@app.route('/MorphologicalStemmer')
def MorphologicalStemmer():
    return render_template("MorphologicalStemmer.html")


@app.route('/MorphologicalStemmer',methods=['POST','GET'])
def MorphologicalStemmer1():
    
    prefixes = []
    with open('prefix.txt', encoding="utf8") as my_file:
        prefixes = [i.strip() for i in my_file]
   
    suffixes = []
    my_file1 = open('suffix.txt', encoding="utf8")
    suffixes = [i.split() for i in my_file1]
    lx = []
    my_file1 = open('lexicon.txt', encoding="utf8")
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

    out_file = f1.split(".")[0].split("_")[0]+"_"+'Tempstemmerout.txt'
    b = open(out_file,'w',encoding = 'utf8')

    out_file = f1.split(".")[0].split("_")[0]+"_"+'ViewTempstemmerout.txt'
    gl= open(out_file,'w',encoding = 'utf8')

    gl.write("ID"+"\t"+"TOKEN_NO"+"\t"+"TOKEN"+"\t"+"PREFIX"+"\t"+"STEM"+"\t"+"SUFFIX"+"\t"+"SUFFIX_FEATURE"+"\t"+"REFERENCE"+"\n")
    
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
                last = l[-1]
                suffix1 = ",".join(str(item) for item in l[1:])
                b.write ("".join(str(kp))+"\t"+"".join(x[0])+"\t"+"".join(x[1])+"\t"+"".join(prefix)+"\t"+"".join(w[1])+"\t"+"".join(suffix)+"\t"+"".join(suffix1)+"\t"+"".join(last)+"\n")
                gl.write ("".join(str(kp))+"\t"+"".join(x[0])+"\t"+"".join(x[1])+"\t"+"".join(prefix)+"\t"+"".join(w[1])+"\t"+"".join(suffix)+"\t"+"".join(suffix1)+"\t"+"".join(last)+"\n")
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
                    b.write ("".join(str(m))+"\t"+"".join(q[0])+"\t" +"".join(q[1])+ "\t"+"".join(prefix) + "\t" + "".join(temp2) + "\t"+"".join("-")+ "\t"+"".join("-")+ "\t"+"".join("-")+"\n")
                    gl.write ("".join(str(m))+"\t"+"".join(q[0])+"\t" +"".join(q[1])+ "\t"+"".join(prefix) + "\t" + "".join(temp2) + "\t"+"".join("-")+ "\t"+"".join("-")+ "\t"+"".join("-")+"\n")
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
                    gl.write ("".join(str(mm))+"\t"+"".join(k[0])+"\t" +"".join(k[1])+"\t"+"".join("-")+"\t"+"".join(temp1) + "\t" +"".join(suffix)+"\t"+"".join(suffix1)+"\t"+"".join(last)+"\n")
               
            k=(3)
            b.write ("".join(str(k))+"\t"+"".join(x[0])+"\t"+"".join(x[1])+"\t"+"".join(prefix)+"\t"+"".join(temp)+"\t"+"".join(suffix)+"\t"+"".join(suffix1)+"\t"+"".join(last)+"\n")
            gl.write ("".join(str(k))+"\t"+"".join(x[0])+"\t"+"".join(x[1])+"\t"+"".join(prefix)+"\t"+"".join(temp)+"\t"+"".join(suffix)+"\t"+"".join(suffix1)+"\t"+"".join(last)+"\n")
    b.close()
    gl.close()
    lines_seen = set() # holds lines already seen

    out_file = f1.split(".")[0].split("_")[0]+"_"+'stemmerout.txt'
    outfile = open(out_file, "w",encoding='utf8')

    out_file = f1.split(".")[0].split("_")[0]+"_"+'Tempstemmerout.txt'
    for line in open(out_file, "r",encoding='utf8'):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
    lines_seen = set() # holds lines already seen

    out_file = f1.split(".")[0].split("_")[0]+"_"+'Viewstemmerout.txt'
    outfile = open(out_file, "w",encoding='utf8')
    
    out_file = f1.split(".")[0].split("_")[0]+"_"+'ViewTempstemmerout.txt'
    for line in open(out_file, "r",encoding='utf8'):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()

    return render_template('stemmerview.html')
    
@app.route('/stemmerview/')
def stemmer():
    return render_template("stemmerview.html")



@app.route('/Morphologicalanalyzer')
def Morphologicalanalyzer():
    return render_template("Morphologicalanalyzer.html")
    
@app.route('/Morphologicalanalyzer',methods=['POST','GET'])

def Morphologicalanalyzer1():
    
    lx = []
    my_file1 = open('lexicon.txt', encoding="utf8")
    lx = [i.split() for i in my_file1]
    #a.write (lx)
    st = []
    f1=request.form['f1']
    f4=open(f1, 'r',encoding='utf-8-sig', errors='ignore')
    st = [i.split() for i in f4]
    #print (st)
    out_file = f1.split(".")[0].split("_")[0]+"_"+'fnloutwithroots.txt'

    a = open(out_file,'w',encoding='utf8')
    a.write("TOKEN_NO"+"\t"+"TOKEN"+"\t"+"PREFIX"+"\t"+"STEM"+"\t"+"SUFFIX"+"\t"+"STATUS""\t"+"CATEGORY"+"\t"+"FEATURES"+"\t"+"FEATURES"+"\n")

    out_file = f1.split(".")[0].split("_")[0]+"_"+'fnloutwithoutroot.txt'
    g = open(out_file,'w',encoding='utf8')
    g.write("TOKEN_NO"+"\t"+"TOKEN"+"\t"+"PREFIX"+"\t"+"STEM"+"\t"+"SUFFIX"+"\t"+"STATUS"+"\n")
    for s in st:
        flag = 0
        for l in lx:
            if s[0] == '0':
                if s[4].startswith(tuple(l)) and s[4].endswith(tuple(l)):
                    flag = 1
                    if l[1] =='J':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಗುಣವಾಚಕ"+"\t"+"-"+"\t"+"-"+"\n")
                    elif l[1] =='D':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾವಿಶೇಷಣ"+"\t"+"-"+"\t"+"-"+"\n")
                    elif l[1] =='A':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಅವ್ಯಯ್ಯ"+"\t"+"-"+"\t"+"-"+"\n")
                    elif l[1] =='N':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+"-"+"\t"+"-"+"\n")
                    elif l[1] =='V':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"-"+"\t"+"-"+"\n")
                    else:
                        a.write(s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Suffix feature and lexicon feature not matched"+"\t"+"-"+"\t"+"-"+"\t"+"-"+"\n")
        if flag == 0:
            if s[0] =='0':
                a.write(s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root word is not in the lexicon"+"\t"+"-"+"\t"+"-"+"\t"+"-"+"\n")
                g.write(s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root word is not in the lexicon"+"\n")

        flag = 0
        for l in lx:
            if s[0] == '1':
                if s[4].startswith(tuple(l)) and s[4].endswith(tuple(l)):
                    flag = 1
                    if l[1] =='J':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಗುಣವಾಚಕ"+"\t"+"-"+"\t"+"-"+"\n")
                    elif l[1] =='D':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾವಿಶೇಷಣ"+"\t"+"-"+"\t"+"-"+"\n")
                    elif l[1] =='A':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಅವ್ಯಯ್ಯ"+"\t"+"-"+"\t"+"-"+"\n")
                    elif l[1] =='N':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+"-"+"\t"+"-"+"\n")
                    elif l[1] =='V':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"-"+"\t"+"-"+"\n")
                    else:
                        a.write(s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Suffix feature and lexicon feature not matched"+"\t"+"-"+"\t"+"-"+"\t"+"-"+"\n")
        if flag == 0:
            if s[0] =='1':
                a.write(s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root word is not in the lexicon"+"\t"+"-"+"\t"+"-"+"\t"+"-"+"\n")
                g.write(s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root word is not in the lexicon"+"\n")

    
        flag = 0
        for l in lx:
            if s[0] == '2':
                if s[4].startswith(tuple(l)) and s[4].endswith(tuple(l)):
                    flag = 1
                    if l[1] =='J':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಗುಣವಾಚಕ"+"\t"+"-"+"\t"+"-"+"\n")
                    elif l[1] =='D':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾವಿಶೇಷಣ"+"\t"+"-"+"\t"+"-"+"\n")
                    elif l[1] =='A':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಅವ್ಯಯ್ಯ"+"\t"+"-"+"\t"+"-"+"\n")
                    elif l[1] =='N':
                        if [sub for sub in l[3] if sub in s[6]]:
                            if s[7] == '1':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಪ್ರತಮಾ ವಿಭಕ್ತಿ, ಏಕ ವಚನಾ"+"\n")
                            if s[7]=='2':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಪ್ರತಮಾ ವಿಭಕ್ತಿ, ಬಾಹು ವಚನಾ"+"\n")
                            if s[7]=='3':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಡಿವಿತಿಯಾ ವಿಭಕ್ತಿ, ಏಕ ವಚನಾ"+"\n")
                            if s[7]=='4':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಡಿವಿಥಿಯಾ ವಿಭಕ್ತಿ, ಬಹು ವಚನಾ"+"\n")
                            if s[7]=='5':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಥ್ರೂಟಿಯಾ ವಿಭಕ್ತಿ, ಏಕ ವಚನಾ"+"\n")
                            if s[7]=='6':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಥ್ರೂಟಿಯಾ ವಿಭಕ್ತಿ, ಬಹು ವಚನಾ"+"\n")
                            if s[7]=='7':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಚತುರ್ಥಿ, ಏಕ ವಚನಾ"+"\n")
                            if s[7]=='8':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಚತುರ್ಥಿ ವಿಭಕ್ತಿ, ಬಾಹು ವಚನಾ"+"\n")
                            if s[7]=='9':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಶಸ್ತಿ ವಿಭಕ್ತಿ, ಏಕ ವಚನಾ"+"\n")
                            if s[7]=='10':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಶಷ್ಟಿ ವಿಭಕ್ತಿ, ಬಹು ವಚನಾ"+"\n")
                            if s[7]=='11':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಸಪ್ತಮಿ, ಇಕಾ ವಚನಾ"+"\n")
                            if s[7]=='12':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಸಪ್ತಮಿ ವಿಭಕ್ತಿ, ಬಾಹು ವಚನಾ"+"\n")
                            if s[7]=='13':
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಸಂಭೋಧನ ಪ್ರತಿಮಾ ವಿಭಕ್ತಿ, ಏಕ ವಚನಾ"+"\n")
                            if s[7]=='14':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಸಂಭೋಧನ ಪ್ರತಿಮಾ ವಿಭಕ್ತಿ, ಬಹು ವಚನಾ"+"\n")
                    elif l[1] =='V':
                        if s[6].startswith(l[4]) or s[6].startswith(l[3]) or s[6].startswith(l[2]):
                            if s[7] == '1':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭೂತಕಾಲ"+"\t"+ "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t"+ "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t"+ "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                            if s[7] == '2':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭೂತಕಾಲ"+"\t"+"ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t"+"ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t"+"ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                            if s[7] == '3':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭೂತಕಾಲ"+"\t" + "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಸ್ತ್ರೀಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ  "+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t"+"ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಸ್ತ್ರೀಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t"+ "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಸ್ತ್ರೀಲಿಂಗ ಲಿಂಗ"+"\n")
                            if s[7] == '4':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭೂತಕಾಲ"+"\t" + "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t" + "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t" + "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                            if s[7] == '5':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭೂತಕಾಲ"+"\t" + "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ತಟಸ್ಥ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t" + "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ತಟಸ್ಥ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t" + "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ತಟಸ್ಥ ಲಿಂಗ"+"\n")
                            if s[7] == '6':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭೂತಕಾಲ"+"\t" +"ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t" +"ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t" +"ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                            if s[7] == '7':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭೂತಕಾಲ"+"\t"  + "ಎರಡನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t"  + "ಎರಡನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t"  + "ಎರಡನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                            if s[7] == '8':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭೂತಕಾಲ"+"\t"+"ಎರಡನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t"+"ಎರಡನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t"+"ಎರಡನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                            if s[7] == '9':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭೂತಕಾಲ"+"\t"+ "ಮೊದಲ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t"+ "ಮೊದಲ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t"+ "ಮೊದಲ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                            if s[7] == '10':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭೂತಕಾಲ"+"\t"+"ಮೊದಲ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t"+ "ಮೊದಲ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t"+ "ಮೊದಲ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                        else:
                            a.write(s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Suffix feature and lexicon feature not matched"+"\n")
        if flag == 0:
            if s[0] == '2':
                a.write(s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root word is not in the lexicon"+"\t"+"-"+"\t"+"-"+"\t"+"-"+"\n")
                g.write(s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root word is not in the lexicon"+"\n")

        flag = 0
        for l in lx:
            if s[0] == '3':
                if s[4].startswith(tuple(l)) and s[4].endswith(tuple(l)):
                    flag = 1
                    if l[1] =='J':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಗುಣವಾಚಕ"+"\t"+"-"+"\t"+"-"+"\n")
                    elif l[1] =='D':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾವಿಶೇಷಣ"+"\t"+"-"+"\t"+"-"+"\n")
                    elif l[1] =='A':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಅವ್ಯಯ್ಯ"+"\t"+"-"+"\t"+"-"+"\n")
                    elif l[1] =='N':
                        if [sub for sub in l[3] if sub in s[6]]:
                            if s[7] == '1':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಪ್ರತಮಾ ವಿಭಕ್ತಿ, ಏಕ ವಚನಾ"+"\n")
                            if s[7]=='2':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಪ್ರತಮಾ ವಿಭಕ್ತಿ, ಬಾಹು ವಚನಾ"+"\n")
                            if s[7]=='3':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಡಿವಿತಿಯಾ ವಿಭಕ್ತಿ, ಏಕ ವಚನಾ"+"\n")
                            if s[7]=='4':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಡಿವಿಥಿಯಾ ವಿಭಕ್ತಿ, ಬಹು ವಚನಾ"+"\n")
                            if s[7]=='5':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಥ್ರೂಟಿಯಾ ವಿಭಕ್ತಿ, ಏಕ ವಚನಾ"+"\n")
                            if s[7]=='6':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಥ್ರೂಟಿಯಾ ವಿಭಕ್ತಿ, ಬಹು ವಚನಾ"+"\n")
                            if s[7]=='7':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಚತುರ್ಥಿ, ಏಕ ವಚನಾ"+"\n")
                            if s[7]=='8':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಚತುರ್ಥಿ ವಿಭಕ್ತಿ, ಬಾಹು ವಚನಾ"+"\n")
                            if s[7]=='9':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಶಸ್ತಿ ವಿಭಕ್ತಿ, ಏಕ ವಚನಾ"+"\n")
                            if s[7]=='10':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಶಷ್ಟಿ ವಿಭಕ್ತಿ, ಬಹು ವಚನಾ"+"\n")
                            if s[7]=='11':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಸಪ್ತಮಿ, ಇಕಾ ವಚನಾ"+"\n")
                            if s[7]=='12':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಸಪ್ತಮಿ ವಿಭಕ್ತಿ, ಬಾಹು ವಚನಾ"+"\n")
                            if s[7]=='13':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಸಂಭೋಧನ ಪ್ರತಿಮಾ ವಿಭಕ್ತಿ, ಏಕ ವಚನಾ"+"\n")
                            if s[7]=='14':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಸಂಭೋಧನ ಪ್ರತಿಮಾ ವಿಭಕ್ತಿ, ಬಹು ವಚನಾ"+"\n")
                    elif l[1] =='V':
                        if s[6].startswith(l[4]) or s[6].startswith(l[3]) or s[6].startswith(l[2]):
                            if s[7] == '1':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭೂತಕಾಲ"+"\t"+ "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t"+ "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t"+ "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                            if s[7] == '2':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭೂತಕಾಲ"+"\t"+"ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t"+"ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t"+"ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                            if s[7] == '3':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭೂತಕಾಲ"+"\t" + "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಸ್ತ್ರೀಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ  "+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t"+"ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಸ್ತ್ರೀಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t"+ "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಸ್ತ್ರೀಲಿಂಗ ಲಿಂಗ"+"\n")
                            if s[7] == '4':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭೂತಕಾಲ"+"\t" + "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t" + "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t" + "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                            if s[7] == '5':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭೂತಕಾಲ"+"\t" + "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ತಟಸ್ಥ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t" + "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ತಟಸ್ಥ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t" + "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ತಟಸ್ಥ ಲಿಂಗ"+"\n")
                            if s[7] == '6':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭೂತಕಾಲ"+"\t" +"ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t" +"ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t" +"ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                            if s[7] == '7':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭೂತಕಾಲ"+"\t"  + "ಎರಡನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t"  + "ಎರಡನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t"  + "ಎರಡನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                            if s[7] == '8':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭೂತಕಾಲ"+"\t"+"ಎರಡನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t"+"ಎರಡನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t"+"ಎರಡನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                            if s[7] == '9':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭೂತಕಾಲ"+"\t"+ "ಮೊದಲ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t"+ "ಮೊದಲ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t"+ "ಮೊದಲ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                            if s[7] == '10':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭೂತಕಾಲ"+"\t"+"ಮೊದಲ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t"+ "ಮೊದಲ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t"+ "ಮೊದಲ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                        else:
                            a.write(s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Suffix feature and lexicon feature not matched"+"\n")
        if flag == 0:
            if s[0] == '3':
                a.write(s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root word is not in the lexicon"+"\t"+"-"+"\t"+"-"+"\t"+"-"+"\n")
                g.write(s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root word is not in the lexicon"+"\n")

    a.close()
    g.close()

    return render_template('Morphologyview.html')
 
@app.route('/Morphologyview/')
def Morphology():
    return render_template("Morphologyview.html") 
        
@app.route("/HOME")
def home():
  return render_template('HOME.html',)
    
@app.route("/VIEW",methods=['GET','POST'])
def VIEW():
  return render_template('VIEW.html')

@app.route("/Noun",methods=['GET','POST'])
def Noun():
    form=NounForm()
    Genders = ['ಪುಲ್ಲಿಂಗ', 'ಸ್ತ್ರೀಲಿಂಗ', 'ನಪುಂಸಕ ಲಿಂಗ', 'ಇತರೆ']
    Noun_categories=['1(ನು - ಹುಡುಗ)','2(ನು - ಅಣ್ಣ)','3(ಳು-ಕಮಲ)','4(ಳು - ಅಕ್ಕ )','5(ವು - ಮರ )','6(ದು - ಚಿಕ್ಕ )','7(ಯು - ಕವಿ )','8(ಯು - ಗೌರಿ )',
                     '9(ಯು - ತಾಯಿ )','10(ವು - ಗುರು )','11(ಉ - ಹೆಣ್ಣು )','12(ಯು - ತಂದೆ )']
#    if form.validate_on_submit():
#         if 'ಮುಖಪುಟ' in request.form:return redirect(url_for('home'))
#    
    if form.is_submitted():
        return render_template('HOME.html',)
    return render_template('NOUN.html',title='Noun',form=form,Genders=Genders,Noun_categories=Noun_categories)


@app.route("/Verb",methods=['GET','POST'])
def Verb():
    form=VerbForm()
    Present_tense=['1R (ತ್ತಾನೆ - ತಿನ್ನು )','2R (ಯುತ್ತಾನೆ - ಕುಡಿ )',]
    Future_tense=['1F (ವನು - ಕಾಡು )','2F (ಯುವನು = ಹರಿ )']
    Past_tense=['1S (ಅಂದನು -ತಿನ್ನು )','2S (ಅಂಡನು -ಕಾಣು )','3S (ಕ್ಕನು - ನಗು )','4S (ತ್ತನು - ಅಳು )','5S  (ಟ್ಟನು - ಈಡು)','6S (ದ್ದನು - ಬೀಳು )','7S (ಇದನು - ಹಾಡು )','8S (ಗ್ಗಿದನು - ಬಾಗು )','9S (ದನು - ಬರೆ)','10S (ಅಂತನು- ನಿಲ್ಲು )']
#    if form.validate_on_submit():
#         if 'ಮುಖಪುಟ' in request.form:return redirect(url_for('home'))
#    
    if form.is_submitted():
        return render_template('HOME.html',)
    return render_template('VERB.html',title='Verb',form=form,Present_tense=Present_tense,Future_tense=Future_tense,Past_tense=Past_tense)

@app.route("/Other",methods=['GET','POST'])
def Other():
    form=OtherForm()
    Other_categories=['ವಿಶೇಷಣ','ಕ್ರಿಯಾವಿಶೇಷಣ','ಅವ್ಯಯ']
#    if form.validate_on_submit():
#         if 'ಮುಖಪುಟ' in request.form:return redirect(url_for('home'))
#    
    if form.is_submitted():
        return render_template('HOME.html',)
    return render_template('OTHER.html',title='Other',form=form,Other_categories=Other_categories)
    

@app.route("/result1", methods= ['GET','POST'])
def result1():
   output1 = request.form['Noun_word']
   output2='N'
   output3 = request.form['Genders']
   if (output3 == 'ಪುಲ್ಲಿಂಗ' ):output3='M'
   if (output3 == 'ಸ್ತ್ರೀಲಿಂಗ' ):output3='F'
   if (output3 == 'ನಪುಂಸಕ ಲಿಂಗ' ):output3='N'
   if (output3 == 'ಇತರೆ' ):output3='X'
   
   output4 = request.form['Noun_categories']
   
   if (output4 == '1(ನು - ಹುಡುಗ)'):output4='1'
   if (output4 == '2(ನು - ಅಣ್ಣ)'):output4='2'
   if (output4 == '3(ಳು-ಕಮಲ)'):output4='3'
   if (output4 == '4(ಳು - ಅಕ್ಕ )'):output4='4'
   if (output4 == '5(ವು - ಮರ )'):output4='5'
   if (output4 == '6(ದು - ಚಿಕ್ಕ )'):output4='6'
   if (output4 == '7(ಯು - ಕವಿ )'):output4='7'
   if (output4 == '8(ಯು - ಗೌರಿ )'):output4='8'
   if (output4 == '9(ಯು - ತಾಯಿ )'):output4='9'
   if (output4 == '10(ವು - ಗುರು )'):output4='10'
   if (output4 == '11(ಉ - ಹೆಣ್ಣು )'):output4='11'
   if (output4 == '12(ಯು - ತಂದೆ )'):output4='12'
   
   
   #final_output=output1 +"\t\t\t"+ output2 +"\t\t" + output3+'\t\t'+output4
   a = open('lexicon.txt','a',encoding="utf-8")
   a.write(output1 +"\t"+ output2 +"\t" + output3+"\t"+output4+"\t"+"\t"+"\n")
   a.close()
   return render_template('HOME.html',)

@app.route("/result2", methods= ['GET','POST'])
def result2():
   output1 = request.form['Verb_word']
   output2='V'
   output3 = request.form['Present_tense']
   if (output3 == '1R (ತ್ತಾನೆ - ತಿನ್ನು )'):output3='1R'
   if (output3 == '2R (ಯುತ್ತಾನೆ - ಕುಡಿ )'):output3='2R'
   
   output4 = request.form['Future_tense']
   
   if (output4 == '1F (ವನು - ಕಾಡು )'):output4='1F'
   if (output4 == '2F (ಯುವನು = ಹರಿ )'):output4='2F'
   output5 = request.form['Past_tense']
  
   if (output5 == '1S (ಅಂದನು -ತಿನ್ನು )'):output5='1S'
   if (output5 == '2S (ಅಂಡನು -ಕಾಣು )'):output5='2S'
   if (output5 == '3S (ಕ್ಕನು - ನಗು )'):output5='3S'
   if (output5 == '4S (ತ್ತನು - ಅಳು )'):output5='4S'
   if (output5 == '5S  (ಟ್ಟನು - ಈಡು)'):output5='5S'
   if (output5 == '6S (ದ್ದನು - ಬೀಳು )'):output5='6S'
   if (output5 == '7S (ಇದನು - ಹಾಡು )'):output5='7S'
   if (output5 == '8S (ಗ್ಗಿದನು - ಬಾಗು )'):output5='8S'
   if (output5 == '9S (ದನು - ಬರೆ)'):output5='9S'
   if (output5 == '10S (ಅಂತನು- ನಿಲ್ಲು )'):output5='10S'
   
   
    # final_output=output1 +"\t\t\t"+ output2 +"\t\t" + output3 +"\t\t"+ output4 +"\t\t" + output5
   a = open('lexicon.txt','a',encoding="utf-8")
   a.write(output1 +"\t"+ output2 +"\t" +" "+"\t"+ output3 +"\t"+ output4 +"\t" + output5+"\n")
   a.close()
   return render_template('HOME.html',)

@app.route("/result3", methods= ['GET','POST'])
def result3():
   output1 = request.form['Other_word']
   output2 = request.form['Other_categories']
   #final_output=output1 +"\t\t\t"+ output2 
   if(output2 == 'ವಿಶೇಷಣ'):output2='J'
   if(output2 == 'ಕ್ರಿಯಾವಿಶೇಷಣ'):output2='D'
   if(output2 == 'ಅವ್ಯಯ'):output2='A'
   
   a = open('lexicon.txt','a',encoding="utf-8")
   a.write(output1 +"\t"+ output2+"\t"+"\t"+"\t"+"\t"+"\n")
   a.close()
   return render_template('HOME.html',)
    
    
@app.route('/cmTokenization')
def cmTokenization():
    return render_template("cmTokenization.html")
    
@app.route('/cmTokenization',methods=['POST','GET'])
def cmTokenization1():
    
    f1=request.form['f1']
    f4=open(f1, 'r',encoding='utf-8-sig', errors='ignore')
    roots = f4.read()
    roots = roots.split()
    g =  open('cmTokenoutput.txt', 'w',encoding='utf8', errors='ignore')
    for line in roots:
        g.write(line+"\n")
    g.close()
    #Normalization
    f5=open('cmTokenoutput.txt','r',encoding='utf-8-sig', errors='ignore')
    roots = f5.readlines()
    mylist =list(dict.fromkeys(roots))
    mk = (1)
    a =  open('cmNormalizationunqtokenoutput.txt', 'w',encoding='utf8', errors='ignore')
    for word in mylist:
        rangeStart = r"\u0C80"
        rangeEnd = r"\u0CFF"
        pattern = rangeStart + '-' + rangeEnd
        if re.match('^[' + pattern + ']+$',word) != None:
            a.write(str(mk)+"\t"+"".join(word))
            mk = mk + 1
    a.close()
    #Stemmer
    prefixes = []
    with open('prefix.txt', encoding="utf8") as my_file:
        prefixes = [i.strip() for i in my_file]
   
    suffixes = []
    my_file1 = open('suffix.txt', encoding="utf8")
    suffixes = [i.split() for i in my_file1]
    lx = []
    my_file1 = open('lexicon.txt', encoding="utf8")
    lx = [i.split() for i in my_file1]
    f6=open('cmNormalizationunqtokenoutput.txt','r',encoding='utf8', errors='ignore')
    mn = ''
    wd = [i.split() for i in f6]
    f7=open('cmNormalizationunqtokenoutput.txt', 'r',encoding='utf8', errors='ignore')
    wqd = [i.split() for i in f7]
    f8=open('cmNormalizationunqtokenoutput.txt', 'r',encoding='utf8', errors='ignore')
    wqd1 = [i.split() for i in f8]
    f9=open('cmNormalizationunqtokenoutput.txt', 'r',encoding='utf8', errors='ignore')
    wqd2 = [i.split() for i in f9]
    b = open('cmTempstemmeroutput.txt','w',encoding = 'utf8')
    gl= open('cmViewTempstemmeroutput.txt','w',encoding = 'utf8')
    gl.write("ID"+"\t"+"TOKEN_NO"+"\t"+"TOKEN"+"\t"+"PREFIX"+"\t"+"STEM"+"\t"+"SUFFIX"+"\t"+"SUFFIX_FEATURE"+"\t"+"CASE & NUMBER"+"\n")
    
    for q,w,k,x,l in itertools.zip_longest(wd,wqd,wqd1,wqd2,lx):
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
                last = l[-1]
                suffix1 = ",".join(str(item) for item in l[1:])
                b.write ("".join(str(kp))+"\t"+"".join(x[0])+"\t"+"".join(x[1])+"\t"+"".join(prefix)+"\t"+"".join(w[1])+"\t"+"".join(suffix)+"\t"+"".join(suffix1)+"\t"+"".join(last)+"\n")
                gl.write ("".join(str(kp))+"\t"+"".join(x[0])+"\t"+"".join(x[1])+"\t"+"".join(prefix)+"\t"+"".join(w[1])+"\t"+"".join(suffix)+"\t"+"".join(suffix1)+"\t"+"".join(last)+"\n")
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
                    b.write ("".join(str(m))+"\t"+"".join(q[0])+"\t" +"".join(q[1])+ "\t"+"".join(prefix) + "\t" + "".join(temp2) + "\t"+"".join("-")+ "\t"+"".join("-")+ "\t"+"".join("-")+"\n")
                    gl.write ("".join(str(m))+"\t"+"".join(q[0])+"\t" +"".join(q[1])+ "\t"+"".join(prefix) + "\t" + "".join(temp2) + "\t"+"".join("-")+ "\t"+"".join("-")+ "\t"+"".join("-")+"\n")
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
                    gl.write ("".join(str(mm))+"\t"+"".join(k[0])+"\t" +"".join(k[1])+"\t"+"".join("-")+"\t"+"".join(temp1) + "\t" +"".join(suffix)+"\t"+"".join(suffix1)+"\t"+"".join(last)+"\n")
               
            k=(3)
            b.write ("".join(str(k))+"\t"+"".join(x[0])+"\t"+"".join(x[1])+"\t"+"".join(prefix)+"\t"+"".join(temp)+"\t"+"".join(suffix)+"\t"+"".join(suffix1)+"\t"+"".join(last)+"\n")
            gl.write ("".join(str(k))+"\t"+"".join(x[0])+"\t"+"".join(x[1])+"\t"+"".join(prefix)+"\t"+"".join(temp)+"\t"+"".join(suffix)+"\t"+"".join(suffix1)+"\t"+"".join(last)+"\n")
    b.close()
    gl.close()
    lines_seen = set() # holds lines already seen
    outfile = open("cmstemmeroutput.txt", "w",encoding='utf8')
    for line in open("cmTempstemmeroutput.txt", "r",encoding='utf8'):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
    #morphology
    lx = []
    my_file1 = open('lexicon.txt', encoding="utf8")
    lx = [i.split() for i in my_file1]
    #a.write (lx)
    st = []
    f4=open('cmstemmeroutput.txt', 'r',encoding='utf-8-sig', errors='ignore')
    st = [i.split() for i in f4]
    #print (st)
    a = open('cmfinaloutputwithroots.txt','w',encoding='utf8')
    a.write("TOKEN_NO"+"\t"+"TOKEN"+"\t"+"PREFIX"+"\t"+"STEM"+"\t"+"SUFFIX"+"\t"+"STATUS""\t"+"CATEGORY"+"\t"+"FEATURES"+"\t"+"FEATURES"+"\n")
    g = open('cmfinaloutputwithoutroot.txt','w',encoding='utf8')
    g.write("TOKEN_NO"+"\t"+"TOKEN"+"\t"+"PREFIX"+"\t"+"STEM"+"\t"+"SUFFIX"+"\t"+"STATUS"+"\n")
    for s in st:
        flag = 0
        for l in lx:
            if s[0] == '0':
                if s[4].startswith(tuple(l)) and s[4].endswith(tuple(l)):
                    flag = 1
                    if l[1] =='J':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಗುಣವಾಚಕ"+"\t"+"-"+"\t"+"-"+"\n")
                    elif l[1] =='D':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾವಿಶೇಷಣ"+"\t"+"-"+"\t"+"-"+"\n")
                    elif l[1] =='A':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಅವ್ಯಯ್ಯ"+"\t"+"-"+"\t"+"-"+"\n")
                    elif l[1] =='N':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+"-"+"\t"+"-"+"\n")
                    elif l[1] =='V':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"-"+"\t"+"-"+"\n")
                    else:
                        a.write(s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Suffix feature and lexicon feature not matched"+"\t"+"-"+"\t"+"-"+"\t"+"-"+"\n")
        if flag == 0:
            if s[0] =='0':
                a.write(s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root word is not in the lexicon"+"\t"+"-"+"\t"+"-"+"\t"+"-"+"\n")
                g.write(s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root word is not in the lexicon"+"\n")

        flag = 0
        for l in lx:
            if s[0] == '1':
                if s[4].startswith(tuple(l)) and s[4].endswith(tuple(l)):
                    flag = 1
                    if l[1] =='J':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಗುಣವಾಚಕ"+"\t"+"-"+"\t"+"-"+"\n")
                    elif l[1] =='D':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾವಿಶೇಷಣ"+"\t"+"-"+"\t"+"-"+"\n")
                    elif l[1] =='A':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಅವ್ಯಯ್ಯ"+"\t"+"-"+"\t"+"-"+"\n")
                    elif l[1] =='N':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+"-"+"\t"+"-"+"\n")
                    elif l[1] =='V':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"-"+"\t"+"-"+"\n")
                    else:
                        a.write(s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Suffix feature and lexicon feature not matched"+"\t"+"-"+"\t"+"-"+"\t"+"-"+"\n")
        if flag == 0:
            if s[0] =='1':
                a.write(s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root word is not in the lexicon"+"\t"+"-"+"\t"+"-"+"\t"+"-"+"\n")
                g.write(s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root word is not in the lexicon"+"\n")

    
        flag = 0
        for l in lx:
            if s[0] == '2':
                if s[4].startswith(tuple(l)) and s[4].endswith(tuple(l)):
                    flag = 1
                    if l[1] =='J':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಗುಣವಾಚಕ"+"\t"+"-"+"\t"+"-"+"\n")
                    elif l[1] =='D':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾವಿಶೇಷಣ"+"\t"+"-"+"\t"+"-"+"\n")
                    elif l[1] =='A':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಅವ್ಯಯ್ಯ"+"\t"+"-"+"\t"+"-"+"\n")
                    elif l[1] =='N':
                        if [sub for sub in l[3] if sub in s[6]]:
                            if s[7] == '1':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಪ್ರತಮಾ ವಿಭಕ್ತಿ, ಏಕ ವಚನಾ"+"\n")
                            if s[7]=='2':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಪ್ರತಮಾ ವಿಭಕ್ತಿ, ಬಾಹು ವಚನಾ"+"\n")
                            if s[7]=='3':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಡಿವಿತಿಯಾ ವಿಭಕ್ತಿ, ಏಕ ವಚನಾ"+"\n")
                            if s[7]=='4':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಡಿವಿಥಿಯಾ ವಿಭಕ್ತಿ, ಬಹು ವಚನಾ"+"\n")
                            if s[7]=='5':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಥ್ರೂಟಿಯಾ ವಿಭಕ್ತಿ, ಏಕ ವಚನಾ"+"\n")
                            if s[7]=='6':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಥ್ರೂಟಿಯಾ ವಿಭಕ್ತಿ, ಬಹು ವಚನಾ"+"\n")
                            if s[7]=='7':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಚತುರ್ಥಿ, ಏಕ ವಚನಾ"+"\n")
                            if s[7]=='8':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಚತುರ್ಥಿ ವಿಭಕ್ತಿ, ಬಾಹು ವಚನಾ"+"\n")
                            if s[7]=='9':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಶಸ್ತಿ ವಿಭಕ್ತಿ, ಏಕ ವಚನಾ"+"\n")
                            if s[7]=='10':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಶಷ್ಟಿ ವಿಭಕ್ತಿ, ಬಹು ವಚನಾ"+"\n")
                            if s[7]=='11':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಸಪ್ತಮಿ, ಇಕಾ ವಚನಾ"+"\n")
                            if s[7]=='12':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಸಪ್ತಮಿ ವಿಭಕ್ತಿ, ಬಾಹು ವಚನಾ"+"\n")
                            if s[7]=='13':
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಸಂಭೋಧನ ಪ್ರತಿಮಾ ವಿಭಕ್ತಿ, ಏಕ ವಚನಾ"+"\n")
                            if s[7]=='14':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಸಂಭೋಧನ ಪ್ರತಿಮಾ ವಿಭಕ್ತಿ, ಬಹು ವಚನಾ"+"\n")
                    elif l[1] =='V':
                        if s[6].startswith(l[4]) or s[6].startswith(l[3]) or s[6].startswith(l[2]):
                            if s[7] == '1':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭೂತಕಾಲ"+"\t"+ "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t"+ "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t"+ "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                            if s[7] == '2':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭೂತಕಾಲ"+"\t"+"ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t"+"ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t"+"ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                            if s[7] == '3':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭೂತಕಾಲ"+"\t" + "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಸ್ತ್ರೀಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ  "+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t"+"ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಸ್ತ್ರೀಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t"+ "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಸ್ತ್ರೀಲಿಂಗ ಲಿಂಗ"+"\n")
                            if s[7] == '4':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭೂತಕಾಲ"+"\t" + "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t" + "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t" + "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                            if s[7] == '5':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭೂತಕಾಲ"+"\t" + "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ತಟಸ್ಥ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t" + "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ತಟಸ್ಥ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t" + "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ತಟಸ್ಥ ಲಿಂಗ"+"\n")
                            if s[7] == '6':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭೂತಕಾಲ"+"\t" +"ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t" +"ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t" +"ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                            if s[7] == '7':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭೂತಕಾಲ"+"\t"  + "ಎರಡನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t"  + "ಎರಡನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t"  + "ಎರಡನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                            if s[7] == '8':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭೂತಕಾಲ"+"\t"+"ಎರಡನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t"+"ಎರಡನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t"+"ಎರಡನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                            if s[7] == '9':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭೂತಕಾಲ"+"\t"+ "ಮೊದಲ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t"+ "ಮೊದಲ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t"+ "ಮೊದಲ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                            if s[7] == '10':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭೂತಕಾಲ"+"\t"+"ಮೊದಲ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t"+ "ಮೊದಲ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t"+ "ಮೊದಲ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                        else:
                            a.write(s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Suffix feature and lexicon feature not matched"+"\n")
        if flag == 0:
            if s[0] == '2':
                a.write(s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root word is not in the lexicon"+"\t"+"-"+"\t"+"-"+"\t"+"-"+"\n")
                g.write(s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root word is not in the lexicon"+"\n")

        flag = 0
        for l in lx:
            if s[0] == '3':
                if s[4].startswith(tuple(l)) and s[4].endswith(tuple(l)):
                    flag = 1
                    if l[1] =='J':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಗುಣವಾಚಕ"+"\t"+"-"+"\t"+"-"+"\n")
                    elif l[1] =='D':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾವಿಶೇಷಣ"+"\t"+"-"+"\t"+"-"+"\n")
                    elif l[1] =='A':
                        a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಅವ್ಯಯ್ಯ"+"\t"+"-"+"\t"+"-"+"\n")
                    elif l[1] =='N':
                        if [sub for sub in l[3] if sub in s[6]]:
                            if s[7] == '1':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಪ್ರತಮಾ ವಿಭಕ್ತಿ, ಏಕ ವಚನಾ"+"\n")
                            if s[7]=='2':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಪ್ರತಮಾ ವಿಭಕ್ತಿ, ಬಾಹು ವಚನಾ"+"\n")
                            if s[7]=='3':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಡಿವಿತಿಯಾ ವಿಭಕ್ತಿ, ಏಕ ವಚನಾ"+"\n")
                            if s[7]=='4':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಡಿವಿಥಿಯಾ ವಿಭಕ್ತಿ, ಬಹು ವಚನಾ"+"\n")
                            if s[7]=='5':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಥ್ರೂಟಿಯಾ ವಿಭಕ್ತಿ, ಏಕ ವಚನಾ"+"\n")
                            if s[7]=='6':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಥ್ರೂಟಿಯಾ ವಿಭಕ್ತಿ, ಬಹು ವಚನಾ"+"\n")
                            if s[7]=='7':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಚತುರ್ಥಿ, ಏಕ ವಚನಾ"+"\n")
                            if s[7]=='8':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಚತುರ್ಥಿ ವಿಭಕ್ತಿ, ಬಾಹು ವಚನಾ"+"\n")
                            if s[7]=='9':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಶಸ್ತಿ ವಿಭಕ್ತಿ, ಏಕ ವಚನಾ"+"\n")
                            if s[7]=='10':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಶಷ್ಟಿ ವಿಭಕ್ತಿ, ಬಹು ವಚನಾ"+"\n")
                            if s[7]=='11':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಸಪ್ತಮಿ, ಇಕಾ ವಚನಾ"+"\n")
                            if s[7]=='12':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಸಪ್ತಮಿ ವಿಭಕ್ತಿ, ಬಾಹು ವಚನಾ"+"\n")
                            if s[7]=='13':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಸಂಭೋಧನ ಪ್ರತಿಮಾ ವಿಭಕ್ತಿ, ಏಕ ವಚನಾ"+"\n")
                            if s[7]=='14':
                                a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ನಾಮಪದ"+"\t"+l[2]+"\t"+"ಸಂಭೋಧನ ಪ್ರತಿಮಾ ವಿಭಕ್ತಿ, ಬಹು ವಚನಾ"+"\n")
                    elif l[1] =='V':
                        if s[6].startswith(l[4]) or s[6].startswith(l[3]) or s[6].startswith(l[2]):
                            if s[7] == '1':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭೂತಕಾಲ"+"\t"+ "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t"+ "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t"+ "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                            if s[7] == '2':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭೂತಕಾಲ"+"\t"+"ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t"+"ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t"+"ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                            if s[7] == '3':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭೂತಕಾಲ"+"\t" + "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಸ್ತ್ರೀಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ  "+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t"+"ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಸ್ತ್ರೀಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t"+ "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಸ್ತ್ರೀಲಿಂಗ ಲಿಂಗ"+"\n")
                            if s[7] == '4':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭೂತಕಾಲ"+"\t" + "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t" + "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t" + "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                            if s[7] == '5':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭೂತಕಾಲ"+"\t" + "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ತಟಸ್ಥ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t" + "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ತಟಸ್ಥ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t" + "ಮೂರನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ತಟಸ್ಥ ಲಿಂಗ"+"\n")
                            if s[7] == '6':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭೂತಕಾಲ"+"\t" +"ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t" +"ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t" +"ಮೂರನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಪುಲ್ಲಿಂಗ ಲಿಂಗ"+"\n")
                            if s[7] == '7':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭೂತಕಾಲ"+"\t"  + "ಎರಡನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t"  + "ಎರಡನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t"  + "ಎರಡನೇ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                            if s[7] == '8':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭೂತಕಾಲ"+"\t"+"ಎರಡನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t"+"ಎರಡನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t"+"ಎರಡನೇ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                            if s[7] == '9':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭೂತಕಾಲ"+"\t"+ "ಮೊದಲ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t"+ "ಮೊದಲ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t"+ "ಮೊದಲ ವ್ಯಕ್ತಿ, ಏಕವಚನ, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                            if s[7] == '10':
                                if "S" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ಭೂತಕಾಲ"+"\t"+"ಮೊದಲ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "F" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ"+"\t"+"ಭವಿಷ್ಯತ್ಕಾಲ"+"\t"+ "ಮೊದಲ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                                if "R" in s[6]:
                                    a.write (s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root Found"+"\t"+"ಕ್ರಿಯಾಪದ "+"\t"+"ವರ್ತಮಾನ ಕಾಲ"+"\t"+ "ಮೊದಲ ವ್ಯಕ್ತಿ, ಪ್ಲುಲರ್, ಎಲ್ಲಾ ಲಿಂಗ"+"\n")
                        else:
                            a.write(s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Suffix feature and lexicon feature not matched"+"\n")
        if flag == 0:
            if s[0] == '3':
                a.write(s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root word is not in the lexicon"+"\t"+"-"+"\t"+"-"+"\t"+"-"+"\n")
                g.write(s[1]+"\t"+s[2]+"\t"+s[3]+"\t"+s[4]+"\t"+s[5]+"\t"+"Root word is not in the lexicon"+"\n")

    a.close()
    g.close()
    return render_template('cmTokenization.html')
    
@app.route('/cmTokenview/')
def cmToken():
    return render_template("cmTokenview.html")
if __name__=="__main__":
    app.run()
               
                                        
                                
                       
           
    
                                    
