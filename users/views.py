from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

from .forms import CustomuserCreationForm

class SignupPageView(generic.CreateView):
    form_class = CustomuserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'