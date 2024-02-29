from django.urls import path
from .views import home, signUp, logInModelView, profile, edit_profile, logOut, allCourses, chat, certificate, books, moduls, lesson, homework

urlpatterns = [
    path('', home, name="home"),
    path('signup/', signUp, name="signup"),
    path('login/', logInModelView.as_view(), name="login"),
    path('profile/<int:pk>', profile, name="profile"),
    path('profile/<int:pk>/settings', edit_profile, name="settings"),
    path('profile/<int:pk>/logout', logOut, name="logout"),
    path('profile/<int:pk>/all-courses', allCourses, name="all-courses"),
    path('profile/<int:pk>/chat', chat, name="chat"),
    path('profile/<int:pk>/books', books, name="books"),
    path('profile/<int:pk>/certificate', certificate, name="certificate"),
    path('profile/<int:pk>/modul-<str:name>', moduls, name="moduls"),
    path('profile/<int:pk>/<int:aydi>/lesson-<str:name>', lesson, name="lesson"),
    path('profile/<int:pk>/<int:aydi>/lesson-<str:name>/homework-<int:id>', homework, name="homework"),
]