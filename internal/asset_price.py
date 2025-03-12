
def price_to_dollars_cents(asset_string: str) -> float:
    """price_to_dollars_cents takes a string representing an asset price in the format 
    "DDDCC" where D is a digit representing dollars and C is a digit representing cents. 
    The function returns the asset price as a float.

    Args:
        asset_string (str): The asset price as a string in the format "DDDCC"

    Returns:
        float: The asset price as a float
    """
    
    asset_string = asset_string.strip()  # Remove leading and trailing spaces
    
    return int(asset_string)/100

def price_to_dollars_eighths(asset_string: str) -> float:
    """price_to_dollars_eighths takes a string representing an asset price in the format
    "DDDC0" where D is a digit representing dollars and C is a digit representing eighths of a dollar.

    Args:
        asset_string (str): The asset price as a string in the format "DDDC0"

    Returns:
        float: the asset price as a float
    """
    
    asset_string = asset_string.strip()  # Remove leading and trailing spaces
    
    # If the string is lesss than 2 characters long after stripping white space
    # then the price is less than 1 dollar.
    if len(asset_string) < 2:
        return (int(asset_string)/8)/100
    
    cents = (int(asset_string[-2:])/8)/10
    dollars = int(asset_string[:-2])
    
    return dollars + cents