a = int(input("what is your weight?:"))
b = input("(K)g or (L)bs:")
if b.upper() == "K":
    c = int(a) / 2.2
    print(int(c))
else:
    d = int(a) * 0.45
    print("weight in pounds" + str(d))



