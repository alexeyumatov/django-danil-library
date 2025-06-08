from django.views import View
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import FeedbackForm
from .models import Order
from books.models import Book


class CreateOrder(View):
    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)

        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        user_address = request.POST.get('user_address')
        comment = request.POST.get('comment')

        if user_name and user_email and user_address and comment:
            Order.objects.create(
                book=book,
                user_name=user_name,
                user_email=user_email,
                user_address=user_address,
                comment=comment
            )
            messages.success(request, 'Заказ успешно создан!')
        else:
            messages.error(request, 'Не все поля заполнены!')
        return redirect('detail_book', pk=book_id)


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'profile.html'
    context_object_name = 'orders'
    login_url = 'login'

    def get_queryset(self):
        return Order.objects.filter(user_email=self.request.user.email)


class CreateFeedbackView(CreateView):
    form_class = FeedbackForm
    template_name = 'feedback.html'
    success_url = '/'

    def form_valid(self, form):
        messages.success(self.request, 'Обратная связь успешно отправлена!')
        return super().form_valid(form)
