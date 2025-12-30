from django.forms import ModelForm

from . models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["name", "email", "phone_number", "amount"]
        labels = {
            'name': 'نام',
            'email': 'ایمیل',
            'phone_number': 'شماره تلفن',
            'amount': 'تعداد',
        }
        error_messages = {
            'name': {'required': 'نام الزامی است.'},
            'phone_number': {'required': 'شماره تلفن الزامی است.'},
            'amount': {'required': 'تعداد الزامی است.'},
        }
