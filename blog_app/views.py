from django.shortcuts import render, HttpResponse, redirect
from blog_app.models import CreateBlog
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def home(request):
    allBlogs = reversed(CreateBlog.objects.all())
    context = {"allBlogs": allBlogs}
    return render(request, 'index.html', context)

def createBlog(request):
    if request.user is not None:
        if request.method == 'POST':
            title = request.POST['title']
            metaTitle = request.POST['metaTitle']
            metaDescription = request.POST['metaDescription']
            slug = request.POST['slug']
            blogBody = request.POST['blogBody']
            imageLink = request.POST['imageLink']
            author = request.user
            # print(title, metaTitle, metaDescription, slug, active, blogBody, imageLink)

            if(len(title) > 5 and len(metaTitle)>=5 and len(metaDescription)>=10 and len(slug)>=5 and len(blogBody)!='' and len(imageLink)!=''):
                blog = CreateBlog(title=title, metaTitle=metaTitle, metaDescription=metaDescription, slug=slug, body=blogBody, image=imageLink, author=author)
                blog.save()
                messages.success(request, "Blog created successfully")
                return redirect('home')
            else:
                messages.error(request, "failed to create blog")
                return render(request, "createBlog.html")
        else:
            messages.error(request, "failed to create blog")
            return render(request, "createBlog.html")     
    else:
        messages.error(request, "You must be logged in to create blog")
        return redirect("login")

def blog(request, slug):
    blog = CreateBlog.objects.filter(slug=slug).first()
    # print(blog)
    context = {"blog": blog}
    return render(request, "blog.html", context)

def handleLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "logged In successfully")
            return redirect('home')
        else:
            messages.error(request,"Invalid credentials")
            return redirect("login")
    else:
        return render(request, "login.html")
    

def handleSignup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # checking the validation of the inputs
        if not name.isalnum():
            messages.error(request,"Username Should only contain alphabet and numbers")
            return redirect('signup')

        if pass1 != pass2:
            messages.error(request,"Password did not match")
            return redirect('signup')

        # creating the user
        user = User.objects.create_user(name, email, pass1)
        user.save()
        messages.success(request,"User created successfully")
        return redirect('home')
    else:
        return render(request, "signup.html")
    


def handleLogout(request):
    logout(request)
    messages.success(request, "User logged out successfully")
    return redirect('home')