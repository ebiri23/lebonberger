from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from church.models import Conversation, Utalk, Letter, Lettera

# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def indexa(request):
    
    return render(request, 'indexa.html')

def register(request):
    if request.user.is_authenticated:
                return redirect('/')
    elif request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('signin')
        else:
            messages.info(request, 'Password not the same')
            return redirect('register')
    else:
   
      return render(request, 'register.html')

def signin(request):
    if request.user.is_authenticated:
                return redirect('/')
    
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect ('signin')
    
    else:
        return render (request, 'signin.html')
    
def signout(request):
    auth.logout(request)
    return redirect('/')
    
def reqchat(request):
    return render(request, 'reqchat.html')

def conversation(request, conversation):
    username = request.GET.get('username')
    conversation_details = Conversation.objects.get(name=conversation)
    return render(request, 'conversation.html', {
        'username': username,
        'conversation': conversation,
        'conversation_details': conversation_details
    })

def seenokay(request):
    conversation = request.POST['conversation_name']
    username = request.POST['username']

    if Conversation.objects.filter(name=conversation).exists():
        return redirect('/'+conversation+'/?username='+username)
    else:
        new_conversation = Conversation.objects.create(name=conversation)
        new_conversation.save()
        return redirect('/'+conversation+'/?username='+username)

def share(request):
    utalk = request.POST['utalk']
    username = request.POST['username']
    conversation_id = request.POST['conversation_id']

    new_utalk = Utalk.objects.create(value=utalk, user=username, conversation=conversation_id)
    new_utalk.save()
    return HttpResponse('Message sent successfully')

def getUtalks(request, conversation):
    conversation_details = Conversation.objects.get(name=conversation)

    utalks = Utalk.objects.filter(conversation=conversation_details.id)
    return JsonResponse({"utalks":list(utalks.values())})

def letter(request):
     name = request.POST['name']
     phone = request.POST['phone']
     email = request.POST['email']
     subject = request.POST['subject']
     message = request.POST['message']

     new_letter = Letter.objects.create(name=name, phone=phone, email=email, subject=subject, message=message)
     new_letter.save()
     return redirect('/')

def lettera(request):
     name = request.POST['name']
     phone = request.POST['phone']
     email = request.POST['email']
     subject = request.POST['subject']
     message = request.POST['message']

     new_lettera = Lettera.objects.create(name=name, phone=phone, email=email, subject=subject, message=message)
     new_lettera.save()
     return render(request, 'indexa.html')