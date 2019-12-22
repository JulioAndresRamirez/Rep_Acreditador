from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Asistente
from .forms import AsistenteForm
import re

from django.contrib.auth.models import User, Group


class index(LoginRequiredMixin, TemplateView):
    template_name = 'core/index.html'
    form_class = AsistenteForm()


    def get(self, request, *args, **kwargs):
        context = Asistente.objects.all()
        return render(request, self.template_name, {'asistentes': context, 'form': self.form_class})


class UpdateAsistente(View):

    def get(self, request, pk, *args, **kwargs):
        Asis = Asistente.objects.get(pk=self.kwargs['pk'])
        Asis.validador = True
        Asis.save()
        return redirect(reverse_lazy('index') + '?ok')


class SearchAsistente(View):
    form_class = AsistenteForm
    template_name = 'core/index.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            if re.match('\d{7,8}-[0-9kK]',request.POST['text']):
                Asis = Asistente.objects.filter(identificador=request.POST['text'], validador=False)
                success = True
            else:
                Asis = Asistente.objects.filter(nombre__icontains=request.POST['text'], validador=False)
                success = False

            if Asis.exists():
                return render(request, self.template_name, {'asistentes': Asis, 'form': self.form_class, 'success': success})

        return redirect(reverse_lazy('index') + '?fail')





