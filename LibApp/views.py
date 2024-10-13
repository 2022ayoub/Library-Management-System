from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import BookForm,CategoryForm
# Create your views here.

def index(request):

    if request.method == 'POST' :
        addBook=BookForm(request.POST,request.FILES)
        if addBook.is_valid():
            addBook.save()
    

    if request.method == 'POST' :
        addCategory=CategoryForm(request.POST)
        if addCategory.is_valid():
            addCategory.save()

    
    context={
        'books':Book.objects.all(),
        'categories':Category.objects.all(),
        'form':BookForm(),
        'formCategory':CategoryForm(),
        'nbreBooks':Book.objects.filter(active=True).count(),
        'soldBooks':Book.objects.filter(status='sold').count(),
        'rentalBooks':Book.objects.filter(status='rental').count(),
        'availableBooks':Book.objects.filter(status='available').count(),
    }
    smSold=0
    smRental=0
    for item in context['books']:
        if item.status == 'sold' and item.price :
            smSold+=float(item.price)
        elif item.status == 'rental' and  item.rental_period and item.rental_price_day :
            smRental+=(int(item.rental_period)*float(item.rental_price_day))
    context['profit']=( smRental + smSold)
    context['profitSold']=(smSold)
    context['profitRental']=( smRental)

    return render(request,'pages/index.html',context)

def books(request):
    search=Book.objects.all()
    title=None
    if 'search_name' in request.GET:
        title=request.GET['search_name']
        if title:
            search=search.filter(title__icontains=title)

    if request.method == 'POST' :
        addCategory=CategoryForm(request.POST)
        if addCategory.is_valid():
            addCategory.save()
    context={
        # 'books':Book.objects.all(),
        'books':search,
        'categories':Category.objects.all(),
        'formCategory':CategoryForm(),
    }
    return render(request,'pages/books.html',context)

def delete(request,id):
    deleteBook=get_object_or_404(Book,id=id)
    # if request.method == 'POST' :
    #     addCategory=CategoryForm(request.POST)
    #     if addCategory.is_valid():
    #         addCategory.save()
    if request.method == 'POST' :
        deleteBook.delete()
        return redirect('/')
    context={
        'books':Book.objects.all(),
        'categories':Category.objects.all(),
        'formCategory':CategoryForm(),
    }
    return render(request,'pages/delete.html',context)


def update(request,id):
    idBook=Book.objects.get(id=id)
    if request.method == 'POST' :
        addCategory=CategoryForm(request.POST)
        if addCategory.is_valid():
            addCategory.save()
    if request.method == 'POST' :
        upBook=BookForm(request.POST,request.FILES,instance=idBook)
        if upBook.is_valid():
            upBook.save()
            return redirect('/')
    else:
        upBook=BookForm(instance=idBook)
    context={
        'books':Book.objects.all(),
        'categories':Category.objects.all(),
        'formCategory':CategoryForm(),
        'form':upBook,
    }
    return render(request,'pages/update.html',context)