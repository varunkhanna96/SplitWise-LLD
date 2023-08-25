import enum


class ExpenseType(enum.Enum):
    EXACT = "EXACT"
    PERCENT = "PERCENT"
    EQUAL = "EQUAL"
