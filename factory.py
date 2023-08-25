from typing import List

from enums import ExpenseType
from split import ISplit, PercentSplit
from transaction import TransactionMetadata, EqualTransaction, ExactTransaction, PercentTransaction, ITransaction
from user import User


class ExpenseFactory:

    @staticmethod
    def create_expense(
        expense_type: ExpenseType,
        amount: float,
        user: User,
        splits: List[ISplit],
        transaction_meta: TransactionMetadata
    ) -> ITransaction:
        if expense_type == ExpenseType.EQUAL.value:
            return EqualTransaction(
                amount=amount,
                paid_by=user,
                splits=splits,
                metadata=transaction_meta
            )
        elif expense_type == ExpenseType.EXACT.value:
            return ExactTransaction(
                amount=amount,
                paid_by=user,
                splits=splits,
                metadata=transaction_meta
            )
        else:
            return PercentTransaction(
                amount=amount,
                paid_by=user,
                splits=splits,
                metadata=transaction_meta
            )
