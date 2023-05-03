from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
Gender = (('0', '--'),('M', 'Male'), ('F', 'Female'), ('O', 'Other'))

# Create your models here.

class Game_user(models.Model):
    Via = models.TextField(null=True,blank=True)
    Full_name = models.CharField(max_length=255,blank=True)
    slug = AutoSlugField(populate_from='Full_name', max_length=255, unique=True, db_index=True,null=True,blank=True)
    Game_name = models.CharField(max_length=255,blank=True)
    Email = models.EmailField(max_length=40,blank=True)
    DOB = models.DateField(blank=True,null=True)
    age = models.CharField(max_length=40,blank=True,null=True)
    google_Id = models.CharField(max_length=255,blank=True,null=True)
    facebook_Id = models.CharField(max_length=255,blank=True,null=True)
    Gender = models.CharField(max_length=10,null=False,blank=False,default='0',choices=Gender)
    Password = models.TextField(null=True,blank=True)
    Password2 = models.CharField(max_length=255,blank=True,null=True)
    Country = models.CharField(max_length=255,blank=True,null=True)
    Shirt_num = models.CharField(max_length=255,blank=True,null=True)
    Is_active = models.CharField(max_length=10,default='1',choices=[("1","Active"),('0',"Deactive")])
    Otp = models.CharField(max_length=10,null=True,blank=True)
    Create_at = models.DateTimeField(max_length=255,blank=True,null=True)
    Update_at = models.DateTimeField(max_length=255,blank=True,null=True)

    def __str__(self):
        return f"{self.Full_name}"
        
class Password_store(models.Model):
    GetPlayer = models.ForeignKey(Game_user, on_delete=models.CASCADE,null=True,blank=True)
    Password = models.TextField(null=True,blank=True)
    Password2 = models.CharField(max_length=255,blank=True,null=True)
    Create_at = models.CharField(max_length=255,blank=True,null=True)
  
class Add_Players(models.Model):
    GetPlayer = models.ForeignKey(Game_user, on_delete=models.CASCADE,null=True,blank=True)
    Full_name = models.CharField(max_length=255,blank=True)
    DOB = models.DateField(blank=True,null=True)
    age = models.CharField(max_length=40,blank=True,null=True)
    Country = models.CharField(max_length=255,blank=True,null=True)
    Shirt_num = models.CharField(max_length=255,blank=True,null=True)
    Create_at = models.CharField(max_length=255,blank=True,null=True)  
    
class Post(models.Model):
    title = models.CharField(null=True,blank=True,max_length=255) # remove this 
    slug = AutoSlugField(populate_from='title', max_length=255, unique=True, db_index=True,null=True,blank=True)
    image = models.ImageField(upload_to="CkEditor/",height_field=None, width_field=None, max_length=255,blank=True,null=True) # remove this 
    contain = RichTextField() # add this
    Is_Active = models.CharField(max_length=10,default='1',choices=[("1","Active"),('0',"Deactive")])
    Create_at = models.CharField(max_length=255,null=True,blank=True)
    Update_at = models.CharField(max_length=255,null=True,blank=True)

class Drills(models.Model):
    Name = models.CharField(max_length=255,null=True,blank=True)
    Create_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.Name}"
    
class Drill_Formula(models.Model):
    deal = models.ForeignKey(Drills, on_delete=models.CASCADE,null=True,blank=True)
    Number = models.CharField(max_length=255,null=True,blank=True)
    Condition = models.CharField(max_length=255,null=True,blank=True)
    image = models.ImageField(upload_to="Drills-shape/",height_field=None, width_field=None, max_length=255,blank=True,null=True) # remove this 
    music = models.FileField(upload_to="Drills-Music/",default='Drills-Music/sound-effect.mp3',max_length=255,blank=True,null=True) # remove this 
    image_condition = models.ImageField(upload_to="Drills_condition/",height_field=None, width_field=None, max_length=255,blank=True,null=True) # remove this 
    Create_at = models.DateField(auto_now=True)
    
    def __str__(self):
        if self.Number:
            return f"{self.deal.Name} {self.Number} {self.Condition}"
        else:
            return f"{self.deal.Name} {self.Condition}"
    
class Drill_Data(models.Model):
    Main = models.ForeignKey(Drills, on_delete=models.CASCADE,null=True,blank=True,related_name='Main')
    Main1 = models.ForeignKey(Drills, on_delete=models.CASCADE,null=True,blank=True,related_name='Main1')
    Main2 = models.ForeignKey(Drills, on_delete=models.CASCADE,null=True,blank=True,related_name='Main2')
    Name = models.CharField(max_length=255,null=True,blank=True)
    image = models.ImageField(upload_to="Drills/",height_field=None, width_field=None, max_length=255,blank=True,null=True) # remove this 
    Is_Active = models.CharField(max_length=10,default='1',choices=[("1","Active"),('0',"Deactive")])
    Create_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.Name

class LeaderBoard(models.Model):
    GetPlayer = models.ForeignKey(Game_user, on_delete=models.SET_NULL,null=True,blank=True)
    GetDrill = models.ForeignKey(Drill_Data, on_delete=models.SET_NULL,null=True,blank=True)
    Hits = models.CharField(max_length=255,blank=True,null=True)
    Passing_Time = models.CharField(max_length=255,blank=True,null=True)
    Time_Type = models.CharField(max_length=255,blank=True,null=True)
    Time = models.CharField(max_length=255,blank=True,null=True)
    Avg_Time = models.FloatField(blank=True,null=True)
    Score = models.IntegerField(blank=True,null=True)
    Create_at = models.DateField(auto_now=True)

class Scorebord(models.Model):
    GetPlayer = models.ForeignKey(Game_user, on_delete=models.SET_NULL,null=True,blank=True)
    GetDrill = models.ForeignKey(Drill_Data, on_delete=models.SET_NULL,null=True,blank=True)
    AddPlayer = models.ForeignKey(Add_Players, on_delete=models.CASCADE,null=True,blank=True)
    Hits = models.CharField(max_length=255,blank=True,null=True)
    Passing_Time = models.CharField(max_length=255,blank=True,null=True)
    Time_Type = models.CharField(max_length=255,blank=True,null=True)
    Time = models.CharField(max_length=255,blank=True,null=True)
    Avg_Time = models.FloatField(blank=True,null=True)
    Score = models.IntegerField(blank=True,null=True)
    Create_at = models.DateField(auto_now=True)
    
class Contact_Us(models.Model):
    GetUser = models.ForeignKey(Game_user, on_delete=models.CASCADE,null=True,blank=True)
    Full_name = models.CharField(max_length=255,null=True,blank=True)
    Token = models.TextField(null=True,blank=True)
    Email = models.CharField(max_length=255,null=True,blank=True)
    Subject = models.CharField(max_length=255,null=True,blank=True)
    Message = models.TextField(null=True,blank=True)
    Is_Active = models.CharField(max_length=10,default='1',choices=[("1","Active"),('0',"Deactive")])
    Today = models.DateField(max_length=255,blank=True,null=True)
    Create_at = models.DateTimeField(max_length=255,blank=True,null=True)
    
class Contact_Us_reply(models.Model):
    GetMail = models.ForeignKey(Contact_Us, on_delete=models.CASCADE,null=True,blank=True)
    user = models.CharField(max_length=255,null=True,blank=True)
    Full_name = models.CharField(max_length=255,null=True,blank=True)
    Email = models.CharField(max_length=255,null=True,blank=True)
    Subject = models.CharField(max_length=255,null=True,blank=True)
    Message = models.TextField(null=True,blank=True)
    Today = models.DateField(max_length=255,blank=True,null=True)
    Create_at = models.DateTimeField(max_length=255,blank=True,null=True)

class Country_codes(models.Model):
    Country_name = models.CharField(max_length=255,null=True,blank=True)
    Alpha_3_code = models.CharField(max_length=255,null=True,blank=True)
    Country_code = models.CharField(max_length=255,null=True,blank=True)
    Create_at = models.DateField(auto_now_add=True)
    Update_at = models.DateField(auto_now=True)
    