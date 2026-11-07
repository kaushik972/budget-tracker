"""
Monthly Budget Tracker
----------------------
Reads expenses from expenses.csv and budgets from budgets.csv,
then prints how much was spent in each category, how it compares
with the budget, and flags any category that went over budget.

All amounts are in Japanese yen (JPY).

Built by Kaushik Shivam while learning Python.
Standard library only (csv).
"""

import csv

EXPENSES_FILE = "expenses.csv"
BUDGETS_FILE = "budgets.csv"


def load_budgets(filename):
    """Return {category: monthly_budget}."""
    budgets = {}
    with open(filename, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            budgets[row["category"]] = float(row["monthly_budget"])
    return budgets


def load_expenses(filename):
    """Return {category: total_spent} plus the month label (YYYY-MM)."""
    totals = {}
    month = None
    with open(filename, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            totals[row["category"]] = totals.get(row["category"], 0.0) + float(row["amount"])
            month = row["date"][:7]  # "2026-10-02" -> "2026-10"
    return totals, month


def main():
    budgets = load_budgets(BUDGETS_FILE)
    spent, month = load_expenses(EXPENSES_FILE)

    print(f"Budget report for {month} (JPY)")
    print(f"{'Category':<15}{'Spent':>10}{'Budget':>10}{'Left':>10}  Status")
    print("-" * 58)

    total_spent = 0.0
    total_budget = 0.0
    over = []
    # Show every category that has a budget or any spending
    for category in sorted(set(budgets) | set(spent)):
        s = spent.get(category, 0.0)
        b = budgets.get(category, 0.0)
        total_spent += s
        total_budget += b
        status = "OK"
        if s > b:
            status = "OVER BUDGET"
            over.append(category)
        print(f"{category:<15}{s:>10,.0f}{b:>10,.0f}{b - s:>10,.0f}  {status}")

    print("-" * 58)
    print(f"{'TOTAL':<15}{total_spent:>10,.0f}{total_budget:>10,.0f}"
          f"{total_budget - total_spent:>10,.0f}")

    if over:
        print("\nWatch out - over budget in:", ", ".join(over))
    else:
        print("\nNice work - every category is within budget.")


if __name__ == "__main__":
    main()
