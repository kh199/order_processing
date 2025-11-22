from enum import Enum


class StatusTypes(str, Enum):
    CREATED = "CREATED"
    IN_PROCESSING = "IN_PROCESSING"
    IN_TRANSIT = "IN_TRANSIT"
    DELIVERED = "DELIVERED"
    CANCELED = "CANCELED"
