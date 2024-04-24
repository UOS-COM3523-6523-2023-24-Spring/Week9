from Account import Account
from Branch import Branch
from Customer import Customer
from Payroll import Payroll
from Staff import Staff


class Bank:
    def __init__(self):
        self.accounts = []
        self.customers = []
        self.branches = []
        # self.payroll = None  # this can be removed as the client does not use it as a part of Bank anymore

    def setup_branch(self, branch: Branch):
        self.branches.append(branch)

    def close_branch(self, branch: Branch, transfer_branch: Branch):
        branch.close_branch(transfer_branch)
        self.branches.remove(branch)

    def setup_new_account(self, account: Account, customer: Customer):
        account.set_customer(customer)
        self.accounts.append(account)

        if customer not in self.customers:
            self.customers.append(customer)

    def close_account(self, account: Account):
        account.close_account()
        self.accounts.remove(account)
