import React, { useEffect, useState } from "react";
import DataTable from "../components/DataTable";
import { TextField, Button, Stack } from "@mui/material";

const API_URL = process.env.API_URL + "/trade-records";

const TradeRecords = () => {
  const [data, setData] = useState([]);
  const [ticker, setTicker] = useState("");
  const [expirationDate, setExpirationDate] = useState("");
  const [rowsPerPage, setRowsPerPage] = useState(5); 

  const fetchData = () => {
    let url = `${API_URL}?limit=${rowsPerPage}&sort=desc`;

    if (ticker) url += `&ticker=${ticker}`;
    if (expirationDate) url += `&expiration_date=${expirationDate}`;

    fetch(url)
      .then((res) => res.json())
      .then((data) => setData(data))
      .catch((err) => console.error("Fetch error:", err));
  };

  const handleFilter = () => {
    fetchData();
  };

  useEffect(() => {
    fetchData();
  }, [rowsPerPage]);

  const columns = [
    { field: "ticker_symbol", headerName: "Ticker Symbol" },
    { field: "option_type", headerName: "Option Type" },
    { field: "strike_price", headerName: "Strike Price" },
    { field: "expiration_date", headerName: "Expiration Date" },
    { field: "volume", headerName: "Volume" },
    { field: "price", headerName: "Price" },
  ];

  return (
    <div>
      <h1>Trade Records</h1>
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
        onRowsPerPageChange={(val) => setRowsPerPage(val)}
      />
    </div>
  );
};

export default TradeRecords;
