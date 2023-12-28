
def check_balance(current_balance: int, withdrawal_balance: int):
    if current_balance < withdrawal_balance:
        return True
    return False
