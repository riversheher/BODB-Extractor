import React, { useEffect, useState } from "react";
import DataTable from "../components/DataTable";
import recordTypeMap from "../components/record_type";
import "./organizeFilters.css";
import Button from "@mui/material/Button";

const API_URL = "http://localhost:3001/market-data";

const Tertiary = () => {
  const [data, setData] = useState([]);
  const [ticker, setTicker] = useState("");
  const [recordType, setRecordType] = useState("");
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const fetchData = async () => {
    setIsLoading(true);
    try {
      const params = new URLSearchParams();
      params.append("table", "tertiary_records");
      if (ticker) params.append("ticker", ticker);
      if (recordType) params.append("record_type", recordType);
      if (startDate) params.append("start_date", startDate);
      if (endDate) params.append("end_date", endDate);

      const response = await fetch(`${API_URL}?${params.toString()}`);
      const json = await response.json();
      setData(json);
    } catch (error) {
      console.error("Error fetching market data:", error);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleSearch = () => {
    fetchData();
  };

  const columns = [
    { field: "ticker", headerName: "Ticker Symbol" },
    { field: "record_type", headerName: "Record Type" },
    { field: "timestamp", headerName: "Timestamp" },
    { field: "raw_line", headerName: "Data Line" },
  ];

  return (
    <div>
      <h1>Tertiary Records Table</h1>

      <div style={{ marginBottom: "1rem" }}>
        <div className="filters-container">
          <label className="filter-label">
            Filter by Ticker:
            <input
              type="text"
              value={ticker}
              onChange={(e) => setTicker(e.target.value)}
              placeholder="e.g. AAPL"
              className="filter-input"
            />
          </label>

          <label className="filter-label">
            Filter by Record Type:
            <select
              value={recordType}
              onChange={(e) => setRecordType(e.target.value)}
              className="filter-select"
            >
              <option value="">All</option>
              {Object.entries(recordTypeMap).map(([code, label]) => (
                <option key={code} value={code}>
                  {label}
                </option>
              ))}
            </select>
          </label>

          <label className="filter-label">
            Start Date:
            <input
              type="date"
              value={startDate}
              onChange={(e) => setStartDate(e.target.value)}
              className="filter-input"
            />
          </label>

          <label className="filter-label">
            End Date:
            <input
              type="date"
              value={endDate}
              onChange={(e) => setEndDate(e.target.value)}
              className="filter-input"
            />
          </label>
          <Button
            onClick={handleSearch}
            disabled={isLoading}
            style={{ marginLeft: "1rem" }}
            variant="contained"
          >
            {isLoading ? "Loading..." : "Search"}
          </Button>
        </div>
      </div>

      <DataTable columns={columns} data={Array.isArray(data) ? data : []} />
    </div>
  );
};

export default Tertiary;
