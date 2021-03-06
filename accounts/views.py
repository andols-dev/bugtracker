from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def startpage(request):
    return render(request,'startpage.html')
    # return HttpResponse('this is the page you see when ypu have logged in')

def sign_up_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}')
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    
    return render(request, 'accounts/sign_up.html',context)