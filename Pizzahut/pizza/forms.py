from django import forms
from .models import Pizza

# class PizzaForm(forms.Form):
#     Topping1 = forms.CharField(label='T1', max_length=100)
#     Topping2 = forms.CharField(label='Topping2', max_length=100)
#     size=forms.ChoiceField(label='size',choices=[('small','small'),
#                                                  ('medium','medium'),
#                                                  ('large','large')])

class PizzaForm(forms.ModelForm):
    class Meta:
        model= Pizza
        fields=['topping1','topping2','size']
        labels={'topping1':'Topping1','topping2':'Topping2','size':'Size'}

class MultiplePizzaForm(forms.Form):#django Form
    number=forms.IntegerField(min_value=2,max_value=10)

