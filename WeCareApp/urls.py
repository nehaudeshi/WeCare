from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('gethelp', views.gethelp, name='gethelp'),
    path('volunteer', views.volunteer, name='volunteer'),
    path('blogs', views.blogs, name='blogs'),
    path('contact', views.contact, name='contact'),
    path('profile', views.profile, name='profile'),
    path('signout',views.signoutView, name='signout'),
    path('customSignUp',views.customSignUp, name='customSignUp'),
    path('newBlog',views.newBlog, name='newBlog'),
    path('customLogin',views.customLogin, name='customLogin'),
    # path('editTarget',views.editTarget, name='editTarget'),
]




# <li><a href="/gethelp">Get Help</a></li>
# <li><a href="/volunteer">Volunteer</a></li>
# <li><a href="/blogs">Blogs</a></li>
# <li><a href="/contact">Contact</a></li>
