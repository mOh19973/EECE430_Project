from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from .models import ProfilePhoto
from .forms import PhotoForm


def addphoto(request, username):
    user = User.objects.get(username=username)
    form = PhotoForm()
    if request.method=='POST':
        photo = request.POST['userImg']
        try:
            p = ProfilePhoto.objects.get(userPhoto=user)
            p.userImg = photo
            p.save()

        except ObjectDoesNotExist:
            ProfilePhoto.objects.create(userImg=photo, userPhoto=user)
        return redirect('accounts:profile', username)
    return render(request, 'userphoto/edit_pic.html', {'form': form})
