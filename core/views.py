from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from .forms import CustomUserCreationForm, CustomAuthenticationForm


def home(request):
    return render(request, 'core/index.html')

class SignUpView(View):
    template_name = 'core/signup.html'

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home page after successful registration
        return render(request, self.template_name, {'form': form})

class SignInView(View):
    template_name = 'core/signin.html'

    def get(self, request):
        form = CustomAuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page after successful login
        return render(request, self.template_name, {'form': form})

# Add view for book.
from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'core/book_list.html', {'books': books})
# End of view
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')