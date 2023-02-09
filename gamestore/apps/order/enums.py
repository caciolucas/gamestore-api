from enum import Enum


class PaymentMethod(Enum):
    CREDIT_CARD = "credit_card"
    DEBIT_CARD = "debit_card"
    PAYPAL = "paypal"
    PIX = "pix"

    @classmethod
    def choices(cls):
        return [(tag.value, tag.name) for tag in cls]
