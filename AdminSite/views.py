from django.shortcuts import render,redirect
from django.core.exceptions import *
from django.contrib.auth.hashers import make_password,check_password
from django.http import JsonResponse
from .models import *
from .forms import *
from game.models import *
from time import gmtime, strftime
from django.db.models import F, Sum
from django.conf import settings
from django.core.mail import send_mail
from django.core.paginator import Paginator,EmptyPage
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import re
import math,random

email_pattern = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 

# Create your views here.
# [
#     '%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', # '2006-10-25', '10/25/2006', '10/25/06'
#     '%b %d %Y', '%b %d, %Y',            # 'Oct 25 2006', 'Oct 25, 2006'
#     '%d %b %Y', '%d %b, %Y',            # '25 Oct 2006', '25 Oct, 2006'
#     '%B %d %Y', '%B %d, %Y',            # 'October 25 2006', 'October 25, 2006'
#     '%d %B %Y', '%d %B, %Y',            # '25 October 2006', '25 October, 2006'
# ]

def Login(request):
    if 'id' in request.session:
        return redirect('index')
    else:
        context = {
            'status' : 1,
            'title' : "Login",
        }
        return render(request,"admin-page/Login.html",context)
        # return render(request,"Email/email.html",context)
        
def Login_cr(request):
    if request.method == "POST": 
        username = request.POST['username']
        password = request.POST['password']
        # ad = admin_data.objects.create(
        #     username = username,
        #     password = password,
        # )
        # ad.password = make_password(ad.password)
        # ad.save()
        # return redirect('login')
        user = admin_data.objects.filter(username=username)
        if len(user) > 0:
            pas = check_password(password, user[0].password)
            if pas:
                request.session['id'] = user[0].id
                request.session['lang'] = "English(UK)"
                request.session['lang_image'] = "https://demos.creative-tim.com/test/material-dashboard-pro/assets/img/icons/flags/GB.png"
                return redirect('index')
            else:
                context = {
                'status' : 0,
                'username' : username,
                'title' : "Login",
                'err' : "Password wrong"
                }
                return render(request,"admin-page/Login.html",context)
                # return render(request,"Email/email.html",context)
        else:
            context = {
            'status' : 0,
            'username' : username,
            'password' : password,
            'title' : "Login",
            'err1' : "Unknown User"
            }
            return render(request,"admin-page/Login.html",context)
    else:
        return redirect('login')

def Logout(request):
    if 'id' in request.session:
        del request.session['id']
        del request.session['lang']
        del request.session['lang_image']
        return redirect('login')
    else:
        return redirect('login')
    
def Index_page(request):
    if 'id' in request.session:
        Player = Game_user.objects.filter(Is_active='1').count()
        Block_Player = Game_user.objects.filter(Is_active='0').count()
        drill_active = Drill_Data.objects.filter(Is_Active='1').count()
        drill_block = Drill_Data.objects.filter(Is_Active='0').count()
        Post_active = Post.objects.filter(Is_Active='1').count()
        Post_block = Post.objects.filter(Is_Active='0').count()
        New_req = Contact_Us.objects.filter(Is_Active='1').count()
        if request.method == "POST":
            if 'id' in request.session:
                session = '1'
            else:
                session = '0'
            context = {
                'session' : session,
                'Player' : Player,
                'Block_Player' : Block_Player,
                'New_req' : New_req,
                'drill_block' : drill_block,
                'drill_active' : drill_active,
                'Post_active' : Post_active,
                'Post_block' : Post_block,
            }
            return JsonResponse(context)
        context = {
            'active' : 1,
            'title' : "Home",
            'btitle' : "Dashboard",
            'Player' : Player,
            'Block_Player' : Block_Player,
            'drill_block' : drill_block,
            'drill_active' : drill_active,
            'Post_active' : Post_active,
            'Post_block' : Post_block,
            'New_req' : New_req,
        }
        return render(request,"admin-page/HomePage.html",context)
    else:
        return redirect('login')

def All_Static_Pages(request):
    if 'id' in request.session:
        data = Post.objects.all()
        context = {
            'active' : 3,
            'title' : 'Static Page',
            'data' : data,
            'btitle' : "Static Pages"
        }
        return render(request,"admin-page/Static-Pages.html",context)
    else:
        return redirect('login')
    
def All_Request_Pages(request):
    if 'id' in request.session:
        data = Contact_Us.objects.filter(Is_Active='1')
        context = {
            'active' : 4,
            'title' : 'Contact Request Page',
            'data' : data,
            'btitle' : "Contact Pages"
        }
        return render(request,"admin-page/contact_us.html",context)
    else:
        return redirect('login')

def Request_Back(request,id):
    try:
        if 'id' in request.session:
            data = Contact_Us.objects.get(id=id)
            data1 = Contact_Us_reply.objects.filter(GetMail = id).order_by('id')
            context = {
                'active1' : '01',
                'active' : 4,
                'title' : "Request View Page",
                'btitle' : f"{data.Full_name.upper()}",
                'getbnr' : data,
                'data' : data1,
            }
            return render(request,"admin-page/Request_mail.html",context)
        else:
            return redirect('login')
    except:
        return redirect('All_Request_Pages')

from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

def Request_Reply(request):
    if request.method == "POST":
        ids = request.POST['id']
        Rep = Contact_Us.objects.get(id=ids)
        reply = request.POST['post']
        currentdate = request.POST['Currentdate']
        Conre = Contact_Us_reply.objects.create(
                GetMail = Rep,
                user = 'Admin',
                Full_name = '',
                Email = '',
                Subject = "",
                Message = reply,
                Today = currentdate[0:-9],
                Create_at = currentdate[0:-3],
            )
        mail_subject = f"Reply of contact form."
        html_content = render_to_string('Email/email.html', {
            'Full_name': Rep.Full_name,
            'Email': Rep.Email,
            'subject' : "Reply Of Contact Form",
            'Message': reply,
        })
        text_content = strip_tags(html_content)
        try:
            email_from = "Quickfeet Admin " 
            to_email = [Rep.Email]
            email = EmailMultiAlternatives(mail_subject, text_content, email_from, to_email)
            email.attach_alternative(html_content, "text/html")
            email.send()
        except:
            pass
        Rep.save()
        return redirect('Request_Back',ids)
    else:
        return redirect('All_Request_Pages')
    
def Add_Static_Form_Page(request):
    if 'id' in request.session:
        fors = PostForm
        context = {
            'active1' : '01',
            'active' : 3,
            'fom' : 1,
            'title' : 'Form',
            'btitle' : "Form",
            'form' : fors
        }
        return render(request,"admin-page/Static_form.html",context)
    else:
        return redirect('login')

def Edit_Static_Form_Page(request,id):
    if 'id' in request.session:
        getbnr = Post.objects.get(slug=id)
        fors = PostForm(request.POST or None, instance=getbnr)
        context = {
            'active1' : '01',
            'active' : 3,
            'fom' : 2,
            'title' : getbnr.title,
            'btitle' : "Form",
            'form' : fors,
            'getbnr' : getbnr
        }
        return render(request,"admin-page/Static_form.html",context)
    else:
        return redirect('login')

def Add_Update_Static(request):
    if request.method == "POST":
        dat = strftime('%d %B, %Y') + " " + strftime('%I:%M %p')
        id = request.POST['id']
        if (not id):
            t1 = request.POST['text1']
            if (not t1):
                messages.warning(request, f"Title Is Required")
                return redirect('forms')
            # try:
            #     t2 = request.FILES['text2']
            # except:
            #     messages.warning(request, f"Image Is Required")
                return redirect('forms')
            big1 = request.POST['contain']
            # big1 = big1.replace("\r\n", "")
            Crea = Post.objects.create(
                title = t1,
                slug = t1,
                # image = t2,
                contain = big1,
                Create_at = dat,
                Update_at = dat, 
            ) 
            messages.success(request, f"{t1} Add Successfully")
            return redirect('forms')
        else:
            getbnr = Post.objects.get(id=id)
            getbnr.title = request.POST['text1'] if request.POST['text1'] else getbnr.title
            getbnr.slug = getbnr.title
            # try:
            #     getbnr.image = request.FILES['text2'] if request.FILES['text2'] else getbnr.image
            # except:
            #     getbnr.image
            big1 = request.POST['contain']
            # big1 = big1.replace("\r\n", "")
            getbnr.contain = big1 = big1 if big1 else getbnr.contain
            getbnr.Update_at = dat
            getbnr.save()
            messages.success(request, f"{getbnr.title} Updated")
            return redirect('Edit_Form_Page',getbnr.slug)
    else:
        return redirect('Static_Pages')
  
def static_delete(request,id):
    if 'id' in request.session:
        getpas = Post.objects.get(id=id)
        getpas.delete()
        return redirect("Static_Pages")
    else:
        return JsonResponse({'status':0})
    
def Game_User_Block(request):
    if 'id' in request.session:
        if request.method=='POST':
            id = request.POST.get('pid')
            getu = Game_user.objects.get(id=id)
            if getu.Is_active == '1':
                getu.Is_active = '0'
                getu.save()
                return JsonResponse({'status':1, "msg" : "Block"})
            elif getu.Is_active == '0':
                getu.Is_active = '1'
                getu.save()
                return JsonResponse({'status':2, "msg" : "UnBlock"})
            else:
                return JsonResponse({'status':0})
        else:
            return JsonResponse({'status':0})
    else:
        return JsonResponse({'status':0})
    
def Static_Publish(request):
    if 'id' in request.session:
        if request.method=='POST':
            id = request.POST.get('pid')
            getu = Post.objects.get(id=id)
            if getu.Is_Active == '1':
                getu.Is_Active = '0'
                getu.save()
                return JsonResponse({'status':1, "msg" : "Block"})
            elif getu.Is_Active == '0':
                getu.Is_Active = '1'
                getu.save()
                return JsonResponse({'status':2, "msg" : "UnBlock"})
            else:
                return JsonResponse({'status':0})
        else:
            return JsonResponse({'status':0})
    else:
        return JsonResponse({'status':0})

def drills_Status(request):
    if 'id' in request.session:
        if request.method=='POST':
            id = request.POST.get('pid')
            getu = Drill_Data.objects.get(id=id)
            if getu.Is_Active == '1':
                getu.Is_Active = '0'
                getu.save()
                return JsonResponse({'status':1, "msg" : "Block"})
            elif getu.Is_Active == '0':
                getu.Is_Active = '1'
                getu.save()
                return JsonResponse({'status':2, "msg" : "UnBlock"})
            else:
                return JsonResponse({'status':0})
        else:
            return JsonResponse({'status':0})
    else:
        return JsonResponse({'status':0})

def Drills_List(request):
    if 'id' in request.session:
        data = Drill_Data.objects.all()
        context = {
            'active' : 5,
            'title' : 'Drills Page',
            'data' : data,
            'btitle' : "Drills Pages"
        }
        return render(request,"admin-page/Drills.html",context)
    else:
        return redirect('login')
    
def lang_change(request):
    if request.method=='POST':
        image = request.POST.get('image')
        image_text = request.POST.get('image_text')
        del request.session['lang']
        del request.session['lang_image']
        request.session['lang'] = image_text
        request.session['lang_image'] = image
        return JsonResponse({'status':1})

def Add_Drills_Form_Page(request):
    if 'id' in request.session:
        # data = Drills_listing.objects.all()
        context = {
            'active' : 5,
            'active1' : '01',
            'title' : 'Drills Form Page',
            # 'data' : data,
            'btitle' : "Drills Form Pages",
            "range" : range(1,9),
        }
        return render(request,"admin-page/Drills_form.html",context)
    else:
        return redirect('login')
 
def Drills_Add_Form(request):
    if 'id' in request.session:
        showme = strftime('%d %B, %Y') + " " + strftime('%I:%M %p')
        if request.method == "POST":
            id = request.POST['id']
            if (not id):
                Name = request.POST['Name']
                Drills_Number = request.POST['Drills_Number']
                Drills_Logic = request.POST['Drills_Logic']
                # audio_file = request.FILES['audio_file']
                drd = Drill_Data.objects.create(
                    Name = Name,
                    slug = Name,
                    Drills_Number = Drills_Number,
                    Drills_Logic = Drills_Logic,
                    # Audio = audio_file,
                    Create_at = showme,
                    Update_at = showme,
                )
                messages.success(request, f"Drills Added")
                return redirect('drills')
            else:
                drd = Drill_Data.objects.get(id=id)
                drd.Name = request.POST['Name'] if request.POST['Name'] else drd.Name
                try:
                    drd.Drills_Number = request.POST['Drills_Number'] 
                except:
                    drd.Drills_Number = drd.Drills_Number
                    
                # try:
                #     drd.Audio = request.FILES['audio_file']
                # except:
                #     drd.Audio = drd.Audio

                drd.Drills_Logic = request.POST['Drills_Logic'] if request.POST['Drills_Logic'] else drd.Drills_Logic
                drd.slug = drd.Name
                drd.Update_at = showme
                drd.save()
                messages.success(request, f"{drd.Name} Updated")
                return redirect('Edit_Drills_Form_Page',drd.slug)
        else:
            messages.warning(request, f"Something Wrong")
            return redirect('drills')
    else:
        return redirect('login')

def Edit_Drills_Form_Page(request,id):
    if 'id' in request.session:
        getpas = Drills_listing.objects.get(slug=id)
        
        # digits = '12345678'
        # drill = ''
        # for i in range(3):
        #     drill += digits[math.floor(random.random()*8)]
        
        # hits = 115
        # passing = 90
        # time = 230
        # Avrage = (((((hits/time)*200)*1.5) + ((passing-50)*0.5))/(1.5*100)+(time/1000))*100
        
        context = {
            'active' : 5,
            'active1' : '01',
            'fom' : 2,
            # 'drill' : round(Avrage),
            'title' : f"{getpas.Name}'s Page",
            'getpas' : getpas,
            'btitle' : "Drills Edit Pages",
            "range" : range(1,9)
        }
        return render(request,"admin-page/Drills_form.html",context)
    else:
        return JsonResponse({'status':0})

def Drills_delete(request,id):
    if 'id' in request.session:
        getpas = Drill_Data.objects.get(id=id)
        getpas.delete()
        return redirect("all_drills_list")
    else:
        return JsonResponse({'status':0})

def All_Player_Info(request):
    if 'id' in request.session:
        data = Game_user.objects.all().order_by('-id')
        context = {
            'active' : 2,
            'title' : 'All Players',
            'data' : data,
            'btitle' : "All Players"
        }
        return render(request,"admin-page/User-Tables.html",context)
    else:
        return redirect('login')

def Delete_Player(request,id):
    if 'id' in request.session:
        getpas = Game_user.objects.get(id=id)
        getpas.delete()
    # return JsonResponse({'status':1})
        return redirect("Player_Info")
    else:
        return JsonResponse({'status':0})

def Add_Player_form(request):
    if 'id' in request.session:
        context = {
            'active' : 2,
            'active1' : '01',
            'fom' : '2',
            'title' : f"User's Add Page",
            # 'getpas' : getpas,
            'btitle' : "User's Add Pages",
            'date' : strftime('%Y-%m-%d'),
        }
        return render(request,"admin-page/User_form.html",context)
    else:
        return redirect("login")

def Edit_Player_form(request,id):
    if 'id' in request.session:
        getuser = Game_user.objects.get(slug=id)
        context = {
            'date' : strftime('%Y-%m-%d'),
            'active' : 2,
            'active1' : '01',
            'title' : f"User's Edit Page",
            'btitle' : "User's Edit Pages",
            'id' : getuser.id,
            'Via' : getuser.Via,
            'Full_name' : getuser.Full_name if getuser.Full_name else '',
            'Game_name' : getuser.Game_name if getuser.Game_name else '',
            'Email' : getuser.Email if getuser.Email else '',
            'DOB' : getuser.DOB if getuser.DOB else '',
            'Gender' : getuser.Gender if getuser.Gender else '',
            'Password' : getuser.Password2 if getuser.Password2 else '',
            'Country' : getuser.Country if getuser.Country else '',
            'status' : getuser.Is_active,
        }
        return render(request,"admin-page/User_form.html",context)
    else:
        return redirect("login")

def Add_Update_Player(request):
    if request.method == "POST":
        # dat = strftime('%d %B, %Y') + " " + strftime('%I:%M %p')
        id = request.POST['id']
        dat = request.POST['Currentdate']
        if (not id):
            full_name = request.POST['full_name']
            profile_name = request.POST['profile_name']
            email = request.POST['email'].casefold()
            password = request.POST['password']
            country = request.POST['country']
            DOB = request.POST['DOB']
            if(re.search(email_pattern, email)):
                getmail = Game_user.objects.filter(Email=email,Is_active='1')
                if len(getmail) > 0:    
                    messages.warning(request, f"Email Already Used")
                    return redirect('Add_Player_form')
                else:
                    email = email
            else:
                messages.warning(request, f"Invalid Email")
                return redirect('Add_Player_form')
            user = Game_user.objects.create(
                Via = 'Gmail',
                Full_name = full_name,
                slug = full_name,
                Game_name = profile_name,
                Email = email,
                DOB = DOB,
                Password = make_password(password),
                Password2 = password,
                Country = country,
                Is_active = '1',
                Create_at = dat[0:-3],
                Update_at = dat[0:-3],
            )
            messages.success(request, f"{full_name.title()} Add Successfully")
            return redirect('Add_Player_form')
        else:
            request.POST = request.POST
            chec = Game_user.objects.get(id=id)
            chec.Full_name = request.POST['full_name'] if request.POST['full_name'] else chec.Full_name
            chec.Game_name = request.POST['profile_name'] if request.POST['profile_name'] else chec.Game_name
            chec.DOB = request.POST['DOB'] if request.POST['DOB'] else chec.DOB
            chec.Country = request.POST['country'] if request.POST['country'] else chec.Country
            password = make_password(request.POST['password'])
            chec.Password = password if password else chec.Password
            chec.Password2 = request.POST['password'] if request.POST['password'] else chec.Password2
            email = request.POST['email'].casefold()
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
            chec.slug = request.POST['full_name'] if request.POST['full_name'] else chec.Email
            chec.Update_at = dat[0:-3]
            chec.save()
            messages.success(request, f"{chec.Full_name.title()} Updated")
            return redirect('Edit_Player_form',chec.slug)
            # return redirect('Static_Pages')
    else:
        return redirect('Static_Pages')
  