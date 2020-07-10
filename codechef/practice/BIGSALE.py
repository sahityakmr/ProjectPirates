t = int(input())
while t>0:
    n = int(input())
    price = []
    qty = []
    discount = []
    totalOriginalSellingPrice = []
    totalDiscountedSellingPrice = []
    loss = []

    for i in range(n):
        p,q,d = map(int,input().split())
        price.append(p)
        qty.append(q)
        discount.append(d)
        totalOriginalSellingPrice.append((p*(100-d)/100)*q)
        totalDiscountedSellingPrice.append((p-(p *(1+d/100)* d / 100)) * q)
        loss.append(totalOriginalSellingPrice[i]-totalDiscountedSellingPrice[i])
    print(sum(loss))
    t-=1