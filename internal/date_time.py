from datetime import datetime

def string_to_datetime(date_string: str) -> datetime:
    """string_to_datetime converts the BODB date and time substring
    to a datetime object.  You can read more about the datetime
    object here: https://docs.python.org/3/library/datetime.html
    
    The BODB substring for time and date should be encoded at [6-17]
    in the format: YYMMDDHHMMSS

    Args:
        date_string (str): the BODB date and time substring

    Returns:
        datetime: the datetime representing the BODB date and time
    """
    
    date_string = date_string.strip()  # Remove leading and trailing spaces

    year = int("19" + date_string[0:2])
    month = int(date_string[2:4])
    day = int(date_string[4:6])
    hour = int(date_string[6:8])
    minute = int(date_string[8:10])
    second = int(date_string[10:12])
    
    return datetime(year, month, day, hour, minute, second)