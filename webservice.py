import os
from flask import *
from werkzeug.utils import secure_filename
from src3.roaddatabase import select,selectall,insert
from src3.classify import predictfn
app=Flask(__name__)
@app.route('/login',methods=['post'])
def login():
    username=request.form['username']
    password=request.form['password']
    qry="SELECT * FROM `login` WHERE `username`=%s AND `password`=%s"
    val=(username,password)
    result=select(qry,val)
    id=result[0]
    type=result[3]
    if result is None:
        return jsonify({'task':"invalid"})
    else:
        return jsonify({'task':id+"#"+type})

@app.route('/reg', methods=['GET', 'POST'])
def reg():
    Fname = request.form['Fname']
    Mname = request.form['Mname']
    Lname=request.form['Lname']
    Phone = request.form['Phone']
    Email = request.form['Email']
    username = request.form['username']
    password = request.form['password']
    qry="insert into login values(null,%s,%s,'user')"
    val=(username,password)
    lid=insert(qry,val)
    q="INSERT INTO `userregistration` VALUES(NULL,%s,%s,%s,%s,%s,%s)"
    val=(str(lid),Fname,Mname,Lname,Phone,Email)
    insert(q,val)
    return jsonify({'task':"success"})

@app.route('/viewemergency1',methods=['post'])
def viewemergency1():
    ea_id=request.form['ea_id']
    qry=("select * from department")
    values=('ea_id')
    row_headers = [x[0] for x in qry.description]
    results=select(qry,values)
    json_data = []
    for result in results:
      json_data.append(dict(zip(row_headers, result)))
    print(json_data)
    return jsonify(json_data)

@app.route('/viewsignals',methods=['post'])
def viewsignals():
    ts_id=request.form['ts_id']
    qry=("select * from signals")
    values=('ts_id')
    row_headers = [x[0] for x in qry.description]
    results=select(qry,values)
    json_data = []
    for result in results:
      json_data.append(dict(zip(row_headers, result)))
    print(json_data)
    return jsonify(json_data)

@app.route('/sendproblem',methods=['GET','POST'])
def sendproblem():
    uid=request.form['uid']
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    complaint=request.form['complaint']
    status = request.form['status']
    qry="INSERT INTO complaint VALUES(NULL,%s,%s,%s,'pending')"
    values=(str(uid),latitude,longitude,complaint,status)
    insert(qry,values)
    return jsonify({'task':"success"})


@app.route('/sendemergency',methods=['GET','POST'])
def sendemergency():
    ea_id=request.form['ea_id']
    latitude=request.form['latitude']
    longitude = request.form['longitude']
    description = request.form['description']
    status = request.form['status']
    qry="INSERT INTO emergency VALUES(NULL,%s,%s,curdate(),'pending')"
    values=(str(ea_id),latitude,longitude,description,status)
    insert(qry,values)
    return jsonify({'task':"success"})

@app.route('/viewemergency',methods=['post'])
def viewemergency():
    ea_id=request.form['ea_id']
    qry=("select * from emergency where u_id=%s")
    values=('ea_id')
    row_headers = [x[0] for x in qry.description]
    results=select(qry,values)
    json_data = []
    for result in results:
      json_data.append(dict(zip(row_headers, result)))
    print(json_data)
    return jsonify(json_data)

@app.route('/viewsignal',methods=['post'])
def viewsignal():
    ts_id=request.form['ts_id']
    qry=("select * from signals where ts_id=%s")
    values=('ts_id')
    row_headers = [x[0] for x in qry.description]
    results=select(qry,values)
    json_data = []
    for result in results:
      json_data.append(dict(zip(row_headers, result)))
    print(json_data)
    return jsonify(json_data)

@app.route('/viewposition',methods=['post'])
def viewposition():
    uid=request.form['uid']
    qry=("select * from signals where uid=%s")
    values=('uid')
    row_headers = [x[0] for x in qry.description]
    results=select(qry,values)
    json_data = []
    for result in results:
      json_data.append(dict(zip(row_headers, result)))
    print(json_data)
    return jsonify(json_data)

@app.route('/sportupdate',methods=['GET', 'POST'])
def sportupdate():
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    complaint = request.form['complaint']
    status = request.form['status']
    qry = "UPDATE place SET name=%s,description=%s,latitude=%s,longitude=%s WHERE ip_id=%s"
    values = (str(session['ip_id']),latitude, longitude,complaint,status)
    insert(qry, values)
    return jsonify({'task': "success"})


@app.route('/imgupload',methods=['GET', 'POST'])
def imgupload():
    img=request.files['img']
    lat=request.form['lat']
    long = request.form['long']
    from datetime import datetime
    fn=datetime.now().strftime("%Y%m%d_%H%M%S")+".jpg"
    img.save("static/imgs/"+fn)
    res=predictfn("static/imgs/"+fn)
    if res!="long":
        qry="insert into "




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
