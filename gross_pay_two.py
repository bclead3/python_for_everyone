hrs_s = input("Enter Hours:")
hrs_f = float(hrs_s)
rate_s = input("Enter Rate:")
rate_f = float(rate_s)
gross_f = 0.0
if hrs_f <= 40:
    gross_f = rate_f * hrs_f
else:
    reg_gross_f = rate_f * 40.0
    overtime_f = (hrs_f - 40.0) * rate_f * 1.5
    gross_f = reg_gross_f + overtime_f

print(gross_f)