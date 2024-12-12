
def price_to_dollars_cents(asset_string: str) -> float:
    
    asset_string = asset_string.strip()  # Remove leading and trailing spaces
    
    #the asset price is encoded at [36-40], so we extract the last two digits for cents, and the first three for dollars
    cents = int(asset_string[-2:])/100
    dollars = int(asset_string[:-2])
    
    return dollars + cents

def price_to_dollars_eighths(asset_string: str) -> float:
    
    asset_string = asset_string.strip()  # Remove leading and trailing spaces
    
    cents = (int(asset_string[-2:])/8)/10
    dollars = int(asset_string[:-2])
    
    return dollars + cents