from django.shortcuts import render, redirect
from .models import Practice

# Create your views here.
def index(request):
  context={
    'saying': Practice.objects.all(),
  }
  return render(request, 'practice/index.html', context)

def create(request):
  return render(request, 'practice/create.html')

def created(request):
  title = request.GET.get('title')
  content = request.GET.get('content')

  Practice.objects.create(title=title, content=content)

  return redirect('practice:index')

def delete(request, pk):
  Practice.objects.get(id=pk).delete()
  return redirect('practice:index')

def edit(request, pk):
  context = {
    'saying': Practice.objects.get(id=pk)
  }
  return render(request, 'practice/edit.html', context)

def edited(request, pk):
  new_title = request.GET.get('title')
  new_content = request.GET.get('content')

  saying = Practice.objects.get(id=pk)

  saying.title = new_title
  saying.content = new_content
  saying.save()

  redirect('practice:index')