from django.shortcuts import render
from django.views.generic import FormView 
from . import kavano
from . import forms
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from app.views import ProductList
from django.http import HttpResponse

class ParserFormView(FormView):
    template_name = 'parser.html'
    form_class = forms.ParserForm

    def post(self, request, *args, ** kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parse_data()
            return HttpResponse('sdfsa')
            # return redirect(reverse("ProductList"))
            print('aaa')
        else:
            return super(ParserFormView, self).post(request, *args, **kwargs)