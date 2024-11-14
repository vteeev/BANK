class TransactionError(Exception):
    "Ogolne wyjatki dla transakcji"
    pass

class InvalidInputData(TransactionError):

    def __init__(self,message="Błędne dane wejsciowe"):
        super().__init__(message)

class InsufficientFundsError(TransactionError):
    """Wyjątek dla sytuacji, gdy użytkownik nie ma wystarczających środków."""
    def __init__(self, message="Brak wystarczających środków na koncie."):
        super().__init__(message)

class InvalidTransactionTypeError(TransactionError):
    """Wyjątek dla sytuacji, gdy typ transakcji jest nieprawidłowy."""
    def __init__(self, transaction_type):
        message = f"Niepoprawny typ transakcji: {transaction_type}"
        super().__init__(message)

class FileSaveError(Exception):
    """Wyjątek dla błędów związanych z zapisem pliku CSV."""
    def __init__(self, message="Błąd podczas zapisu pliku transakcji."):
        super().__init__(message)