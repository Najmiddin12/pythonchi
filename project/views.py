from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import SignupForm, LoginUserForm, EditProfileForm, UpdateUserForm, UpdateProfileForm
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Student, Group, Course, Modul, Homework, Lesson, Chat, Books, Certificate, Uyishi, ModulStatus
from django.views.generic import View
from django.contrib.auth.decorators import login_required

def home(request):
    courses = Course.objects.all()
    return render(request, 'project/index.html', {"courses": courses})

def signUp(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            signup = form.save()
            login(request, signup, backend='django.contrib.auth.backends.ModelBackend')
        return redirect(to='home')

    else:
        form = SignupForm()
    return render(request, 'project/signup.html', {"form": form})

def logOut(request, pk):
    student = Student.objects.get(pk=pk)
    if student is not None:
        logout(request)
        return redirect('home')
    return render(request, "layout/nav.html", {"student": student})


class logInModelView(generic.View):
    template_name = 'project/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        user = Student.objects.filter(username=username, last_name=last_name, password=password).first()

        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
        else:
            return redirect('signup')


def profile(request, pk):
    student = Student.objects.get(pk=pk)
    courses = Course.objects.all()
    groups = Group.objects.all().filter(student=student)
    return render(request, 'project/my-course.html', {"student": student, "groups": groups, "courses": courses})

def allCourses(request, pk):
    courses = Course.objects.all()
    student = Student.objects.get(pk=pk)
    return render(request, 'project/all-course.html', {"courses": courses, "student": student})

def settings(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, "project/users-profile.html", {"student": student})

def chat(request, pk):
    chats = Chat.objects.all()
    student = Student.objects.get(pk=pk)
    comments = Uyishi.objects.all().filter(student=student)
    return render(request, "project/chat.html", {"chats": chats, "student": student, "comments": comments})

def books(request, pk):
    books = Books.objects.all()
    student = Student.objects.get(pk=pk)
    return render(request, "project/book.html", {"books": books, "student": student})

def certificate(request, pk):
    student = Student.objects.get(pk=pk)
    certificate = Certificate.objects.all().filter(student=student)
    return render(request, "project/certificate.html", {"certificate": certificate, "student": student})

def moduls(request, pk, name):
    student = Student.objects.get(pk=pk)
    group = Group.objects.get(name=name)
    status = ModulStatus.objects.all().filter(group=group)
    return render(request, "project/course-detail.html", {"moduls": moduls, "group": group, "student": student, "status": status})

def lesson(request, pk, aydi, name):
    student = Student.objects.get(pk=pk)
    group = Group.objects.get(pk=aydi)
    modul = Modul.objects.get(name=name)
    lesson = Lesson.objects.all().filter(group__lesson__modul=modul)
    homeworks = Homework.objects.all().filter(modul__name=modul.name)
    moduls = ModulStatus.objects.all().filter(group=group)
    if request.method == "POST":
        homework = request.FILES.get("homework")
        Uyishi(student=student, modul=modul, homework=homework).save()
        return redirect(to='moduls')
    return render(request, "project/lesson.html", {"modul": modul, "group":group, "lesson": lesson, "student": student, "homeworks": homeworks, "moduls": moduls})

def homework(request, pk, aydi, name, id):
    student = Student.objects.get(pk=pk)
    group = Group.objects.get(pk=aydi)
    modul = Modul.objects.get(name=name)
    homework = Homework.objects.get(id=id)
    homeworks = Homework.objects.all().filter(modul__name=modul.name)
    moduls = ModulStatus.objects.all().filter(group=group)
    lesson = Lesson.objects.all().filter(modul__name=modul.name)
    try:
        uyi = Uyishi.objects.get(student=student, group=group, modul=modul, hw=homework)
        return render(request, "project/homework.html",
               {"modul": modul, "lesson": lesson, "group": group, "student": student, "homework": homework, "homeworks": homeworks, "uyishi": uyi, "moduls": moduls})
    except Uyishi.DoesNotExist:
        if request.method == "POST":
            homework_text = request.POST.get('homework')  # Assuming the input field's name is 'homework_text'

            # Create a new Uyishi instance and save it
            uyishi = Uyishi(student=student, group=group, modul=modul, hw=homework, homework=homework_text)
            uyishi.save()

            return redirect('homework', pk=student.pk, aydi=group.pk, name=modul.name, id=homework.id)
        return render(request, "project/uyishi.html",
               {"modul": modul, "group": group, "lesson": lesson, "student": student, "homework": homework, "homeworks": homeworks, "moduls": moduls})


@login_required
def edit_profile(request, pk):
    if request.POST:

        student = Student.objects.get(pk=request.user.id)
        student.username = request.POST.get('username')
        student.last_name = request.POST.get('last_name')
        student.about = request.POST.get('about')
        student.address = request.POST.get('address')
        student.age = request.POST.get('age')
        student.edu_name = request.POST.get('edu_name')
        student.number = request.POST.get('number')
        student.telegram = request.POST.get('telegram')
        student.linkedin = request.POST.get('linkedin')
        student.github = request.POST.get('github')
        student.save()

        return redirect('settings', pk=student.pk)

    student = Student.objects.get(pk=pk)
    return render(request, 'project/users-profile.html', {'student': student})