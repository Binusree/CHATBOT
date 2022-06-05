from flask import Flask,render_template,request,session,redirect
import demjson
import datetime
from  DBConnection import Db

app = Flask(__name__)
app.secret_key="abc"
app.debug=True

@app.route('/',methods=['get','post'])
def home():
    return  render_template('main_home/home.html')


@app.route('/log',methods=['get','post'])
def login():
    if request.method=="POST":
        username=request.form['name']
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
                return '''<script>alert('user not found');window.location="/log"</script>'''
        else:
            return '''<script>alert('user not found');window.location="/log"</script>'''

    else:
        return render_template('login.html')


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
        qry = db.select("SELECT * FROM `teacher`,`event` WHERE `teacher`.teacher_id=`event`.`teacher_id` ")
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
        return  render_template('TEACHER/teach_home.html')
    else:
        return redirect('/')



@app.route('/teacher_sign',methods=['get','post'])
def teacher_sign():
    if request.method=="POST":
        teachername=request.form['name']
        place= request.form['place']
        post = request.form['post']
        pin = request.form['pin']
        photo= request.files['photo']
        date=datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        photo.save(r"C:\Users\HP\PycharmProjects\chatbot\static\teacher_photo\\"+date+'.jpg')
        path="/static/teacher_photo/"+date+'.jpg'
        gender = request.form['RadioGroup1']
        qualification = request.form['qualification']
        phoneno = request.form['no']
        email = request.form['email']
        password = request.form['pass']
        confirm_password= request.form['re_pass']
        db = Db()
        qry1=db.selectOne("select * from login WHERE username='"+email+"'")
        if qry1 is not None:
            return '''<script>alert('Already mail exist');window.location="/teacher_sign"</script>'''
        else:
            if password==confirm_password:
                    qry = db.insert("insert into login(username,password,user_type) VALUES('" + email + "','" + confirm_password + "','pending')")
                    db.insert("insert into teacher VALUES('"+str(qry)+"','"+teachername+"','"+place+"','"+post+"','"+pin+"','"+str(path)+"','"+gender+"','"+qualification+"','"+phoneno+"','"+email+"')")

                    return '''<script>alert('added successfully');window.location="/log"</script>'''
            else:
                    return '''<script>alert('password mismatch');window.location="/teacher_sign"</script>'''

    else:
        return render_template('TEACHER/teacher_reg.html')


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

# @app.route('/add_group_members',methods=['get','post'])
# def add_group_members():
#     if session['lg'] == "lin":
#         if request.method=="POST":
#             groupname = request.form['select']
#             studentname = request.form['select2']
#             db = Db()
#             qry1=db.selectOne("select * from group_members WHERE group_id='"+groupname+"' and student_id='"+studentname+"' ")
#             if qry1 is not None:
#                 return '''<script>alert('Already added ');window.location="/add_group_members"</script>'''
#             else:
#                 qry = db.insert(" insert into group_members(group_id,student_id) VALUES('"+groupname+"','"+studentname+"')")
#                 return '''<script>alert('added successfully');window.location="/teacher_homepage"</script>'''
#         else:
#             db=Db()
#             qry=db.select("select * from groups where teacher_id='"+str(session['lid'])+"'")
#             qry1=db.select("select * from student")
#             return render_template('TEACHER/add group member.html',data=qry,data1=qry1)
#     else:
#         return redirect('/')






@app.route('/add_group_membersssss/<gid>')
def add_group_membersssss(gid):
    if session['lg'] == "lin":

            db=Db()
            qry1=db.select("select * from student")
            return render_template('TEACHER/adgrm.html',data=qry1,g=gid)
    else:
        return redirect('/')



@app.route('/add_gsmembersssss/<gid>/<sid>')
def add_gsmembersssss(gid,sid):
    if session['lg'] == "lin":
        db=Db()

        qry1 = db.selectOne(  "select * from group_members WHERE group_id='" + gid + "' and student_id='" + sid + "' ")
        if qry1 is not None:
            return '''<script>alert('Already added ');window.location="/view_group"</script>'''
        else:
            qry = db.insert(" insert into group_members(group_id,student_id) VALUES('"+gid+"','"+sid+"')")
            return '''<script>alert('added successfully');window.location="/teacher_homepage"</script>'''

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

@app.route('/view_feedbacks')
def view_feedbacks():
    if session['lg'] == "lin":
        db = Db()
        qry = db.select("SELECT feedbacks,student_name FROM feedback,student WHERE feedback.feedback_id=student.student_id")
        return render_template('TEACHER/view feedback.html',data=qry)
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
        return render_template('TEACHER/teacher_sign.html',data=qry)
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

@app.route('/t_s_chat')
def t_s_chat():
    if session['lg'] == "lin":
        return render_template("TEACHER/teacher_student_chat.html")
    else:
        return redirect('/')

@app.route('/company_staff_chat', methods=['post'])
def company_staff_chat():
    if session['lg'] == "lin":
        db = Db()
        a = session['lid']
        q1 = "select * from student"
        res = db.select(q1)
        v = {}
        if len(res) > 0:
            v["status"] = "ok"
            v['data'] = res
        else:
            v["status"] = "error"

        rw = demjson.encode(v)
        print(rw)
        return rw
    else:
        return redirect('/')

@app.route('/chatsnd', methods=['post'])
def chatsnd():
    if session['lg'] == "lin":
        db = Db()
        c = session['lid']
        b = request.form['n']
        print(b)
        m = request.form['m']

        q2 = "insert into chat values(null,'" + str(c) + "','" + str(b) + "','" + m + "',now())"
        res = db.insert(q2)
        v = {}
        if int(res) > 0:
            v["status"] = "ok"

        else:
            v["status"] = "error"

        r = demjson.encode(v)

        return r
    else:
        return login()

@app.route('/chatrply', methods=['post'])
def chatrply():
    if session['lg'] == "lin":
        print("...........................")
        c = session['lid']
        b = request.form['n']
        print("<<<<<<<<<<<<<<<<<<<<<<<<")
        print(b)
        t = Db()
        qry2 = "select * from chat ORDER BY chat_id ASC ";
        res = t.select(qry2)
        print(res)

        v = {}
        if len(res) > 0:
            v["status"] = "ok"
            v['data'] = res
            v['id'] = c
        else:
            v["status"] = "error"

        rw = demjson.encode(v)
        return rw
    else:
        return login()


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
    s=qry['login_id']
    q2=db.selectOne("select * from student WHERE student_id='"+str(s)+"'")

    res={}
    if qry :
        res['status']="ok"
        res['type']=qry['user_type']
        res['lid']=qry['login_id']
        res['email']=qry['username']
        res['name']=q2['student_name']
        res['photo']=q2['photo']
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
    name = request.form['n']
    place = request.form['pla']
    post = request.form['post']
    pin = request.form['pin']
    photo = request.files['pic']
    date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
    # photo.save(r"D:\chatbot\static\student_photo\\" + date + '.jpg')
    photo.save(r"C:\Users\HP\PycharmProjects\chatbot\static\student_photo\\" + date + '.jpg')
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







@app.route('/add_chat',methods=['post'])
def add_chat():
    lid = request.form['id']
    toid = request.form['toid']
    message = request.form['message']
    db=Db()

    q2="insert into chat(from_id,to_id,message,date)values('"+lid+"','"+toid+"','"+message+"',curdate())"
    res = db.insert(q2)
    res1 = {}
    res1['status'] = "Inserted"
    return demjson.encode(res1)

@app.route('/view_chat',methods=['post'])
def view_chat():
    lid = request.form['id']
    toid = request.form['toid']
    lastid = request.form['lastid']
    db=Db()
    print(lid,toid,lastid)
    q2="select chat.* from chat where chat_id>'"+lastid+"' and ((from_id='"+lid+"' and to_id='"+toid+"') or (from_id='"+toid+"' and to_id='"+lid+"'))"
    res = db.select(q2)
    print(res)
    res1 = {}
    res1['status'] = "ok"
    res1['data'] = res
    return demjson.encode(res1)
@app.route('/view_staff',methods=['post'])
def view_chatcouncillor():
    lid = request.form['lid']
    db=Db()

    print(lid)
    # qry = db.selectOne("select * from student,course where student.stud_course_id=course.course_id and student.stud_id='" + str(lid) + "'")
    # print(qry)
    # cid = qry['stud_course_id']
    # y = qry['batch']
    q = db.select("select * from teacher ")
    # print(q, cid)
    res1 = {}
    res1['status'] = "ok"
    res1['data'] = q
    return demjson.encode(res1)

# =====================================================================================================================================
#                                             MAIN SECTION---CHAT BOAT
# ====================================================================================================================================


# @app.route('/chatbot_add_chat',methods=['post'])
# def chatbot_add_chat():
#     lid = request.form['id']
#     # toid = request.form['toid']
#     message = request.form['message']
#     db=Db()
#
#     q2="insert into chatbotchat(from_id,to_id,botmsg,date)values('"+lid+"',1,'"+message+"',curdate())"
#     res = db.insert(q2)
#     q3=db.select("select * from chatboat")
#     for i in q3:
#         qtns=i['questions']
#         print(qtns)
#         import spacy
#         nlp = spacy.load("en_core_web_lg")
#         doc1 = nlp(qtns)
#         doc2 = nlp(message)
#         print(doc1, doc2)
#         ans = (doc1.similarity(doc2))
#         print(ans)
#
#         db.insert("insert into chatbotchat(from_id,to_id,botmsg,date)values(1,'"+str(lid)+"','"+str(ans)+"',curdate())")
#
#         res1 = {}
#         res1['status'] = "Inserted"
#         return demjson.encode(res1)


@app.route('/chatbot_add_chat',methods=['post'])
def chatbot_add_chat():
    lid = request.form['id']
    # toid = request.form['toid']
    message = request.form['message']
    db=Db()

    q2="insert into chatbotchat(from_id,to_id,botmsg,date)values('"+lid+"',1,'"+message+"',curdate())"
    res = db.insert(q2)
    q3=db.select("select * from chatboat")
    score=[]
    ans=[]
    for i in q3:
        qtns=i['questions']
        answer=i['answers']
        import spacy
        # nlp = spacy.load("en_core_web_lg")

        sim=cht(message, qtns)
        print("LL ", sim, qtns)
        score.append(sim)
        ans.append(answer)



    res1 = {}
    res1['status'] = "Inserted"
    temp=round(score[0],2)
    score[0]=round(score[0],2)
    for j in range(1, len(score)):
        if round(score[j]>temp):
            temp=round(score[j], 2)
            score[j]=round(score[j], 2)
    print("High   ",temp)
    if temp<0.65:
        answ="Sorry.. i didnt get you"
    else:
        idx=score.index(temp)
        answ=str(ans[idx])
    db.insert(
        "insert into chatbotchat(from_id,to_id,botmsg,date)values(1,'" + str(lid) + "','" + answ + "',curdate())")

    return demjson.encode(res1)

def cht(a,b):

    import spacy
    nlp = spacy.load("en_core_web_lg")
    doc1 = nlp(a)
    doc2 = nlp(b)
    print(doc1,doc2)
    ans=(doc1.similarity(doc2))
    print(ans)
    return ans



@app.route('/chatbot_view_chat',methods=['post'])
def chatbot_view_chat():
    lid = request.form['id']
    # toid = request.form['toid']
    lastid = request.form['lastid']
    db=Db()
    # print(lid,lastid)
    q2="select chatbotchat.* from chatbotchat where chatbot_chat_id>'"+lastid+"' and ((from_id='"+lid+"' and to_id=1) or (from_id=1 and to_id='"+lid+"'))"
    res = db.select(q2)
    # print(res)
    res1 = {}
    res1['status'] = "ok"
    res1['data'] = res
    return demjson.encode(res1)

@app.route('/chatbot_delete_chat',methods=['post'])
def chatbot_delete_chat():
    lid = request.form['id']
    db=Db()
    db.delete("delete from chatbotchat WHERE from_id='"+lid+"'")
    db.delete("delete from chatbotchat WHERE to_id='"+lid+"'")
    res1 = {}
    res1['status'] = "ok"
    return demjson.encode(res1)





if __name__ == '__main__':
    app.run(host="0.0.0.0")
