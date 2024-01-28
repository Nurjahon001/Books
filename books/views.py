from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView, View
from .models import Books

class BookList(View):
    def get(self,request):
        books=Books.objects.order_by('create_at')
        context={
            'books':books
        }
        return render(request,'book/book_list.html',context=context)


class BookDetailView(View):
    def get(self,request,pk):
        # book = get_object_or_404(Books, pk=pk)
        book=Books.objects.get(pk=pk)
        context = {
            'book': book
        }
        return render(request,'book/book_detail.html',context=context)
