import dataclasses
from typing import Optional

from user import User


@dataclasses.dataclass
class ISplit:
    user: User
    amount: Optional[float] = None


class ExactSplit(ISplit):
    pass


class PercentSplit(ISplit):
    percentage: float


class EqualSplit(ISplit):
    pass
