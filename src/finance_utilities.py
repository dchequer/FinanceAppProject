# Import the necessary libraries
import numpy as np
from typing import Tuple, List, Dict

# Define a function to calculate loan payments
def calculate_loan_payment(loan_amount: float, interest_rate: float, loan_term: float) -> float:
  monthly_rate = interest_rate / 12
  num_payments = loan_term * 12
  loan_payment = loan_amount * (monthly_rate / (1 - (1 + monthly_rate)**(-num_payments)))
  return loan_payment

# Define a function to calculate compound interest
def calculate_compound_interest(initial_investment: float, interest_rate: float, num_years: float) -> float:
  final_value = initial_investment * (1 + interest_rate)**num_years
  return final_value

# Define a function to convert between interest rate types
def convert_interest_rate(rate: float, from_type: str, to_type: str) -> float:
  # Convert annual percentage rate (APR) to effective annual rate (EAR)
  if from_type == "APR" and to_type == "EAR":
    ear = (1 + rate/12)**12 - 1
    return ear

  # Convert effective annual rate (EAR) to annual percentage rate (APR)
  elif from_type == "EAR" and to_type == "APR":
    apr = 12 * ((1 + rate)**(1/12) - 1)
    return apr

  # Return the input rate if the conversion is not supported
  else:
    return rate

# Define a function to calculate the present value of an investment
def calculate_present_value(future_value: float, interest_rate: float, num_years: float) -> float:
  present_value = future_value / (1 + interest_rate)**num_years
  return present_value

# Define a function to calculate stock data metrics
def calculate_stock_metrics(returns: List[float]) -> Tuple[float, float, float]:
  # Calculate the mean and standard deviation of the returns
  mean_return = np.mean(returns)
  std_return = np.std(returns)

  # Calculate the return on investment (ROI)
  roi = (mean_return * 252) / 100

  # Calculate the Sharpe ratio
  sharpe_ratio = (mean_return * 252) / (std_return * np.sqrt(252))

  # Calculate the beta
  beta = 1

  # Return the calculated metrics
  return roi, sharpe_ratio, beta

# Define a function to generate a financial report
def generate_financial_report(data: Dict[str, List[float]]) -> Tuple[float, float, float, float]:
  # Calculate the total revenue and total expenses
  total_revenue = sum(map(int, data["revenue"]))
  total_expenses = sum(map(int, data["expenses"]))

  # Calculate the net income
  net_income = total_revenue - total_expenses

  # Calculate the net profit margin
  net_profit_margin = net_income / total_revenue

  # Return the calculated metrics
  return total_revenue, total_expenses, net_income, net_profit_margin


if __name__ == "__main__":
  # Test the financial functions
  loan_amount = 100000
  interest_rate = 0.05
  loan_term = 30

  loan_payment = calculate_loan_payment(loan_amount, interest_rate, loan_term)
  print(f"Loan payment: ${loan_payment:.2f}")

  initial_investment = 10000
  interest_rate = 0.05
  num_years = 10

  final_value = calculate_compound_interest(initial_investment, interest_rate, num_years)
  print(f"Final value: ${final_value:.2f}")

  rate = 0.06
  from_type = "APR"
  to_type = "EAR"

  converted_rate = convert_interest_rate(rate, from_type, to_type)
  print(f"Converted rate: {converted_rate:.4f}")

  future_value = 100000
  interest_rate = 0.05
  num_years = 10

  present_value = calculate_present_value(future_value, interest_rate, num_years)
  print(f"Present value: ${present_value:.2f}")

  returns = [0.02, 0.05, 0.03, -0.02, 0.04]

  roi, sharpe_ratio, beta = calculate_stock_metrics(returns)
  print(f"ROI: {roi:.2f}%, Sharpe ratio: {sharpe_ratio:.2f}, Beta: {beta:.2f}")

  data = {
    "revenue": [100000, 150000, 130000, 170000, 200000],
    "expenses": [50000, 60000, 50000, 70000, 80000]
  }

  total_revenue, total_expenses, net_income, net_profit_margin = generate_financial_report(data)
  print(f"Total revenue: ${total_revenue:.2f}, Total expenses: ${total_expenses:.2f}, Net income: ${net_income:.2f}, Net profit margin: {net_profit_margin:.2f}")

