from django.http import HttpResponse
from django.shortcuts import render
from django.http.request import HttpRequest
from src import finance_utilities as finance
from src import countDots as dots

def home(request: HttpRequest) -> HttpResponse:
  return render(request, 'home.html')

def loan_payment_calculator(request: HttpRequest) -> HttpResponse:
  if request.method == 'POST':
    loan_amount = float(request.POST['loan_amount'])
    interest_rate = float(request.POST['interest_rate'])
    loan_term = int(request.POST['loan_term'])

    loan_payment = finance.calculate_loan_payment(loan_amount, interest_rate, loan_term)

    context = {
      'loan_payment': loan_payment
    }

    return render(request, 'loan_payment_calculator.html', context)

  else:
    return render(request, 'loan_payment_calculator.html')

# Define additional views for the other finance tasks here...
def compound_interest_calculator(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        principal = float(request.POST['principal'])
        interest_rate = float(request.POST['interest_rate'])
        time = int(request.POST['time'])
    
        compound_interest = finance.calculate_compound_interest(principal, interest_rate, time)
    
        context = {
        'compound_interest': compound_interest
        }
    
        return render(request, 'compound_interest_calculator.html', context)
    
    else:
        return render(request, 'compound_interest_calculator.html')

def interest_rate_converter(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        interest_rate = float(request.POST['interest_rate'])
        time = int(request.POST['time'])
    
        effective_interest_rate = finance.calculate_effective_interest_rate(interest_rate, time)
    
        context = {
        'effective_interest_rate': effective_interest_rate
        }
    
        return render(request, 'interest_rate_converter.html', context)
    
    else:
        return render(request, 'interest_rate_converter.html')

def present_value_calculator(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        future_value = float(request.POST['future_value'])
        interest_rate = float(request.POST['interest_rate'])
        time = int(request.POST['time'])
    
        present_value = finance.calculate_present_value(future_value, interest_rate, time)
    
        context = {
        'present_value': present_value
        }
    
        return render(request, 'present_value_calculator.html', context)
    
    else:
        return render(request, 'present_value_calculator.html')

def stock_metrics_calculator(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        price = float(request.POST['price'])
        dividend = float(request.POST['dividend'])
        growth_rate = float(request.POST['growth_rate'])
    
        stock_metrics = finance.calculate_stock_metrics(price, dividend, growth_rate)
    
        context = {
        'stock_metrics': stock_metrics
        }
    
        return render(request, 'stock_metrics_calculator.html', context)
    
    else:
        return render(request, 'stock_metrics_calculator.html')

def future_value_calculator(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        present_value = float(request.POST['present_value'])
        interest_rate = float(request.POST['interest_rate'])
        time = int(request.POST['time'])
    
        future_value = finance.calculate_future_value(present_value, interest_rate, time)
    
        context = {
        'future_value': future_value
        }
    
        return render(request, 'future_value_calculator.html', context)
    
    else:
        return render(request, 'future_value_calculator.html')

def financial_report_generator(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        revenue = request.POST['revenue']
        #print(revenue)
        expenses = request.POST['expenses']

        financial_report = finance.generate_financial_report(
            {
                'revenue': revenue, 
                'expenses': expenses
            })
    
        context = {
        'financial_report': financial_report
        }
    
        return render(request, 'financial_report_generator.html', context)
    
    else:
        return render(request, 'financial_report_generator.html')

def domino_counter(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        image = request.POST['image']

        domino_count = dots(image)
        context = {
        'domino_counter': domino_count
        }
    
        return render(request, 'domino_counter.html', context)
    
    else:
        return render(request, 'domino_counter.html')
        