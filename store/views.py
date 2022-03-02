from django.shortcuts import render,redirect
from .models import Product,Customer,Category,Vendor
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from django.views import View
# Create your views here.

def index(request):
    if request.method == 'POST':
        product = request.POST.get('product')
        print(product)

        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product] = quantity + 1
            else:
                cart[product] = 1

        else:
            cart={}
            cart[product] = 1
        request.session['cart'] = cart
        return redirect('Index')
    if request.method == 'GET':
        products = Product.GetAllProducts()
        return render(request,'index.html',{'products':products})
def SignUp(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        PostData = request.POST
        first_name = PostData.get('firstname')
        last_name = PostData.get('lastname')
        email = PostData.get("email")
        passwrd = PostData.get('password')
        repass= PostData.get('repass')
        if passwrd != repass:
            return  HttpResponse("<h1>PASSWORD DIDNT MATCHED PLEASE FILL AGAIN</h1>")
        else:
            print(first_name,last_name,email,passwrd)
            custmr = Customer(first_name=first_name,
                              last_name= last_name,
                              email=email,
                              password=passwrd)
            custmr.password=make_password(custmr.password)
            custmr.register()
            return redirect("Index")
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer = Customer.getuser(email)
        if customer:
            flag = check_password(password,customer.password)
            if  flag == True:
                request.session['customer_id'] = customer.id
                request.session['customer_email'] = customer.email

                return redirect("Index")
            else:
                return HttpResponse('<h1>WRONG EMAIL OR PASSWORD</h1>')

        else:
            return HttpResponse('<h1>WRONG EMAIL OR PASSWORD</h1>')
def logout(request):
    request.session.clear()
    return redirect('Login')

def vendsingup(request):
    if request.method == 'GET':
        return render(request, 'vendor_signup.html')
    else:
        PoostData = request.POST
        first_name = PoostData.get('firstname')
        last_name = PoostData.get('lastname')
        email = PoostData.get("email")
        passwrd = PoostData.get('password')
        repass= PoostData.get('repass')
        if passwrd != repass:
            return  HttpResponse("<h1>PASSWORD DIDNT MATCHED PLEASE FILL AGAIN</h1>")
        else:
            print(first_name,last_name,email,passwrd)
            vend = Vendor(first_name=first_name,
                              last_name= last_name,
                              email=email,
                              password=passwrd)
            vend.password=make_password(vend.password)
            vend.save()
            return redirect("Index")
def cart(request):
    if request.method == 'GET':
        ids = list(request.session.get('cart').keys())
        product = Product.get_product_by_id(ids)
        print(product)
    return render(request, 'cart.html')



