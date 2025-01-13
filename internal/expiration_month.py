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
    
    year = option_date.year
    month = int(month_string)
    day = 1
    
    # Find the weekday for the first day of the expiration month.
    weekday = datetime.datetime(year, month, day).isoweekday()
    
    # Find difference between weekday and friday
    difference = 5 - weekday
    if difference < 0:
        difference += 7
    
    # Add difference to day
    day += difference
    
    # Add 14 to day to get the third friday, then add one more to get the saturday
    # in total add 15
    day += 15

    
    return datetime.datetime(year, month, day)