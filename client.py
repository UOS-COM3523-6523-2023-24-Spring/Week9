from Account import Account
from Bank import Bank
from Branch import Branch
from Staff import Staff
from Customer import Customer
from Payroll import Payroll


def client():
    bank = Bank()

    branch_london = Branch(location="London")
    bank.setup_branch(branch_london)
    assert branch_london in bank.branches
    assert branch_london.get_opening_time() == "9:00"

    branch_london.set_opening_time("8:00")
    assert branch_london.get_opening_time() == "8:00"

    staff_john = Staff(name="John")
    branch_london.add_staff(staff_john)
    assert staff_john in branch_london.get_staff()

    branch_sheffield = Branch(location="Sheffield")
    bank.setup_branch(branch_sheffield)
    assert branch_sheffield in bank.branches
    assert branch_sheffield.get_opening_time() == "9:00"

    bank.close_branch(branch=branch_london, transfer_branch=branch_sheffield)
    assert branch_london not in bank.branches
    assert branch_sheffield in bank.branches
    assert staff_john in branch_sheffield.get_staff()

    customer_alice = Customer(name="Alice")
    account_alice = Account()
    bank.setup_new_account(account=account_alice, customer=customer_alice)
    assert account_alice in bank.accounts
    assert customer_alice in bank.customers
    assert customer_alice.get_address() == "NO ADDRESS"
    assert customer_alice.get_phone_number() == "NO PHONE NUMBER"

    account_alice_new = Account()
    bank.setup_new_account(account=account_alice_new, customer=customer_alice)
    assert account_alice_new in bank.accounts
    assert len(bank.customers) == 1

    account_alice.add_funds(amount=1000)
    assert account_alice.get_balance() == 1000.0

    account_alice.add_interest()
    assert account_alice.get_balance() == 1000.0 + 0.05 * 1000.0

    bank.close_account(account=account_alice)
    assert account_alice.get_balance() == 0
    assert account_alice.get_customer() is None
    assert account_alice not in bank.accounts

    payroll = Payroll()
    payroll.set_staff_category_pay_schedule(staff_category="Manager", date="31")
    assert payroll.get_staff_category_pay_day("Manager") == "31"

    return True
