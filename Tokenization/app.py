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
    roots = f4.read()
    roots = roots.split()
    g =  open('output.txt', 'w',encoding='utf8', errors='ignore')
    for line in roots:
        g.write(line+"\n")
    g.close()
    
    return render_template('f1.html')
        

    
if __name__=="__main__":
    app.run()
               
                                        
                                
                       
           
    
                                    
