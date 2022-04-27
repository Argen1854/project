from django.shortcuts import get_object_or_404, render
from django.views import generic
from . import models

class ProductList(generic.ListView):
    template_name = 'index.html'
    queryset = models.Product.objects.all()

    def get_queryset(self):
        if self.request.GET.get('search') == None:
            return super().get_queryset()
        a = self.request.GET.get('search')
        return models.Product.objects.filter(title__icontains=a)


class DetailView(generic.DetailView):
    template_name = 'detail.html'

    def get_object(self, **kwargs):
        id = self.kwargs.get('id')
        return get_object_or_404(models.Product, id=id)

