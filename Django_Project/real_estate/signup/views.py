from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
s=''
em=''
pwd=''
phone=''
rid=''

# Create your views here.
def signaction(request):
    global fn,ln,s,em,pwd,rid,phone
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="password",database='real_estate')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="reg_id":
                rid=value
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="sex":
                s=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
            if key == "phone":
                phone = value
        ca="select * from  users where USER_ID= '{}'" .format(rid)
        cursor.execute(ca)
        tel = tuple(cursor.fetchall())
        if(tel==()):
            
            c="insert into users Values('{}','{}','{}','{}','{}','{}','{}')".format(rid,fn,ln,s,em,pwd,phone)
            cursor.execute(c)
            m.commit()
            return render(request,'login_page.html')
        else:
            return render(request, 'error.html')
        
    return render(request,'signup_page.html')