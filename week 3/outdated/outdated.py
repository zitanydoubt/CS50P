months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    date = input("Date: ")
    try:
        if "/" in date:
            mm,dd,yyyy = map(int, date.split("/"))
        elif "," in date:
            mmdd, yyyy = date.split(", ")
            mm, dd = mmdd.split(" ")
            mm = months.index(mm) + 1
            mm, dd = int(mm), int(dd)
        if dd > 31 or mm > 12:
            raise Exception
    except:
        pass
    else:
        print(f"{yyyy}-{mm:02}-{dd:02}")
        break

