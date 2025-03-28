import React, { useEffect, useState } from "react";
import DataTable from "../components/DataTable";
import { TextField, Button, Stack } from "@mui/material";

const API_URL = process.env.API_URL + "/market-data";

const MarketData = () => {
  const [data, setData] = useState([]);
  const [ticker, setTicker] = useState("");
  const [expirationDate, setExpirationDate] = useState("");
  const [rowsPerPage, setRowsPerPage] = useState(5);

  const fetchData = () => {
    let url = `${API_URL}?limit=${rowsPerPage}&sort=desc`;
    if (ticker) url += `&ticker=${ticker}`;

    fetch(url)
      .then((res) => res.json())
      .then((data) => setData(data))
      .catch((err) => console.error("Fetch error:", err));
  };

  useEffect(() => {
    fetchData();
  }, [rowsPerPage]); 

  const handleFilter = () => {
    fetchData();
  };

  const columns = [
    { field: "ticker_symbol", headerName: "Ticker Symbol" },
    { field: "strike_price", headerName: "Strike Price" },
    { field: "timestamp", headerName: "Timestamp" },
    { field: "expiration_date", headerName: "Expiration Date" },
    { field: "underlying_price", headerName: "Underlying Price" },
    { field: "bid", headerName: "Bid" },
    { field: "ask", headerName: "Ask" },
  ];

  return (
    <div>
      <h1>Market Data Table</h1>
      <Stack direction="row" spacing={2} mb={2}>
        <TextField
          label="Ticker Symbol"
          value={ticker}
          onChange={(e) => setTicker(e.target.value)}
        />
        <TextField
          label="Expiration Date"
          type="date"
          value={expirationDate}
          InputLabelProps={{ shrink: true }}
          onChange={(e) => setExpirationDate(e.target.value)}
        />
        <Button variant="contained" onClick={handleFilter}>
          Apply Filters
        </Button>
      </Stack>
      <DataTable
        columns={columns}
        data={data}
        rowsPerPage={rowsPerPage}
        onRowsPerPageChange={(newVal) => setRowsPerPage(newVal)}
      />
    </div>
  );
};

export default MarketData;
