-- Create the table
CREATE TABLE index_leaps (
    ticker VARCHAR(10) PRIMARY KEY,
    index_name VARCHAR(255),
    expiration_years VARCHAR(50)
);

-- Insert data into the table
INSERT INTO index_leaps (ticker, index_name, expiration_years) VALUES
('OAX', 'S&P 100 Index', '1993'),
('OBX', 'S&P 100 Index', '1994'),
('OLX', 'S&P 100 Index', '1992, 1995'),
('OCX', 'S&P 100 Index', '1996'),
('LSW', 'S&P 500 Index', '1993'),
('LSY', 'S&P 500 Index', '1994'),
('LSX', 'S&P 500 Index', '1992, 1995'),
('LSZ', 'S&P 500 Index', '1996'),
('WRU', 'Russell 2000 Index', '1994'),
('VRU', 'Russell 2000 Index', '1995'),
('LRU', 'Russell 2000 Index', '1996'),
('WBG', 'CBOE BioTech Index', '1994'),
('VBG', 'CBOE BioTech Index', '1995'),
('LBG', 'CBOE BioTech Index', '1996'),
('VEX', 'CBOE Mexico Index', '1995'),
('VNX', 'Nikkei 300 Index', '1995');
