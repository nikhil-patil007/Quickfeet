from rest_framework import status
# from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import *
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.hashers  import make_password,check_password
from time import gmtime, strftime
from datetime import date
import datetime 

import re
import math,random
email_pattern = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 
# mobile_pattern = '^[0-9]{10}$'

def genrateOtp():
    digits = '0123456789'
    OTP = ''
    for i in range(4):
        OTP += digits[math.floor(random.random()*10)]
    return OTP

# @api_view(['POST'])
# def Sign_Up_Player(request):
#     data = request.data
#     showtime = strftime("%Y-%m-%d %H:%M", )
#     via = data['via']
#     if (not via):
#         return Response({"status": 0 , 'msg' : "Please Add Data Type"})
    
#     if via == "Gmail":
#         email = data['email'].casefold()
#         email = email.replace(" ", "")
#         password = data['password']
#         cpassword = data['cpassword']
        
#         if (not email):
#             return Response({"status" : 0,"msg" : "Email Can't be Empty.!"})
#         if (not password):
#             return Response({"status" : 0,"msg" : "Password Can't be Empty.!"})
#         if (not cpassword):
#             return Response({"status" : 0,"msg" : "Confirm Password Can't be Empty.!"})
        
#         if(re.search(email_pattern, email)):
#             chec = Game_user.objects.filter(Email = email,Is_active = '1')
#             if len(chec) > 0:
#                 return Response({"status" : 0,"msg" : f"Email Is Alread Used with {chec[0].Via}"})
#             else:
#                 if password != cpassword:
#                     return Response({'status' : 0 , 'msg' : "Password Doesn't Match.!"})
#                 else:
#                     password = make_password(password)
#                     adduser = Game_user.objects.create(
#                         Via = via,
#                         Email = email,
#                         slug = email,
#                         Password = password,
#                         Password2 = password,
#                         Create_at = showtime,
#                         Update_at = showtime,
#                     )
#                     # if adduser.Gender == '0':
#                     #         Gender = ''
#                     # else:
#                     #     Gender = adduser.Gender
#                     data = {
#                         "id": adduser.id,
#                         "via": adduser.Via,
#                         "Full_Name": adduser.Full_name if adduser.Full_name else '',
#                         "Player_Name": adduser.Game_name if adduser.Game_name else '',
#                         "Email": adduser.Email if adduser.Email else '',
#                         # "Gender": Gender,
#                         "Shirt_num": adduser.Shirt_num if adduser.Shirt_num else '',
#                         "DOB": adduser.age if adduser.age else '',
#                         "Country": adduser.Country if adduser.Country else ''
#                     }
#                     addpas = Password_store.objects.create(
#                         GetPlayer = adduser,
#                         Password = adduser.Password,
#                         Password2 = adduser.Password2,
#                         Create_at = adduser.Create_at,
#                     )
#                     return Response({"status" : 1,"msg" : "User Register Successfully",'data':data})
#         else:
#             return Response({"status" : 0,"msg" : "Enter Valid Email."})
    
#     elif via == "Google":
#         email = data['email'].casefold()
#         server_id = data['server_id']
#         Full_name = data['Full_name']
#         chec = Game_user.objects.filter(Email = email,google_Id = server_id,Is_active = '1')
#         if len(chec) > 0:
#             # data = {
#             #     "id": chec[0].id,
#             #     "Full_Name": chec[0].Full_name if chec[0].Full_name else '',
#             #     "Player_Name": chec[0].Game_name if chec[0].Game_name else '',
#             #     "Email": chec[0].Email if chec[0].Email else '',
#             #     # "Gender": Gender,
#             #     "Shirt_num": chec[0].Shirt_num if chec[0].Shirt_num else '',
#             #     "DOB": chec[0].age if chec[0].age else '',
#             #     "Country": chec[0].Country if chec[0].Country else ''
#             # }
#             return Response({"status": 0 , 'msg' : f"Email Is Already Used with {chec[0].Via}"})
#             # return Response({"status" : 1,"msg" : "User Register Successfully",'data':data})
#         else:
#             adduser = Game_user.objects.create(
#                 Via = via,
#                 Email = email,
#                 slug = email,
#                 Full_name = Full_name,
#                 google_Id = server_id,
#                 Create_at = showtime,
#                 Update_at = showtime,
#             )
#             data = {
#                 "id": adduser.id,
#                 "via": adduser.Via,
#                 "Full_Name": adduser.Full_name if adduser.Full_name else '',
#                 "Player_Name": adduser.Game_name if adduser.Game_name else '',
#                 "Email": adduser.Email if adduser.Email else '',
#                 # "Gender": Gender,
#                 "Shirt_num": adduser.Shirt_num if adduser.Shirt_num else '',
#                 "DOB": adduser.age if adduser.age else '',
#                 "Country": adduser.Country if adduser.Country else ''
#             }
#             return Response({"status" : 1,"msg" : "User Register Successfully",'data':data})
    
#     elif via == "Facebook":
#         return Response({"status": 1 , 'msg' : "Facebook Type Data Send"})
    
#     else:
#         return Response({"status": 0 , 'msg' : "Method Is Wrong"})

@api_view(['POST'])
def Sign_Up_Player(request):
    data = request.data
    showtime = strftime("%Y-%m-%d %H:%M")
    via = data['via']
    email = data['email'].casefold()
    email = email.replace(" ", "")
    password = data['password']
    cpassword = data['cpassword']
    # For Google
    server_id = data['server_id']
    Full_name = data['Full_name']

    if (not via):
        return Response({"status": 0 , 'msg' : "Please Add Data Type"})

    if via == "Gmail":
        if (not email):
            return Response({"status" : 0,"msg" : "Email Can't be Empty.!"})
        if (not password):
            return Response({"status" : 0,"msg" : "Password Can't be Empty.!"})
        if (not cpassword):
            return Response({"status" : 0,"msg" : "Confirm Password Can't be Empty.!"})
        
        if (not (re.search(email_pattern, email))):
            return Response({"status" : 0,"msg" : "Enter Valid Email."})
        
    if via == "Google":
        if (not email):
            return Response({"status" : 0,"msg" : "Email Can't be Empty.!"})
    
        if (not (re.search(email_pattern, email))):
            return Response({"status" : 0,"msg" : "Enter Valid Email."})
        
    chec = Game_user.objects.filter(Email = email,Is_active = '1')
    if len(chec) > 0:
        return Response({"status" : 0,"msg" : f"Email Is Alread Used with {chec[0].Via}"})
    else:
        if password != cpassword:
            return Response({'status' : 0 , 'msg' : "Password Doesn't Match.!"})
        else:
            if via == "Gmail":
                password = make_password(password)
                adduser = Game_user.objects.create(
                    Via = via,
                    Email = email,
                    slug = email,
                    Password = password,
                    Password2 = password,
                    Create_at = showtime,
                    Update_at = showtime,
                )
                data = {
                    "id": adduser.id,
                    "via": adduser.Via,
                    "Full_Name": adduser.Full_name if adduser.Full_name else '',
                    "Player_Name": adduser.Game_name if adduser.Game_name else '',
                    "Email": adduser.Email if adduser.Email else '',
                    "Shirt_num": adduser.Shirt_num if adduser.Shirt_num else '',
                    "DOB": adduser.age if adduser.age else '',
                    "Country": adduser.Country if adduser.Country else ''
                }
                addpas = Password_store.objects.create(
                    GetPlayer = adduser,
                    Password = adduser.Password,
                    Password2 = adduser.Password2,
                    Create_at = adduser.Create_at,
                )
                return Response({"status" : 1,"msg" : "User Register Successfully",'data':data})
    
            if via == "Google":
                adduser = Game_user.objects.create(
                    Via = via,
                    Email = email,
                    slug = email,
                    Full_name = Full_name,
                    google_Id = server_id,
                    Create_at = showtime,
                    Update_at = showtime,
                )
                data = {
                    "id": adduser.id,
                    "via": adduser.Via,
                    "Full_Name": adduser.Full_name if adduser.Full_name else '',
                    "Player_Name": adduser.Game_name if adduser.Game_name else '',
                    "Email": adduser.Email if adduser.Email else '',
                    "Shirt_num": adduser.Shirt_num if adduser.Shirt_num else '',
                    "DOB": adduser.age if adduser.age else '',
                    "Country": adduser.Country if adduser.Country else ''
                }
                return Response({"status" : 1,"msg" : "User Register Successfully",'data':data})

@api_view(['GET'])
def User_Is_active(request,id):
    try:
        chec = Game_user.objects.get(id=id)
        if chec.Is_active == '1':
            return Response({'status' : 1,'msg' : "User Is Active"})
        if chec.Is_active == '0':
            return Response({'status' : 0,'msg' : "User Is Inactive"})
    except:
        return Response({'status' : 0,'msg' : "Id Not Found"})

# @api_view(['POST'])
# def Login_Player(request):
#     data = request.data
#     via = data['via']
#     if (not via):
#         return Response({"status": 0 , 'msg' : "Please Add Data Type"})
#     if via == "Gmail":
#         email = data['email'].casefold()
#         email = email.replace(" ", "")
#         password = data['password']
       
#         if (not email):
#             return Response({"status": 0 , 'msg' : "Please Enter Email"})
#         if (not password):
#             return Response({"status": 0 , 'msg' : "Please Enter Password"})
       
#         if(re.search(email_pattern, email)):
#             chec = Game_user.objects.filter(Via = via,Email = email)
#             if len(chec) > 0:
#                 if chec[0].Is_active == '1':
#                     ps = check_password(password, chec[0].Password)
#                     if ps:
#                         data = {
#                             "id": chec[0].id,
#                             "via": chec[0].Via,
#                             "Full_Name": chec[0].Full_name if chec[0].Full_name else '',
#                             "Player_Name": chec[0].Game_name if chec[0].Game_name else '',
#                             "Email": chec[0].Email if chec[0].Email else '',
#                             "Shirt_num": chec[0].Shirt_num if chec[0].Shirt_num else '',
#                             "DOB": chec[0].age if chec[0].age else '',
#                             "Country": chec[0].Country if chec[0].Country else ''
#                         }
#                         return Response({"status" : 1,"msg" : "Login Successfully","data": data})
#                     elif password == chec[0].Password:
#                         chec[0].Password = make_password(password)
#                         chec[0].Password1 = password
#                         chec[0].save()
#                         data = {
#                             "id": chec[0].id,
#                             "via": chec[0].Via,
#                             "Full_Name": chec[0].Full_name if chec[0].Full_name else '',
#                             "Player_Name": chec[0].Game_name if chec[0].Game_name else '',
#                             "Email": chec[0].Email if chec[0].Email else '',
#                             "Shirt_num": chec[0].Shirt_num if chec[0].Shirt_num else '',
#                             "DOB": chec[0].age if chec[0].age else '',
#                             "Country": chec[0].Countr if chec[0].Countr else ''
#                         }
#                         return Response({"status" : 1,"msg" : "Login Successfully","data": data})
#                     else:
#                         return Response({"status" : 0,"msg" : "Password is Wrong"})
#                 else:
#                     return Response({"status" : 0,"msg" : "User's Account Is Not Found"})
#             else:
#                 chec1 = Game_user.objects.filter(Email = email)
#                 if len(chec1) > 0:
#                     return Response({"status" : 0,"msg" : f"Email Is Alread Used with {chec1[0].Via}"})
#                 else:
#                     return Response({"status" : 0,"msg" : "User's Account Is Not Found"})
#         else:
#             return Response({"status": 0 , 'msg' : "Enter Valid Email."})
    
#     elif via == "Google":
#         email = data['email'].casefold()
#         server_id = data['server_id']
#         Full_name = data['Full_name']
#         chec = Game_user.objects.filter(Via = via,Email = email,google_Id = server_id,Is_active = '1')
#         if len(chec) > 0:
#             data = {
#                 "id": chec[0].id,
#                 "via": chec[0].Via,
#                 "Full_Name": chec[0].Full_name if chec[0].Full_name else '',
#                 "Player_Name": chec[0].Game_name if chec[0].Game_name else '',
#                 "Email": chec[0].Email if chec[0].Email else '',
#                 # "Gender": Gender,
#                 "Shirt_num": chec[0].Shirt_num if chec[0].Shirt_num else '',
#                 "DOB": chec[0].age if chec[0].age else '',
#                 "Country": chec[0].Country if chec[0].Country else ''
#             }
#             return Response({"status" : 1,"msg" : "Login Successfully",'data':data})
#         else:
#             chec1 = Game_user.objects.filter(Email = email)
#             if len(chec1) > 0:
#                 return Response({"status" : 0,"msg" : f"Email Is Alread Used with {chec1[0].Via}"})
#             else:
#                 return Response({"status" : 0,"msg" : "User's Account Is Not Found"})
    
#     elif via == "Facebook":
#         return Response({"status": 1 , 'msg' : "Facebook Type Data Send"})
    
#     else:
#         return Response({"status": 0 , 'msg' : "Method Is Wrong"})

@api_view(['POST'])
def Login_Player(request):
    data = request.data
    via = data['via']
    email = data['email'].casefold()
    email = email.replace(" ", "")
    password = data['password']
    server_id = data['server_id']
    Full_name = data['Full_name']
    
    if (not via):
        return Response({"status": 0 , 'msg' : "Please Add Data Type"})
    
    if via == "Gmail":
        if (not email):
            return Response({"status": 0 , 'msg' : "Please Enter Email"})
        if (not password):
            return Response({"status": 0 , 'msg' : "Please Enter Password"})
        if(not (re.search(email_pattern, email))):
            return Response({"status": 0 , 'msg' : "Enter Valid Email."})

    if via == "Google":  
        if (not email):
            return Response({"status": 0 , 'msg' : "Please Enter Email"})
        if(not (re.search(email_pattern, email))):
            return Response({"status": 0 , 'msg' : "Enter Valid Email."})
            
    chec1 = Game_user.objects.filter(Email = email,Is_active = '1')
    if len(chec1) > 0:
        if via == "Gmail":
            chec = Game_user.objects.filter(Via = via,Email = email,Is_active = '1')
            if len(chec) > 0:
                ps = check_password(password, chec[0].Password)
                if ps:
                    data = {
                        "id": chec[0].id,
                        "via": chec[0].Via,
                        "Full_Name": chec[0].Full_name if chec[0].Full_name else '',
                        "Player_Name": chec[0].Game_name if chec[0].Game_name else '',
                        "Email": chec[0].Email if chec[0].Email else '',
                        "Shirt_num": chec[0].Shirt_num if chec[0].Shirt_num else '',
                        "DOB": chec[0].age if chec[0].age else '',
                        "Country": chec[0].Country if chec[0].Country else ''
                    }
                    return Response({"status" : 1,"msg" : "Login Successfully","data": data})
                elif password == chec[0].Password:
                    chec[0].Password = make_password(password)
                    chec[0].Password1 = password
                    chec[0].save()
                    data = {
                        "id": chec[0].id,
                        "via": chec[0].Via,
                        "Full_Name": chec[0].Full_name if chec[0].Full_name else '',
                        "Player_Name": chec[0].Game_name if chec[0].Game_name else '',
                        "Email": chec[0].Email if chec[0].Email else '',
                        "Shirt_num": chec[0].Shirt_num if chec[0].Shirt_num else '',
                        "DOB": chec[0].age if chec[0].age else '',
                        "Country": chec[0].Countr if chec[0].Countr else ''
                    }
                    return Response({"status" : 1,"msg" : "Login Successfully","data": data})
                else:
                    return Response({"status" : 0,"msg" : "Password is Wrong"})
            else:
                chec = Game_user.objects.filter(Email = email,Is_active = '1')
                return Response({"status": 0 , 'msg' : f"Please Login With {chec[0].Via}"})
        elif via == "Google":
            chec = Game_user.objects.filter(Via = via,Email = email,google_Id = server_id,Is_active = '1')
            if len(chec) > 0:
                data = {
                    "id": chec[0].id,
                    "via": chec[0].Via,
                    "Full_Name": chec[0].Full_name if chec[0].Full_name else '',
                    "Player_Name": chec[0].Game_name if chec[0].Game_name else '',
                    "Email": chec[0].Email if chec[0].Email else '',
                    # "Gender": Gender,
                    "Shirt_num": chec[0].Shirt_num if chec[0].Shirt_num else '',
                    "DOB": chec[0].age if chec[0].age else '',
                    "Country": chec[0].Country if chec[0].Country else ''
                }
                return Response({"status" : 1,"msg" : "Login Successfully",'data':data})
            else:
                chec = Game_user.objects.filter(Email = email,Is_active = '1')
                return Response({"status": 0 , 'msg' : f"Please Login With {chec[0].Via}"})
        else:
            return Response({"status" : 0,"msg" : f"Email Is Alread Used with {chec1[0].Via}"})
    else:
        return Response({"status": 0 , 'msg' : "User's Account Is Not Found"})

@api_view(['GET'])
def Profile_view(request,id):
    try:
        chec = Game_user.objects.get(id=id)
        return Response({
            "status" : 1,
            'msg' : "User Profile View successfully",
            "id": chec.id,
            "via": chec.Via,
            "Full_Name": chec.Full_name if chec.Full_name else '',
            "Player_Name": chec.Game_name if chec.Game_name else '',
            "Email": chec.Email if chec.Email else '',
            "Shirt_num": chec.Shirt_num if chec.Shirt_num else '',
            "DOB": chec.DOB if chec.DOB else '',
            "Country": chec.Country if chec.Country else '',
        })
    except:
        return Response({'status' : 0,'msg' : "Id Not Found"})

@api_view(['POST'])
def Edit_Profile(request,id):
    try:
        data = request.data
        showtime = strftime("%Y-%m-%d %H:%M", )
        chec = Game_user.objects.get(id=id)
        # via = data['via']
        # if (not via):
        #     return Response({"status": 0 , 'msg' : "Please Add Data Type"})
        # chec.Gender = data['Gender'] if data['Gender'] else chec.Gender
        chec.Full_name = data['Full_Name'] if data['Full_Name'] else chec.Full_name
        chec.Game_name = data['Player_Name'] if data['Player_Name'] else chec.Game_name
        chec.Shirt_num = data['Shirt_num'] if data['Shirt_num'] else chec.Shirt_num
        chec.DOB = data['DOB'] if data['DOB'] else chec.DOB
        if data['DOB']:
            year = int(data['DOB'][:4])
            month = int(data['DOB'][5:7])
            day = int(data['DOB'][8:])
            today = date.today()
            age = today.year - year -((today.month, today.day) < (month, day))
            chec.age = age
        else:
            if len(str(chec.DOB)) == 10:
                year = int(str(chec.DOB)[:4])
                month = int(str(chec.DOB)[5:7])
                day = int(str(chec.DOB)[8:])
                today = date.today()
                age = today.year - year -((today.month, today.day) < (month, day))
                chec.age = age
            else:
                chec.age = "0"
        chec.Country = data['Country'] if data['Country'] else chec.Country
        email = data['email'].casefold()
        if(re.search(email_pattern, email)):
            getmail = Game_user.objects.filter(Email=email,Is_active='1')
            if len(getmail) > 0:
                for i in getmail:
                    if chec.Email == i.Email:
                        chec.Email = chec.Email
                    elif email == i.Email and chec.Email != i.Email:
                        return Response({"status" : "0",'msg': "Email Is Already Used"})
                    else:
                        chec.Email = email
            else:
                chec.Email = email
        else:
            chec.Email = chec.Email
        chec.Update_at = showtime
        chec.slug = chec.Full_name if chec.Full_name else chec.Email
        chec.save()
        return Response({"status": 1 , 'msg' : "User Updated Successfully"})
    except:
        return Response({"status": 0 , 'msg' : "Id Not Found"})

@api_view(['POST'])
def Forgot_Password(request):
    try:
        data = request.data
        email = data['email'].casefold()
        if(re.search(email_pattern, email)):
            chec = Game_user.objects.filter(Email = email,Is_active = '1')
            if len(chec) > 0:
                if chec[0].Via == 'Gmail':
                    digits = '0123456789'
                    OTP = ''
                    for i in range(4):
                        OTP += digits[math.floor(random.random()*len(digits))]
                    chec[0].Otp = '0000'
                    chec[0].save()
                    # mail_subject = 'Forgot Password From Quickfeet'
                    # message = f'Hi {chec[0].Email},\n Set New Password Help Of This Otp \n Your Otp is:- \'{chec[0].Otp}\' \n Thank You' 
                    # email_from = settings.EMAIL_HOST_USER
                    # to_email = [chec[0].Email,]
                    # send_mail(mail_subject, message, email_from, to_email)
                    data = {
                        "id": chec[0].id,
                        "via": chec[0].Via,
                        "Full_Name": chec[0].Full_name,
                        "Player_Name": chec[0].Game_name,
                        "Email": chec[0].Email,
                        "Shirt_num": chec[0].Shirt_num,
                        "DOB": chec[0].age,
                        "Country": chec[0].Country
                    }
                    return Response({"status" : 1,'msg' : "Forgot Password Successfully","data" : data})
                else:
                    return Response({"status" : 0,'msg' : f"Email Is Alread Used with {chec[0].Via}"})
            else:
                return Response({"status" : 0,'msg' : "Email Not Founded"})
        else:
            return Response({"status" : 0,"msg" : "Enter Valid Email."})
    except:
        return Response({"status" : 0,"msg" : "SomeThing Wrong"})

@api_view(['POST'])
def Verify_otp(request):
    try:
        data = request.data
        email = data['email'].casefold()
        otp = data['otp']
        if (not email):
            return Response({'status':0,'msg' : "Please Enter Email"})
        
        if (not otp):
            return Response({'status':0,'msg' : "Please Enter Otp"})
        
        if(re.search(email_pattern, email)):
            chec = Game_user.objects.filter(Via = 'Gmail',Email = email,Is_active = '1')
            if len(chec) > 0:
                if str(otp) == str(chec[0].Otp):
                    # digits = '0123456789'
                    # OTP = ''
                    # for i in range(4):
                    #     OTP += digits[math.floor(random.random()*10)]
                    # chec[0].Otp = OTP
                    # chec[0].save()
                    return Response({"status" : 1,'msg' : "Otp Verified Successfully"})
                else:
                    return Response({"status" : 0,'msg' : "Otp Doesn't Match"})
            else:
                return Response({"status" : 0,'msg' : "Email Not Founded"})
        else:
            return Response({"status" : 0,"msg" : "Enter Valid Email."})
    except:
        return Response({"status" : 0,"msg" : "SomeThing Wrong"})

@api_view(['POST'])
def Forgot_change_password(request):
    # try:
    data = request.data
    showtime = strftime("%Y-%m-%d %H:%M", )
    email = data['email'].casefold()
    password = data['password']
    cpassword = data['cpassword']
    if (not email):
        return Response({'status':0,'msg' : "Please Enter Email"})
    
    if (not password):
        return Response({'status':0,'msg' : "Please Enter Password"})
    
    if (not cpassword):
        return Response({'status':0,'msg' : "Please Enter Cofirm Password"})
    
    if(re.search(email_pattern, email)):
        chec = Game_user.objects.filter(Via = 'Gmail',Email = email,Is_active = '1')
        if len(chec) > 0:
            if cpassword != password:
                return Response({"status" : 0,'msg' : "Password Doesn't Match"})
            else:
                addpas = Password_store.objects.filter(GetPlayer=chec[0].id,Password2=password)
                if len(addpas) > 0:
                    return Response({"status" : 0,'msg' : "You have already used this password"})
                else:  
                    # digits = '0123456789'
                    # OTP = ''
                    # for i in range(4):
                    #     OTP += digits[math.floor(random.random()*10)]
                    # chec[0].Otp = OTP
                    chec[0].Password = make_password(password)
                    chec[0].Password2 = password
                    chec[0].Update_at = showtime
                    chec[0].save()
                    addpas = Password_store.objects.create(
                        GetPlayer = chec[0],
                        Password = make_password(password),
                        Password2 = password,
                        Create_at = showtime,
                    )
                    data = {
                            "id": chec[0].id,
                            "Full_Name": chec[0].Full_name,
                            "Player_Name": chec[0].Game_name,
                            "Email": chec[0].Email,
                            "Shirt_num": chec[0].Shirt_num,
                            "DOB": chec[0].age,
                            "Country": chec[0].Country
                        }
                    return Response({"status" : 1,'msg' : "Password Updated","data":data})
        else:
            return Response({"status" : 0,'msg' : "Email Not Founded"})
    else:
        return Response({"status" : 0,"msg" : "Enter Valid Email."})
    # except:
    #     return Response({"status" : 0,"msg" : "SomeThing Wrong"})

@api_view(['POST'])       
def Add_Game_Player(request):
    try:
        showtime = strftime('%d %B, %Y') + " " + strftime('%I:%M %p')
        data = request.data
        id = data['GetPlayer']
        Full_name = data['Full_name']
        DOB = data['DOB']
        if DOB:
            year = int(DOB[:4])
            month = int(DOB[5:7])
            day = int(DOB[8:])
            today = date.today()
            age1 = today.year - year -((today.month, today.day) < (month, day))
            age = age1
        else:
            age = ''
        Country = data['Country']
        Shirt_num = data['Shirt_num']
        if (not id) or id == '0':
            return Response({"status" : 0,'msg' : "Please Add Id"})
        else:
            getusr = Game_user.objects.get(id=id)
            adpl = Add_Players.objects.create(
                GetPlayer = getusr,
                Create_at = showtime,
                Full_name = Full_name,
                DOB = DOB,
                age = age,
                Country = Country,
                Shirt_num = Shirt_num
            )
            return Response({"status" : 1,'msg' : "Player Add Successfully"})
    except:
        return Response({"status" : 0,'msg' : "Id Not Founded"})

@api_view(['GET'])
def List_Of_Player(request,id):
    try:
        adpl = Add_Players.objects.filter(GetPlayer = id)
        if len(adpl) > 0:
            ls = []
            for i in adpl:
                dic = {}
                dic['id'] = i.id
                dic['Full_name'] = i.Full_name
                dic['DOB'] = i.age
                dic['Country'] = i.Country
                dic['Shirt_num'] = i.Shirt_num
                ls.append(dic)
            return Response({'status':1,'msg':'Players List Show Successfully','data':ls})
        else:
            return Response({'status':0,'msg':'No Record'})
    except:
        return Response({"status" : 0,'msg' : "Id Not Founded"})

@api_view(['POST'])   
def View_Game_Player(request):
    try:
        data = request.data
        id = data['id']
        if (not id) or id == '0':
            return Response({"status" : 0,'msg' : "Please Add Id"})
        else:
            adpl = Add_Players.objects.get(id=id)
            data = {
                'id' : adpl.id,
                'Full_name' : adpl.Full_name if adpl.Full_name else '',
                'DOB' : adpl.DOB if adpl.DOB else '',
                'Country' : adpl.Country if adpl.Country else '',
                'Shirt_num' : adpl.Shirt_num if adpl.Shirt_num else ''
            }
            return Response({"status" : 1,'msg' : "Player Profile View Successfully","data":data})
    except:
        return Response({"status" : 0,'msg' : "Id Not Founded"})

@api_view(['POST'])
def Edit_Game_Player(request):
    try:
        data = request.data
        id = data['id']
        if (not id) or id == '0':
            return Response({"status" : 0,'msg' : "Please Add Id"})
        else:
            adpl = Add_Players.objects.get(id=id)
            adpl.Full_name = data['Full_name'] if data['Full_name'] else adpl.Full_name
            adpl.DOB = data['DOB'] if data['DOB'] else adpl.DOB
            if data['DOB']:
                year = int(data['DOB'][:4])
                month = int(data['DOB'][5:7])
                day = int(data['DOB'][8:])
                today = date.today()
                age1 = today.year - year -((today.month, today.day) < (month, day))
                adpl.age = age1
            else:
                if len(str(adpl.DOB)) == 10:
                    year = int(str(adpl.DOB)[:4])
                    month = int(str(adpl.DOB)[5:7])
                    day = int(str(adpl.DOB)[8:])
                    today = date.today()
                    age = today.year - year -((today.month, today.day) < (month, day))
                    adpl.age = age
                else:
                    use.age = "0"
            adpl.Country = data['Country'] if data['Country'] else adpl.Country
            adpl.Shirt_num = data['Shirt_num'] if data['Shirt_num'] else adpl.Shirt_num
            adpl.save()
            return Response({"status" : 1,'msg' : "Player Update Successfully"})
    except:
        return Response({"status" : 0,'msg' : "Id Not Founded"})

@api_view(['POST'])   
def Delete_Game_Player(request):
    try:
        data = request.data
        id = data['id']
        if (not id) or id == '0':
            return Response({"status" : 0,'msg' : "Please Add Id"})
        else:
            adpl = Add_Players.objects.get(id=id)
            adpl.delete()
            return Response({"status" : 1,'msg' : "Player Delete successfully."})
    except:
        return Response({"status" : 0,'msg' : "Id Not Founded"})

from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

@api_view(['POST'])
def Contact_Me(request):
    # try:
    # import random
    # import string

    # N = 15
    # code = ''.join(random.choices(string.ascii_letters + string.digits, k = N))
    data = request.data
    id = data['id']
    Full_name = data['Full_name'].title()
    GetUser = Game_user.objects.get(id=id)
    Email = data['Email'].casefold()
    Subject = data['Subject'].title()
    Message = data['Message'].title()
    currentdate = data['date']
    currenttime = data['time']
    current = f"{currentdate} {currenttime}"
    
    if(re.search(email_pattern, Email)):
        contctme = Contact_Us.objects.filter(GetUser = GetUser)
        if len(contctme) > 0:
            Conre = Contact_Us_reply.objects.create(
                GetMail = contctme[0],
                user = 'User',
                Full_name = Full_name,
                Email = Email,
                Subject = Subject,
                Message = Message,
                Today = currentdate,
                Create_at = current,
            )
            contctme[0].Full_name = Full_name
            contctme[0].Email = Email
            contctme[0].Subject = Subject
            contctme[0].Today = currentdate
            contctme[0].Create_at = current
            contctme[0].save()
            mail_subject = f"You receive a request of contact form. Please find details."
            html_content = render_to_string('email.html', {
                'Full_name': Full_name,
                'Email': Email,
                'Subject' : Subject,
                'Message': Message,
                'current': current,
            })
            text_content = strip_tags(html_content)
            # try:
            email_from = settings.EMAIL_HOST_USER
            to_email = [email_from,]
            email = EmailMultiAlternatives(mail_subject, text_content, Full_name, to_email)
            email.attach_alternative(html_content, "text/html")
            email.send()
        # except:
            #     pass
            return Response({'status' : 1,'msg' : "Your Appliction Sent To Admin."})
        else:
            ond = Contact_Us.objects.create(
                GetUser = GetUser,
                Full_name = Full_name,
                Email = Email,
                Subject = Subject,
                Message = Message,
                Today = currentdate,
                Create_at = current,
            )
            Conre = Contact_Us_reply.objects.create(
                GetMail = ond,
                user = 'User',
                Full_name = ond.Full_name,
                Email = ond.Email,
                Subject = ond.Subject,
                Message = ond.Message,
                Today = currentdate,
                Create_at = ond.Create_at,
            )
            mail_subject = f"You receive a request of contact form. Please find details."
            html_content = render_to_string('email.html', {
                'Full_name': Full_name,
                'Email': Email,
                'Subject' : Subject,
                'Message': Message,
                'current': current,
            })
            text_content = strip_tags(html_content)
            email_from = settings.EMAIL_HOST_USER
            to_email = [email_from,]
            email = EmailMultiAlternatives(mail_subject, text_content, Full_name, to_email)
            email.attach_alternative(html_content, "text/html")
            email.send()
            return Response({'status' : 1,'msg' : "Your Appliction Sent To Admin."})
    else:
        return Response({'status' : 0,'msg' : "Please Enter Valid Email"})
    # except:
    #     return Response({'status' : 0,'msg' : "User Id Not Found"})

@api_view(['GET'])
def Drill_list(request):
    try:
        Drill = Drill_Data.objects.filter(Is_Active='1')
        data = []
        for i in Drill:
            res = {}
            res['id'] = i.id
            res['Name'] = i.Name
            if i.image:
                res['image'] = i.image.url
            else:
                res['image'] = ''
            data.append(res)
        return Response({"status": 1 , 'msg' : "Suceess Drills Listing",'data':data})
    except:
        return Response({"status": 0 , 'msg' : "Something Wrong"})

@api_view(['GET'])
def Drill_Play(request,id,last_num):
    try:
        last_number = int(last_num)
        Drill = Drill_Data.objects.get(id=id,Is_Active='1')
        if Drill:
            lis = []
            if Drill.Main:
                lis.append(Drill.Main.id)
            if Drill.Main1:
                lis.append(Drill.Main1.id)
            if Drill.Main2:
                lis.append(Drill.Main2.id)
            formula = Drill_Formula.objects.filter(deal__in=lis).order_by('?')
            data = []
            response = []
            if Drill.Name == "Recall":
                for i in formula:
                    res = {}
                    res['id'] = i.id
                    res['Drill_Name'] = Drill.Name.capitalize()
                    res['color'] = ""
                    if i.image:
                        res['Image'] = i.image.url
                    else:
                        res['Image'] = ''
                        
                    if i.music:
                        res['music'] = i.music.url
                    else:
                        res['music'] = ''
                    if i.Number:
                        res['Condition'] = i.Number
                        res['Display'] = i.Condition
                    else:
                        res['Condition'] = i.Condition
                        res['Display'] = i.Condition
                    data.append(res)
                for j in range(3):
                    dril = data[math.floor(random.random()*len(data))]
                    response.append(dril)
                values = "0"
                mark = response[0]['Display']
            elif Drill.Name == "Calculator":
                values = "1"
                if last_number == 0:
                    for i in formula:
                        res = {}
                        res['id'] = i.id
                        res['Drill_Name'] = Drill.Name.capitalize()
                        res['color'] = ""
                        if i.image:
                            res['Image'] = i.image.url
                        else:
                            res['Image'] = ''
                        
                        res['music'] = "/quickfeet/media/Drills-Music/sound-effect.mp3"
                    
                        res['Condition'] = i.Condition
                        res['Display'] = i.Condition
                
                        data.append(res)
                    
                    for j in range(1):
                        response.append(data[math.floor(random.random()*len(data))])
                    mark = response[0]['Display']
                else:
                    res = {}
                    val = True
                    # str = 0
                    while val:
                        # if str == 15:
                        #     val = False
                        # str = str + 1
                        r1 = random.randint(1, 7)
                        list1 = ["+","-","*","/"]
                        sym = random.choice(list1)
                        if sym == "+":
                            num = (last_number) + r1
                        if sym == "-":
                            num = (last_number) - r1
                        if sym == "*":
                            num = (last_number) * r1
                        if sym == "/":
                            num = (last_number) / r1
                        
                        if num == 1 or num == 2 or num == 3 or num == 4 or num == 5 or num == 6 or num == 7 or num == 8:
                            val = False
                            
                    res['id'] = 0
                    res['Drill_Name'] = Drill.Name.capitalize()
                    if sym == "+":
                        res['color'] = sym
                    elif sym == "-":
                        res['color'] = sym
                    elif sym == "*":
                        res['color'] = sym
                    elif sym == "/":
                        res['color'] = sym
                    else:
                        res['color'] = ""
                    res['Image'] = ""
                    res['music'] = "/quickfeet/media/Drills-Music/sound-effect.mp3"
                    res['Condition'] = f"{int(num)}"
                    res['Display'] = f"{r1}"
                    # res['Display'] = f"{last_number}{sym}{r1}"
                    response.append(res)
                    mark = response[0]['Display']
            else:
                values = "0"
                for i in formula:
                    res = {}
                    res['id'] = i.id
                    res['Drill_Name'] = Drill.Name.capitalize()
                    res['color'] = ""
                    if i.image:
                        res['Image'] = i.image.url
                    else:
                        res['Image'] = ''
                        
                    if i.music:
                        res['music'] = i.music.url
                    else:
                        res['music'] = ''
                    if Drill.Name == "Make It 9":
                        res['Condition'] = i.Number
                        # res['Condition1'] = Drill.Name
                        res['Display'] = i.Condition
                    else:
                        if i.Number:
                            res['Condition'] = i.Condition
                            res['Display'] = i.Number
                        else:
                            res['Condition'] = i.Condition
                            res['Display'] = i.Condition
                    data.append(res)
                
                for j in range(1):
                    dril = data[math.floor(random.random()*len(data))]
                    response.append(dril)
                mark = response[0]['Display']
            # return Response({"status": 1 ,'Vals': values , 'msg' : "Drilly Play Successfully",'data': response})
            return Response({"status": 1 ,'Vals': values , 'msg' : f"{mark} Got Hit",'data': response})
        else:
            return Response({"status": 0 , 'msg' : "Drill Doesn't Active Now"})
    except:
        return Response({"status": 0 , 'msg' : "Drill Doesn't Active Now"})

@api_view(['POST'])
def Drill_Calculator_Play(request,id):
    data = request.data
    last_number = data['last_number']
    last_number = int(last_number)
    Drill = Drill_Data.objects.get(id=id,Is_Active='1')
    if Drill:
        lis = []
        if Drill.Main:
            lis.append(Drill.Main.id)
        if Drill.Main1:
            lis.append(Drill.Main1.id)
        if Drill.Main2:
            lis.append(Drill.Main2.id)
        formula = Drill_Formula.objects.filter(deal__in=lis).order_by('?')
        data = []
        response = []
        if last_number == 0:
            for i in formula:
                res = {}
                res['id'] = i.id
                res['Drill_Name'] = Drill.Name.capitalize()
                if i.image:
                    res['Image'] = i.image.url
                else:
                    res['Image'] = ''
                
                res['music'] = "/quickfeet/media/Drills-Music/sound-effect.mp3"
            
                res['Condition'] = i.Condition
                res['Display'] = i.Condition
        
                data.append(res)
            
            for j in range(1):
                response.append(data[math.floor(random.random()*len(data))])
        else:
            res = {}
            val = True
            # str = 0
            while val:
                # if str == 15:
                #     val = False
                # str = str + 1
                r1 = random.randint(1, 7)
                list1 = ["+","-","*","/"]
                sym = random.choice(list1)
                if sym == "+":
                    num = (last_number) + r1
                if sym == "-":
                    num = (last_number) - r1
                if sym == "*":
                    num = (last_number) * r1
                if sym == "/":
                    num = (last_number) / r1
                
                if num == 1 or num == 2 or num == 3 or num == 4 or num == 5 or num == 6 or num == 7 or num == 8:
                    val = False
                    
            res['id'] = 0
            res['Drill_Name'] = Drill.Name.capitalize()
            res['Image'] = ""
            res['music'] = "/quickfeet/media/Drills-Music/sound-effect.mp3"
            res['Condition'] = f"{int(num)}"
            res['Display'] = f"{sym}{r1}"
            response.append(res)
        return Response({"status": 1 , 'msg' : "Drilly Play Successfully",'data': response})
    else:
        return Response({"status": 0 , 'msg' : "Drill Doesn't Active Now"})

@api_view(['POST'])
def Score_add(request):
    data = request.data
    player = data['user_id']
    dril = data['drill_id']
    addplayer = data['player_id']
    hits = data['hits']
    passing_time = data['Passing_Time']
    Time_Type = data['Time_Type']
    time = data['time']
    ava = int(time) / int(hits)
    scor = (((((int(hits)/int(time))*200)*1.5)+((int(passing_time)-50)*0.5))/(1.5*100)+(int(time)/1000))*100
    GetPlayer = Game_user.objects.get(id=player)
    GetDrill = Drill_Data.objects.get(id=dril)
    if (not addplayer) or addplayer == '0':
        sc = LeaderBoard.objects.create(
            GetPlayer = GetPlayer,
            GetDrill = GetDrill,
            Hits = hits,
            Passing_Time = passing_time,
            Time_Type = Time_Type,
            Time = time,
            Avg_Time = ava,
            Score = scor,
        )
        data = {
            'user_id' : sc.GetPlayer.id,
            'drill_id' : sc.GetDrill.id,
            'hits' : sc.Hits,
            'passing_time' : sc.Passing_Time,
            'time_type' : sc.Time_Type,
            'time' : sc.Time,
            'Avg_Time' : sc.Avg_Time,
            'Score' : sc.Score,
        }
        return Response({"status": 1 , 'msg' : "Score Added Successfully","data" : data})
    else:
        adpl = Add_Players.objects.get(id=addplayer)
        sc = Scorebord.objects.create(
            GetPlayer = GetPlayer,
            GetDrill = GetDrill,
            AddPlayer = adpl,
            Hits = hits,
            Passing_Time = passing_time,
            Time_Type = Time_Type,
            Time = time,
            Avg_Time = ava,
            Score = scor,
        )
        data = {
            'user_id' : sc.AddPlayer.id,
            'drill_id' : sc.GetDrill.id,
            'hits' : sc.Hits,
            'passing_time' : sc.Passing_Time,
            'time_type' : sc.Time_Type,
            'time' : sc.Time,
            'Avg_Time' : sc.Avg_Time,
            'Score' : sc.Score,
        }
        return Response({"status": 1 , 'msg' : "Score Added Successfully","data" : data})
    
@api_view(['GET'])
def Spiner_List_Of_Player(request,id):
    try:
        adpl = Add_Players.objects.filter(GetPlayer = id)
        ls = [{'id': 0,'Full_name' :"Select Player","DOB" : "","Country":"","Shirt_num":""}]
        for i in adpl:
            dic = {}
            dic['id'] = i.id
            dic['Full_name'] = i.Full_name
            dic['DOB'] = i.age
            dic['Country'] = i.Country
            dic['Shirt_num'] = i.Shirt_num
            ls.append(dic)
        return Response({'status':1,'msg':'Players Listing Successfully','data':ls})
    except:
        return Response({"status" : 0,'msg' : "Id Not Founded"})

@api_view(['GET'])
def Spiner_Drill_list(request):
    try:
        Drill = Drill_Data.objects.filter(Is_Active='1')
        data = [{'id': 0,'Name' :"Select Drill","image" : ""}]
        for i in Drill:
            res = {}
            res['id'] = i.id
            res['Name'] = i.Name
            if i.image:
                res['image'] = i.image.url
            else:
                res['image'] = ''
            data.append(res)
        return Response({"status": 1 , 'msg' : "Suceess Drills Listing",'data':data})
    except:
        return Response({"status": 0 , 'msg' : "Something Wrong"})

@api_view(['GET'])
def Drill_formul(request,id):
    try:
        Drill = Drill_Data.objects.get(id=id,Is_Active='1')
        # if Drill.Name == 'Calculator':
        #     for i in formula:    
        # else:
        if Drill:
            lis = []
            if Drill.Main:
                lis.append(Drill.Main.id)
            if Drill.Main1:
                lis.append(Drill.Main1.id)
            if Drill.Main2:
                lis.append(Drill.Main2.id)
            formula = Drill_Formula.objects.filter(deal__in=lis)
            data = []
            for i in formula:
                res = {}
                res['id'] = i.id
                res['Drill_Name'] = Drill.Name.capitalize()
                if i.Number:
                    res['Condition'] = i.Number
                    res['Display'] = i.Condition
                else:
                    res['Condition'] = i.Condition
                    res['Display'] = i.Condition
                data.append(res)
            return Response({"status": 1 , 'msg' : "Success",'data': data})
        else:
            return Response({"status": 0 , 'msg' : "Drill Doesn't Active Now"})
    except:
        return Response({"status": 0 , 'msg' : "Drill Doesn't Active Now"})

@api_view(['GET'])
def Post_List(request):
    try:
        pp = Post.objects.filter(Is_Active='1')
        lis = []
        if len(pp) > 0:
            sq = 0
            for i in pp:
                if sq == 2:
                    sq = 1
                else:
                    sq = sq + 1
                res = {}
                res['id'] = i.id
                res['seq'] = f"{sq}"
                res['title'] = i.title
                if i.image:
                    res['image'] = i.image.url
                else:
                    res['image'] = ''
                print(i.id)
                lis.append(res)
            return Response({"status": 1 , 'msg' : "Static Page Lisint Successfully",'data':lis})
        else:
            return Response({"status": 0 , 'msg' : "No Records"})
    except:
        return Response({"status": 0 , 'msg' : "Something Wrong"})
    
@api_view(['GET'])
def Post_view(request,id):
    try:
        pp = Post.objects.get(Is_Active='1',id=id)
        if pp.image:
            image = pp.image.url
        else:
            image = ''
        lis = {
            "id" : pp.id,
            "title" : pp.title.capitalize(),
            "image" : image,
            "contain" : pp.contain 
        }
        return Response({"status": 1 , 'msg' : "Static Page View successfully",'data':lis})
    except:
        return Response({"status": 0 , 'msg' : "Something Wrong"})

@api_view(['POST'])
def Leaderboard_view(request):
    data = request.data
    age = data['age']
    dril_id = data['Drill_id']
    time = data['time']
    if (not age) and (not dril_id) and (not time):
        print("first")
        scoreboard = LeaderBoard.objects.all().order_by('-Score')
    
    if age and (not dril_id) and (not time):
        lis = []
        if age == '1':
            gg = Game_user.objects.all()
            for j in gg:
                if int(j.age) <= 9:
                    lis.append(j.id)
        if age == '2':
            gg = Game_user.objects.all()
            for j in gg:
                if int(j.age) <= 9 or int(j.age) <=16:
                    lis.append(j.id)
                    print(j.id)
        if age == '3':
            gg = Game_user.objects.all()
            for j in gg:
                if int(j.age) >= 16:
                    lis.append(j.id)
        scoreboard = LeaderBoard.objects.filter(GetPlayer__in=lis).order_by('-Score')
    
    if (not age) and dril_id and (not time):
        dr = Drill_Data.objects.get(id=dril_id)
        scoreboard = LeaderBoard.objects.filter(GetDrill=dr).order_by('-Score')
    
    if (not age) and (not dril_id) and time:
        if time == 'All':
            scoreboard = LeaderBoard.objects.all().order_by('-Score')
        else:
            if len(time) == 4:
                scoreboard = LeaderBoard.objects.filter(Create_at__year__lte=time,Create_at__year__gte=time).order_by('-Score')
            if len(time) == 2:
                yer = date.today().year
                scoreboard = LeaderBoard.objects.filter(Create_at__month__lte=time,Create_at__month__gte=time,Create_at__year__lte=yer,Create_at__year__gte=yer).order_by('-Score')
    
    if age and dril_id and (not time):
        lis = []
        if age == '1':
            gg = Game_user.objects.all()
            for j in gg:
                if int(j.age) <= 9:
                    lis.append(j.id)
        if age == '2':
            gg = Game_user.objects.all()
            for j in gg:
                if int(j.age) <= 9 or int(j.age) <=16:
                    lis.append(j.id)
                    print(j.id)
        if age == '3':
            gg = Game_user.objects.all()
            for j in gg:
                if int(j.age) >= 16:
                    lis.append(j.id)
        dr = Drill_Data.objects.get(id=dril_id)
        scoreboard = LeaderBoard.objects.filter(GetPlayer__in=lis,GetDrill=dr).order_by('-Score')
    
    if age and (not dril_id) and time:
        lis = []
        if age == '1':
            gg = Game_user.objects.all()
            for j in gg:
                if int(j.age) <= 9:
                    lis.append(j.id)
        if age == '2':
            gg = Game_user.objects.all()
            for j in gg:
                if int(j.age) <= 9 or int(j.age) <=16:
                    lis.append(j.id)
                    print(j.id)
        if age == '3':
            gg = Game_user.objects.all()
            for j in gg:
                if int(j.age) >= 16:
                    lis.append(j.id)
        if time == 'All':
            scoreboard = LeaderBoard.objects.filter(GetPlayer__in=lis).order_by('-Score')
        else:
            if len(time) == 4:
                scoreboard = LeaderBoard.objects.filter(GetPlayer__in=lis,Create_at__year__lte=time,Create_at__year__gte=time).order_by('-Score')
            if len(time) == 2:
                yer = date.today().year
                scoreboard = LeaderBoard.objects.filter(GetPlayer__in=lis,Create_at__month__lte=time,Create_at__month__gte=time,Create_at__year__lte=yer,Create_at__year__gte=yer).order_by('-Score')
    
    if age and dril_id and time:
        lis = []
        if age == '1':
            gg = Game_user.objects.all()
            for j in gg:
                if int(j.age) <= 9:
                    lis.append(j.id)
        if age == '2':
            gg = Game_user.objects.all()
            for j in gg:
                if int(j.age) <= 9 or int(j.age) <=16:
                    lis.append(j.id)
                    print(j.id)
        if age == '3':
            gg = Game_user.objects.all()
            for j in gg:
                if int(j.age) >= 16:
                    lis.append(j.id)
        dr = Drill_Data.objects.get(id=dril_id)
        if time == 'All':
            scoreboard = LeaderBoard.objects.filter(GetDrill=dr,GetPlayer__in=lis).order_by('-Score')
        else:
            if len(time) == 4:
                scoreboard = LeaderBoard.objects.filter(GetDrill=dr,GetPlayer__in=lis,Create_at__year__lte=time,Create_at__year__gte=time).order_by('-Score')
            if len(time) == 2:
                yer = date.today().year
                scoreboard = LeaderBoard.objects.filter(GetDrill=dr,GetPlayer__in=lis,Create_at__month__lte=time,Create_at__month__gte=time,Create_at__year__lte=yer,Create_at__year__gte=yer).order_by('-Score')
    
    if (not age) and dril_id and time:
        dr = Drill_Data.objects.get(id=dril_id)
        if time == 'All':
            scoreboard = LeaderBoard.objects.filter(GetDrill=dr).order_by('-Score')
        else:
            if len(time) == 4:
                scoreboard = LeaderBoard.objects.filter(GetDrill=dr,Create_at__year__lte=time,Create_at__year__gte=time).order_by('-Score')
            if len(time) == 2:
                yer = date.today().year
                scoreboard = LeaderBoard.objects.filter(GetDrill=dr,Create_at__month__lte=time,Create_at__month__gte=time,Create_at__year__lte=yer,Create_at__year__gte=yer).order_by('-Score')
    
    lis = []
    j = 0
    for i in scoreboard:
        res = {}
        j = j + 1
        res['Rank'] = j
        res['id'] = i.id
        if i.GetPlayer:
            res['Player_Name'] = i.GetPlayer.Full_name if i.GetPlayer.Full_name else ''
            res['Country'] = i.GetPlayer.Country if i.GetPlayer.Country else ''
            res['GetDrill'] = i.GetDrill.Name if i.GetDrill.Name else ''
        else:
            res['Player_Name'] = ''
            res['Country'] = ''
            res['GetDrill'] = ''
        res['Hits'] = i.Hits
        res['Passing_Time'] = i.Passing_Time
        res['Time'] = i.Time
        res['Avg_Time'] = format(i.Avg_Time, '.2f')
        res['Score'] = f"{i.Score}"
        res['Date'] = i.Create_at
        lis.append(res)
    return Response({"status": 1 , 'msg' : "Leaderboard Scores Listing","data" : lis})

@api_view(['POST'])
def Score_view(request,id):
    data = request.data
    player = data['Player_id']
    dril_id = data['Drill_id']
    time = data['time']
    
    if player and (not dril_id) and (not time):
        ad = Add_Players.objects.get(id=player)
        scoreboard = Scorebord.objects.filter(AddPlayer=ad,GetPlayer=id).order_by('-Score')
    
    if player and dril_id and (not time):
        ad = Add_Players.objects.get(id=player)
        dr = Drill_Data.objects.get(id=dril_id)
        scoreboard = Scorebord.objects.filter(GetDrill=dr,AddPlayer=ad,GetPlayer=id).order_by('-Score')

    if player and (not dril_id) and time:
        ad = Add_Players.objects.get(id=player)
        if time == 'All':
            scoreboard = Scorebord.objects.filter(AddPlayer=ad,GetPlayer=id).order_by('-Score')
        else:
            if len(time) == 4:
                scoreboard = Scorebord.objects.filter(AddPlayer=ad,GetPlayer=id,Create_at__year__lte=time,Create_at__year__gte=time).order_by('-Score')
            if len(time) == 2:
                yer = date.today().year
                scoreboard = Scorebord.objects.filter(AddPlayer=ad,GetPlayer=id,Create_at__month__lte=time,Create_at__month__gte=time,Create_at__year__lte=yer,Create_at__year__gte=yer).order_by('-Score')
                
    if (not player) and dril_id and (not time):
        dr = Drill_Data.objects.get(id=dril_id)
        scoreboard = Scorebord.objects.filter(GetDrill=dr,GetPlayer=id).order_by('-Score')
    
    if (not player) and dril_id and time:
        dr = Drill_Data.objects.get(id=dril_id)
        if time == 'All':
            scoreboard = Scorebord.objects.filter(GetDrill=dr,GetPlayer=id).order_by('-Score')
        else:
            if len(time) == 4:
                scoreboard = Scorebord.objects.filter(GetDrill=dr,GetPlayer=id,Create_at__year__lte=time,Create_at__year__gte=time).order_by('-Score')
            if len(time) == 2:
                yer = date.today().year
                scoreboard = Scorebord.objects.filter(GetDrill=dr,GetPlayer=id,Create_at__month__lte=time,Create_at__month__gte=time,Create_at__year__lte=yer,Create_at__year__gte=yer).order_by('-Score')
             
    if player and dril_id and time:
        ad = Add_Players.objects.get(id=player)
        dr = Drill_Data.objects.get(id=dril_id)
        if time == 'All':
            scoreboard = Scorebord.objects.filter(AddPlayer=ad,GetDrill=dr,GetPlayer=id).order_by('-Score')
        else:
            if len(time) == 4:
                scoreboard = Scorebord.objects.filter(AddPlayer=ad,GetDrill=dr,GetPlayer=id,Create_at__year__lte=time,Create_at__year__gte=time).order_by('-Score')
            if len(time) == 2:
                yer = date.today().year
                scoreboard = Scorebord.objects.filter(AddPlayer=ad,GetDrill=dr,GetPlayer=id,Create_at__month__lte=time,Create_at__month__gte=time,Create_at__year__lte=yer,Create_at__year__gte=yer).order_by('-Score')
             
    if (not player) and (not dril_id) and time:
        if time == 'All':
            scoreboard = Scorebord.objects.filter(GetPlayer=id).order_by('-Score')
        else:
            if len(time) == 4:
                scoreboard = Scorebord.objects.filter(GetPlayer=id,Create_at__year__lte=time,Create_at__year__gte=time).order_by('-Score')
            if len(time) == 2:
                yer = date.today().year
                scoreboard = Scorebord.objects.filter(GetPlayer=id,Create_at__month__lte=time,Create_at__month__gte=time,Create_at__year__lte=yer,Create_at__year__gte=yer).order_by('-Score')
    
    if (not player) and (not dril_id) and (not time):
        scoreboard = Scorebord.objects.filter(GetPlayer=id).order_by('-Score')
        
    lis = []
    j = 0
    for i in scoreboard:
        res = {}
        j = j + 1
        res['Rank'] = j
        res['id'] = i.id
        if i.AddPlayer:
            res['Player_Name'] = i.AddPlayer.Full_name
            res['Country'] = i.AddPlayer.Country
        else:
            res['Player_Name'] = ''
            res['Country'] = ''
        res['GetDrill'] = i.GetDrill.Name
        res['Hits'] = i.Hits
        res['Passing_Time'] = i.Passing_Time
        res['Time'] = i.Time
        res['Avg_Time'] = format(i.Avg_Time, '.2f')
        res['Score'] = f"{i.Score}"
        res['Date'] = i.Create_at
        lis.append(res)
    return Response({"status": 1 , 'msg' : "Scoreboard Scores Listing","data" : lis})

@api_view(['POST'])
def ChangePassword(request,id):
    try:
        data = request.data
        showtime = strftime("%Y-%m-%d %H:%M", )
        currenpassword = data['currenpassword']
        newpassword = data['newpassword']
        cnewpassword = data['cnewpassword']
        chec = Game_user.objects.get(id=id)
        ps = check_password(currenpassword, chec.Password)
        if ps:
            if newpassword != cnewpassword:
                return Response({'status' : 0 , 'msg' : "Password Doesn't Match.!"})
            else:
                addpas = Password_store.objects.filter(GetPlayer=id,Password2=cnewpassword)
                if len(addpas) > 0:
                    return Response({"status" : 0,'msg' : "You have already used this password"})
                else:  
                    chec.Password = make_password(newpassword)
                    chec.Password2 = cnewpassword
                    chec.save()
                    addpas = Password_store.objects.create(
                        GetPlayer = chec,
                        Password = make_password(newpassword),
                        Password2 = cnewpassword,
                        Create_at = showtime,
                    )
                    return Response({'status' : 1,'msg' : "Password Updated"})
        else:
            return Response({'status' : 0,'msg' : "Current Password Is Wrong"})
    except:
        return Response({'status' : 0,'msg' : "Id Not Found"})

@api_view(['GET'])
def country_list(request):
    try:
        allcontry = Country_codes.objects.all()
        if len(allcontry) > 0:
            ls = []
            for i in allcontry:
                res = {}
                res['id'] = i.id
                res['country_name'] = i.Country_name
                res['country_alph_3'] = i.Alpha_3_code
                res['country_code'] = i.Country_code
                ls.append(res)
            return Response({'status' : 1,'msg' : "Success","data":ls})
        else:
            return Response({'status' : 0,'msg' : "No Records"})
    except:
        return Response({'status' : 0,'msg' : "Something Wrong"})