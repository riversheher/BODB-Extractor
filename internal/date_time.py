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
    
    year = int("19" + date_string[0:2].strip())
    month = int(date_string[2:4].strip())
    day = int(date_string[4:6].strip())
    hour = int(date_string[6:8].strip())
    minute = int(date_string[8:10].strip())
    second = int(date_string[10:12].strip())
    
    return datetime(year, month, day, hour, minute, second)