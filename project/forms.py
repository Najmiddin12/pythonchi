from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Student, Uyishi, Homework

"""
class UserPublicDetailsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['user'].widget.attrs.update({
            'hidden': "hidden"
        })

        self.fields['user'].widget.attrs.update({
            'hidden': "hidden"
        })

        self.fields['bio'].widget.attrs.update({
            "rows": "3"
        })

        self.fields['currently_hacking_on'].widget.attrs.update({
            "rows": "2"
        })

        self.fields['currently_learning'].widget.attrs.update({
            "rows": "2"
        })

        self.fields['skills_language'].widget.attrs.update({
            "rows": "2",
            "placeholder": "eg: django, python, java, javascript"
        })

        self.fields['education'].widget.attrs.update({
            "rows": "3"
        })
        self.fields['work'].widget.attrs.update({
            "rows": "3"
        })

    class Meta:
        model = Student
        fields = "__all__"


class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your first name'
        })

        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })

    class Meta:
        fields = ['first_name', 'password']


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your first name'
        })

        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your last name'
        })

        self.fields['number'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your phone number'
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm your password'
        })

    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    number = forms.CharField(max_length=150)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'number', 'password1', 'password2']
"""

class LoginUserForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["username", "last_name", "password"]

class SignupForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["username", "last_name", "number", "password"]

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['username', 'last_name', 'about', 'address', 'age', 'edu_name', 'number', 'telegram', 'linkedin', 'github']

class HomeworkForm(forms.Form):
    student = forms.ModelChoiceField(queryset=Student.objects.all())
    hw = forms.ModelChoiceField(queryset=Homework.objects.all())
    homework = forms.CharField(max_length=25555)


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username',]


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Student
        fields = ['last_name', 'about', 'address', 'age', 'edu_name', 'number', 'telegram', 'linkedin', 'github']
