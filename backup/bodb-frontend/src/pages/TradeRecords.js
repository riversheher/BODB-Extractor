import React, { useEffect, useState } from "react";
import DataTable from "../components/DataTable";

const API_URL = "http://localhost:3001/market-data";

const TradeRecords = () => {
  const [data, setData] = useState([]);
  const [ticker, setTicker] = useState("");
  const [minStrike, setMinStrike] = useState("");
  const [maxStrike, setMaxStrike] = useState("");
  const [minUnderlying, setMinUnderlying] = useState("");
  const [maxUnderlying, setMaxUnderlying] = useState("");
  const [minVolume, setMinVolume] = useState("");
  const [maxVolume, setMaxVolume] = useState("");
  const [minPrice, setMinPrice] = useState("");
  const [maxPrice, setMaxPrice] = useState("");
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const [minExpiration, setMinExpiration] = useState("");
  const [maxExpiration, setMaxExpiration] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const fetchData = async () => {
    setIsLoading(true);
    try {
      const params = new URLSearchParams();
      params.append("table", "trades");
      if (ticker) params.append("ticker", ticker);
      if (startDate) params.append("start_date", startDate);
      if (endDate) params.append("end_date", endDate);
      if (minExpiration) params.append("min_expiration", minExpiration);
      if (maxExpiration) params.append("max_expiration", maxExpiration);
      if (minStrike) params.append("min_strike", minStrike);
      if (maxStrike) params.append("max_strike", maxStrike);
      if (minUnderlying) params.append("min_underlying", minUnderlying);
      if (maxUnderlying) params.append("max_underlying", maxUnderlying);
      if (minVolume) params.append("min_volume", minVolume);
      if (maxVolume) params.append("max_volume", maxVolume);
      if (minPrice) params.append("min_price", minPrice);
      if (maxPrice) params.append("max_price", maxPrice);

      const response = await fetch(`${API_URL}?${params.toString()}`);
      const json = await response.json();
      setData(json);
    } catch (error) {
      console.error("Error fetching trade records:", error);
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
    { field: "volume", headerName: "Volume" },
    { field: "price", headerName: "Price" },
  ];

  return (
    <div>
      <h1>Trade Records Table</h1>

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

        <div style={{ marginTop: "1rem" }}>
          <label>
            Min Strike Price:
            <input
              type="number"
              step="0.01"
              value={minStrike}
              onChange={(e) => setMinStrike(e.target.value)}
            />
          </label>

          <label style={{ marginLeft: "1rem" }}>
            Max Strike Price:
            <input
              type="number"
              step="0.01"
              value={maxStrike}
              onChange={(e) => setMaxStrike(e.target.value)}
            />
          </label>

          <label style={{ marginLeft: "1rem" }}>
            Min Underlying Price:
            <input
              type="number"
              step="0.01"
              value={minUnderlying}
              onChange={(e) => setMinUnderlying(e.target.value)}
            />
          </label>

          <label style={{ marginLeft: "1rem" }}>
            Max Underlying Price:
            <input
              type="number"
              step="0.01"
              value={maxUnderlying}
              onChange={(e) => setMaxUnderlying(e.target.value)}
            />
          </label>
        </div>

        <div style={{ marginTop: "1rem" }}>
          <label>
            Min Volume:
            <input
              type="number"
              value={minVolume}
              onChange={(e) => setMinVolume(e.target.value)}
            />
          </label>

          <label style={{ marginLeft: "1rem" }}>
            Max Volume:
            <input
              type="number"
              value={maxVolume}
              onChange={(e) => setMaxVolume(e.target.value)}
            />
          </label>

          <label style={{ marginLeft: "1rem" }}>
            Min Price:
            <input
              type="number"
              step="0.01"
              value={minPrice}
              onChange={(e) => setMinPrice(e.target.value)}
            />
          </label>

          <label style={{ marginLeft: "1rem" }}>
            Max Price:
            <input
              type="number"
              step="0.01"
              value={maxPrice}
              onChange={(e) => setMaxPrice(e.target.value)}
            />
          </label>
        </div>

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

export default TradeRecords;
