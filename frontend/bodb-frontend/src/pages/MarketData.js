import React, { useEffect, useState } from "react";
import DataTable from "../components/DataTable";

const API_URL = "http://localhost:3001/market-data";

const MarketData = () => {
  const [data, setData] = useState([]);
  const [ticker, setTicker] = useState("");
  const [minUnderlying, setMinUnderlying] = useState("");
  const [maxUnderlying, setMaxUnderlying] = useState("");
  const [minStrike, setMinStrike] = useState("");
  const [maxStrike, setMaxStrike] = useState("");
  const [minBid, setMinBid] = useState("");
  const [maxBid, setMaxBid] = useState("");
  const [minAsk, setMinAsk] = useState("");
  const [maxAsk, setMaxAsk] = useState("");
  const [minExpiration, setMinExpiration] = useState("");
  const [maxExpiration, setMaxExpiration] = useState("");
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const fetchData = async () => {
    setIsLoading(true);
    try {
      const params = new URLSearchParams();
      params.append("table", "quotes");
      if (ticker) params.append("ticker", ticker);
      if (startDate) params.append("start_date", startDate);
      if (endDate) params.append("end_date", endDate);
      if (minUnderlying) params.append("min_underlying", minUnderlying);
      if (maxUnderlying) params.append("max_underlying", maxUnderlying);
      if (minStrike) params.append("min_strike", minStrike);
      if (maxStrike) params.append("max_strike", maxStrike);
      if (minBid) params.append("min_bid", minBid);
      if (maxBid) params.append("max_bid", maxBid);
      if (minAsk) params.append("min_ask", minAsk);
      if (maxAsk) params.append("max_ask", maxAsk);
      if (startDate) params.append("start_date", startDate);
      if (endDate) params.append("end_date", endDate);
      if (minExpiration) params.append("min_expiration", minExpiration);
      if (maxExpiration) params.append("max_expiration", maxExpiration);

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
    { field: "timestamp", headerName: "Timestamp" },
    { field: "expiration_date", headerName: "Expiration Date" },
    { field: "strike_price", headerName: "Strike Price" },
    { field: "underlying_price", headerName: "Underlying Price" },
    { field: "bid", headerName: "Bid" },
    { field: "ask", headerName: "Ask" },
  ];

  return (
    <div>
      <h1>Market Data Table</h1>

      <div style={{ marginBottom: "1rem" }}>
        <label>
          Ticker:{" "}
          <input
            type="text"
            value={ticker}
            onChange={(e) => setTicker(e.target.value)}
            placeholder="e.g. AAPL"
          />
        </label>

        <label>
          Min Underlying Price:
          <input
            type="number"
            value={minUnderlying}
            onChange={(e) => setMinUnderlying(e.target.value)}
            step="0.01"
          />
        </label>

        <label style={{ marginLeft: "1rem" }}>
          Max Underlying Price:
          <input
            type="number"
            value={maxUnderlying}
            onChange={(e) => setMaxUnderlying(e.target.value)}
            step="0.01"
          />
        </label>

        <label style={{ marginLeft: "1rem" }}>
          Min Strike Price:
          <input
            type="number"
            value={minStrike}
            onChange={(e) => setMinStrike(e.target.value)}
            step="0.01"
          />
        </label>

        <label style={{ marginLeft: "1rem" }}>
          Max Strike Price:
          <input
            type="number"
            value={maxStrike}
            onChange={(e) => setMaxStrike(e.target.value)}
            step="0.01"
          />
        </label>
      </div>

      <div style={{ marginTop: "1rem" }}>
        <label>
          Min Bid:
          <input
            type="number"
            value={minBid}
            onChange={(e) => setMinBid(e.target.value)}
            step="0.01"
          />
        </label>

        <label style={{ marginLeft: "1rem" }}>
          Max Bid:
          <input
            type="number"
            value={maxBid}
            onChange={(e) => setMaxBid(e.target.value)}
            step="0.01"
          />
        </label>

        <label style={{ marginLeft: "1rem" }}>
          Min Ask:
          <input
            type="number"
            value={minAsk}
            onChange={(e) => setMinAsk(e.target.value)}
            step="0.01"
          />
        </label>

        <label style={{ marginLeft: "1rem" }}>
          Max Ask:
          <input
            type="number"
            value={maxAsk}
            onChange={(e) => setMaxAsk(e.target.value)}
            step="0.01"
          />
        </label>

        <label style={{ marginLeft: "1rem" }}>
          Start Date:{" "}
          <input
            type="date"
            value={startDate}
            onChange={(e) => setStartDate(e.target.value)}
          />
        </label>

        <label style={{ marginLeft: "1rem" }}>
          End Date:{" "}
          <input
            type="date"
            value={endDate}
            onChange={(e) => setEndDate(e.target.value)}
          />
        </label>
        <div style={{ marginTop: "1rem" }}>
          <label>
            Min Expiration Date:{" "}
            <input
              type="date"
              value={minExpiration}
              onChange={(e) => setMinExpiration(e.target.value)}
            />
          </label>

          <label style={{ marginLeft: "1rem" }}>
            Max Expiration Date:{" "}
            <input
              type="date"
              value={maxExpiration}
              onChange={(e) => setMaxExpiration(e.target.value)}
            />
          </label>
        </div>

        <button
          onClick={handleSearch}
          disabled={isLoading}
          style={{ marginLeft: "1rem" }}
        >
          {isLoading ? "Loading..." : "Search"}
        </button>
      </div>

      <DataTable columns={columns} data={data} />
    </div>
  );
};

export default MarketData;
