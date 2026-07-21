class CleaningStats:
    """Represent statistics calculated from cleaned student data."""

    def __init__(
        self,
        average_age: float,
        average_score: float,
        highest_score: int,
        lowest_score: int,
    ) -> None:
        self.average_age = average_age
        self.average_score = average_score
        self.highest_score = highest_score
        self.lowest_score = lowest_score