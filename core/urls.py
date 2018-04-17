from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

from .views import home, UserProfileView, RegisterView

urlpatterns = [
    # url(r'^social/myauth/$', VkView.as_view(), name='vkauth'),
    url(r'^login/$', LoginView.as_view(template_name='core/login.html'), name='login'),
    url(r'^logout/$', login_required(LogoutView.as_view()), name='logout'),
    url(r'^registration/$', RegisterView.as_view(), name='registration'),
    url(r'^profile/$', UserProfileView.as_view(), name='profile'),
    url(r'$', home, name='home'),
    url(r'^.*?/$', home)
]
