from django.shortcuts import render
from .models import Option
from .forms import OptionForm
from .black_scholes import calculate_option_price

def option_pricing_view(request):
    if request.method == "POST":
        form = OptionForm(request.POST)
        if form.is_valid():
            option = form.save(commit=False)
            option_price = calculate_option_price(option)
            return render(request, './option_result.html', {'option': option, 'option_price': option_price, 'form': form})
    else:
        form = OptionForm()

    return render(request, './option_form.html', {'form': form})
