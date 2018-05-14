from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

from .views import home, LoginView, UserProfileView, RegisterView, AccountValidationView

urlpatterns = [
    # url(r'^social/myauth/$', VkView.as_view(), name='vkauth'),
    url(r'^login/$', LoginView.as_view(template_name='core/login.html'), name='login'),
    url(r'^logout/$', login_required(LogoutView.as_view()), name='logout'),
    url(r'^registration/$', RegisterView.as_view(), name='registration'),
    url(r'^confirmation/(?P<pk>[-\w]+)/$', AccountValidationView.as_view(), name='confirmation'),
    url(r'^profile/$', UserProfileView.as_view(), name='profile'),
    url(r'$', home, name='home'),
    url(r'^.*?/$', home)
]
