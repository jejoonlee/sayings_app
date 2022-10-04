from django.shortcuts import render, redirect
from .models import Practice
from .forms import practiceForm

# Create your views here.
def index(request):
  context={
    'saying': Practice.objects.all(),
  }
  return render(request, 'practice/index.html', context)

def create(request):

  if request.method == "POST":
    practice = practiceForm(request.POST)

    if practice.is_valid():
      practice.save()
      return redirect('practice:index')

  else:
    practice_form = practiceForm()
  context = {
    'practice_form' : practice_form,
  }

  return render(request, 'practice/create.html', context)

# def created(request):
#   title = request.GET.get('title')
#   content = request.GET.get('content')

#   Practice.objects.create(title=title, content=content)

#   return redirect('practice:index')

def delete(request, pk):
  Practice.objects.get(id=pk).delete()
  return redirect('practice:index')

def edit(request, pk):
  saying = Practice.objects.get(id=pk)
  
  if request.method == 'POST':
    saying_form = practiceForm(request.POST, instance=saying)

    if saying_form.is_valid():
      saying_form.save()
      return redirect('practice:index')

  else:
    saying_form = practiceForm(instance=saying)
  context = {
    'saying_form': saying_form
  }
  return render(request, 'practice/edit.html', context)

# def edited(request, pk):
#   new_title = request.GET.get('title')
#   new_content = request.GET.get('content')

#   saying = Practice.objects.get(id=pk)

#   saying.title = new_title
#   saying.content = new_content
#   saying.save()

#   redirect('practice:index')