from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView, View
from .models import Books,BookReview
from django.contrib.auth.mixins import  LoginRequiredMixin
class BookList(LoginRequiredMixin,View):
    def get(self,request):
        books=Books.objects.order_by('create_at')
        search_query=request.GET.get('q')
        if search_query:
            books=books.filter(title__icontains=search_query)
        # context={
        #     'books':books
        # }

        paginator = Paginator(books, 2)  # Show 10 books per page
        page = request.GET.get('page')
        try:
            books = paginator.page(page)
        except PageNotAnInteger:
            books = paginator.page(1)
        except EmptyPage:
            books = paginator.page(paginator.num_pages)

        return render(request,'book/book_list.html',{'books':books})


class BookDetailView(LoginRequiredMixin,View):
    def get(self,request,pk):
        # book = get_object_or_404(Books, pk=pk)
        book=Books.objects.get(pk=pk)
        # book_review=BookReview.objects.all()
        context = {
            'book': book,
            # 'book_review':book_review
        }
        return render(request,'book/book_detail.html',context=context)
