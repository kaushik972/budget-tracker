# Monthly Budget Tracker

Reads a month of expenses from a CSV file and compares each category with its budget, flagging anything that went over.

## Why I built this

I'm a student in Japan living on a budget, so I track where my yen goes each month. I used to do this in Excel; rewriting it in Python was good practice for working with CSV data and dictionaries — and the "over budget" warnings are more honest than I am with myself.

## What it does

- Reads `expenses.csv` (date, category, amount) and `budgets.csv` (category, monthly budget)
- Prints spent vs budget vs amount left, per category
- Flags categories that went **over budget** and shows the month total
- All amounts in JPY

## How to run

```bash
cd budget-tracker
python budget_tracker.py
```

Add your own spending to `expenses.csv` and change the limits in `budgets.csv` to make it yours.

## Sample output (October 2026 sample data)

```
Budget report for 2026-10 (JPY)
Category            Spent    Budget      Left  Status
----------------------------------------------------------
Entertainment      14,500    10,000    -4,500  OVER BUDGET
Food               24,550    20,000    -4,550  OVER BUDGET
Other               2,200     3,000       800  OK
Rent               55,000    55,000         0  OK
Study               6,300     5,000    -1,300  OVER BUDGET
Transport           4,500     6,000     1,500  OK
Utilities           7,400     8,000       600  OK
----------------------------------------------------------
TOTAL             114,450   107,000    -7,450

Watch out - over budget in: Entertainment, Food, Study
```

(The sample data overspends on purpose, so you can see the warnings working.)

## Files

- `budget_tracker.py` — the program
- `expenses.csv` — one month of sample expenses
- `budgets.csv` — monthly budget per category

## Next steps

- Handle several months in one file and compare month to month
- Add a new expense from the command line instead of editing the CSV
- Show spending as a simple text bar chart

*Standard library only. Built while learning Python.*
