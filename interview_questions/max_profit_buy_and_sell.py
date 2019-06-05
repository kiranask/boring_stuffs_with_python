"""
Fid the maximum profit of buy and sell stock :

Algorithm:

Step 1 : Get 3 Variables, minValue, profit, maxProfit

Step 2:

Get the Min Value
min value  =
If (min< a[i])
min  = a[i]

Step 3:
Find the profit
profit  = a[i] - min
max profit ?

Step 4:
Check
profit > max profit
If (profit> maxProfit)
maxProfit = profit;


"""

def max_profit(arr,n):
    min=arr[0]
    max=0
    max_profit =0

    for i in range(1,n):
        if arr[i]<=min:
            min=arr[i]

        profit=arr[i]-min
        if profit>max_profit:
            max_profit=profit


    return max_profit


print(max_profit([1,3,4,5,6,19],6))


