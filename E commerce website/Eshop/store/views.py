from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models.product import Product
from.models.category import Category
from.models.customer import Custmore
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from django.views import View
 
# print(make_password('1234'))
# print(check_password('1234','pbkdf2_sha256$390000$mRzLxWwq6VFxXO10UpiV8U$Ds3Zhv4vfrwInBS3T2HgOw5ke61pRhI0L6ss7a2LFKg='))
# Create your views here.
def index(request):
    products=None
    category=Category.objects.all()
    categoryID=request.GET.get('categories')
    if categoryID:
        products=Product.objects.filter( category=categoryID)
        print('######################',products)
    else:
        products=Product.objects.all()
    context = {'products':products,'category':category,}
    return render(request,'index.html',context)


def validateCustomer(customer):
    error_message = None
    if(not customer.first_name):
        error_message = "First Name Required"
    elif not customer.first_name:
        if len(customer.first_name)<4:
            error_message = 'First Name must be 4 charctore'  
    elif not customer.last_name:
        if len(customer.last_name)<4:
            error_message = 'last Name must be 4 charctore' 
    elif not customer. phone_name:
        error_message = 'phone Number reuuired' 
    elif len(customer.phone_name)<10:
        error_message = 'Phone No must be 10 char long' 
    elif len(customer.email)<5:
        error_message = 'email must be 5 char long' 
            
    elif Custmore.objects.filter(email=customer.email).exists():
        error_message = 'Email is already exist'
        print('email already exist')
    
    return error_message   



def registerUser(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone_name = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
                                                                                                            
        value = {
                'first_name' : first_name,
                'last_name'  : last_name,
                'phone_name' : phone_name,
                'email'      : email,
            }
         # error message=None
            # if(not first_name):
            #     error_message = "First Name Required"
            # elif not first_name:
            #     if len(first_name)<4:
            #         error_message = 'First Name must be 4 charctore'  
            # elif not last_name:
            #     if len(last_name)<4:
            #         error_message = 'last Name must be 4 charctore' 
            # elif not  phone_name:
            #      error_message = 'phone Number reuuired' 
            # elif len(phone_name)<10:
            #     error_message = 'Phone No must be 10 char long' 
            # elif len(email)<5:
            #     error_message = 'email must be 5 char long' 
            
            # elif Custmore.objects.filter(email=email).exists():
            #     error_message = 'Email is already exist'
            #     print('email already exist')
                         
        error_message = None
        customer = Custmore(first_name=first_name,last_name=last_name, phone_name=phone_name, email= email,password=password)
        error_message=validateCustomer(customer)
         #saving
        if not error_message:
            customer = Custmore(first_name=first_name,last_name=last_name, phone_name=phone_name, email= email,password=password)
            customer.password = make_password(customer.password)
            customer.save()
            return redirect('homepage')
        else:  
                
            return render(request,'signup.html',{'error':error_message,'values':value})
            
    
            
            
def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    # else:
    #     if request.method == 'POST':
    #         first_name = request.POST.get('firstname')
    #         last_name = request.POST.get('lastname')
    #         phone_name = request.POST.get('phone')
    #         email = request.POST.get('email')
    #         password = request.POST.get('password')
    else:
        if request.method == 'POST':
            return registerUser(request)
            
            
           
            # validation
            # value = {
            #     'first_name' : first_name,
            #     'last_name'  : last_name,
            #     'phone_name' : phone_name,
            #     'email'      : email,
            # }
            
            # error message=None
            # if(not first_name):
            #     error_message = "First Name Required"
            # elif not first_name:
            #     if len(first_name)<4:
            #         error_message = 'First Name must be 4 charctore'  
            # elif not last_name:
            #     if len(last_name)<4:
            #         error_message = 'last Name must be 4 charctore' 
            # elif not  phone_name:
            #      error_message = 'phone Number reuuired' 
            # elif len(phone_name)<10:
            #     error_message = 'Phone No must be 10 char long' 
            # elif len(email)<5:
            #     error_message = 'email must be 5 char long' 
            
            # elif Custmore.objects.filter(email=email).exists():
            #     error_message = 'Email is already exist'
            #     print('email already exist')
                         
                       
                 
                          
            
            # #saving
            # if not error_message:
            #     customer = Custmore(first_name=first_name,last_name=last_name, phone_name=phone_name, email= email,password=password)
            #     customer.password = make_password(customer.password)
            #     customer.save()
            #     return redirect('homepage')
            # else:  
                
            #     return render(request,'signup.html',{'error':error_message,'values':value})





def login(request):
    if request.method =='GET':
        return render(request,'login.html') 
    else:
      if request.method =='POST':
        email= request.POST.get('email')
        password=request.POST.get('password')
    try:
        customer= Custmore.objects.get(email=email)
         
        error_message = None   #Agr customer he to es case me password check krna pdega mtlab hash password ko real password se
        if customer:
            flag=check_password(password,customer.password)
            
            if flag:
                return redirect('homepage')
            else:
              error_message='Email or password Invalid'  
    except:          
       # else:
            error_message='Email or password Invalid'
           
            return render(request,'login.html',{'error':error_message})
            
    
      