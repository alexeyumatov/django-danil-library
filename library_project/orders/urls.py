from django.urls import path

from .views import CreateOrder, OrderListView, CreateFeedbackView

urlpatterns = [
    path(
        'create_order/<int:book_id>/',
        CreateOrder.as_view(),
        name='create_order'
    ),
    path('profile/', OrderListView.as_view(), name='profile'),
    path('feedback/', CreateFeedbackView.as_view(), name='feedback'),
]
