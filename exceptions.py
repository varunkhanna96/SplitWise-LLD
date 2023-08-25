class InvalidSplitException(Exception):
    def __init__(self, msg='Invalid split type found', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class InvalidAmountException(Exception):
    pass


class InvalidPercentageException(Exception):
    pass
