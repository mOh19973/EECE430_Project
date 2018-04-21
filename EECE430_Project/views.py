from django.shortcuts import render, redirect


def homepage(request):
    user = request.user
    return render(request, 'homepage.html', {'user': user})


def account_redirect(request):
    return redirect('accounts:profile', username=request.user.username)
