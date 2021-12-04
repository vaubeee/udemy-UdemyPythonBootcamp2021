monthly_revenues = [
1500, 
2800, 
1300, 
2600, 
3000, 
7000, 
1500, 
2200,
3000,
4300,
1900,
5000
]

total_count_best_month = 0
total = sum(monthly_revenues)
total_best_month = 0

for revenue in monthly_revenues:
    if revenue >= 2000:
        total_best_month += revenue
        total_count_best_month += 1

print(f"Total revenue: {total}$, total of best month: {total_count_best_month}: {total_best_month}$")
