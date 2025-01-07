

def get_record_type(str: type):
    """get_record_type returns the record type for the BODB record.
    
    The BODB record type is encoded at [0-1] in the BODB record.
    
    Args:
        str (type): the BODB record
    
    Returns:
        str: the record type
    """
    
    return 0