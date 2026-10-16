"""Constants and category definitions for the NLP Engine."""

from enum import Enum


class ComplaintCategory(str, Enum):
    """The 6 exact complaint category IDs supported by the system."""
    WATER_SUPPLY = "water_supply"
    ROAD_DAMAGE = "road_damage"
    GARBAGE = "garbage"
    DRAINAGE = "drainage"
    STREETLIGHT = "streetlight"
    OTHER = "other"


# List of valid category ID strings
VALID_CATEGORY_IDS = [category.value for category in ComplaintCategory]

# Default confidence threshold for requiring human review
DEFAULT_CONFIDENCE_THRESHOLD = 0.65
