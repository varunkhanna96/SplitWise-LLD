from dataclasses import dataclass
from typing import Optional, List, Type

from exceptions import InvalidSplitException, InvalidAmountException, InvalidPercentageException
from split import ISplit, ExactSplit, EqualSplit, PercentSplit
from user import User


@dataclass
class TransactionMetadata:
    name: str
    notes: Optional[str] = None
    img_url: Optional[str] = None


class ITransaction:
    split_type: Type[ISplit]

    def __init__(self, amount: float, paid_by: User, splits: List[ISplit], metadata):
        self.amount = amount
        self.paid_by = paid_by
        self.splits = splits
        self.metadata = metadata
        self.validate()
        self.set_split_amounts()

    def set_split_amounts(self) -> None:
        raise NotImplementedError

    def validate(self):
        if not all([isinstance(split, self.split_type) for split in self.splits]):
            raise InvalidSplitException(f"Invalid split type found for {str(self.split_type)}")


class ExactTransaction(ITransaction):
    split_type: Type[ISplit] = ExactSplit

    def validate(self):
        super().validate()
        sum_splits = sum([split.amount for split in self.splits])
        if sum_splits != self.amount:
            raise InvalidAmountException(f"Amount entered do not sum up to {self.amount}")

    def set_split_amounts(self) -> None:
        pass


class PercentTransaction(ITransaction):
    split_type: Type[ISplit] = PercentSplit

    def validate(self):
        super().validate()
        sum_splits = sum([split.percentage for split in self.splits])
        if sum_splits != 100:
            raise InvalidPercentageException(f"Percentage entered do not sum up to 100")

    def set_split_amounts(self) -> None:
        for split in self.splits:
            split: PercentSplit
            percentage = split.percentage
            split.amount = self.amount * percentage / 100


class EqualTransaction(ITransaction):
    split_type: Type[ISplit] = EqualSplit

    def set_split_amounts(self) -> None:
        total_splits = len(self.splits)
        one_split_amount = self.amount / total_splits
        for split in self.splits:
            split.amount = one_split_amount
