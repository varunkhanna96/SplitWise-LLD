import dataclasses
from typing import Dict, List

from enums import ExpenseType
from split import ISplit
from transaction import ITransaction, TransactionMetadata
from user import User
from factory import ExpenseFactory


@dataclasses.dataclass
class SplitWiseApp:

    transactions: List[ITransaction] = dataclasses.field(default_factory=list)
    user_map: Dict[str, User] = dataclasses.field(default_factory=dict)
    balance_sheet: Dict[str, Dict[str, float]] = dataclasses.field(default_factory=dict)

    def show_balance(self, user_id: str):
        balances = self.balance_sheet.get(user_id, {})
        for key, value in balances.items():
            print(f"User {key} owes {value} amount to user {user_id}")

    def show_balances(self):
        for key in self.balance_sheet.keys():
            self.show_balance(user_id=key)

    def add_expense(self, expense_type: ExpenseType, amount: float, paid_by: User, splits: List[ISplit], transaction_meta: TransactionMetadata):
        expense_cls = ExpenseFactory.create_expense(
            expense_type=expense_type,
            amount=amount,
            user=paid_by,
            splits=splits,
            transaction_meta=transaction_meta
        )
        self.transactions.append(expense_cls)
        for split in expense_cls.splits:
            paid_to = split.user
            balances = self.balance_sheet.get(paid_by.id, {})
            if not balances.get(paid_to.id):
                balances[paid_to.id] = 0
            balances[paid_to.id] += split.amount
