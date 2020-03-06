from django.urls import path

from misaghestan.payments.views import pay_online, show_checkout_index

app_name = "payments"
urlpatterns = [
    path('checkout', show_checkout_index, name='show_checkout_index'),
    path('checkout/<int:transaction_id>/pay_online', pay_online, name='pay_online'),]
