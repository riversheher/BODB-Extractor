import React, { useEffect, useState } from "react";
import DataTable from "../components/DataTable";

const API_URL = "http://localhost:3001/market-data?table=quotes"; 

const MarketData = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        fetch(API_URL)
            .then((response) => response.json())
            .then((data) => setData(data))
            .catch((error) => console.error("Error fetching market data:", error));
    }, []);

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
            <DataTable columns={columns} data={data} />
        </div>
    );
};

export default MarketData;
