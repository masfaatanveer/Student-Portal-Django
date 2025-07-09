from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContactForm

class HomeView(TemplateView):
    template_name = "index.html"

class AboutView(TemplateView):
    template_name = "about.html"

class ServicesView(TemplateView):
    template_name = "services.html"

class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('home:home')
    
    def form_valid(self, form):
        form.save()
        messages.success(
            self.request, 
            "Your message has been received! We'll contact you soon."
        )
        return super().form_valid(form)