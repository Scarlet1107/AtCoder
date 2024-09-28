deposit, years, interest_rate = map(float, input().split())

interest_rate = interest_rate / 100

interest = 0

if(years < 3):
    for i in range(int(years)):
        interest += deposit * interest_rate
    ans = deposit + interest
    print(int(ans))
else:
    for i in range(int(years)):
        interest += deposit * interest_rate * 182/365
        deposit += interest
        interest += deposit * interest_rate * 183/365
        deposit += interest
    ans = deposit
    print(int(ans))
