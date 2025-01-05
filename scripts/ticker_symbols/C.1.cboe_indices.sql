-- Create the table
CREATE TABLE cboe_indices (
    ticker VARCHAR(10) PRIMARY KEY,
    index_name VARCHAR(255),
    exercise_style VARCHAR(50)
);

-- Insert data into the table
INSERT INTO cboe_indices (ticker, index_name, exercise_style) VALUES
('OEX', 'S&P 100 Index', 'American'),
('OEZ', 'S&P 100 Index - OEX strike overflow', NULL),
('CPO', 'S&P 100 Index - CAPS', 'European'),
('SPX', 'S&P 500 Index', 'European'),
('SPZ', 'S&P 500 Index - SPX strike overflow', NULL),
('NSX', 'S&P 500 Index - PM Expiration', 'European'),
('SPL', 'S&P 500 Index - Long-Dated', 'European'),
('SPQ', 'S&P 500 Index - End-of-Quarter', 'European'),
('CPS', 'S&P 500 Index - CAPS', 'European'),
('BIX', 'S&P Banking Index', 'European'),
('BGX', 'CBOE BioTech Index', 'European'),
('CEX', 'S&P Chemical Index', 'European'),
('CWX', 'CBOE Computer Software Index', 'European'),
('EVX', 'CBOE Environmental Index', 'European'),
('GAX', 'CBOE Gaming Index', 'European'),
('GTX', 'CBOE Global Telecommunications Index', 'European'),
('HCX', 'S&P Health Care Index', 'European'),
('IUX', 'S&P Insurance Index', 'European'),
('RIX', 'CBOE REIT Index', 'European'),
('RLX', 'S&P Retail Index', 'European'),
('TCX', 'CBOE U. S. Telecommunications Index', 'European'),
('TRX', 'S&P Transportation Index', 'European'),
('FSX', 'FT-SE 100 Index', 'European'),
('ISX', 'CBOE Israel Index', 'European'),
('MEX', 'CBOE Mexico Index', 'European'),
('MZX', 'CBOE Mexico Index (MEX strike overflow)', NULL),
('NIK', 'Nikkei 300 Index', 'European'),
('NDK', 'NASDAQ 100 Index', 'European'),
('RUT', 'Russell 2000 Index', 'European'),
('SGX', 'S&P/Barra Growth Index', 'European'),
('SVX', 'S&P/Barra Value Index', 'European');
