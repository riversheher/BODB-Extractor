import express from 'express';
import cors from 'cors';
import pkg from 'pg';
import dotenv from 'dotenv';

dotenv.config();
const { Pool } = pkg;

const app = express();
const port = 3001;

console.log("Server file is running...");

const pool = new Pool({
  host: process.env.DB_HOST,
  port: 5432,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
  ssl: { rejectUnauthorized: false }
});

app.use(cors());

app.get('/market-data', async (req, res) => {
  const { table, ticker } = req.query;

  const VALID_TABLES = ['quotes', 'trades', 'tertiary_records'];
  if (!VALID_TABLES.includes(table)) {
    return res.status(400).json({ error: 'Invalid table name' });
  }

  let sql = `SELECT * FROM ${table} LIMIT 100`;
  const values = [];

  if (ticker) {
    sql += ` WHERE ticker_symbol = $1`;
    values.push(ticker);
  }

  try {
    const result = await pool.query(sql, values);
    res.json(result.rows);
  } catch (err) {
    console.error('Query error:', err);
    res.status(500).json({ error: 'Query failed' });
  }
});

console.log("Ready to listen on port", port);
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});