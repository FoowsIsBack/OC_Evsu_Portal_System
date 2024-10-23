#dave.py
#RED (Title) = \x1b[38:5:196m
#Yellow = \x1b[38:5:148m
#Cyan (Text) = \x1b[38:5:195m
#Sky Blue (Bg Color) = \x1b[38:5:74m
#Green = \x1b[38:5:28m

#How to run
#1. source my_virtual_env/bin/activate.fish
#2. python /home/foows/coding/py/Evsu_System.py

import os
import time
import getpass
import pyotp

def clear():
    if os.name == 'nt':  
        os.system('cls')
    else:
        os.system('clear')

def loading():
    print("""
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mLOG IN EVSU STUDENT PORTAL                \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│           \x1b[38:5:195mPlease wait a minute Loading Screen\x1b[38:5:28m.             \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m╰────────────────────────────────────────────────────────────╯""")
    time.sleep(1)
    clear()
    print("""
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mLOG IN EVSU STUDENT PORTAL                \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│           \x1b[38:5:195mPlease wait a minute Loading Screen\x1b[38:5:28m..            \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m╰────────────────────────────────────────────────────────────╯""")
    time.sleep(1)
    clear()
    print("""
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mLOG IN EVSU STUDENT PORTAL                \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│           \x1b[38:5:195mPlease wait a minute Loading Screen\x1b[38:5:28m...           \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m╰────────────────────────────────────────────────────────────╯""")
    time.sleep(1)
    clear()
    print("""
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mLOG IN EVSU STUDENT PORTAL                \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│           \x1b[38:5:195mPlease wait a minute Loading Screen\x1b[38:5:28m....          \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m╰────────────────────────────────────────────────────────────╯""")
    time.sleep(1)
    clear()
    print("""
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mLOG IN EVSU STUDENT PORTAL                \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│           \x1b[38:5:195mPlease wait a minute Loading Screen\x1b[38:5:28m.....         \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m╰────────────────────────────────────────────────────────────╯""")
    time.sleep(5)
    clear()
    portal()

def login():
    global user, passw
    print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mLOG IN EVSU STUDENT PORTAL                \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────╯""")
    user1 = input("    \x1b[38:5:74m├───\x1b[38:5:148m>\x1b[38:5:195m Username\x1b[38:5:28m:\x1b[38:5:148m ")
    print("    \x1b[38:5:74m│")
    passw1 = getpass.getpass("    \x1b[38:5:74m╰───\x1b[38:5:148m>\x1b[38:5:195m Password\x1b[38:5:28m:\x1b[38:5:148m ")
    if user1 == user and passw == passw1:
        clear()
        loading()
    else:
        clear()
        print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mLOG IN EVSU STUDENT PORTAL                \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│        \x1b[38:5:195mInvalid \x1b[38:5:196musername \x1b[38:5:195mor \x1b[38:5:196mpassword\x1b[38:5:28m. \x1b[38:5:195mPlease try again      \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m╰────────────────────────────────────────────────────────────╯""")
        choice = input("     \x1b[38:5:195mPress Enter to Go Back\x1b[38:5:28m:\x1b[38:5:148m ")
        clear()
        login()

def backtomain():
    print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                       \x1b[38:5:196mLOG OUT ACCOUNT\x1b[38:5:28m.                     \x1b[38:5:74m│
    \x1b[38:5:74m╰────────────────────────────────────────────────────────────╯""")
    time.sleep(1)
    clear()

    print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                       \x1b[38:5:196mLOG OUT ACCOUNT\x1b[38:5:28m..                    \x1b[38:5:74m│
    \x1b[38:5:74m╰────────────────────────────────────────────────────────────╯""")
    time.sleep(1)
    clear()

    print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                       \x1b[38:5:196mLOG OUT ACCOUNT\x1b[38:5:28m...                   \x1b[38:5:74m│
    \x1b[38:5:74m╰────────────────────────────────────────────────────────────╯""")
    time.sleep(1)
    clear()

    print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                       \x1b[38:5:196mLOG OUT ACCOUNT\x1b[38:5:28m....                  \x1b[38:5:74m│
    \x1b[38:5:74m╰────────────────────────────────────────────────────────────╯""")
    time.sleep(1)
    clear()

    print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                       \x1b[38:5:196mLOG OUT ACCOUNT\x1b[38:5:28m.....                 \x1b[38:5:74m│
    \x1b[38:5:74m╰────────────────────────────────────────────────────────────╯""")
    time.sleep(3)
    clear()
    main()

def logout():
    print("""
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                 \x1b[38:5:196mWELCOME TO EVSU STUDENT PORTAL             \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│       \x1b[38:5:195mAre you sure you want to \x1b[38:5:196mlog out \x1b[38:5:195mof your \x1b[38:5:196maccount\x1b[38:5:195m?    \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │         
    \x1b[38:5:74m│                       \x1b[38:5:148m1\x1b[38:5:28m. \x1b[38:5:195mYes                               \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │   
    \x1b[38:5:74m│                       \x1b[38:5:148m2\x1b[38:5:28m. \x1b[38:5:196mNo                                \x1b[38:5:74m│   
    \x1b[38:5:74m│                                                            │ 
    \x1b[38:5:74m├────────────────────────────────────────────────────────────╯""")
    choice = int(input("    \x1b[38:5:74m╰───\x1b[38:5:148m>\x1b[38:5:195m Choice:\x1b[38:5:148m "))
    clear()

    if choice == 1:
        backtomain()
    elif choice == 2:
        main()

def portal():
    print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                 \x1b[38:5:196mWELCOME TO EVSU STUDENT PORTAL             \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│                     \x1b[38:5:148m1\x1b[38:5:28m. \x1b[38:5:195mQuiz                                \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            \x1b[38:5:74m│
    \x1b[38:5:74m│                     \x1b[38:5:148m2\x1b[38:5:28m. \x1b[38:5:195mView Score                          \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            \x1b[38:5:74m│
    \x1b[38:5:74m│                     \x1b[38:5:148m3\x1b[38:5:28m. \x1b[38:5:195mDataBase                            \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            \x1b[38:5:74m│
    \x1b[38:5:74m│                     \x1b[38:5:148m0\x1b[38:5:28m. \x1b[38:5:195mLog Out                             \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m├────────────────────────────────────────────────────────────╯""")
    choice = int(input("    \x1b[38:5:74m╰───\x1b[38:5:148m>\x1b[38:5:195m Choice:\x1b[38:5:148m "))
    clear()

    if choice == 1:
        tools()
    elif choice == 2:
        viewscore()
    elif choice == 3:
        databasemain()
    elif choice == 0:
        logout()

question = {
        "     \x1b[38:5:148m1\x1b[38:5:28m. \x1b[38:5:195mWho developed \x1b[38:5:196mPython \x1b[38:5:195mprogramming language?\x1b[38:5:28m:\x1b[38:5:148m ": "guido van rossum",
        "     \x1b[38:5:148m2\x1b[38:5:28m. \x1b[38:5:195mWho developed \x1b[38:5:196min HTML\x1b[38:5:195m?\x1b[38:5:28m:\x1b[38:5:148m ": "tim berners lee",
        "     \x1b[38:5:148m3\x1b[38:5:28m. \x1b[38:5:195mWho developed \x1b[38:5:196mC \x1b[38:5:195mprogramming language?\x1b[38:5:28m:\x1b[38:5:148m ": "rennis ritchie",
        "     \x1b[38:5:148m4\x1b[38:5:28m. \x1b[38:5:195mWho developed \x1b[38:5:196mC++ \x1b[38:5:195mprogramming language?\x1b[38:5:28m:\x1b[38:5:148m ": "bjarne stroustrup",
        "     \x1b[38:5:148m5\x1b[38:5:28m. \x1b[38:5:195mWho developed in \x1b[38:5:196mjavascript\x1b[38:5:195m?\x1b[38:5:28m:\x1b[38:5:148m ": "brendan eich"
    }

def qa():
    global question
    global score
    score = 0
    print(f"""
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                   \x1b[38:5:195mWELCOME TO \x1b[38:5:196mQUIZ GAME                     \x1b[38:5:74m│
    \x1b[38:5:74m╰────────────────────────────────────────────────────────────╯""")
    for question, correct_answer in question.items():
        answer = input(question).lower()
        if answer == correct_answer:
            score += 20
    clear()
    portal()

def tools():
    print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                      \x1b[38:5:196mQUIZ EVSU PORTAL                      \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│                \x1b[38:5:148m1\x1b[38:5:28m. \x1b[38:5:195mQuestion and Answer                      \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            \x1b[38:5:74m│
    \x1b[38:5:74m│                \x1b[38:5:148m0\x1b[38:5:28m. \x1b[38:5:195mExit                                     \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m├────────────────────────────────────────────────────────────╯""")
    choice = int(input("    \x1b[38:5:74m╰───\x1b[38:5:148m>\x1b[38:5:195m Choice:\x1b[38:5:148m "))
    clear()

    if choice == 1:
        database()
    elif choice == 0:
        portal()

def viewscore():
    global score
    global user
    print(f"""
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                   \x1b[38:5:196mQUIZ STUDENT RESULT                      \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                   \x1b[38:5:195mYour Score is\x1b[38:5:28m: \x1b[38:5:28m{score}                   
    \x1b[38:5:74m╰────────────────────────────────────────────────────────────╯""")
    choice = input("     \x1b[38:5:195mPress Enter to Go Back\x1b[38:5:28m:\x1b[38:5:148m ")
    clear()
    portal()

course = [
    "BS in Information Technology (BSIT)",
    "BS in Civil Engineering (BSCE)",
    "BS in Mechanical Engineering (BSME)",    
    "BS in Industrial Technology (Culinary Arts)",
    "BS in Industrial Technology (Electronics)",
]

def database():
    global name1, age1, address, email, course
    print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                   \x1b[38:5:196mEVSU REGISTER STUDENT                    \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤ 
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│          \x1b[38:5:148m1\x1b[38:5:28m. \x1b[38:5:195mBS in Information Technology (\x1b[38:5:148mBSIT\x1b[38:5:74m)            \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            \x1b[38:5:74m│
    \x1b[38:5:74m│          \x1b[38:5:148m2\x1b[38:5:28m. \x1b[38:5:195mBS in Civil Engineering (\x1b[38:5:148mBSCE\x1b[38:5:74m)                 \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            \x1b[38:5:74m│
    \x1b[38:5:74m│          \x1b[38:5:148m3\x1b[38:5:28m. \x1b[38:5:195mBS in Mechanical Engineering (\x1b[38:5:148mBSME\x1b[38:5:74m)            \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            \x1b[38:5:74m│
    \x1b[38:5:74m│          \x1b[38:5:148m4\x1b[38:5:28m. \x1b[38:5:195mBS in Industrial Technology (\x1b[38:5:148mCulinary Arts\x1b[38:5:74m)    \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            \x1b[38:5:74m│
    \x1b[38:5:74m│          \x1b[38:5:148m5\x1b[38:5:28m. \x1b[38:5:195mBS in Industrial Technology (\x1b[38:5:148mElectronics\x1b[38:5:74m)      \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m╰────────────────────────────────────────────────────────────╯""")
    name1 = input("     \x1b[38:5:195mFull Name\x1b[38:5:28m:\x1b[38:5:148m ")
    age1 = input("     \x1b[38:5:195mAge\x1b[38:5:28m:\x1b[38:5:148m ")
    address = input("     \x1b[38:5:195mAddress\x1b[38:5:28m:\x1b[38:5:148m ")
    email = input("     \x1b[38:5:195mEmail\x1b[38:5:28m:\x1b[38:5:148m ")
    course_choice = int(input("     \x1b[38:5:195mCourse (\x1b[38:5:148m1\x1b[38:5:195m-\x1b[38:5:148m5\x1b[38:5:195m)\x1b[38:5:28m:\x1b[38:5:148m "))
    course = course[course_choice - 1]
    clear()
    qa()

def databasemain():
    print(f""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                   \x1b[38:5:196mEVSU STUDENT DATABASE                    \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤   
    \x1b[38:5:74m│                                              
    \x1b[38:5:74m│    \x1b[38:5:195mStudent Name\x1b[38:5:28m:   \x1b[38:5:195m{name1}      
    \x1b[38:5:74m│
    \x1b[38:5:74m│    \x1b[38:5:195mAge\x1b[38:5:28m:            \x1b[38:5:195m{age1} 
    \x1b[38:5:74m│
    \x1b[38:5:74m│    \x1b[38:5:195mAddress\x1b[38:5:28m:        \x1b[38:5:195m{address}  
    \x1b[38:5:74m│
    \x1b[38:5:74m│    \x1b[38:5:195mEmail\x1b[38:5:28m:          \x1b[38:5:195m{email}  
    \x1b[38:5:74m│
    \x1b[38:5:74m│    \x1b[38:5:195mCourse\x1b[38:5:28m:         \x1b[38:5:195m{course}   
    \x1b[38:5:74m│                                    
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m╰────────────────────────────────────────────────────────────╯""")
    choice = input("    \x1b[38:5:195mPress Enter to Go Back\x1b[38:5:28m:\x1b[38:5:148m ")
    clear()
    portal()

def signup(): 
    global user, passw
    print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mORMOC CITY EVSU PORTAL                    \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│           \x1b[38:5:195mCreate a new account for \x1b[38:5:196mEVSU \x1b[38:5:74m\x1b[38:5:195mStudent            \x1b[38:5:195m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m├────────────────────────────────────────────────────────────╯""")
    user = input("    \x1b[38:5:74m├───\x1b[38:5:148m> \x1b[38:5:195mUsername\x1b[38:5:28m:\x1b[38:5:148m ")
    print("    \x1b[38:5:74m│")
    passw = getpass.getpass("    \x1b[38:5:74m╰───\x1b[38:5:148m>\x1b[38:5:195m Password\x1b[38:5:28m:\x1b[38:5:148m ")
    clear()
    registerdone()

def registerdone():
        print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mORMOC CITY EVSU PORTAL                    \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│                    \x1b[38:5:195mAccount Registered\x1b[38:5:28m.                     \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m╰────────────────────────────────────────────────────────────╯""")
        time.sleep(1)
        clear()
        print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mORMOC CITY EVSU PORTAL                    \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│                    \x1b[38:5:195mAccount Registered\x1b[38:5:28m..                    \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m╰────────────────────────────────────────────────────────────╯""")
        time.sleep(1)
        clear()
        print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mORMOC CITY EVSU PORTAL                    \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│                    \x1b[38:5:195mAccount Registered\x1b[38:5:28m...                   \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m╰────────────────────────────────────────────────────────────╯""")
        time.sleep(1)
        clear()
        print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mORMOC CITY EVSU PORTAL                    \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│                    \x1b[38:5:195mAccount Registered\x1b[38:5:28m....                  \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m╰────────────────────────────────────────────────────────────╯""")
        time.sleep(1)
        clear()
        print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mORMOC CITY EVSU PORTAL                    \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│                    \x1b[38:5:195mAccount Registered\x1b[38:5:28m.....                 \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m╰────────────────────────────────────────────────────────────╯""")
        time.sleep(3)
        choice = input("     \x1b[38:5:195mPress Enter to Go Back\x1b[38:5:28m:\x1b[38:5:148m ") 
        clear()

def changepassdone():
        print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mORMOC CITY EVSU PORTAL                    \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│                \x1b[38:5:195mAccount Change \x1b[38:5:196mPassword\x1b[38:5:28m.                    \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m└────────────────────────────────────────────────────────────╯""")
        time.sleep(1)
        clear()
        print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mORMOC CITY EVSU PORTAL                    \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│                \x1b[38:5:195mAccount Change \x1b[38:5:196mPassword\x1b[38:5:28m..                   \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m└────────────────────────────────────────────────────────────╯""")
        time.sleep(1)
        clear()
        print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mORMOC CITY EVSU PORTAL                    \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│                \x1b[38:5:195mAccount Change \x1b[38:5:196mPassword\x1b[38:5:28m...                  \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m└────────────────────────────────────────────────────────────╯""")
        time.sleep(1)
        clear()
        print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mORMOC CITY EVSU PORTAL                    \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│                \x1b[38:5:195mAccount Change \x1b[38:5:196mPassword\x1b[38:5:28m....                 \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m└────────────────────────────────────────────────────────────╯""")
        time.sleep(1)
        clear()
        print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mORMOC CITY EVSU PORTAL                    \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│                \x1b[38:5:195mAccount Change \x1b[38:5:196mPassword\x1b[38:5:28m.....                \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m└────────────────────────────────────────────────────────────╯""")
        time.sleep(2)
        choice = input("     \x1b[38:5:195mPress Enter to Go Back\x1b[38:5:28m:\x1b[38:5:148m ") 
        clear()

def changeuserdone():
        print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mORMOC CITY EVSU PORTAL                    \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│                \x1b[38:5:195mAccount Change \x1b[38:5:196mUsername\x1b[38:5:28m.                    \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m└────────────────────────────────────────────────────────────╯""")
        time.sleep(1)
        clear()
        print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mORMOC CITY EVSU PORTAL                    \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│                \x1b[38:5:195mAccount Change \x1b[38:5:196mUsername\x1b[38:5:28m..                   \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m└────────────────────────────────────────────────────────────╯""")
        time.sleep(1)
        clear()
        print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mORMOC CITY EVSU PORTAL                    \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│                \x1b[38:5:195mAccount Change \x1b[38:5:196mUsername\x1b[38:5:28m...                  \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m└────────────────────────────────────────────────────────────╯""")
        time.sleep(1)
        clear()
        print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mORMOC CITY EVSU PORTAL                    \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│                \x1b[38:5:195mAccount Change \x1b[38:5:196mUsername\x1b[38:5:28m....                 \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m└────────────────────────────────────────────────────────────╯""")
        time.sleep(1)
        clear()
        print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mORMOC CITY EVSU PORTAL                    \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│                \x1b[38:5:195mAccount Change \x1b[38:5:196mUsername\x1b[38:5:28m.....                \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m└────────────────────────────────────────────────────────────╯""")
        time.sleep(2)
        choice = input("     \x1b[38:5:195mPress Enter to Go Back\x1b[38:5:28m:\x1b[38:5:148m ") 
        clear()

def changeuser():
    global user
    print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mORMOC CITY EVSU PORTAL                    \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│                \x1b[38:5:195mAccount Change \x1b[38:5:196mUsername                     \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m├────────────────────────────────────────────────────────────╯""")
    olduser = input("    \x1b[38:5:74m├───\x1b[38:5:148m>\x1b[38:5:195m Current Username\x1b[38:5:28m:\x1b[38:5:148m ")
    print("    \x1b[38:5:74m│")
    if olduser == user:
        newuser = input("    \x1b[38:5:74m├───\x1b[38:5:148m>\x1b[38:5:195m New Username\x1b[38:5:28m:\x1b[38:5:148m ")
        print("    \x1b[38:5:74m│")
        newuser1 = input("    \x1b[38:5:74m╰───\x1b[38:5:148m>\x1b[38:5:195m Confirm New Username\x1b[38:5:28m:\x1b[38:5:148m ")
    if newuser == newuser1:
        user = newuser1
        clear()
        changeuserdone()

def changepass():
    global passw
    print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mORMOC CITY EVSU PORTAL                    \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│                \x1b[38:5:195mAccount Change \x1b[38:5:196mPassword                     \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m├────────────────────────────────────────────────────────────╯""")
    oldpass = input("    \x1b[38:5:74m├───\x1b[38:5:148m>\x1b[38:5:195m Current Password\x1b[38:5:148m:\x1b[38:5:148m ")
    print("    \x1b[38:5:74m│")
    if oldpass == passw:
        newpass = getpass.getpass("    \x1b[38:5:74m├───\x1b[38:5:148m>\x1b[38:5:195m New Password\x1b[38:5:28m:\x1b[38:5:148m ")
        print("    \x1b[38:5:74m│")
        newpass1 = getpass.getpass("    \x1b[38:5:74m╰───\x1b[38:5:148m>\x1b[38:5:195m Confirm New Password\x1b[38:5:28m:\x1b[38:5:148m ")
    if newpass == newpass1:
        passw = newpass1
        clear()
        changepassdone()

def username():
        global user, passw
        print(f"""
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mMY ACCOUNT EVSU PORTAL                    \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│  \x1b[38:5:195mUsername\x1b[38:5:28m: \x1b[38:5:148m{user}                           
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│  \x1b[38:5:195mPassword\x1b[38:5:28m: \x1b[38:5:148m{passw}                          
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m└────────────────────────────────────────────────────────────╯""")
        choice = input("     \x1b[38:5:195mPress Enter to Go Back\x1b[38:5:28m:\x1b[38:5:148m ")
        clear()
def start():
    clear()
    secret = "KRSXG4TCA5KQ6D2E"
    totp = pyotp.TOTP(secret)
    
    otp = input("OTP from Google Authenticator: ")
    if totp.verify(otp):
        print("\x1b[38;2;0;255;58mWelcome to Evsu Portal")
        time.sleep(3)
        clear()
        main()
    else:
        print("Invalid OTP!!")
        quit(1)

def main():
    print("""
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mORMOC CITY EVSU PORTAL                    \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│                 \x1b[38:5:148m1\x1b[38:5:28m. \x1b[38:5:74m\x1b[38:5:195mLog in                                  \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            \x1b[38:5:74m│
    \x1b[38:5:74m│                 \x1b[38:5:148m2\x1b[38:5:28m. \x1b[38:5:195mSign Up                                 \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            \x1b[38:5:74m│
    \x1b[38:5:74m│                 \x1b[38:5:148m3\x1b[38:5:28m. \x1b[38:5:195mMy Account                              \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            \x1b[38:5:74m│
    \x1b[38:5:74m│                 \x1b[38:5:148m4\x1b[38:5:28m. \x1b[38:5:195mChange Username                         \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            \x1b[38:5:74m│
    \x1b[38:5:74m│                 \x1b[38:5:148m5\x1b[38:5:28m. \x1b[38:5:195mChange Password                         \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            \x1b[38:5:74m│
    \x1b[38:5:74m│                 \x1b[38:5:148m0\x1b[38:5:28m. \x1b[38:5:195mExit                                    \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m├────────────────────────────────────────────────────────────╯""")
    choice = int(input("    \x1b[38:5:74m╰───\x1b[38:5:148m>\x1b[38:5:195m Choice:\x1b[38:5:148m "))
    clear()

    if choice == 1:
        login()
    elif choice == 2:
        signup()
    elif choice == 3:
        username()
    elif choice == 4:
        changeuser()
    elif choice == 5:
        changepass()
    elif choice == 0:
        print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mORMOC CITY EVSU PORTAL                    \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│         \x1b[38:5:195mThank you for using the \x1b[38:5:196mEVSU \x1b[38:5:195mStudent \x1b[38:5:196mPortal        \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m└────────────────────────────────────────────────────────────╯""")
        quit()

while True:
    start()
    main()
