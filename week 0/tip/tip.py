def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dtf = float(d.strip().replace("$", ""))
    return (dtf)


def percent_to_float(p):
    ptf = float(p.strip().replace("%", ""))
    return (ptf/100)



main()