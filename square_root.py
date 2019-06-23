# below is square root calculator

ans = 0
neg_check = False
x = int(input("Please enter some number:"))
if x < 0:
    neg_check = True
while ans**2 < x:
    ans += 1
if ans**2 == x:
    print("Thank you", ans)
else:
    print("Not perfect square, ")
if neg_check:
    print("did you mean", -x, "?")

