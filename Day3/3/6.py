employees = {
    "AADIL": 55000,
    "GULAM": 75000,
    "HASNAIN": 62000,
    "RAZZAK": 90000,
    "AFROZ": 80000,
    "ALEX": 68000
}

sorted_employees = sorted(
    employees.items(),
    key=lambda item: item[1],
    reverse=True
)

print("Top 3 highest paid employees:")

for name, salary in sorted_employees[:3]:
    print(name, salary)