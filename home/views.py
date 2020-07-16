from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# HTML Pages
def home(request):
    return render(request, 'home/home.html')

def about(request):
    messages.success(request, 'This is about page')
    return render(request, 'home/about.html')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<5:
            messages.error(request, 'Invalid Information')
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, 'Your message has been successfully sent!')
    return render(request, 'home/contact.html')

def search(request):
    query = request.GET['query']
    if len('query') > 70:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
    
    if allPosts.count() == 0:
        messages.warning(request, 'No search result founds!')
    params = {'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)

# Authentication APIs
def handleSignup(request):
    if request.method == 'POST':
        # Get the post's parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        #Check for erroeneous inputs
        if len(username) > 10:
            messages.error(request, 'Your username must be under 10 character!')
            return redirect('/')
        if not username.isalnum():
            messages.error(request, 'Your username must contain alpha numeric!')
            return redirect('/')
        if password1 != password2:
            messages.error(request, 'Password do not match!')
            return redirect('/')

        # Create the user
        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname 
        myuser.last_name = lname 
        myuser.save()
        messages.success(request, 'Your account has been successfully created!')
        return redirect('/')
    
    else:
        return HttpResponse('404 - Page Not Found')

def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpass']
        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully Logged In!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials, Please try agani')
            return redirect('home')

    return HttpResponse('404 - Page Not Found')

def handleLogout(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out')
    return redirect('home')
