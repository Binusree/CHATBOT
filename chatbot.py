from flask import Flask,render_template,request,session,redirect
import demjson
import datetime
from  DBConnection import Db

app = Flask(__name__)
app.secret_key="abc"
app.debug=True

@app.route('/',methods=['get','post'])
def login():
    if request.method=="POST":
        username=request.form['username']
        password=request.form['pass']
        db = Db()
        qry=db.selectOne("select * from login where username='"+username+"' and password='"+password+"'")
        if qry is not None:
            if qry['user_type']=='admin':
                session['lg']='lin'
                return '''<script>alert('login successfully');window.location="/admin_homepage"</script>'''
            elif qry['user_type']=='teacher':
                session['lg']='lin'

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
    if session['lg']=='lin':
        return  render_template('ADMIN/adminhomeindex.html')
    else:
        return redirect('/')


@app.route('/view_approved_teachers')
def view_approved_teachers():
    if session['lg']=="lin":
        db=Db()
        qry=db.select("SELECT * FROM login,teacher WHERE teacher.teacher_id=login.login_id AND login.user_type='teacher'")

        return render_template('ADMIN/approvedteacher.html',data=qry)
    else:
        return redirect('/')
@app.route('/block_teacher/<tid>')
def block_teacher(tid):
    if session['lg'] == "lin":
        db=Db()
        db.update("update login set user_type='blocked' where login_id='" + tid + "' ")
        return '''<script>alert('blocked');window.location="/view_approved_teachers"</script>'''
    else:
        return redirect('/')
@app.route('/unblock_teacher/<tid>')
def unblock_teacher(tid):
    if session['lg'] == "lin":
        db=Db()
        db.update("update login set user_type='teacher' where login_id='" + tid + "' ")

        return '''<script>alert('unblock');window.location="/view_blocked_teachers"</script>'''
    else:
        return redirect('/')

@app.route('/view_blocked_teachers')
def view_blocked_teachers():
    if session['lg'] == "lin":
        db = Db()
        qry = db.select("SELECT * FROM login,teacher WHERE teacher.teacher_id=login.login_id AND login.user_type='blocked'")

        return render_template('ADMIN/blockedteacher.html',data=qry)
    else:
        return redirect('/')


@app.route('/view_registered_teachers')
def view_registered_teachers():
    if session['lg'] == "lin":
        db = Db()
        qry = db.select("SELECT * FROM login,teacher WHERE teacher.teacher_id=login.login_id AND login.user_type='pending'")

        return render_template('ADMIN/registeredteacher.html',data=qry)
    else:
        return redirect('/')

@app.route('/approve_teacher/<tid>')
def approve_teacher(tid):
    if session['lg'] == "lin":
        db=Db()
        db.update("update login set user_type='teacher' where login_id='"+tid+"' ")
        return '''<script>alert('approved');window.location="/view_registered_teachers"</script>'''
    else:
        return redirect('/')

@app.route('/reject_teacher/<tid>')
def reject_teacher(tid):
    if session['lg'] == "lin":
        db=Db()
        db.delete("delete from login where login_id='"+tid+"'")
        db.delete("delete from teacher where teacher_id='"+tid+"'")
        return '''<script>alert('rejected');window.location="/view_registered_teachers"</script>'''

    else:
        return redirect('/')


@app.route('/view_events_approval')
def view_events_approval():
    if session['lg'] == "lin":
        db = Db()
        qry = db.select("SELECT * FROM event,teacher WHERE teacher.teacher_id=event.event_id ")
        return render_template('ADMIN/view events & approval.html', data=qry)
    else:
        return redirect('/')

@app.route('/approve_events/<eid>')
def approve_events(eid):
    if session['lg'] == "lin":
        db=Db()
        db.update("update event set status='approved' where event_id='"+eid+"' ")
        return '''<script>alert('approved');window.location="/view_events_approval"</script>'''
    else:
        return redirect('/')
@app.route('/reject_events/<eid>')
def reject_events(eid):
    if session['lg'] == "lin":
        db=Db()
        db.delete("delete from event where event_id='" + eid + "'")
        return '''<script>alert('rejected');window.location="/view_events_approval"</script>'''
    else:
        return redirect('/')

@app.route('/view_feedback')
def view_feedback():
    if session['lg'] == "lin":
        db = Db()
        qry = db.select("SELECT feedbacks,student_name FROM feedback,student WHERE feedback.feedback_id=student.student_id")
        return render_template('ADMIN/view feedback.html',data=qry)

    else:
        return redirect('/')

@app.route('/sent_notifications',methods=['get','post'])
def sent_notifications():
    if session['lg'] == "lin":
        if request.method=="POST":
            notifications = request.form['textarea']
            db = Db()
            qry=db.selectOne("select * from notification where notification='"+notifications+"' ")
            if qry is not None:
                return '''<script>alert('Already added ');window.location="/sent_notifications"</script>'''
            else:
                qry=db.insert("insert into notification(notification,date) VALUES('"+notifications+"',curdate())")
                return '''<script>alert('added successfully');window.location="/admin_homepage"</script>'''

        else:
            return render_template('ADMIN/sent notifications.html')
    else:
        return redirect('/')


# -----------------------------------------------------------------------------------------------------------------------------------------------------
#                                                       TEACHER MODULE
# -----------------------------------------------------------------------------------------------------------------------------------------------------

@app.route('/teacher_homepage')
def teacher_homepage():
    if session['lg'] == 'lin':
        return  render_template('TEACHER/teacher_homeindex.html')
    else:
        return redirect('/')



@app.route('/teacher_sign',methods=['get','post'])
def teacher_sign():
    if request.method=="POST":
        teachername=request.form['name']
        place= request.form['place']
        post = request.form['post']
        pin = request.form['pin']
        photo= request.files['fileField']
        date=datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        photo.save(r"C:\Users\HP\PycharmProjects\chatbot\chatbot\static\teacher_photo\\"+date+'.jpg')
        #photo.save(r"C:\Users\IDZ\Downloads\chatbot\static\teacher_photo\\"+date+'.jpg')
        path="/static/teacher_photo/"+date+'.jpg'
        gender = request.form['RadioGroup1']
        qualification = request.form['qualification']
        phoneno = request.form['no']
        email = request.form['email']
        password = request.form['pass']
        confirm_password= request.form['conpass']
        db = Db()
        qry1=db.selectOne("select * from login WHERE username='"+email+"'")
        if qry1 is not None:
            return '''<script>alert('Already mail exist');window.location="/teacher_sign"</script>'''
        else:
            if password==confirm_password:
                    qry = db.insert("insert into login(username,password,user_type) VALUES('" + email + "','" + confirm_password + "','pending')")
                    db.insert("insert into teacher VALUES('"+str(qry)+"','"+teachername+"','"+place+"','"+post+"','"+pin+"','"+str(path)+"','"+gender+"','"+qualification+"','"+phoneno+"','"+email+"')")

                    return '''<script>alert('added successfully');window.location="/"</script>'''
            else:
                    return '''<script>alert('password mismatch');window.location="/teacher_sign"</script>'''

    else:
        return render_template('TEACHER/teacherregisteration.html')


@app.route('/view_update_teacher_profile',methods=['get','post'])
def view_update_teacher_profile():
    if session['lg'] == "lin":
        if request.method == "POST":
            teachername = request.form['textfield']
            place = request.form['textfield2']
            post = request.form['textfield3']
            pin = request.form['textfield4']
            photo = request.files['fileField']
            date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
            photo.save(r"C:\Users\HP\PycharmProjects\chatbot\static\teacher_photo\\" + date + '.jpg')
            path = "/static/teacher_photo/" + date + '.jpg'
            gender = request.form['RadioGroup1']
            qualification = request.form['textfield7']
            phoneno = request.form['textfield8']
            email = request.form['textfield9']
            db=Db()
            if request.files!=None:
                if photo.filename!="":
                    db.update("update teacher set teacher_name='"+teachername+"',place='"+place+"',post='"+post+"',pin='"+pin+"',photo='"+str(path)+"',gender='"+gender+"',qualification='"+qualification+"',phoneno='"+phoneno+"',email='"+email+"' where teacher_id='"+str(session['lid'])+"'")
                    return '''<script>alert('update successfully');window.location="/view_update_teacher_profile "</script>'''

                else:
                    db.update("update teacher set teacher_name='"+teachername+"',place='"+place+"',post='"+post+"',pin='"+pin+"',gender='"+gender+"',qualification='"+qualification+"',phoneno='"+phoneno+"',email='"+email+"' where teacher_id='"+str(session['lid'])+"'")
                    return '''<script>alert('update successfully');window.location="/view_update_teacher_profile "</script>'''

            else:
                db.update("update teacher set teacher_name='" + teachername + "',place='" + place + "',post='" + post + "',pin='" + pin + "',gender='" + gender + "',qualification='" + qualification + "',phoneno='" + phoneno + "',email='" + email + "' where teacher_id='" + str(session['lid']) + "'")
                return '''<script>alert('update successfully');window.location="/view_update_teacher_profile "</script>'''
        else:
            db=Db()
            qry = db.selectOne("select * from teacher where teacher_id='"+str(session['lid'])+"'")

            return render_template('TEACHER/view and update profile.html',data=qry)
    else:
        return redirect('/')

@app.route('/add_group',methods=['get','post'])
def add_group():
    if session['lg'] == "lin":
        if request.method=="POST":
            groups = request.form['textfield']
            db = Db()
            qry1=db.selectOne("select * from groups WHERE group_name='"+groups+"' ")
            if qry1 is not None:
                return '''<script>alert('Already added ');window.location="/add_group"</script>'''
            else:
                qry = db.insert(" insert into groups(teacher_id,group_name) VALUES('"+str(session['lid'])+"','" + groups + "')")
                return '''<script>alert('added successfully');window.location="/teacher_homepage"</script>'''

        else:
            return render_template('TEACHER/add group.html')
    else:
        return redirect('/')

@app.route('/add_group_members',methods=['get','post'])
def add_group_members():
    if session['lg'] == "lin":
        if request.method=="POST":
            groupname = request.form['select']
            studentname = request.form['select2']
            db = Db()
            qry1=db.selectOne("select * from group_members WHERE group_id='"+groupname+"' and student_id='"+studentname+"' ")
            if qry1 is not None:
                return '''<script>alert('Already added ');window.location="/add_group_members"</script>'''
            else:
                qry = db.insert(" insert into group_members(group_id,student_id) VALUES('"+groupname+"','"+studentname+"')")
                return '''<script>alert('added successfully');window.location="/teacher_homepage"</script>'''
        else:
            db=Db()
            qry=db.select("select * from groups where teacher_id='"+str(session['lid'])+"'")
            qry1=db.select("select * from student")
            return render_template('TEACHER/add group member.html',data=qry,data1=qry1)
    else:
        return redirect('/')



@app.route('/create_events',methods=['get','post'])
def create_events():
    if session['lg'] == "lin":
        if request.method=="POST":
            events = request.form['textfield']
            description=request.form['textarea']
            db = Db()
            qry = db.insert(" insert into event(teacher_id,events,description,date,status) VALUES('"+str(session['lid'])+"','" + events + "','"+description+"',curdate(),'pending')")
            return '''<script>alert('added successfully');window.location="/teacher_homepage"</script>'''

        else:
            return render_template('TEACHER/create events.html')

    else:
        return redirect('/')

@app.route('/view_event_status')
def view_event_status():
    if session['lg'] == "lin":
        db = Db()
        qry = db.select("SELECT * FROM event  WHERE teacher_id='"+str(session['lid'])+"'")
        return render_template('TEACHER/view event status.html',data=qry)
    else:
        return redirect('/')

@app.route('/view_notifications')
def view_notifications():
    if session['lg'] == "lin":
        db = Db()
        qry = db.select("SELECT * FROM notification")
        return render_template('TEACHER/view notifications.html',data=qry)
    else:
        return redirect('/')


@app.route('/share_idea',methods=['get','post'])
def share_idea():
    if session['lg'] == "lin":
        if request.method=="POST":
            Idea = request.form['textarea']
            db = Db()
            qry1=db.selectOne("select * from ideas WHERE ideas='"+Idea+"' ")
            if qry1 is not None:
                return '''<script>alert('Already added ');window.location="/share_idea"</script>'''
            else:
                qry = db.insert(" insert into ideas(teacher_id,ideas,date) VALUES('"+str(session['lid'])+"','" + Idea + "',curdate())")
                return '''<script>alert('added successfully');window.location="/teacher_homepage"</script>'''
        else:
            return render_template('TEACHER/share ideas.html')
    else:
        return redirect('/')

@app.route('/share_articles',methods=['get','post'])
def share_articles():
    if session['lg'] == "lin":
        if request.method=="POST":
            articlename = request.form['textfield']
            article = request.files['fileField']
            date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
            article.save(r"C:\Users\HP\PycharmProjects\chatbot\static\articles_file\\" + date + '.jpg')
            path = "/static/articles_file/" + date + '.jpg'
            db = Db()
            qry = db.insert(" insert into articles(teacher_id,article_name,articles,date) VALUES('"+str(session['lid'])+"','" + articlename + "','"+str(path)+"',curdate())")
            return '''<script>alert('added successfully');window.location="/teacher_homepage"</script>'''
        else:
            return render_template('TEACHER/share articles.html')
    else:
        return redirect('/')

@app.route('/view_rating')
def view_rating():
    if session['lg'] == "lin":
        db = Db()
        qry = db.select("SELECT * FROM rating,student WHERE rating.student_id=student.student_id")
        return render_template('TEACHER/view rating.html',data=qry)
    else:
        return redirect('/')

@app.route('/view_group')
def view_group():
    if session['lg'] == "lin":
        db = Db()
        qry = db.select("SELECT * FROM groups WHERE teacher_id='"+str(session['lid'])+"'")
        qry1=db.select("select * from group_members ")
        return render_template('TEACHER/view group.html',data=qry,data1=qry1)
    else:
        return redirect('/')

@app.route('/delete_group/<gid>')
def delete_group(gid):
    if session['lg'] == "lin":
        db=Db()
        db.delete("delete from groups where group_id='"+gid+"'")
        db.delete("delete from group_members where group_id='"+gid+"'")
        return '''<script>alert('deleted');window.location="/view_group"</script>'''
    else:
        return redirect('/')

@app.route('/view_group_members/<gid>')
def view_group_members(gid):
    if session['lg'] == "lin":
        db = Db()
        qry = db.select("SELECT * FROM group_members,student WHERE group_members.student_id=student.student_id and group_members.group_id='"+gid+"'")
        return render_template('TEACHER/view group members.html',data=qry)
    else:
        return redirect('/')

@app.route('/delete_group_member/<gmid>')
def delete_group_member(gmid):
    if session['lg'] == "lin":
        db=Db()
        db.delete("delete from group_members where group_member_id='"+gmid+"'")
        return '''<script>alert('deleted');window.location="/view_group_member"</script>'''
    else:
        return redirect('/')

# @app.route('/adminhomepage')
# def adminhomepage():
#
#     return render_template('ADMIN/adminhome.html')

@app.route('/logout')
def logout():
    session.clear()
    session['lg']=""
    return redirect('/')

# ------------------------------------------------------------------------------------------------------------------------------------------------
#                                                    STUDENT MODULE ---ANDROID
# -----------------------------------------------------------------------------------------------------------------------------------------------------

@app.route('/and_login',methods=['post'])
def and_login():
    username=request.form['u']
    password=request.form['p']
    db=Db()
    qry = db.selectOne("select * from login where username='" + username + "' and password='" + password + "'")
    res={}
    if qry :
        res['status']="ok"
        res['type']=qry['user_type']
        res['lid']=qry['login_id']
        return demjson.encode(res)

    else:
        res['status']="none"
        return demjson.encode(res)


@app.route('/and_viewprofile',methods=['post'])
def and_viewprofile():
    id=request.form['id']
    db=Db()
    qry=db.selectOne("select * from student where student_id='"+id+"'")
    res = {}
    if qry:
        res['status'] = "ok"
        res['data']=qry
        return demjson.encode(res)
    else:
        res['status']="none"
        return demjson.encode(res)


@app.route('/and_approvedevents',methods=['post'])
def and_approvedevents():
    db=Db()
    qry=db.select("select * from event,teacher where event.teacher_id=teacher.teacher_id and event.status='approved'")
    res = {}
    if qry:
        res['status'] = "ok"
        res['data']=qry
        return demjson.encode(res)
    else:
        res['status']="none"
        return demjson.encode(res)


@app.route('/and_viewarticles',methods=['post'])
def and_viewarticles():
    db=Db()
    qry=db.select("select * from articles,teacher where teacher.teacher_id=articles.teacher_id ")
    res = {}
    if qry:
        res['status'] = "ok"
        res['data']=qry
        return demjson.encode(res)
    else:
        res['status']="none"
        return demjson.encode(res)



@app.route('/and_viewideas',methods=['post'])
def and_viewideas():
    db=Db()
    qry=db.select("select * from ideas,teacher where teacher.teacher_id=ideas.teacher_id ")
    res = {}
    if qry:
        res['status'] = "ok"
        res['data']=qry
        return demjson.encode(res)
    else:
        res['status']="none"
        return demjson.encode(res)

@app.route('/and_viewnotifications',methods=['post'])
def and_viewnotifications():
    db=Db()
    qry=db.select("select * from notification")
    res = {}
    if qry:
        res['status'] = "ok"
        res['data']=qry
        return demjson.encode(res)
    else:
        res['status']="none"
        return demjson.encode(res)


@app.route('/and_viewgroup',methods=['post'])
def and_viewgroup():
    id = request.form['id']
    db = Db()
    qry = db.select("SELECT * FROM groups,teacher,group_members WHERE groups.teacher_id=teacher.teacher_id AND groups.group_id=group_members.group_id AND group_members.student_id='"+id+"'")
    res = {}
    if qry:
        res['status'] = "ok"
        res['data'] = qry
        return demjson.encode(res)
    else:
        res['status'] = "none"
        return demjson.encode(res)

@app.route('/and_view_groupmembers',methods=['post'])
def and_viewgroupmembers():
    gid = request.form['gid']
    db = Db()
    qry = db.select("select * from group_members,student where group_members.student_id=student.student_id and group_id='"+gid+"'")
    res = {}
    if qry:
        res['status'] = "ok"
        res['data'] = qry
        return demjson.encode(res)
    else:
        res['status'] = "none"
        return demjson.encode(res)

@app.route('/and_sendfeedback',methods=['post'])
def and_sendfeedback():
    id = request.form['id']
    f = request.form['fed']
    db = Db()
    qry = db.insert("insert into feedback(student_id,feedbacks,date) VALUES ('"+id+"','"+f+"',curdate())")
    res = {}
    if qry:
        res['status'] = "ok"
        return demjson.encode(res)
    else:
        res['status'] = "none"
        return demjson.encode(res)



@app.route('/and_signup',methods=['post'])
def and_signup():
    db=Db()
    name = request.form['na']
    place = request.form['pl']
    post = request.form['post']
    pin = request.form['pin']
    photo = request.files['pic']
    date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
    # photo.save(r"C:\Users\HP\PycharmProjects\chatbot\static\teacher_photo\\"+date+'.jpg')
    photo.save(r"C:\Users\HP\PycharmProjects\chatbot\chatbot\static\student_photo\\" + date + '.jpg')
    path = "/static/student_photo/" + date + '.jpg'
    gender = request.form['g']
    course = request.form['c']
    phoneno = request.form['ph']
    email = request.form['e']
    password = request.form['p']

    qry = db.insert("insert into login(username,password,user_type) VALUES('" + email + "','" + password + "','student')")
    qry1= db.insert("insert into student VALUES('" + str(qry) + "','" + name + "','" + place + "','" + post + "','" + pin + "','" + str(path) + "','" + gender + "','" + course + "','" + phoneno + "','" + email + "')")

    res = {}
    if qry:
        res['status'] = "ok"
        return demjson.encode(res)
    else:
        res['status'] = "none"
        return demjson.encode(res)



@app.route('/and_rate_articles',methods=['post'])
def and_rate_articles():
    id = request.form['id']
    r = request.form['rate']
    a = request.form['aid']
    db = Db()
    qry = db.insert("insert into rating_article(student_id,ratings,date,article_id) VALUES ('"+id+"','"+r+"',curdate(),'"+a+"')")
    res = {}
    if qry:
        res['status'] = "ok"
        return demjson.encode(res)
    else:
        res['status'] = "none"
        return demjson.encode(res)

@app.route('/and_rate_ideas',methods=['post'])
def and_rate_ideas():
    id = request.form['id']
    r = request.form['rate']
    a = request.form['iid']
    db = Db()
    qry = db.insert("insert into rating_ideas(student_id,ratings,date,idea_id) VALUES ('"+id+"','"+r+"',curdate(),'"+a+"')")
    res = {}
    if qry:
        res['status'] = "ok"
        return demjson.encode(res)
    else:
        res['status'] = "none"
        return demjson.encode(res)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
