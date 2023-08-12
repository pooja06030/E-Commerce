from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import Category
from store.middlewares.auth import auth_Middleware


#Add to cart function
@auth_Middleware
def index(request):
    print('############################')
    products=None
    category=Category.objects.all()
    categoryID=request.GET.get('categories')
    if categoryID:
        products=Product.objects.filter( category=categoryID)
        print('######################',products)
    else:
        products=Product.objects.all()
    context = {'products':products,'category':category,}  # hm yha request krenge index page pr or pta krenge aap konse user ho to yha email or customer id ko print kryayenge kyuki login pr to hmne uski id or customer email save kiya ab index page prjayga to index page check krega aap konse user ho
    print('you are' ,request.session.get('customer_email'))
    return render(request,'index.html',context)


#Add card function
def index_1(request):
    print('#################post',index_1)  #ek hi product pr duble click krne se uski qwantity encrise ho jayegi
    if request.method=='POST':
        product = request.POST.get('product') #esme profit ye he ki me bina login ke bhi session ko manage kr pa rhi hu
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                cart[product]=quantity+1
            else:
                cart[product]=1    
        else:
            cart ={}
            cart['product']=1
        
        request.session['cart']=cart  
        print('go to' ,request.session.get('cart')) 
            
        return redirect('homepage')
  

