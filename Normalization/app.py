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
    
    f1=request.form['f1']
    f4=open(f1, 'r',encoding='utf-8-sig', errors='ignore')
    roots = f4.readlines()
    mylist =list(dict.fromkeys(roots))
    mylist.sort()
    mk = (1)
    out_file = f1.split(".")[0]+"_"+'Normalizationunqtokenoutput.txt'
    a =  open(out_file, 'w',encoding='utf8', errors='ignore')
    for word in mylist:
        rangeStart = r"\u0C80"
        rangeEnd = r"\u0CFF"
        pattern = rangeStart + '-' + rangeEnd
        if re.match('^[' + pattern + ']+$',word) != None:
            a.write(str (mk)+"\t"+"".join(word))
            mk = mk + 1
    a.close()
    mk = (1)
    out_file1 = f1.split(".")[0]+"_"+'Normalizationtokenoutput.txt'
    a =  open(out_file1, 'w',encoding='utf8', errors='ignore')
    for word in roots:
        rangeStart = r"\u0C80"
        rangeEnd = r"\u0CFF"
        pattern = rangeStart + '-' + rangeEnd
        if re.match('^[' + pattern + ']+$',word) != None:
            a.write(str (mk)+"\t"+"".join(word))
            mk = mk + 1
    a.close()
    return render_template('f1.html')
           
if __name__=="__main__":
    app.run()
               
                                        
                                
                       
           
    
                                    
