#views.py #handling the posted data using forms and rendering the template

from django.http import HttpResponseRedirect
from .forms import MyForm
from django.shortcuts import render

def formview(request):
    if request.method=="POST":
       form = MyForm(request.POST)
       if form.is_valid():
          form.save()
          return HttpResponseRedirect('/success')
    else:
      form = MyForm()
      return render(request,'myform.html',{'form': form})
