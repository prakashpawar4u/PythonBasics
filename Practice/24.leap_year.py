def is_leap(year):
    leap = False
    if 1900 <= year <= 10000:
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    leap = True
            # print(year)

            else:
                leap = True

    # Write your logic here

    return leap


year = int(input())