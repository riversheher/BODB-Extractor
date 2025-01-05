-- Create the table
CREATE TABLE interest_rate_options (
    ticker VARCHAR(10) PRIMARY KEY,
    underlying VARCHAR(255)
);

-- Insert data into the table
INSERT INTO interest_rate_options (ticker, underlying) VALUES
('IRX', '13-week T-bill'),
('VXB', '13-week T-bill (1995 LEAP)'),
('LXB', '13-week T-bill (1996 LEAP)'),
('FVX', '5-year Note'),
('VXV', '5-year Note (1995 LEAP)'),
('LXV', '5-year Note (1996 LEAP)'),
('TNX', '10-year Note'),
('VXN', '10-year Note (1995 LEAP)'),
('LXN', '10-year Note (1996 LEAP)'),
('TYX', '30-year Bond'),
('VYY', '30-year Bond (1995 LEAP)'),
('LTY', '30-year Bond (1996 LEAP)'),
('LTX', 'Weighted Average Long-Term Rate (discontinued)');
