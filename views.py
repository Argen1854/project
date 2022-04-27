from django.forms import forms
from django.shortcuts import get_object_or_404, render
from django.views import generic
from . import models, forms
# Create your views here.

class BookListView(generic.ListView):
    template_name = "book/booklist.html"
    queryset = models.BookList.objects.all()

    def get_queryset(self):
        return models.BookList.objects.all()

    
class BookDetailView(generic.DetailView):
    template_name = 'book/bookdetail.html'
    
    def get_object(self, *kwargs):
        id = self.kwargs.get('id')
        return get_object_or_404(models.BookList, id=id)


class CreateBookView(generic.CreateView):
    template_name = 'book/add_book.html'
    form_class = forms.ListBook
    queryset = models.BookList.objects.all()
    success_url = '/book/'

    def form_valid(self, form):
        return super().form_valid(form=form)
    
class UpdateBookView(generic.UpdateView):
    template_name = 'book/update.html'
    form_class = forms.ListBook
    success_url = '/book/'

    def get_object(self, *kwargs):
        id = self.kwargs.get('id')
        return get_object_or_404(models.BookList, id=id)

    def form_valid(self, form):
        return super(UpdateBookView, self).form_valid(form=form)


class DeleteBook(generic.DeleteView):
    template_name = 'book/delete.html'
    success_url = '/book/'

    def get_object(self, *kwargs):
        id = self.kwargs.get('id')
        return get_object_or_404(models.BookList, id=id)

