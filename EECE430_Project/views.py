from django.shortcuts import render, redirect


def homepage(request):
    return render(request, 'cars/homepage.html')


def account_redirect(request):
    return redirect('accounts:profile', username=request.user.username)
