# We're looking to find out how much money we have after a day with friends on Saturday. 
# Our code does the trick but we learned about keeping out code DRY recently and want to make it more efficent by making it DRY.
# I want you to accomplish this by making functions where you see repeated code. 
# Some things to note. When we have a positive number that gets split up and 85% goes into checking and 15% goes into savings. 
# All negative numbers gets taken out of the checking account.

savings = 1096.25
checking = 1590.80
CHECKING_MULTIPLIER = 0.85
SAVINGS_MULTIPLIER = 0.15


def process_transaction (amount, savings, checking):
    if amount <0: 
         checking += amount
    else:
        checking += amount * CHECKING_MULTIPLIER
        savings += amount * SAVINGS_MULTIPLIER




def saturdays_bank_transactions(transactions) -> (float, float):
    savings = 1096.25
    checking = 1590.80
    CHECKING_MULTIPLIER = 0.85
    SAVINGS_MULTIPLIER = 0.15

    for items in range(10):
        process_transaction(transactions[int(items)], savings, checking)

    return checking, savings





def main():
    transactions = [300.00, -50.00, -5.00, -20, 15.72, 2083.93, -1034.00, -420.00, -5.23, -15.93, -72.90]
    new_balance = saturdays_bank_transactions(transactions)
    print("Your new checking balance is:", '${:.2f}'.format(round(new_balance[0], 2)), "\n", "Your new savings balance is:", '${:.2f}'.format(round(new_balance[1], 2)))

main()




#if __name__ == "__main__":
    #transactions = [300.00, -50.00, -5.00, -20, 15.72, 2083.93, -1034.00, -420.00, -5.23, -15.93, -72.90]
    #new_balance = saturdays_bank_transactions(transactions)
    #print("Your new checking balance is:", '${:.2f}'.format(round(new_balance[0], 2)), "\n", "Your new savings balance is:", '${:.2f}'.format(round(new_balance[1], 2)))



