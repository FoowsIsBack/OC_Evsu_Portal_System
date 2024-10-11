#dave.py
#RED (Title) = \x1b[38:5:196m
#Yellow = \x1b[38:5:148m
#Cyan (Text) = \x1b[38:5:195m
#Sky Blue (Bg Color) = \x1b[38:5:74m
#Green = \x1b[38:5:28m

import os
import time
import getpass

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
    \x1b[38:5:74m│           \x1b[38:5:195mPlease wait a minute Loading Screen\x1b[38:5:28m....           \x1b[38:5:74m│
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
    \x1b[38:5:74m╰────────────────────────────────────────────────────────────╯""")
    user1 = input("    \x1b[38:5:195mUsername\x1b[38:5:28m:\x1b[38:5:148m ")
    passw1 = getpass.getpass("    \x1b[38:5:195mPassword\x1b[38:5:28m:\x1b[38:5:148m ")
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
        choice = input("    \x1b[38:5:195mPress Enter to Go Back\x1b[38:5:28m:\x1b[38:5:148m ")
        clear()
        login()

def portal():
    print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                 \x1b[38:5:196mWELCOME TO EVSU STUDENT PORTAL             \x1b[38:5:74m|
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│                     \x1b[38:5:148m1\x1b[38:5:28m. \x1b[38:5:195mQuiz                                \x1b[38:5:74m│
    \x1b[38:5:74m│                     \x1b[38:5:148m2\x1b[38:5:28m. \x1b[38:5:195mView Score                          \x1b[38:5:74m│
    \x1b[38:5:74m│                     \x1b[38:5:148m3\x1b[38:5:28m. \x1b[38:5:195mDataBase                            \x1b[38:5:74m│
    \x1b[38:5:74m│                     \x1b[38:5:148m0\x1b[38:5:28m. \x1b[38:5:195mExit                                \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m╰────────────────────────────────────────────────────────────╯""")
    choice = int(input("    x1b[38:5:195mChoice\x1b[38:5:28m:\x1b[38:5:148m "))
    clear()

    if choice == 1:
        tools()
    elif choice == 2:
        viewscore()
    elif choice == 3:
        databasemain()
    elif choice == 0:
        main()

question = {
        "    |  1. Who developed Python programming language?: ": "guido van rossum",
        "    |  2. Who developed in HTML?: ": "tim berners lee",
        "    |  3. Who developed C programming language?: ": "rennis ritchie",
        "    |  4. Who developed C++ programming language?: ": "bjarne stroustrup",
        "    |  5. Who developed in javascript?: ": "brendan eich"
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
    \x1b[38:5:74m│                   \x1b[38:5:196mQUIZ EVSU PORTAL                         \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│                \x1b[38:5:148m1\x1b[38:5:28m. \x1b[38:5:195mQuestion and Answer                      \x1b[38:5:74m│
    \x1b[38:5:74m│                \x1b[38:5:148m0\x1b[38:5:28m. \x1b[38:5:195mExit                                     \x1b[38:5:74m│
    \x1b[38:5:74m╰────────────────────────────────────────────────────────────╯""")
    choice = int(input("    \x1b[38:5:195mChoice\x1b[38:5:28m\x1b[38:5:28m: "))
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
    choice = input("    \x1b[38:5:195mPress Enter to Go Back\x1b[38:5:28m:\x1b[38:5:148m ")
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
    \x1b[38:5:74m│          \x1b[38:5:148m1\x1b[38:5:28m. \x1b[38:5:195mBS in Information Technology (BSIT)            \x1b[38:5:74m│
    \x1b[38:5:74m│          \x1b[38:5:148m2\x1b[38:5:28m. \x1b[38:5:195mBS in Civil Engineering (BSCE)                 \x1b[38:5:74m│
    \x1b[38:5:74m│          \x1b[38:5:148m3\x1b[38:5:28m. \x1b[38:5:195mBS in Mechanical Engineering (BSME)            \x1b[38:5:74m│
    \x1b[38:5:74m│          \x1b[38:5:148m4\x1b[38:5:28m. \x1b[38:5:195mBS in Industrial Technology (Culinary Arts)    \x1b[38:5:74m│
    \x1b[38:5:74m│          \x1b[38:5:148m5\x1b[38:5:28m. \x1b[38:5:195mBS in Industrial Technology (Electronics)      \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m╰────────────────────────────────────────────────────────────╯""")
    name1 = input("     Full Name: ")
    age1 = input("     Age: ")
    address = input("     Address: ")
    email = input("     Email: ")
    course_choice = int(input("     Course (1-5): "))
    course = course[course_choice - 1]
    clear()
    qa()

def databasemain():
    print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                   \x1b[38:5:196mEVSU STUDENT DATABASE                    \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤   
    \x1b[38:5:74m│                                                            │
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
    \x1b[38:5:74m╰────────────────────────────────────────────────────────────╯""")
    user = input("    \x1b[38:5:195mUsername\x1b[38:5:28m:\x1b[38:5:148m ")
    passw = getpass.getpass("    \x1b[38:5:195mPassword\x1b[38:5:28m:\x1b[38:5:148m ")
    clear()
    registerdone()

def registerdone():
        print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mORMOC CITY EVSU PORTAL                    \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│                    \x1b[38:5:148mAccount Registered\x1b[38:5:28m.                     \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m╰────────────────────────────────────────────────────────────╯""")
        time.sleep(1)
        clear()
        print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mORMOC CITY EVSU PORTAL                    \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│                    \x1b[38:5:148mAccount Registered\x1b[38:5:28m..                    \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m╰────────────────────────────────────────────────────────────╯""")
        time.sleep(1)
        clear()
        print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mORMOC CITY EVSU PORTAL                    \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│                    \x1b[38:5:148mAccount Registered\x1b[38:5:28m...                   \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m╰────────────────────────────────────────────────────────────╯""")
        time.sleep(1)
        clear()
        print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mORMOC CITY EVSU PORTAL                    \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│                    \x1b[38:5:148mAccount Registered\x1b[38:5:28m....                  \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m╰────────────────────────────────────────────────────────────╯""")
        time.sleep(1)
        clear()
        print(""" 
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mORMOC CITY EVSU PORTAL                    \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│                    \x1b[38:5:148mAccount Registered\x1b[38:5:28m.....                 \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m╰────────────────────────────────────────────────────────────╯""")
        time.sleep(3)
        choice = input("    \x1b[38:5:195mPress Enter to Go Back\x1b[38:5:28m:\x1b[38:5:148m ") 
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
        choice = input("    \x1b[38:5:195mPress Enter to Go Back\x1b[38:5:28m:\x1b[38:5:148m ") 
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
        choice = input("    \x1b[38:5:195mPress Enter to Go Back\x1b[38:5:28m:\x1b[38:5:148m ") 
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
    \x1b[38:5:74m└────────────────────────────────────────────────────────────╯""")
    olduser = input("    \x1b[38:5:195mCurrent Username\x1b[38:5:28m:\x1b[38:5:148m ")
    if olduser == user:
        newuser = input("    \x1b[38:5:195mNew Username\x1b[38:5:28m:\x1b[38:5:148m ")
        newuser1 = input("    \x1b[38:5:195mConfirm New Username\x1b[38:5:28m:\x1b[38:5:148m ")
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
    \x1b[38:5:74m└────────────────────────────────────────────────────────────╯""")
    oldpass = input("    \x1b[38:5:195mCurrent Password\x1b[38:5:148m:\x1b[38:5:148m ")
    if oldpass == passw:
        newpass = getpass.getpass("    \x1b[38:5:195mNew Password\x1b[38:5:28m:\x1b[38:5:148m ")
        newpass1 = getpass.getpass("    \x1b[38:5:195mConfirm New Password\x1b[38:5:28m:\x1b[38:5:148m ")
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
    \x1b[38:5:74m│                    \x1b[38:5:195mUsername\x1b[38:5:28m: \x1b[38:5:148m{user}                           
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│                    \x1b[38:5:195mPassword\x1b[38:5:28m: \x1b[38:5:148m{passw}                          
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m└────────────────────────────────────────────────────────────╯""")
        choice = input("    \x1b[38:5:195mPress Enter to Go Back\x1b[38:5:28m:\x1b[38:5:148m ")
        clear()

def main():
    print("""
    \x1b[38:5:74m╭────────────────────────────────────────────────────────────╮
    \x1b[38:5:74m│                  \x1b[38:5:196mORMOC CITY EVSU PORTAL                    \x1b[38:5:74m│
    \x1b[38:5:74m├────────────────────────────────────────────────────────────┤
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m│                 \x1b[38:5:148m1\x1b[38:5:28m. \x1b[38:5:74m\x1b[38:5:195mLog in                                  \x1b[38:5:74m│
    \x1b[38:5:74m│                 \x1b[38:5:148m2\x1b[38:5:28m. \x1b[38:5:195mSign Up                                 \x1b[38:5:74m│
    \x1b[38:5:74m│                 \x1b[38:5:148m3\x1b[38:5:28m. \x1b[38:5:195mMy Account                              \x1b[38:5:74m│
    \x1b[38:5:74m│                 \x1b[38:5:148m4\x1b[38:5:28m. \x1b[38:5:195mChange Username                         \x1b[38:5:74m│
    \x1b[38:5:74m│                 \x1b[38:5:148m5\x1b[38:5:28m. \x1b[38:5:195mChange Password                         \x1b[38:5:74m│
    \x1b[38:5:74m│                 \x1b[38:5:148m0\x1b[38:5:28m. \x1b[38:5:195mExit                                    \x1b[38:5:74m│
    \x1b[38:5:74m│                                                            │
    \x1b[38:5:74m└────────────────────────────────────────────────────────────╯""")
    choice = int(input("    \x1b[38:5:195mChoice\x1b[38:5:28m:\x1b[38:5:148m "))
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
    main()