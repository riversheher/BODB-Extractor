import express from "express";
import cors from "cors";
import pkg from "pg";
import dotenv from "dotenv";

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
  ssl: { rejectUnauthorized: false },
});

app.use(cors());

app.get("/market-data", async (req, res) => {
  const {
    table,
    ticker,
    record_type,
    start_date,
    end_date,
    min_underlying,
    max_underlying,
    min_strike,
    max_strike,
    min_bid,
    max_bid,
    min_ask,
    max_ask,
    min_volume,
    max_volume,
    min_price,
    max_price,
    min_expiration,
    max_expiration,
  } = req.query;

  const VALID_TABLES = ["quotes", "trades", "tertiary_records"];
  if (!VALID_TABLES.includes(table)) {
    return res.status(400).json({ error: "Invalid table name" });
  }

  let sql = `SELECT * FROM ${table} WHERE 1=1`;
  const values = [];
  let idx = 1;

  if (ticker) {
    sql += ` AND ticker = $${idx++}`;
    values.push(ticker);
  }

  if (record_type && table === "tertiary_records") {
    sql += ` AND record_type = $${idx++}`;
    values.push(record_type);
  }

  if (start_date) {
    sql += ` AND timestamp >= $${idx++}`;
    values.push(start_date);
  }

  if (end_date) {
    sql += ` AND timestamp <= $${idx++}`;
    values.push(end_date);
  }

  if (min_underlying) {
    sql += ` AND underlying_price >= $${idx++}`;
    values.push(min_underlying);
  }
  if (max_underlying) {
    sql += ` AND underlying_price <= $${idx++}`;
    values.push(max_underlying);
  }
  if (min_strike) {
    sql += ` AND strike_price >= $${idx++}`;
    values.push(min_strike);
  }
  if (max_strike) {
    sql += ` AND strike_price <= $${idx++}`;
    values.push(max_strike);
  }
  if (min_bid) {
    sql += ` AND bid >= $${idx++}`;
    values.push(min_bid);
  }
  if (max_bid) {
    sql += ` AND bid <= $${idx++}`;
    values.push(max_bid);
  }
  if (min_ask) {
    sql += ` AND ask >= $${idx++}`;
    values.push(min_ask);
  }
  if (max_ask) {
    sql += ` AND ask <= $${idx++}`;
    values.push(max_ask);
  }
  if (min_volume) {
    sql += ` AND volume >= $${idx++}`;
    values.push(min_volume);
  }
  if (max_volume) {
    sql += ` AND volume <= $${idx++}`;
    values.push(max_volume);
  }
  if (min_price) {
    sql += ` AND price >= $${idx++}`;
    values.push(min_price);
  }
  if (max_price) {
    sql += ` AND price <= $${idx++}`;
    values.push(max_price);
  }
  if (min_expiration) {
    sql += ` AND expiration_date >= $${idx++}`;
    values.push(min_expiration);
  }
  if (max_expiration) {
    sql += ` AND expiration_date <= $${idx++}`;
    values.push(max_expiration);
  }

  sql += ` ORDER BY timestamp DESC LIMIT 100`;

  try {
    const result = await pool.query(sql, values);
    res.json(result.rows);
  } catch (err) {
    console.error("Query error:", err);
    res.status(500).json({ error: "Query failed" });
  }
});

console.log("Ready to listen on port", port);
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
