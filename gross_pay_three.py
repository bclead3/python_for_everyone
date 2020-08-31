def computepay(h, r):
    f_hours = 0.0
    f_rate = 0.0
    try:
        f_hours = float(h)
        f_rate = float(r)
    except ValueError:
        print(f"There was a problem converting the inputs '{h}', '{r}' into float values")
        quit()
    if f_hours <= 40:
        f_gross = f_rate * f_hours
    else:
        f_reg_gross = f_rate * 40.0
        f_overtime = (f_hours - 40.0) * f_rate * 1.5
        f_gross = f_reg_gross + f_overtime
    return f_gross


rate = 10.5
hrs = input("Enter Hours:")
p = computepay(hrs, rate)
print("Pay", p)
