import requests,random
import urllib.request, json
already_registered=True
user_in=False
user=""
userid=""
password=""
log=input("Register or Login")
if(log.lower()=="register"):
    user = input("Enter Teachername")
    userid = input("Enter TeacherId")
    password = input("Enter password")
    d={}
    with urllib.request.urlopen("https://melvinmathew0102.000webhostapp.com/TeacherRegister.php") as url:
        data = json.loads(url.read().decode())
        for x in data['Details']:
            if(userid==x['T_ID']):
                print("T_Id already Registered")
                user_in=False
                already_registered=True
                break
            else:
                already_registered=False
        if(already_registered==False):
            print("Successfully Registered")
            user_in=True
            values = {'UserID': userid, 'password': password, 'UserName': user}
            requests.post("https://melvinmathew0102.000webhostapp.com/teacher.php", values)
elif(log.lower()=="login"):
    user=""
    userid = input("Enter T_Id")
    password = input("Enter password")
    with urllib.request.urlopen("https://melvinmathew0102.000webhostapp.com/TeacherRegister.php") as url:
        data = json.loads(url.read().decode())
        for x in data['Details']:
            if(userid==x['T_ID'] and password==x['T_Password']):
                user=x['T_Name']
                print("Successfully Loged IN")
                user_in=True
                already_registered=True
                break
            else:
                already_registered=False
        if(already_registered==False):
            print("Login UnSuccessfull")
            user_in = False
while(True):
    if(user_in):
        print("Hi ",user)
        d=[]
        ans=input("Answer Specific,Verify")
        if(ans.lower()=='verify'):
            data = ""
            print("Available Questions")
            answered = True
            with urllib.request.urlopen("https://melvinmathew0102.000webhostapp.com/Teacher_ans.php") as url:
                data = json.loads(url.read().decode())
                for x in data['Questions']:
                    print("Student_ID =", x['UserID'], ",", x['Username'] + " Asked " + x['Ask_global'])
                    print("\t", x['ans_by'], " answered ", x['ans'])
                    d.append({x['ans_by']:x['ans']})
                    if (x['ans_by'] != 'None'):
                        print("\t", "Verified :", x['verified'])
                        answered = True
                    else:
                        answered = False

            uid = input("Enter Student_id")
            q = input("Enter Question to be verified")
            answer_id=input("Enter Id of Answered Student")
            answer=input("Enter answer")
            rew = input("Rejected or approved")
            question = q.strip()
            values = {'UserID': uid, 'ans_by': answer_id, 'ans': answer, 'verified': rew, 'question': q}
            data = requests.post("https://melvinmathew0102.000webhostapp.com/ans_group.php", values)
            if (data):
                print("Entered Successfully")
            else:
                print("Network Error")
            if(rew=='yes'):
                reward = [5, 10, 15, 20]
                ran_reward = random.choice(reward)
                values = {'userid': answer_id,'reward':ran_reward}
                data = requests.post("https://melvinmathew0102.000webhostapp.com/reward.php", values)
                if (data):
                    print("Rewarded Successfully")
                else:
                    print("Network Error")
            elif(rew=='no'):
                values = {'UserID': uid, 'ans_by': 'None', 'ans': '', 'verified': 'NO', 'question': q}
                data = requests.post("https://melvinmathew0102.000webhostapp.com/ans_group.php", values)
        elif(ans.lower()=='answer'):
            with urllib.request.urlopen("https://melvinmathew0102.000webhostapp.com/teacher_question_display.php")as url:
                data=json.loads(url.read().decode())
                counter=0
                for a in data['details']:
                    if(userid==a['T_ID']):
                        counter+=1
                        print("Student id:",a['Stud_ID']," asked",a['Question'])
                        if(a['Ans_Specific']!=''):
                            print("You answered: ",a['Ans_Specific'])
                    if(counter==0):
                        print("NO STUDENT ASKED ANY QUESTION")
                        break
            answered=False
            uid = input("Enter Student_id whose question has to be answered")
            q = input("Enter Question to be answered")
            with urllib.request.urlopen("https://melvinmathew0102.000webhostapp.com/teacher_question_display.php") as url:
                data = json.loads(url.read().decode())
                for x in data['details']:
                    if (x['Ans_Specific'] != '' and x['Question'] == q and x['Stud_ID'] == uid):
                        answered = True
                        break
                    else:
                        answered = False
            if (answered == False):
                question = q.strip()
                ans = input("Enter answer")
                submt = input("Post?")
                if (submt.lower() == 'yes'):
                    values = {'Stud_id': uid, 'ans_specific': ans, 'spec_id': userid, 'verified': 'Yes', 'Question': q}
                    data = requests.post("https://melvinmathew0102.000webhostapp.com/Teacher_ans_specific.php", values)
                    if (data):
                        print("Entered Successfully")
                    else:
                        print("Network Error")
            else:
                print("Already answered")
