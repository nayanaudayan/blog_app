# from django.shortcuts import render

# # Create your views here.

from imaplib import _Authenticator
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.http import JsonResponse
from requests import post





def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already exists'})
        
        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)
        # Do something with the user object (e.g. log the user in, redirect to the home page, etc.)

    return render(request, 'template/signup.html')



def login_view(request):
    if request.method == 'POST':
        # Process the form submission
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = _Authenticator(request, username=username, password=password)

        if user is not None:
            # Log in the user
            login(request, user)

            # Redirect to a success page or wherever you want
            return redirect('home')
        else:
            # You can add appropriate error handling here
            return redirect('login')

    # Render the login page
    return render(request, 'template/login.html')


def home_view(request):
    # posts = post.objects.all()  # Assuming you have a 'Post' model for your blog posts
    return render(request, 'template/home.html', )

def about_view(request):
    return render(request, 'template/about.html')

def base_view(request):
    return render(request, 'template/base.html')

def index_view(request):
    return render(request, 'template/index.html')

def postdetail_view(request):
    return render(request, 'template/post_detail.html')

def popular_view(request):
    return render(request, 'template/popular.html')


def addpost_view(request):
     msg=""
     if request.method == 'POST':
            po_title= request.POST['p_title']            
            po_num = request.POST['p_num']
            po_description = request.POST['p_description']
            po_author = request.POST['p_author']
            product_exist = Product.objects.filter(p_numb=po_num).exists()  
            if not product_exist:
                add_products = Product(
                    p_name = po_title,
                    p_number = po_num,
                    p_details = po_description,
                    p_author = po_author,
                    )                
                add_products.save()
                msg="Product Added Succesfully"
            else:
                 msg="product Already Added"

    # return render(request,'reseller_app/add_product.html',{'status':msg})

     return render(request, 'template/addpost.html' ,{'status':msg})

