from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


# Create your views here.
def login(request):
    return render(request, 'user_management/login.html')


def test(request):
    print("test")
    pass


class Register(CreateView):
    template_name = 'user_management/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)
