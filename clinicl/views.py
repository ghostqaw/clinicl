from django.shortcuts import render
from django.views.generic import TemplateView
from clinicApp.models import Slide, Doctor

class HomeView(TemplateView):
    template_name = 'html/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['slides'] = Slide.objects.all()
        context['user'] = user
        context['is_doctor'] = Doctor.objects.filter(iin=Doctor.iin).exists()  # Добавьте это
        return context





