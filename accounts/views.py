from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import generic, View
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'accounts/default_page.html'
    context_object_name = 'UserForm'

    def get_queryset(self):
        return UserForm.objects.all()


class UserFormView(View):
    form_class = UserForm
    template_name = 'accounts/RegistrationForm.html'

    # Display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # Cleaned normalised data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns user objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('cars/default_index.html')

        return render(request, self.template_name, {'form': form})
