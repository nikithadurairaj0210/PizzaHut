from django.shortcuts import render
from .forms import PizzaForm,MultiplePizzaForm
from django.forms import formset_factory

# Create your views here.
def homepage(request):
    return render(request,'pizza/home.html')
def order(request):
    multiple_pizzaform=MultiplePizzaForm()
    if request.method=='POST':
        filled_form=PizzaForm(request.POST)
        if filled_form.is_valid():
            note='Thanks your order as been placed!!'
        else:
            note='Please Try Again...'
        return render(request, 'pizza/order.html', {'pizzaform': filled_form,'note':note,'multiple_piza_form':multiple_pizzaform})
    else:
        form = PizzaForm() #empty Form
        return render(request,'pizza/order.html', {'pizzaform':form,'multiple_pizza_form':multiple_pizzaform})

def pizzas(request):
    no_of_pizzas=2
    if request.method=='GET':
        filled_multiple_pizza_form=MultiplePizzaForm(request.GET)
        if filled_multiple_pizza_form.is_valid():
            no_of_pizzas=filled_multiple_pizza_form.cleaned_data['number']
        print(no_of_pizzas)
    PizzaFormset=formset_factory(PizzaForm, extra=no_of_pizzas)
    formsets=PizzaFormset()
    if request.method=='POST':
        filled_formset=PizzaFormset(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                form.save()
            note='order placed successfully'
        else:
            note='Sorry Order not placed please try Again'
        return render(request, 'pizza/pizzas.html', {'formset': formsets,'note':note})
    return render(request,'pizza/pizzas.html',{'formset':formsets})
