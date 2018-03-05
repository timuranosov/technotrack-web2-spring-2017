from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import User


class UserProfileView(DetailView):
    template_name = 'core/profile.html'
    model = User

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        return context


def home(request):
    return render(request, template_name='core/vkhome.html')
