

def get_record_type(in_str: str) -> str:
    """get_record_type returns the record type for the BODB record.
    
    The BODB record type is encoded at [0-1] in the BODB record.
    
    an encoding of 1 means it is a trade, an encoding of 2 means it is a quote.
    
    Most records processed should be trades or quotes.  However, other record types will be supported
    as needed.
    
    Args:
        str (type): the BODB record
    
    Returns:
        str: the record type
    """
    #remove whitespace for consistency
    parsed = in_str.strip()
    
    match parsed:
        case "0":
            return "04HALT"
        case "1":
            return "Trade"
        case "2":
            return "Quote"
        case "3":
            # Record is part of a combination trade
            return "01SPRD"
        case "4":
            # Record is part of a stradle
            return "01STDL"
        case "5":
            # Reopen after trading halt
            return "02HALT"
        case "6":
            # Recorded Late, In Sequence
            return "01LATE"
        case "7":
            # Recorded Late, Out of Sequence
            return "01OSEQ"
        case "8":
            # Opening Trade, Recorded Late, Out of Sequence
            return "01OPEN"
        case "9":
            # Opening Trade, Recorded Late, In Sequence
            return "01OPNL"
        case "20":
            # Cancel Recorded Late, In Sequence
            return "03LATE"
        case "21":
            # Cancel Recorded Late, Out of Sequence
            return "03OSEQ"
        case "22":
            # Cancel Opening Trade, Recorded Late, Out of Sequence
            return "03OPEN"
        case "23":
            # Cancel Record is Part of a Combination Trade
            return "03SPRD"
        case "24":
            # Cancel Record is Part of a Straddle
            return "03STDL"
        case "25":
            # Cancel Cancel the Opening Trade
            return "03CNCO"
        case "26":
            # Cancel Another Trade, not the Last or Opening Trade
            return "03CNCL"
        case "27":
            # Cancel the Last Trade, if it is not the opening trade
            return "03CANC"
        case "28":
            # Cancel the only trade of the day
            return "03CNOL"
        case "29":
            # Cancel the Opening Trade, Recorded Late, in sequence
            return "03OPNL"
        case "40":
            # Underlying Start of RAES the Electronic Execution System
            return "04AUTO"
        case "41":
            # Trade Transaction was executed electronically
            return "01RAES"
        case "42":
            # unsure of this record type
            return "04END"
        case "43":
            # Quote Opening Rotation
            return "02ROTA"
        case "44":
            # Underlying Opening Rotation
            return "04ROTA"
        case "45":
            # Underlying End of opening Roataion
            return "04ENDR"
        case "46":
            # Quote start of RAES the Electronic Execution System
            return "02AUTO"
        case "47":
            # Unsure of this record type
            return "04END"
        case "48":
            # Unsure of this record type
            return "04ENDF"
        case "60":
            # Underlying Recorded under fast trading conditions
            return "04FAST"
        case "61":
            # Trade Recorded under fast trading conditions
            return "01FAST"
        case "62":
            # Quote Recorded under fast trading conditions
            return "02FAST"
        case "63":
            # Trade Closing Record
            return "01CLOS"
        case "64":
            # Quote Closing Record
            return "02CLOS"
        case "65":
            # Underlying Closing Record
            return "04CLOS"
        case "66":
            # unsure of this record type
            return "03REOP"
        case "67":
            # unsure of this record type
            return "02ZZZZ"
        case _:
            return "Unknown"