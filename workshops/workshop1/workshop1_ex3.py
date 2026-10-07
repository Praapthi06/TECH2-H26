import numpy as np


def tax(income):
    """_summary_
    Return the taxes owed for a given income.
    Parameters
    ----------
    income
        Gross income
    Returns
    ----------
    Tax owed
    """

    if income <= 300_000:
        print('Income is below 300k')
        taxes = 0

    elif 300_000 < income <= 700_000:
        print('Income is between 300k and 700k')
        taxes = 0.2 * (income - 300_000)
    else:
        print('Income is above 700k')
        taxes = 0.2 * (700_000 - 300_000) + 0.35 * (income - 700_000)

    return taxes


incomes = np.linspace(0, 1_200_000, 13)
taxes_loop = []

for income in incomes:
    # Compute taxes for current income level
    taxes = tax(income)
    # Append to list
    taxes_loop.append(taxes)
    # Income after tax
    net_income = income - taxes

    print(
        f'Gross income: {income:10.0f};'
        f'Taxes: {taxes: 10.0f};'
        f'Net income: {net_income: 10.0f}'
    )

    """

#Enumeration alternative 

incomes = np.linspace(0, 1_200_000, 13)
taxes_arr = np.zeros(len(incomes))

for i, income in enumerate(incomes):
    taxes_arr[i] = tax(income)
    net_income = income - taxes_arr[i]
    print(f'Gross income: {income:10.0f}; Taxes: {taxes_arr[i]:10.0f}; Net income: {net_income:10.0f}')

    """
