from django.shortcuts import render, HttpResponse, redirect
from home.models import *
from blog.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, "home/home.html")

def about(request):
    return render(request, "home/about.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "please fill the form correctly!")
        else:
            contact = Contact(name = name, email = email, phone = phone, content = content)
            contact.save()
            messages.success(request, "Your Message sent successfully.")
    return render(request, "home/contact.html")


def search(request):
    query = request.GET['query']
    if len(query)>78:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
        if allPosts.count() == 0:
            messages.warning(request, "No search result found . Please refine your query")
    params = {'allPosts':allPosts, 'query':query}
    return render(request, "home/search.html", params)


def answer(request):
    return render(request, "home/answer.html")

@login_required(login_url = 'handleLogin')
def user(request):
    return render(request, "home/user.html")


def handleSignup(request):
    if request.method == 'POST':
        # get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous inputs
        if len(username) > 10:
                    messages.error(request, "username must unser 10 charecter")
                    return redirect('home')

        if not username.isalnum():
                    messages.error(request, "username should only contain letters and numbers")
                    return redirect('home')

        if pass1 != pass2:
                    messages.error(request, "password do not match")
                    return redirect('home')


        #Create User
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "your account has been successfully created")
        return redirect('home')

    else:
        return HttpResponse(" 404 - Not Found ")


def handleLogin(request):
    if request.method == 'POST':
        # get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "successfully login")
            return redirect('home')
        else:
            messages.error(request, "Invalid credential plesae try again")  
            return redirect('home')
    
    return HttpResponse(" 404 - Not Found ")

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logout !")
    return redirect('home')


    