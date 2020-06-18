#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import files of the code flask is for connection,
#render_template is for connecting the html pages
#redirect and url_for and session is handling the url request and to maintain session

from flask import Flask,render_template,redirect, url_for,request,flash,session
import pandas as pd

import pymysql


# In[2]:


#instance of flask

app = Flask(__name__) 
#creating key for the session
app.config['SECRET_KEY'] = 'y_so_secret_tcs' 
#DataBase connection with localhost with password and Name of DataBase And with Auto commit to avoid frequent commits
db = pymysql.connect("localhost","root","","bankSQL", autocommit=True )
#database instance
conn = db.cursor()
#global variables for customer id n account id
global customerid,accid
customerid=100000000
accid=100000000


# In[3]:


#code for login which reads index html file
@app.route('/')
def index():
    return  render_template("index.html")


# In[4]:


#code for login
@app.route('/login',methods=['POST','GET'])
def login():
#this reads the values from the post method from html
    error = None
    if request.method == 'POST':
        username=request.form['uname']
        psw=request.form['psw']
        print(username)
 #to check the username is present in database and for login into page    
    try:
        session['cid'],session['cssn']=None,None
        sql=("""select SSN,Username,Password from userstore where Username=%s and Password=%s""",(username,psw))
        conn.execute(*sql)
        ssn,un,psw,=conn.fetchone()

#loading session with variables        
        session['username'],session['psw'],session['SSN']=un,psw,ssn
        print(session['SSN'])
        if request.form['uname'] != un or request.form['psw'] != psw: 
            error="Invalid Credentials. Please try again."
            return render_template('index.html',er=error)
        else:
            return render_template("dash.html",welcome=session.get('username'),val=True,vala=True,vals=True)
       
    except:
            error="Invalid Credentials. Please try again."
            return render_template('index.html',er=error)
            print("error")
                
#return statement is used to send the html page in post method to client            
    return render_template('index.html',er=error)
       


# In[5]:


#code for adding the new customer               
@app.route('/addncus',methods=['POST','GET'])
def addncus():
     if request.method == 'POST':
        ssnid=request.form['ssn']
        
#to verify the ssn is 9 digit
        if(len(ssnid)!=9):
            error="plz give 9 digit SSN"
            return render_template('dash.html',welcome=session.get('username'),er=error,vala=True,vals=True)
            
            
        name=request.form['name']
        age=request.form['age']
        addl1=request.form['addressl1']
        addl2=request.form['addressl2']
        state=request.form['state']
        city=request.form['city']
        addl1=addl1+addl2 
        global customerid
        customerid+=1
        
        print(customerid)
        try:
            msg="customer created successfully"
            print(msg)
            
#code for inserting the values into database to the table Customer
            tuplev=(ssnid,customerid,name,addl1,state,city,age,msg)
            sql=("""insert into Customer(SSNID,Customerid,Name,Address,State,City,Age,message) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",tuplev)
            conn.execute(*sql)
             
            return render_template("dash.html",welcome=session.get('username'),vala=True,vals=True)
        except:
            error="process coudnt b done"
            #return statement is used to send the html page in post method to client
            return render_template('dash.html',welcome=session.get('username'),er=error,vala=True,vals=True)
            print("error")
    
     
       
        
            
        
                    
                    
        
  
            


# In[ ]:



    


# In[6]:



#code for updating the customer table of database

@app.route('/updatecus',methods=['POST','GET'])
def updatecus():
    #code to verify which customerid to be updated 
    if(session.get('cssn')==None):
                error="plz find which customer"
                print(error)
                return render_template('dash.html',welcome=session.get('username'),er=error,val=True,vala=True,vals=True)
                
    if request.method == 'POST':
        try:
            ssn=session.get('cssn')
            print(ssn)     
            sql=("""select SSNID,Customerid,Name,Address,Age from Customer where SSNID=%s""",(ssn))
            conn.execute(*sql)
            cssid,cusid,coname,coaddress,coage=conn.fetchone()
            name=request.form['name']
            age=request.form['age']
            addl1=request.form['address']
            msg="customer updated succesfully"
            tuplev=(name,addl1,age,msg,ssn)
            
            
#sql command for the update statement
            sql=("""update Customer set Name=%s,Address=%s,Age=%s,message=%s where SSNID=%s""",tuplev)
            conn.execute(*sql)
            return render_template("dash.html",welcome=session.get('username'),vala=True,vals=True,cssid=cssid,cusid=cusid,cname=cname,cadd=coaddress,cage=coage)
        except:
            error="process coudnt b done"
            return render_template('dash.html',welcome=session.get('username'),vala=True,vals=True)
            print("error")
            
#return statement is used to send the html page in post method to client        


# In[7]:


#code for searching the customer

@app.route('/searchcustomer',methods=['POST','GET'])
def searchcus():
     if request.method == 'POST':
        try:
            ssn=request.form['ssnid']
            cid=request.form['cid']
            
            
            
#sql query to find the values of valid
            sql=("""select SSNID,Customerid from Customer where Customerid=%s and SSNID=%s""",(cid,ssn))
            try:
                conn.execute(*sql)
                cssn,caid=conn.fetchone()
                if(str(caid)!=cid and str(cssn)!=ssn):
                    error="process coudnt b done due incorrect values"
                    return render_template('dash.html',welcome=session.get('username'),vala=True,vals=True,er=error)        
            except: 
                error="process coudnt b done due incorrect values"
                print(error)
                return render_template('dash.html',welcome=session.get('username'),vala=True,vals=True,er=error)

            
#session updation
         
            session['cid'],session['cssn']=cid,ssn
            sql=("""select SSNID,Customerid,Name,Address,Age from Customer where SSNID=%s""",(ssn))
            conn.execute(*sql)
            cssid,cusid,coname,coaddress,coage=conn.fetchone()
            print(coage)
    
#return statement is used to send the html page in post method to client    
            return render_template("dash.html",welcome=session.get('username'),vala=True,vals=True,cssid=cssid,cusid=cusid,cname=coname,cadd=coaddress,cage=coage)

                              
        except:
            error="process coudnt b done"
            return render_template('dash.html',welcome=session.get('username'),val=True,vala=True,vals=True,er=error)
            print("error")
            
            
            








# In[8]:


#code for deleting customer


@app.route('/deletecustomer',methods=['POST','GET'])
def deletecustomer():
    if(session.get('cssn')==None):    
        error="plz find which customer"
        print(error)
        return render_template('dash.html',welcome=session.get('username'),er=error,val=True,vala=True,vals=True)
    
    print((session.get('cssn')))
    sql=("""select SSNID,Customerid,Name,Address,Age from Customer where SSNID=%s""",(session.get('cssn')))
    conn.execute(*sql)
    print((session.get('cssn')))
    cssid,cusid,cname,cadd,cage=conn.fetchone()
    
#sql query for deleting the customer
    sql=("""delete from Customer where SSNID=%s and Customerid=%s""",(cssid,cusid))
    conn.execute(*sql)
#session is cleared here
    session.pop('cssn', None)
    session.pop('cid', None)
    return render_template("dash.html",vala=True,vals=True,welcome=session.get('username'),cssid=cssid,cusid=cusid,cname=cname,cadd=cadd,cage=cage)
#return statement is used to send the html page in post method to client




# In[9]:


#code for logout

@app.route('/logout',methods=['POST','GET'])
def logout():
    if request.method == 'POST':
#session is cleared here
        if 'lout' in request.form:
                    session.pop('username', None)
                    session.pop('passwrd', None)
                    session.pop('SSN', None)
    #return statement is used to send the html page in post method to client
                    return render_template("index.html")
        


# In[10]:


#code for adding account
@app.route('/addaccount',methods=['POST','GET'])
def addaccount():
    if request.method == 'POST':
        cid=request.form['cid']
        acctype=request.form['acctype']
        amt=request.form['amount']
        try:
#sql query for verifying the customer details
            sql=("""select Customerid from Customer where Customerid=%s""",(cid))
            conn.execute(*sql)
            caid=conn.fetchone()
            if(str(caid[0])!=cid):
                error="process coudnt b done due incorrect values"
                print(error)
                return render_template('dash.html',welcome=session.get('username'),val=True,vala=True,vals=True,er=error)        
        except: 
            error="process coudnt b done due incorrect values"
            print(error)
            return render_template('dash.html',welcome=session.get('username'),val=True,vala=True,vals=True,er=error)
            
        try:
            global accid
            accid+=1
            print(accid)
            msg="account created succesfully"
            tuplev=(accid,cid,amt,acctype,msg)
            print(tuplev)
#code for inserting to the values to account table
            sql=("""insert into Account(Accountid,cusid,Balance,accounttype,msg) VALUES (%s,%s,%s,%s,%s)""",tuplev)
            print(conn.execute(*sql))
            tuplev=(accid,cid,amt,msg)
#code for inserting the values to personalaccount table
            sql=("""insert into personalaccount(aid,cid,abalance,msg)VALUES(%s,%s,%s,%s)""",tuplev)
            conn.execute(*sql)  
            return render_template('dash.html',welcome=session.get('username'))
        except:
            error="process coudnt b done"
            return render_template('dash.html',welcome=session.get('username'),val=True,vala=True,vals=True)
            print("error")
        
            
            
            


# In[11]:


#code for deleting the account
@app.route('/deleteaccount',methods=['POST','GET'])
def deleteaccount():
    if request.method == 'POST':
        
        cid=request.form['cid']
        acctype=request.form['acctype']
        aid=request.form['aid']
 #values are verified here for accuracy            
        try:
            sql=("""select Accountid,cusid from Account where cusid=%s and Accountid=%s""",(cid,aid))
            conn.execute(*sql)
            caid,fcid=conn.fetchone()
            print(caid)
            
        except:
            error="process coudnt b done due incorrect values"
            print(error)
            return render_template('dash.html',welcome=session.get('username'),val=True,vala=True,vals=True,er=error)
            
        try:
            tuplev=(aid,cid)
#code for deleting the account 
            sql=("""delete from Account where Accountid=%s and cusid=%s""",tuplev)
            conn.execute(*sql)
            amt="0"
            msg="account deleted"
            tuplev=(aid,cid,amt,msg)
            print(tuplev)
#code for inserting values into personalaccount
            sql=("""insert into personalaccount(aid,cid,abalance,msg)VALUES(%s,%s,%s,%s)""",tuplev)
            conn.execute(*sql)  
            return render_template('dash.html',welcome=session.get('username'))
        except:
#return statement is used to send the html page in post method to client
            error="process coudnt b done"
            return render_template('dash.html',welcome=session.get('username'),val=True,vala=True,vals=True)
            print("error")







# In[ ]:





# In[12]:


#code for deposit the money to specific account
@app.route('/depositmoney',methods=['POST','GET'])
def depositmoney():
    if request.method == 'POST':
        amt=request.form['amt'] 
   #code to verify the details given in the search account are correct 
        try:      
            sql=("""select Accountid,cusid,balance,accounttype from Account where Accountid=%s""",(session.get('aid')))
            conn.execute(*sql)
            aid,cusid,bal,at=conn.fetchone()
    
            bal=float(amt)+float(bal)
        
            msg="amount is debited"
            tuplev=(bal,msg,(session.get('aid')))
#code for updating the table in database of acccount
            sql=("""update Account set balance=%s,msg=%s where Accountid=%s""",tuplev)
            conn.execute(*sql)
            tuplev=((session.get('aid')),cusid,bal,msg)
#code for updating the database of table personalaccount
            sql=("""insert into personalaccount(aid,cid,abalance,msg)VALUES(%s,%s,%s,%s)""",tuplev)
            conn.execute(*sql)  
            sql=("""select Accountid,cusid,balance,accounttype from Account where Accountid=%s""",(session.get('aid')))
            conn.execute(*sql)
            aid,cusid,bal,at=conn.fetchone()
            print(aid)
#return statement is used to send the html page in post method to client
            return render_template('dash.html',welcome=session.get('username'),val=True,vals=True,aid=aid,cusid=cusid,bal=bal,at=at)
     
        except:
#if any exception its handled here
            error="process coudnt b done"
            return render_template('dash.html',welcome=session.get('username'),val=True,vala=True,vals=True,er=error)
            print("error") 
            
            
            

            




# In[13]:


#code for withdrawmoney
@app.route('/withdrawmoney',methods=['POST','GET'])
def withdrawmoney():
    if request.method == 'POST':
        amt=request.form['amt'] 
  #code to verify details are correct or not  
        try:      
            sql=("""select Accountid,cusid,balance,accounttype from Account where Accountid=%s""",(session.get('aid')))
            conn.execute(*sql)
            aid,cusid,bal,at=conn.fetchone()
    
            bal=float(bal)-float(amt)
        
            msg="amount is credited"
            tuplev=(bal,msg,(session.get('aid')))
#code for the updating the account table in database
            sql=("""update Account set balance=%s,msg=%s where Accountid=%s""",tuplev)
            conn.execute(*sql)
            tuplev=((session.get('aid')),cusid,bal,msg)
#code for the inserting the values into personal account
            sql=("""insert into personalaccount(aid,cid,abalance,msg)VALUES(%s,%s,%s,%s)""",tuplev)
            conn.execute(*sql)
            sql=("""select Accountid,cusid,balance,accounttype from Account where Accountid=%s""",(session.get('aid')))
            conn.execute(*sql)
            aid,cusid,bal,at=conn.fetchone()
            print(aid)
  #return statement is used to send the html page in post method to client          
            return render_template('dash.html',welcome=session.get('username'),val=True,vals=True,aid=aid,cusid=cusid,bal=bal,at=at)
     
        except:
            error="process coudnt b done"
            return render_template('dash.html',welcome=session.get('username'),val=True,vala=True,vals=True)
            print("error") 
            
            
            
    
            





# In[14]:


#code to transfer money 
@app.route('/transfermoney',methods=['POST','GET'])
def transfermoney():
    if request.method == 'POST':
        aidt=request.form['cid'] 
        amt=request.form['amt'] 
        try: 
#code to verify the details
            sql=("""select Accountid,cusid,balance,accounttype from Account where Accountid=%s""",(session.get('aid')))
            conn.execute(*sql)
            aid,cusid,bal,at=conn.fetchone()
            print(bal)
            bal=float(bal)-float(amt)
            print(bal)
            msg="amount is credited"
            tuplev=(bal,msg,(session.get('aid')))
#code to update the account table
            sql=("""update Account set balance=%s,msg=%s where Accountid=%s""",tuplev)
            conn.execute(*sql)
            tuplev=((session.get('aid')),cusid,bal,msg)
    #code to update the personalaccount table
            sql=("""insert into personalaccount(aid,cid,abalance,msg)VALUES(%s,%s,%s,%s)""",tuplev)
            conn.execute(*sql)
            sql=("""select Accountid,cusid,balance,accounttype from Account where Accountid=%s""",aidt)
            conn.execute(*sql)
            aid,cusid,bal,at=conn.fetchone()
            print(bal)
            bal=float(bal)+float(amt)
            msg="amount is debited"
            print(aidt)
            tuplev=(bal,msg,aidt)
    #code to update the account table
            sql=("""update Account set balance=%s,msg=%s where Accountid=%s""",tuplev)
            conn.execute(*sql)
            print(msg,aidt)
            
            tuplev=((session.get('aid')),cusid,bal,msg)
            sql=("""insert into personalaccount(aid,cid,abalance,msg)VALUES(%s,%s,%s,%s)""",tuplev)
            conn.execute(*sql)
            
            sql=("""select Accountid,cusid,balance,accounttype from Account where Accountid=%s""",(session.get('aid')))
            conn.execute(*sql)
            aid,cusid,bal,at=conn.fetchone()
            print(aid)
    #return statement is used to send the html page in post method to client        
            return render_template('dash.html',welcome=session.get('username'),val=True,vals=True,aid=aid,cusid=cusid,bal=bal,at=at)
     
        except:
            error="process coudnt b done"
            return render_template('dash.html',welcome=session.get('username'),val=True,vala=True,vals=True)
            print("error") 
            
            
            



# In[15]:


#code for the account statement
@app.route('/accountstatement',methods=['POST','GET'])
def accountstatement():
    if request.method == 'POST':
        sdate=request.form['startdate']
        edate=request.form['lastdate']
        print(sdate)
        print(edate)
        try:
            tuplel=((session.get('aid')),sdate,edate)
        #code to select data form the personal account table
            sql=("""select transid,abalance,msg,datea from personalaccount where aid=%s and datea BETWEEN %s and %s""",tuplel)
            conn.execute(*sql)
            data=conn.fetchall()
    #return statement is used to send the html page in post method to client
            return render_template('dash.html',welcome=session.get('username'),val=True,data=data,vals=True)
        except:
            error="process coudnt b done"
            return render_template('dash.html',welcome=session.get('username'),val=True,data="none",er=error,vala=True,vals=True)
            print("error")
        
            


# In[16]:


#code for customer Status
@app.route('/customeraccstatus',methods=['POST','GET'])
def customerstatus():

    try:
    
        sql=("""select SSNID,Customerid,message,datec from Customer""")
        conn.execute(sql)
        cdata=conn.fetchall()
        sql=("""select Accountid,cusid,balance,Accounttype,msg,cdate from Account""")
        conn.execute(sql)
        adata=conn.fetchall()
#return statement is used to send the html page in post method to client
        return render_template('dash.html',welcome=session.get('username'),val=True,cdata=cdata,adata=adata,vala=True)
    except:
        error="process coudnt b done"
        return render_template('dash.html',welcome=session.get('username'),val=True,data="none",er=error,vala=True,vals=True)
        print("error")
        
            


# In[17]:


#code for searching account
@app.route('/searchaccount',methods=['POST','GET'])
def searchaccount():
     if request.method == 'POST':
        aid=request.form['aid']
        try:
    #code to verify the details
            sql=("""select Accountid,cusid from Account where Accountid=%s """,(aid))
            try:
                conn.execute(*sql)
                caid,cssn=conn.fetchone()
                if str(caid)!=aid:
                    error="process coudnt b done due incorrect values"
                    print(error)
                    return render_template('dash.html',welcome=session.get('username'),val=True,er=error,vala=True,vals=True)
            except:
                error="process coudnt b done due incorrect value"
                print(error)
                return render_template('dash.html',welcome=session.get('username'),val=True,er=error,vala=True,vals=True)
            
            session['aid']=aid
         #code to select data form the personal account table
            print(session.get('aid'))
            sql=("""select Accountid,cusid,balance,accounttype from Account where Accountid=%s""",(aid))
            conn.execute(*sql)
            aid,cusid,bal,at=conn.fetchone()
            
            return render_template('dash.html',vals=True,welcome=session.get('username'),val=True,aid=aid,cid=cusid,bal=bal,at=at)
 #return statement is used to send the html page in post method to client                             
        except:
            error="process coudnt b done"
            return render_template('dash.html',welcome=session.get('username'),val=True,er=error,vala=True,vals=True)
            print("error")


# In[ ]:


#code for running the application
if __name__ == '__main__':
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:




