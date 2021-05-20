# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000.0

while principal > 0:
    payment_with_extra = payment
    if extra_payment_start_month <= month < extra_payment_end_month:
        payment_with_extra += extra_payment
    principal = principal * (1 + rate/12) - payment_with_extra
    total_paid = total_paid + payment_with_extra
    month += 1
    print(month, round(total_paid, 2), round(principal, 2))

print('Total paid', round(total_paid, 2))
print('Months', month)
