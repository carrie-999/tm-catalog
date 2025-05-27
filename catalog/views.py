from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import NameRegistration
from .forms import NameRegistrationForm

from django.http import HttpResponse

def test_view(request):
    return HttpResponse("🍀 TEST OK 🍀")


class NameListView(ListView):
    model = NameRegistration
    template_name = 'catalog/name_list.html'
    context_object_name = 'names'
    paginate_by = 20

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(name__icontains=q)
        status = self.request.GET.get('status')
        if status:
            qs = qs.filter(status=status)
        order = self.request.GET.get('order', 'name')
        return qs.order_by(order)

class NameCreateView(LoginRequiredMixin, CreateView):
    model = NameRegistration
    form_class = NameRegistrationForm
    template_name = 'catalog/register.html'
    success_url = reverse_lazy('catalog:list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
