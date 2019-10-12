from django.shortcuts import render, redirect, HttpResponse
from .models import Book, Author
def index(request):
    context = {
        "all_the_books": Book.objects.all()
    }
    return render(request, "books_authors_app/addabook.html", context)
def addbooks(request):
    Book.objects.create(title=request.POST['title'],desc=request.POST['description'])
    return redirect('/')
def renderbooks(request, theid):
    context = {
        "book": Book.objects.get(id=theid),
        "authors": Author.objects.all()
    }
    return render(request, "books_authors_app/bookdetails.html", context)
def addauthors(request, theid):
    book = Book.objects.get(id=theid)
    book.authors.add(Author.objects.get(id=request.POST['authorid']))
    return redirect(f"/books/{theid}")
def newauthor(request):
    context = {
        "all_the_authors": Author.objects.all()
    }
    return render(request,"books_authors_app/addanauthor.html", context)
def authoradded(request):
    Author.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],notes=request.POST['notes'])
    return redirect("/authors")
def authordetails(request, theid):
    context = {
        "author": Author.objects.get(id= theid),
        "all_the_books": Book.objects.all()
    }
    return render(request, "books_authors_app/authordetails.html", context)
def selectbook(request, theid):
    author = Author.objects.get(id=theid)
    author.books.add(Book.objects.get(id=request.POST['bookid']))
    return redirect(f"/authors/{theid}")


# Create your views here.
