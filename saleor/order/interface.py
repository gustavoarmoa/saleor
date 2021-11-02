from dataclasses import dataclass
from decimal import Decimal

from ..payment.models import Payment


@dataclass
class OrderPaymentAction:
    """Used to transmit data about payment-related events."""

    payment: Payment
    amount: Decimal