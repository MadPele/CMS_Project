from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import User, Message, Topic
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.db import IntegrityError


class Login(TemplateView):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        nick = request.POST.get('nick')
        password = request.POST.get('password')
        user = User.objects.get(nick=nick, password=password)
        if user:
            request.session['user'] = user.nick
            return redirect(reverse('home'))
        else:
            error = "Such User don't exist"
            return render(request, 'login.html', {'error': error})


class Register(TemplateView):

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        if request.POST.get('password') != request.POST.get('password2'):
            error_pass = 'Passwords are different'
            return render(request, 'register.html', {'error_pass': error_pass})

        try:
            nick = request.POST.get('nick')
            email = request.POST.get('email')
            password = request.POST.get('password')
            User.objects.create(nick=nick, email=email, password=password)
            return HttpResponse(f'{nick} created')
        except IntegrityError:
            error_nick_or_email = "Nick/Email is already registered"
            return render(request, 'register.html', {'error_nick_or_email': error_nick_or_email})


class ResetPassword(TemplateView):

    def get(self, request):
        return render(request, 'resetpassword.html')

    def post(self, request):

        nick = request.POST.get('nick')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.get(nick=nick)

        if user.email == email:

            if request.POST.get('password') != request.POST.get('password2'):
                error_pass = 'Passwords are different'
                return render(request, 'resetpassword.html', {'error_pass': error_pass})

            user.password = password
            return HttpResponse('Password has been reset')

        error_nick_or_email = "Such User don't exist"
        return render(request, 'resetpassword.html', {'error_nick_or_email': error_nick_or_email})


class Home(TemplateView):

    def get(self, request):
        if request.session.get('user'):
            topics = Topic.objects.all()
            user = request.session.get('user')
            return render(request, 'home.html', {'topics': topics, 'user': user})
        else:
            return redirect(reverse('login'))


class ShowTopic(TemplateView):

    def get(self, request, topic_id):
        if request.session.get('user'):
            user = request.session.get('user')
            topic = Topic.objects.get(pk=topic_id)
            print(topic.message)
            print(topic.message)
            print(topic.message)
            print(topic.message)
            print(topic.message)
            return render(request, 'show_topic.html', {'user': user, 'topic': topic, 'messages': messages})
        else:
            return redirect(reverse('login'))


class AddMessage(TemplateView):

    def get(self, request, topic_id):
        if request.session.get('user'):
            topic = Topic.objects.get(pk=topic_id)
            user = request.session.get('user')
            return render(request, 'add_message.html', {'user': user, 'topic': topic})
        else:
            return redirect(reverse('login'))


class AddTopic(TemplateView):

    def get(self, request):
        if request.session.get('user'):
            user = request.session.get('user')
            return render(request, 'add_topic.html', {'user': user})
        else:
            return redirect(reverse('login'))

    def post(self, request):
        name = request.POST.get('name')
        topic = Topic.objects.create(name=name)
        return redirect(reverse('show_topic', kwargs={'topic_id': topic.id}))


class Logout(TemplateView):

    def get(self, request):
        if request.session.get('user'):
            request.session['user'] = ''
            return redirect(reverse('login'))
        else:
            return redirect(reverse('login'))

