import mysql.connector as sql
from time import gmtime,strftime

conn=sql.connect(host="localhost", user="root", passwd="kingpin123",database="dvd")
if conn.is_connected():
    print("Successfully connected!\n")
    
c1=conn.cursor()
print("WELCOME TO CD/DVD STORE")
a=strftime("%a,%d%b%y",gmtime())
print(a)
name=input("\nEnter your name: ")
n=name.capitalize()
print(' ')
print('Welcome,',n)
print(' ')
print("1. Login")
print("2. Create account")
print("3. Exit")
print('')
choice=int(input("Enter your choice: "))
print(' ')
if choice==1:
    a=int(input("Enter user_id: "))
    b=int(input("Enter password: "))
    c1.execute("SELECT passwd FROM login WHERE user_id = "+str(a)+";")
    data=c1.fetchall()
    data=data[0]
    data=list(data)
    data=data[0]
    data=str(data)
    print(' ')
    print(' ')
    conn.cursor()
    conn.commit()

    print(' ')
    print('THE MENU\n')
    print('1. Online order')
    print('2. CD details')
    print('3. DVD details')
    print('4. Job opportunities\n')
    choice2=int(input("Enter your choice:"))
    if choice2==5:
          v_year_of_release=int(input("Enter the year of release:"))
          v_language=input("Enter the language:")
          print("1.horror")
          print("2.comedy")
          print("3.action")
          print("4.inspiration")
          print("5.sentimental")
          v_type_of_movie=input("type of movie u want:")
          v_movie_name=input("enter movie name:")
          print("details uploaded")
          V_SQL_INSERT1="insert into cd_details values("+str(v_year_of_release)+",'"+v_type_of_movie+"','"+v_movie_name+"','"+v_language+"')"
          c1.execute(V_SQL_INSERT1)
          print("movie added to your cart")
          conn.commit()

    if choice2==6:
          v_dvd_model=input("enter dvd model:")
          v_dvd_name=input("enter dvd company:")
          v_version=int(input("enter the version you need:"))
          v_range_of_amt=int(input("the amt of product u expect:"))
          if v_range_of_amt>=5000:
                      print("best products awaits you")
          else:
                      print("we can provide the best if there is offers")
    V_SQL_INSERT2="insert into dvd_detail values('"+v_dvd_model+"','"+v_dvd_name+"',"+str(v_version)+","+str(v_range_of_amt)+")"
    c1.execute(V_SQL_INSERT2)
    print("dvd added to your cart !!!")
    conn.commit()

    if choice2==1:
            v_customer_name=input("Enter name:")
            print("Welcome",v_customer_name,"to our shop")
            v_age=int(input("Enter your age:"))
            v_mobile_number=int(input("Enter your phone:"))
            v_cd_or_dvd=input("Enter what you want(cd or dvd):")
            if v_cd_or_dvd=="cd":
               v_year_of_release=int(input("Enter the year:"))
               v_language=input("Enter your language:")
               print("1.horror")
               print("2.comedy")
               print("3.action")
               print("4.inspiration")
               print("5.sentimental")
               v_type_of_movie=input("Enter the type of movie you want:")
               v_movie_name=input("Enter the movie name:")
               print("details uploaded")
               V_SQL_INSERT1="INSERT INTO cd_details values("+str(v_year_of_release)+",'"+v_type_of_movie+"','"+v_movie_name+"','"+v_language+"')"
               c1.execute(V_SQL_INSERT1)
               print("movie added to your cart")
               conn.commit()
            elif v_cd_or_dvd=="dvd":
                v_dvd_model=input("Enter dvd model:")
                v_dvd_name=input("Enter dvd name:")
                v_version=int(input("Enter the version you need:"))
                v_range_of_amt=int(input("The amount of product you expect:"))
                if v_range_of_amt>=10000:
                    print("best products awaits you")
                else:
                    print("we can provide the best if there is offers")
                V_SQL_INSERT2="insert into dvd_detail values('"+v_dvd_model+"','"+v_dvd_name+"',"+str(v_version)+","+str(v_range_of_amt)+")"
                c1.execute(V_SQL_INSERT2)
                print("dvd added to your cart !!!")
                conn.commit()
            else:
                print("sorry we didn't get you")

            V_SQL_INSERT1="insert into online values('"+v_customer_name+"',"+str(v_age)+","+str(v_mobile_number)+",'"+v_cd_or_dvd+"')"
            c1.execute(V_SQL_INSERT1)
            comments=input("you can give comments:")
            conn.commit()
            print("your order will accepted once u detail ur material")
    if choice2==7:
        v_name=print("You are",n)
        print(" ")
        v_age=int(input("Enter your age:"))
        print(" ")
        v_qualification=input("Enter your qualification:")
        print(" ")
        v_date_of_birth=input("Enter your date of birth:")
        print(" ")
        print("1. manager")
        print(" ")
        print("2. salesman")
        print(" ")
        print("3. general employee")
        print(" ")
        print("4. multi task")
        print(" ")
        v_type_of_work=int(input("Enter the type of work you want:"))
        if v_type_of_work==1:
                print("vacancy available:1")
                print("attend interview and if you perform fine")
                print("call letter will be sent")
                print("you can take over the post of manager once you get the call letter")
                print("salary per month:$500 or Rs35000")
        elif v_type_of_work==2:
                print("vacancy available:6")
                print("you can join the job from tomorrow if vacancy available")
                print("salary per month:$100 or Rs7000")
        elif v_type_of_work==3:
                print("vacancy available:10")
                print("you can join if vacancy available")
                print("salary per month:$75 or Rs5150")
        elif v_type_of_work==4:
                print("vacancy available:3")
                print("you can join if performance in the interview is good")
                print("salary per month:$400 or Rs28000")
        else:
                print("SORRY, we didn't understand.")
        V_SQL_INSERT2="insert into job values('"+v_name+"',"+str(v_age)+",'"+v_qualification+"',"+str(v_date_of_birth )+",'"+v_type_of_work+"')"
        c1.execute(V_SQL_INSERT2)
        comments=input("you can give comments:")
        conn.commit()
        
            
        
if choice==2:
        print('To create your account, please enter your user id and password')
        c1=conn.cursor()
        c1.execute("CREATE TABLE login(user_id varchar(100) primary key,passwd varchar(100),name varchar(100))")
        v_user_id=int(input("\nChoose your user id (in integer): "))
        v_passwd=int(input("Create your password (in integer): "))
        v_name=input("Your full name: ")
        c1=conn.cursor()
        update="INSERT INTO login values("+ str(v_user_id) +","+ str(v_passwd) +",'"+ v_name +"')"
        c1.execute(update)
        conn.commit()
        print("\nAccount created!")
    
if choice==3:
        print("THANK YOU",n)
        print("VISIT AGAIN")
        comments=input("You can give comments:")

