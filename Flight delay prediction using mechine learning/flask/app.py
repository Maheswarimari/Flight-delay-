from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import pickle
import os


model = pickle.load(open('flight.pk1','rb' ))
app = Flask(_name_)

@app.route('/')
def home():
         return render_template("index.html")
        @app.route('/prediction',metods =['POST'])

def predict():
        name = request.form['name']
        month=request.form['month']
        dayof month=request.form['dayofmonth']
        dayofweek=request.form['dayofweek']
        origin=request.form['origin']
        if(origin=="msp");
        origin1,origin2,origin3,origin4,origin5=0,0,0,1
        if(origin="dtw");
        origin1,origin2,origin3,origin4,origin5=1,0,0,0,0
       if(origin="jkf");
      origin1,origin2,origin3,origin4,origin5=0,0,1,0,0
      if(origin1,origin2,origin3,origin4,origin5=0,1,0,0,0
         if(origin=="alt");
        origin1,origin2,origin3,origin4,origin5=0,0,0,1,0


destination=request.form('destination')
if(destination=="msp");
destinationa1,destination2,destination3,destination4,destination5=0,0,0,0,1
if(destination=="dtw");
destination1,destination2,destination3,destination4,destination5=1,0,0,0,0
if(destination=="jkf")
destination1,destination2,destination3,destination4,destination5=0,0,1,0,0
if(destination=="sea");
destination1,destination2,destination3,destination4,destination5=0,1,0,0,0
if(destination=="alt");
  destination1,destination2,destination3,destination4,destination5=0,0,0,1,0
  dept=request.form['dept']
arrtime=request.form['arrtime']
actdept=request.form['actdept']
dept15=int(dep-int(actdept))
total=[(name,month,dayofweek,origin1,origin2,origin3,origin4,origin5,destination1,destination2,destination4,destination5)]
y_pred=model.predict(total)
print(y_pred)
if(y_pred[0,1]);
ans="The Flight will be on time"
else:
ans="The Flight will be delayed"
return render_template("index.html",showcase=ans)

if_name =='_main_' :
app.run(debug=True)
