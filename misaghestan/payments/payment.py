from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from zeep import Client

from misaghestan.subscriptions.models import SubscriptionTransaction, UserSubscription


class Zarinpal:

    zarinpal_errors = {
        -1: 'اطلاعات ارسال شده ناقص است',
        -2: 'آیپی یا مرچنت کد صحیح نیست',
        -3: 'سطح تایید پذیرنده کمتر از نقره ای است',
    }

    @classmethod
    def get_zarinpal_client(cls):
        zarinpal_client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
        return zarinpal_client

    @classmethod
    def checkout(cls, request) -> (any, str):
        """
        verify payment
        """

        authority = request.GET.get('Authority')
        status = request.GET.get('Status')
        transaction: SubscriptionTransaction = SubscriptionTransaction.objects.get(reservation=authority, paid=False)

        try:
            reference, verify_status = cls.zarinpal_verify(transaction.amount, authority)
            transaction.handle_successful_transaction(reference)
            
            return transaction , ''
        except Exception as e:
            return transaction, str(e)

    @classmethod
    def zarinpal_verify(cls, amount, authority) -> tuple:
        # result = cls.get_zarinpal_client().service.PaymentVerification(settings.ZARINPAL_MERCHANT_ID,
        #                                                                authority, amount)
        return 'asdasd', 100

        if result.Status == 100:
            return result.RefID, result.Status
        else:
            raise Exception(cls.zarinpal_errors[result.Status])

    @classmethod
    def zarinpal_payment_request(cls, user, amount, title, email, mobile) -> tuple:
        amount = amount  # Toman / Required
        description = title  # Required
        email = email  # Optional
        mobile = mobile  # Optional
        callback_url = reverse(settings.ZARINPAL_CALLBACK_URL)
        result = cls.get_zarinpal_client().service.PaymentRequest(settings.ZARINPAL_MERCHANT_ID, amount, description,
                                                                  email, mobile, callback_url)
        return str('23r42g34t34t43t43'), 100

        if result.Status == 100:
        # return str('23r42g34t34t43t43'), 100
            return str(result.Authority), result.Status
        else:
            raise Exception(cls.zarinpal_errors[result.Status])
