from flask import *
from src3.roaddatabase import select, insert, selectall
app = Flask(__name__, template_folder='templates')
app.secret_key="key"
@app.route('/')
def index():
    return render_template('login.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')


@app.route('/login1', methods=['GET', 'POST'])
def login1():
    username = request.form['username']
    password = request.form['password']
    qry = "select * from login where username=%s AND password=%s"
    values = (username, password)
    result = select(qry,values)
    if (result == None):
        return '''<script>alert("invalid user");window.location="/"</script>'''
    elif (result[3] == "admin"):
        session['id'] = result[0]
        session['lid'] = result[0]
        session['ip_id'] = result[0]
        session['uid'] = result[0]
        return '''<script>window.location="admin"</script>'''
    elif (result[3] == "user"):
        session['id']=result[0]
    elif (result[3] == "police"):
        session['lid'] = result[0]
        return '''<script>window.location="user_home"</script>'''
    else:
        return '''<script>alert("invalid user");window.location="/"</script>'''



@app.route('/admin')
def admin1():
    return render_template('admin.html')

@app.route('/viewpolice')
def viewpolice():
    qry = "SELECT * FROM police"
    result = selectall(qry)
    return render_template('viewpolice.html', value=result)


@app.route('/pdelete')
def pdelete():
   id=request.args.get('id')
   qry="DELETE FROM police WHERE lid=%s"
   values=(str(id))
   result=insert(qry,values)
   qry = "DELETE FROM login WHERE id=%s"
   values = (str(id))
   insert(qry, values)
   return '''<script>alert("Confirm Deletion?");window.location="viewpolice"</script>'''


@app.route('/addpolice1',methods=['GET','POST'])
def addpolice1():
    return render_template('addpolice.html')



@app.route('/addpolice', methods=['GET', 'POST'])
def addpolice():
    fname = request.form['fname']
    mname = request.form['mname']
    lname = request.form['lname']
    phone = request.form['phone']
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    qry = "INSERT INTO login VALUES(NULL,%s,%s,'police')"
    values = (username, password)
    lid = insert(qry, values)
    qry = "INSERT INTO police VALUES(NULL,%s,%s,%s,%s,%s,%s)"
    print(qry)
    values = (str(lid),fname,mname,lname,phone, email)
    insert(qry, values)
    return '''<script>alert("successfully registered");window.location="viewpolice"</script>'''

@app.route('/viewsignal')
def viewsignal():
    qry = "SELECT * FROM signals"
    result = selectall(qry)
    return render_template('viewsignal.html', value=result)



@app.route('/addsignal1',methods=['GET','POST'])
def addsignal1():
    return render_template('addsignal.html')




@app.route('/addsignal', methods=['GET', 'POST'])
def addsignal():
    name = request.form['name']
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    qry = "INSERT INTO signals VALUES(NULL,%s,%s,%s)"
    print(qry)
    values = (name,latitude,longitude)
    insert(qry, values)
    return '''<script>alert("successfully added");window.location="viewsignal"</script>'''

@app.route('/sdelete')
def sdelete():
   id=request.args.get('id')
   qry="DELETE FROM signals WHERE ts_id=%s"
   values=(str(id))
   result=insert(qry,values)
   qry = "DELETE FROM login WHERE id=%s"
   values = (str(id))
   insert(qry, values)
   return '''<script>alert("Confirm deletion?");window.location="viewsignal"</script>'''





@app.route('/viewplace')
def viewplace():
    qry = "SELECT * FROM place"
    result = selectall(qry)
    return render_template('viewplace.html', value=result)


@app.route('/pldelete')
def pldelete():
   id=request.args.get('id')
   qry="DELETE FROM place WHERE ip_id=%s"
   values=(str(id))
   result=insert(qry,values)
   qry = "DELETE FROM login WHERE id=%s"
   values = (str(id))
   insert(qry, values)
   return '''<script>alert("Confirm Deletion?");window.location="viewplace"</script>'''


@app.route('/addplace1',methods=['GET','POST'])
def addplace1():
    return render_template('addplace.html')



@app.route('/addplace', methods=['GET', 'POST'])
def addplace():
    name = request.form['name']
    description = request.form['description']
    latitude = request.form['latitude']
    longitude = request.form['longitude']

    qry = "INSERT INTO place VALUES(NULL,%s,%s,%s,%s)"
    print(qry)
    values = (name,description,latitude,longitude)
    insert(qry, values)
    return '''<script>alert("successfully registered");window.location="admin"</script>'''

@app.route('/updateplace')
def updateplace():
    ip_id=request.args.get('id')
    session['ip_id']=ip_id
   # qry = "SELECT * FROM login WHERE Login_id=%s"
    #values =(str(session['Login_id']))
   # res=select(qry, values)
    qry = "SELECT * FROM place WHERE ip_id=%s"
    values=(str(session['ip_id']))
    result=select(qry, values)
    return render_template('updateplace.html',values=result,)

@app.route('/placeupdate1',methods=['GET', 'POST'])
def placeupdate1():
    name= request.form['name']
    description = request.form['description']
    latitude = request.form['latitude']
    longitude = request.form['longitude']

    qry = "UPDATE place SET name=%s,description=%s,latitude=%s,longitude=%s WHERE ip_id=%s"
    values = (str(session['ip_id']),name,description,latitude, longitude)
    insert(qry, values)
    return '''<script>alert("updated successfully");window.location="viewplace"</script>'''


@app.route('/viewreplyy')
def viewreplyy ():
    qry="SELECT `userregistration`.`fname`,`userregistration`.`mname`,`userregistration`.`lname`,`complaint`.* FROM `complaint` JOIN `userregistration` ON `userregistration`.lid=`complaint`.`uid` WHERE `complaint`.`status`='pending'"
    result = selectall(qry)
    return render_template('viewreply.html', value=result)


@app.route('/addreplyy')
def addreplyy():
    uid=request.args.get('id')
    session['uid']=uid
    return render_template('addreply.html')

@app.route('/replyy', methods=['GET', 'POST'])
def replyy():
        status = request.form['status']
        qry = "UPDATE complaint SET status=%s WHERE status='pending' AND sc_id=%s"
        values = (status,str(session['uid']))
        insert(qry, values)
        return '''<script>alert("reply send successfully");window.location="viewreplyy"</script>'''

@app.route('/viewusers')
def viewusers():
    qry = "SELECT `userregistration`.*,`login`.`User_type` FROM `userregistration` JOIN `login` ON `login`.`id`=`userregistration`.`lid` WHERE `login`.`User_type`='user' OR `login`.`User_type`='block'"
    result = selectall(qry)
    return render_template('viewusers.html', value=result)


@app.route('/appr',methods=['get','post'])
def appr():
    id = request.args.get('id')
    qry = "UPDATE login set User_type='user' WHERE User_type='block' AND id=%s"
    values = (str(id))
    insert(qry, values)
    return '''<script>alert("confirm unblock");window.location="viewusers"</script>'''

@app.route('/addusers1')
def addusers1():
    return render_template('addusers.html')

@app.route('/adduser', methods=['GET', 'POST'])
def adduser():
    fname = request.form['fname']
    mname = request.form['mname']
    lname = request.form['lname']
    phone = request.form['phone']
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    qry = "INSERT INTO login VALUES(NULL,%s,%s,'user')"
    values = (username, password)
    lid = insert(qry, values)
    qry = "INSERT INTO userregistration VALUES(NULL,%s,%s,%s,%s,%s,%s)"
    print(qry)
    values = (str(lid), fname, mname,lname,phone, email)
    insert(qry, values)
    return '''<script>alert("successfully registered");window.location="/"</script>'''

@app.route('/block',methods=['get','post'])
def block():
   id=request.args.get('id')
   qry = "UPDATE login SET `User_type`='block' WHERE id=%s"
   values = (str(id))
   insert(qry, values)
   return '''<script>alert("Confirm block?");window.location="viewusers"</script>'''

@app.route('/logout')
def logout():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

