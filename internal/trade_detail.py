def get_volume(bodb_string: str) -> int:
    """gets the volume integer from an encoded bodb string.

    Args:
        bodb_string (str): A string representing a numeric

    Returns:
        int: the volume of the trade
    """
    
    cleaned = bodb_string.strip()
    
    try:
        return int(cleaned)
    except Exception:
        raise Exception().add_note("could not convert volume string to int")

