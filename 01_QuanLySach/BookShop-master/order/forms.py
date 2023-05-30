from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	DIVISION_CHOICES = (
		('P1', 'P1'),
		('P2', 'P2'),
		('P3', 'P3 '),
		('P4', 'P4'),
		('P5', 'P5'),
		('P6', 'P6'),
	)

	DISCRICT_CHOICES = (
		('Q1', 'Q1'), 
		('Q2', 'Q2'),
		('Q3', 'Q3'),
		('Q4', 'Q4'), 
		('Gò Vấp', 'Gò Vấp'),
		('Tân Bình', 'Tân Bình'),
		('Bình Thanh', 'Bình Thạnh'), 
		('Tân Phú', 'Tân Phú'),
		('Q12', 'Q12'),
		('Q9', 'Q9'), 
	)

	PAYMENT_METHOD_CHOICES = (
		('Momo', 'Momo'),
		('Zalopay;','Zalopay')
	)

	division = forms.ChoiceField(choices=DIVISION_CHOICES)
	district =  forms.ChoiceField(choices=DISCRICT_CHOICES)
	payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())

	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'address', 'division', 'district', 'zip_code', 'payment_method', 'account_no', 'transaction_id']
