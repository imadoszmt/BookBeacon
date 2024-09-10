from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Book, Request, Notification
from .forms import UserRegistrationForm, BookRequestForm

@ensure_csrf_cookie
def home(request):
    return render(request, 'core/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = UserRegistrationForm()
    return render(request, 'core/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid credentials'})
    return render(request, 'core/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request):
    return render(request, 'core/profile.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'core/book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'core/book_detail.html', {'book': book})

@login_required
def request_list(request):
    requests = Request.objects.filter(user=request.user)
    return render(request, 'core/request_list.html', {'requests': requests})

@login_required
def create_request(request):
    if request.method == 'POST':
        form = BookRequestForm(request.POST)
        if form.is_valid():
            book_request = form.save(commit=False)
            book_request.user = request.user
            book_request.save()
            return redirect('request_list')
    else:
        form = BookRequestForm()
    return render(request, 'core/create_request.html', {'form': form})

@login_required
def notification_list(request):
    notifications = Notification.objects.filter(user=request.user)
    return render(request, 'core/notification_list.html', {'notifications': notifications})