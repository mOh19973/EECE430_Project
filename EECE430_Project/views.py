from django.shortcuts import render, redirect


def homepage(request):
    return render(request, 'homepage.html')


def account_redirect(request):
    return redirect('accounts:profile', username=request.user.username)
