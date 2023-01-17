from django.shortcuts import render
import mysql.connector as sql
from datetime import date
today = date.today()
sdate=''
buyer_id=''
property_id = ''
na=''
p=''
a=''
uid=''
id=''
e=''
m=''
kw=''
em=''
pwd=''
wd=''
phone=''
email=''
prop_id=''
prop_name=''
size=''
price=''
location = ''
type = ''
owner_id =''
rs=''
loc=''
# Create your views here.

def home(request):
    return render(request, "home.html")
def about(request):
    return render(request, "about.html")

def alogin(request):
    global uid,pwd
    
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="password",database='real_estate')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="uid":
                id=value
            if key=="password":
                wd=value
        
      
        if id!='admin' and wd!='admin':
            return render(request,"home.html")
        else:
            return render(request, "dashboard.html")
        
def adminp(request):
    global a
    if request.method=="POST":
        d=request.POST
        for key,value in d.items():
            if key=="ad":
                a=value
            if key=="uid":
                id=value
            if key=="password":
                wd=value
      
        if a=='admin':
            return render(request,"adminlpage.html")
        elif id!='admin' and wd!='admin':
            return render(request,"home.html")
        else:
            return render(request, "home.html")

def loginaction(request):
    global uid,pwd

    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="password",database='real_estate')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="uid":
                uid=value
            if key=="password":
                pwd=value
        
        c="select * from  users where USER_ID= '{}' and password = '{}'" .format(uid,pwd)
        # c = "insert into val values('{}','{}')".format(uid , pwd)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
      
        if t==():
            return render(request,"signup_page.html")
        else:
            return render(request, "home.html")
        
        
        
        

        
    return render(request,'login_page.html')

def contactus(request):
    global na,p,e,m,uid
    sdate = today.strftime('%Y-%m-%d')
    if request.method=="POST":
        lk=sql.connect(host="localhost",user="root",passwd="password",database='real_estate')
        cursor=lk.cursor()
        e=request.POST
        for key,value in e.items():
            if key=="name":
                na=value
            if key=="uid":
                uid=value
            if key=="phone":
                p=value
            if key=="email":
                e=value
            if key=="message":
                m=value
        f="insert into ENQUIRY Values('{}','{}','{}','{}','{}','{}')".format(uid,na,p,e,m,sdate)
        cursor.execute(f)
        lk.commit()
        return render(request,'contact.html')
    return render(request,'contact.html')

def allprops(request): 
    # if request.method=="POST":
    lk=sql.connect(host="localhost",user="root",passwd="password",database='real_estate')
    cursor=lk.cursor()
    fa= "SELECT PID , PROPERTY_DESCRIPTION.PNAME , TYPE , SIZE,  LOCATION , S_PRICE ,  R_S FROM PROPERTY_DESCRIPTION JOIN PROPERTY_STATUS USING (PID) WHERE PROPERTY_STATUS.BOUGHT = 'NO'"
    cursor.execute(fa)
    t = tuple(cursor.fetchall())
    thead=["PROPERTY IMAGE ","PID","PNAME","TYPE","SIZE","LOCATION","S_PRICE","R_S"] 
    return render(request, "buy.html",{'users': t, "thead": thead})

def showif(request):
    # if request.method=="POST":
    lk=sql.connect(host="localhost",user="root",passwd="password",database='real_estate')
    cursor=lk.cursor()
    fa= "SELECT PID , PROPERTY_DESCRIPTION.PNAME , TYPE , SIZE,  LOCATION , S_PRICE ,  R_S FROM PROPERTY_DESCRIPTION  JOIN PROPERTY_STATUS USING (PID) WHERE PROPERTY_STATUS.BOUGHT = 'NO'  AND TYPE = 'independent floor'"
    cursor.execute(fa)
    t = tuple(cursor.fetchall())
    thead=["PROPERTY IMAGE ","PID","PNAME","TYPE","SIZE","LOCATION","S_PRICE","R_S"] 
    return render(request, "buy.html",{'users': t, "thead": thead})

def showvilla(request):
    lk=sql.connect(host="localhost",user="root",passwd="password",database='real_estate')
    cursor=lk.cursor()
    fa= "SELECT PID , PROPERTY_DESCRIPTION.PNAME , TYPE , SIZE,  LOCATION , S_PRICE ,  R_S FROM PROPERTY_DESCRIPTION  JOIN PROPERTY_STATUS USING (PID) WHERE PROPERTY_STATUS.BOUGHT = 'NO'  AND TYPE ='villa'"
    cursor.execute(fa)
    t = tuple(cursor.fetchall())
    thead=["PROPERTY IMAGE ","PID","PNAME","TYPE","SIZE","LOCATION","S_PRICE","R_S"]
    return render(request, "buy.html",{'users': t, "thead": thead})

def showbf(request):
    # if request.method=="POST":
    lk=sql.connect(host="localhost",user="root",passwd="password",database='real_estate')
    cursor=lk.cursor()
    fa= "SELECT PID , PROPERTY_DESCRIPTION.PNAME , TYPE , SIZE,  LOCATION , S_PRICE ,  R_S FROM PROPERTY_DESCRIPTION  JOIN PROPERTY_STATUS USING (PID) WHERE PROPERTY_STATUS.BOUGHT = 'NO'  AND TYPE ='builder floor'"
    cursor.execute(fa)
    t = tuple(cursor.fetchall())
    thead=["PROPERTY IMAGE ","PID","PNAME","TYPE","SIZE","LOCATION","S_PRICE","R_S"] 
    return render(request, "buy.html",{'users': t, "thead": thead})

def showappartment(request):
    # if request.method=="POST":
    lk=sql.connect(host="localhost",user="root",passwd="password",database='real_estate')
    cursor=lk.cursor()
    fa= "SELECT PID , PROPERTY_DESCRIPTION.PNAME , TYPE , SIZE,  LOCATION , S_PRICE ,  R_S FROM PROPERTY_DESCRIPTION  JOIN PROPERTY_STATUS USING (PID) WHERE PROPERTY_STATUS.BOUGHT = 'NO'  AND TYPE ='APPARTMENT'"
    cursor.execute(fa)
    t = tuple(cursor.fetchall())
    thead=["PROPERTY IMAGE ","PID","PNAME","TYPE","SIZE","LOCATION","S_PRICE","R_S"]
    return render(request, "buy.html",{'users': t, "thead": thead})

def sort(request):
    global loc
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="password",database='real_estate')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="location":
                loc=value

    fa ="SELECT PID , PROPERTY_DESCRIPTION.PNAME , TYPE , SIZE,  LOCATION , S_PRICE ,  R_S FROM PROPERTY_DESCRIPTION  JOIN PROPERTY_STATUS USING (PID) WHERE PROPERTY_STATUS.BOUGHT = 'NO'  AND   LOCATION ='{}'".format(loc)
    cursor.execute(fa)
    t = tuple(cursor.fetchall())
    thead=["PROPERTY IMAGE ","PID","PNAME","TYPE","SIZE","LOCATION","S_PRICE","R_S"]
    return render(request, "buy.html",{'users': t, "thead": thead})

def buyprops(request):
    global property_id , buyer_id ,sdate
    sdate = today.strftime('%Y-%m-%d')
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="password",database='real_estate')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="pid":
                property_id=value
            if key=="buyer_id":
                buyer_id=value
        
        ca="select * from  users where USER_ID= '{}'" .format(buyer_id)
        cursor.execute(ca)
        tel = tuple(cursor.fetchall())
        if(tel!=()):
            c1= "INSERT INTO PBOUGHT VALUES( '{}','{}','{}','{}','{}')".format(property_id ,sdate,0, buyer_id,'NULL')
            cursor.execute(c1)
            
            c2= "UPDATE PBOUGHT  INNER JOIN OWNERS ON OWNERS.PID = PBOUGHT.PID INNER JOIN PROPERTY_STATUS ON PROPERTY_STATUS.PID = PBOUGHT.PID SET  PBOUGHT.B_PRICE= PROPERTY_STATUS.S_PRICE,  PBOUGHT.SELLER_ID = OWNERS.OWNER_ID"
            cursor.execute(c2)
            # c3= "UPDATE PROPERTY_STATUS INNER JOIN PBOUGHT ON PROPERTY_STATUS.PID = PBOUGHT.PID  SET  PROPERTY_STATUS.BOUGHT ='YES'"
            # cursor.execute(c3)
            # c4="UPDATE OWNERS INNER JOIN PBOUGHT ON OWNERS.PID = PBOUGHT.PID  SET  OWNERS.OWNER_ID = PBOUGHT.BUYER_ID"
            # cursor.execute(c4)
            # c5="UPDATE OWNERS INNER JOIN USERS ON OWNERS.OWNER_ID = USERS.USER_ID  SET  OWNERS.EMAIL = USERS.EMAIL ,OWNERS.PHONE = USERS.PNO"
            # cursor.execute(c5)
            m.commit()
        else:
            return render(request, "error.html")
        
    else:
            return render(request, 'error.html')

    # if request.method=="POST":
    #     m=sql.connect(host="localhost",user="root",passwd="password",database='real_estate')
    #     cursor=m.cursor()
    #     d=request.POST
    #     for key,value in d.items():
    #         if key=="pid":
    #             property_id=value
    #         if key=="buyer_id":
    #             buyer_id=value
        
    #     ca="select * from  users where USER_ID= '{}'" .format(buyer_id)
    #     cursor.execute(ca)
    #     tel = tuple(cursor.fetchall())
    #     if(tel!=()):
    #         c1= "UPDATE PBOUGHT  INNER JOIN OWNERS ON OWNERS.PID = PBOUGHT.PID INNER JOIN PROPERTY_STATUS ON PROPERTY_STATUS.PID = PBOUGHT.PID SET  PBOUGHT.B_PRICE= PROPERTY_STATUS.S_PRICE,  PBOUGHT.SELLER_ID = OWNERS.OWNER_ID"
    #         cursor.execute(c1)
    #         m.commit()
    #     else:
    #         return render(request, "error.html")
        
    # else:
    #         return render(request, 'error.html')
    

    # if request.method=="POST":
    #     m=sql.connect(host="localhost",user="root",passwd="password",database='real_estate')
    #     cursor=m.cursor()
    #     d=request.POST
    #     for key,value in d.items():
    #         if key=="pid":
    #             property_id=value
    #         if key=="buyer_id":
    #             buyer_id=value
        
    #     ca="select * from  users where USER_ID= '{}'" .format(buyer_id)
    #     cursor.execute(ca)
    #     tel = tuple(cursor.fetchall())
    #     if(tel!=()):
    #         c1= "UPDATE PROPERTY_STATUS INNER JOIN PBOUGHT ON PROPERTY_STATUS.PID = PBOUGHT.PID  SET  PROPERTY_STATUS.BOUGHT ='YES'"
    #         cursor.execute(c1)
    #         m.commit()
    #     else:
    #         return render(request, "error.html")
        
    # else:
    #         return render(request, 'error.html')

    
        
    return render(request,'home.html')

def buyersallprop(request):
    global id
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="password",database='real_estate')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="user_id":
                id=value
            
    fa="CALL SHOWALLPROPS('{}')".format(id)
    # fa= "SELECT PNAME , FIRST_NAME,LAST_NAME , B_PRICE FROM  OWNERS O, PBOUGHT B , USERS U WHERE O.PID = B.PID AND B.BUYER_ID =U.USER_ID AND BUYER_ID ='{}'".format(id)
    cursor.execute(fa)
    t = tuple(cursor.fetchall())
    thead=[" PNAME" , "FIRST_NAME","LAST_NAME" , "VALUE"]
    return render(request, "dashboard.html",{'users': t, "thead": thead})

def asset(request):
    global id
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="password",database='real_estate')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="user_id":
                id=value
            
    fa="CALL ASSET('{}')".format(id)

    # fa= "SELECT SUM(B_PRICE) FROM PBOUGHT JOIN PROPERTY_STATUS ON PBOUGHT.PID = PROPERTY_STATUS.PID WHERE PBOUGHT.BUYER_ID = '{}' AND  PROPERTY_STATUS.R_S ='SELL'".format(id)
    cursor.execute(fa)
    t = tuple(cursor.fetchall())
    thead=[" TOTAL ASSET VALUE"]
    return render(request, "dashboard.html",{'users': t, "thead": thead})

def mesfilter(request):
    global kw
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="password",database='real_estate')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="key_word":
                kw=value
    # fa="CALL keyword('{}')".format(kw)
    fa= "SELECT NAME, MESSAGE FROM ENQUIRY WHERE MESSAGE LIKE '%{}%'".format(kw)
    cursor.execute(fa)
    t = tuple(cursor.fetchall())
   
    thead=[" NAME" , 'MESSAGE']
    if t==():
        thead=["NO MESSAGE WITH THIS KEYWORD"]
    return render(request, "dashboard.html",{'users': t, "thead": thead})

def data(request):
    global type
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="password",database='real_estate')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="tn":
                type=value
        
    fa= "SELECT * FROM {}".format(type)
    cursor.execute(fa)
    t = tuple(cursor.fetchall())
    # if t==():
    #     thead=["EMPTY"]
    # thead=[" NAME" , 'MESSAGE']
    return render(request, "dashboard.html",{'users': t})

def sellprops(request):
    global prop_name,size,price,prop_id,location,type,owner_id,rs,email,phone
    if request.method=="POST":
        
        m=sql.connect(host="localhost",user="root",passwd="password",database='real_estate')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="property_name":
                prop_name=value
            if key=="property_id":
                prop_id=value
            if key=="size":
                size=value
            if key=="price":
                price=value
            if key=="location":
                location=value
            if key=="rs":
                rs=value
            if key=="type":
                type=value
            if key=="email":
                email=value
            if key=="owner_id":
                owner_id=value
            if key=="phone":
                phone=value
        ca="select * from  users where USER_ID= '{}'" .format(owner_id)
        cursor.execute(ca)
        tel = tuple(cursor.fetchall())
        if(tel!=()):
            
            # c="insert into property Values('{}','{}','{}','{}','{}','{}','{}','{}')".format(prop_name,type,rs,size,price,location,owner_id,email)
            # cursor.execute(c)
            c1= "INSERT INTO PROPERTY_DESCRIPTION VALUES( '{}','{}','{}','{}','{}')".format(prop_id ,prop_name, type, size, location)
            cursor.execute(c1)
            m.commit()
           
        else:
            return render(request, 'error.html')
        

        m=sql.connect(host="localhost",user="root",passwd="password",database='real_estate')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="property_name":
                prop_name=value
            if key=="property_id":
                prop_id=value
            if key=="size":
                size=value
            if key=="price":
                price=value
            if key=="location":
                location=value
            if key=="rs":
                rs=value
            if key=="type":
                type=value
            if key=="email":
                email=value
            if key=="owner_id":
                owner_id=value
            if key=="phone":
                phone=value
        ca="select * from  users where USER_ID= '{}'" .format(owner_id)
        cursor.execute(ca)
        tel = tuple(cursor.fetchall())
        if(tel!=()):
        

            c2="INSERT INTO PROPERTY_STATUS VALUES( '{}','{}','{}','{}','{}')".format(prop_id ,prop_name,rs,price,'no')
            cursor.execute(c2)

            
            m.commit()
            
        else:
            return render(request, 'error.html')

        m=sql.connect(host="localhost",user="root",passwd="password",database='real_estate')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="property_name":
                prop_name=value
            if key=="property_id":
                prop_id=value
            if key=="size":
                size=value
            if key=="price":
                price=value
            if key=="location":
                location=value
            if key=="rs":
                rs=value
            if key=="type":
                type=value
            if key=="email":
                email=value
            if key=="owner_id":
                owner_id=value
            if key=="phone":
                phone=value
        ca="select * from  users where USER_ID= '{}'" .format(owner_id)
        cursor.execute(ca)
        tel = tuple(cursor.fetchall())
        if(tel!=()):
        

            c3 ="INSERT INTO OWNERS VALUES( '{}','{}','{}','{}','{}')".format(owner_id ,prop_id ,prop_name,email,phone)
            cursor.execute(c3)
            m.commit()
            
        else:
            return render(request, 'error.html')

    return render(request,'sell.html')