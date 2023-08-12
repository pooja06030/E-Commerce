from django.shortcuts import render,redirect
from store.models.customer import Custmore
from django.contrib import messages
from django.contrib.auth.hashers import check_password



# print(make_password('1234'))
# print(check_password('1234','pbkdf2_sha256$390000$mRzLxWwq6VFxXO10UpiV8U$Ds3Zhv4vfrwInBS3T2HgOw5ke61pRhI0L6ss7a2LFKg='))
# # Create your views here.

def login(request):     # jese aapne login kiya means custmore ne login kiya to me uski infonamtion ko save krna chahta hu session me
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
            flag=check_password=(password,customer.password)
            
            if flag:
                 #request.session se ek session dictionery milega esme mene value set kr di customer
                request.session['customer_email']=customer.email#information save hone ke bad hm check krenge aap konse user ho index ya home page pr
                request.session['customer']=customer.id
                return redirect('homepage')
            else:
              error_message='Email or password Invalid'  
    except:          
       # else:
            error_message='Email or password Invalid'
           
            return render(request,'login.html',{'error':error_message})
        


def logout(request):       #Agr hm session ko clear kr dete to hm logout ho jayenge
    request.session.clear() 
    return redirect('login')    