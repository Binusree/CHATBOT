from flask import Flask,render_template,request,session
import datetime
from  DBConnection import Db

app = Flask(__name__)
app.secret_key="abc"


@app.route('/',methods=['get','post'])
def login():
    if request.method=="POST":
        username=request.form['textfield']
        password=request.form['textfield2']
        db = Db()
        qry=db.selectOne("select * from login where username='"+username+"' and password='"+password+"'")
        if qry is not None:
            if qry['user_type']=='admin':
                return '''<script>alert('login successfully');window.location="/admin_homepage"</script>'''
            elif qry['user_type']=='teacher':
                session['lid']=qry['login_id']
                return '''<script>alert('login successfully');window.location="/teacher_homepage"</script>'''
            else:
                return '''<script>alert('user not found');window.location="/"</script>'''
        else:
            return '''<script>alert('user not found');window.location="/"</script>'''

    else:
        return render_template('index.html')


@app.route('/admin_homepage')
def homepage():
    return  render_template('ADMIN/homepage.html')



@app.route('/view_approved_teachers')
def view_approved_teachers():
    db=Db()
    qry=db.select("SELECT * FROM login,teacher WHERE teacher.teacher_id=login.login_id AND login.user_type='teacher'")

    return render_template('ADMIN/view approved teachers.html',data=qry)

@app.route('/block_teacher/<tid>')
def block_teacher(tid):
    db=Db()
    db.update("update login set user_type='blocked' where login_id='" + tid + "' ")

    return '''<script>alert('blocked');window.location="/view_approved_teachers"</script>'''
@app.route('/unblock_teacher/<tid>')
def unblock_teacher(tid):
    db=Db()
    db.update("update login set user_type='teacher' where login_id='" + tid + "' ")

    return '''<script>alert('unblock');window.location="/view_approved_teachers"</script>'''


@app.route('/view_blocked_teachers')
def view_blocked_teachers():
    db = Db()
    qry = db.select("SELECT * FROM login,teacher WHERE teacher.teacher_id=login.login_id AND login.user_type='blocked'")

    return render_template('ADMIN/view blocked teachers.html',data=qry)



@app.route('/view_registered_teachers')
def view_registered_teachers():
    db = Db()
    qry = db.select("SELECT * FROM login,teacher WHERE teacher.teacher_id=login.login_id AND login.user_type='pending'")

    return render_template('ADMIN/view registerd teacher.html',data=qry)

@app.route('/approve_teacher/<tid>')
def approve_teacher(tid):
    db=Db()
    db.update("update login set user_type='teacher' where login_id='"+tid+"' ")
    return '''<script>alert('approved');window.location="/view_registered_teachers"</script>'''

@app.route('/reject_teacher/<tid>')
def reject_teacher(tid):
    db=Db()
    db.delete("delete from login where login_id='"+tid+"'")
    db.delete("delete from teacher where teacher_id='"+tid+"'")
    return '''<script>alert('rejected');window.location="/view_registered_teachers"</script>'''




@app.route('/view_events_approval')
def view_events_approval():
    db = Db()
    qry = db.select("SELECT * FROM event,teacher WHERE teacher.teacher_id=event.event_id ")
    return render_template('ADMIN/view events & approval.html', data=qry)
@app.route('/approve_events/<eid>')
def approve_events(eid):
    db=Db()
    db.update("update event set status='approved' where event_id='"+eid+"' ")
    return '''<script>alert('approved');window.location="/view_events_approval"</script>'''
@app.route('/reject_events/<eid>')
def reject_events(eid):
    db=Db()
    db.delete("delete from event where event_id='" + eid + "'")
    return '''<script>alert('rejected');window.location="/view_events_approval"</script>'''


@app.route('/view_feedback')
def view_feedback():
    db = Db()
    qry = db.select("SELECT feedbacks,student_name FROM feedback,student WHERE feedback.feedback_id=student.student_id")
    return render_template('ADMIN/view feedback.html',data=qry)



@app.route('/sent_notifications',methods=['get','post'])
def sent_notifications():
    if request.method=="POST":
        notifications = request.form['textarea']
        db = Db()
        qry=db.insert("insert into notification(notification,date) VALUES('"+notifications+"',curdate())")
        return '''<script>alert('added successfully');window.location="/admin_homepage"</script>'''

    else:
        return render_template('ADMIN/sent notifications.html')


@app.route('/teacher_homepage')
def teacher_homepage():
    return  render_template('TEACHER/teacher_homepage.html')

@app.route('/teacher_sign',methods=['get','post'])
def teacher_sign():
    if request.method=="POST":
        teachername=request.form['textfield']
        place= request.form['textfield2']
        post = request.form['textfield3']
        pin = request.form['textfield4']
        photo= request.files['fileField']
        date=datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        photo.save(r"C:\Users\HP\PycharmProjects\chatbot\static\teacher_photo\\"+date+'.jpg')
        path="/static/teacher_photo/"+date+'.jpg'
        gender = request.form['RadioGroup1']
        qualification = request.form['textfield7']
        phoneno = request.form['textfield8']
        email = request.form['textfield9']
        password = request.form['textfield10']
        confirm_password= request.form['textfield11']
        db = Db()
        if password==confirm_password:
            qry = db.insert("insert into login(username,password,user_type) VALUES('" + email + "','" + confirm_password + "','pending')")
            db.insert("insert into teacher VALUES('"+str(qry)+"','"+teachername+"','"+place+"','"+post+"','"+pin+"','"+str(path)+"','"+gender+"','"+qualification+"','"+phoneno+"','"+email+"')")

            return '''<script>alert('added successfully');window.location="/teacher_homepage"</script>'''
        else:
            return '''<script>alert('password mismatch');window.location="/teacher_sign"</script>'''
    else:
        return render_template('TEACHER/teacher_sign.html')


@app.route('/view_update_teacher_profile')
def view_update_teacher_profile():

        return render_template('TEACHER/view and update profile.html')


@app.route('/add_group',methods=['get','post'])
def add_group():
    if request.method=="POST":
        groups = request.form['textfield']
        db = Db()
        db.insert("insert into group(group_name) VALUES('"+groups+"')")
        return '''<script>alert('added successfully');window.location="/teacher_homepage"</script>'''

    else:
       return render_template('TEACHER/add group.html')


if __name__ == '__main__':
    app.run()
