from django.urls import path

from . import views
from items.views import ItemsListView

urlpatterns = [
    path('', ItemsListView.as_view(), name='home'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.SuccessView.as_view()),
    path('cancelled/', views.CancelledView.as_view()),

]
