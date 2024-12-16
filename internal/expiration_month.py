import datetime


def get_expiration_date(month_string: str, option_date: datetime) -> datetime:
    """get_expiration_date returns the expiration date as a datetime object.
    Note that the expiration date is almost always on the saturday following the third friday of the month.
    
    The expected string input is the month in the format "MM".
    
    The date of the expiration will have to be calculated based on the option_date and the month_string.
    The details of the calculation can be found in the bodb_guide.pdf file if there are implementation challenges.

    Args:
        month_string (str): _description_

    Returns:
        datetime: _description_
    """
    return datetime.datetime.now()