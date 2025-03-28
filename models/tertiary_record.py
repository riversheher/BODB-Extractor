from datetime import datetime

class tertiary_record:
    def __init__(self,
                 record_type: str,
                 timestamp: datetime,
                 ticker: str,
                 raw_line: str,
                 fingerprint: str):
        self.record_type = record_type
        self.timestamp = timestamp
        self.ticker = ticker
        self.raw_line = raw_line
        self.fingerprint = fingerprint

    def to_tuple(self):
        return (
            self.record_type,
            self.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            self.ticker,
            self.raw_line,
            self.fingerprint
        )

    def __str__(self):
        return f"Tertiary_Record: {self.record_type}, {self.timestamp}, {self.ticker}"