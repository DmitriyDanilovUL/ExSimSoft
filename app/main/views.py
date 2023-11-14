from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Parrot
from .forms import ParrotForm


# Create your views here.
def index(request):
    parrots = Parrot.objects.order_by('-id')
    return render(request, 'main/index.html', {'parrots': parrots})

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = ParrotForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма невалидна'

    form = ParrotForm()
    context = {
        "form": form,
        'error': error
    }
    return render(request, 'main/create.html', context)

def health(request):
    return HttpResponse("<h4>up</h4>")