import React, { useEffect, useState } from "react";
import DataTable from "../components/DataTable";

const API_URL = "https://xyz123.execute-api.us-east-2.amazonaws.com/prod/market-data"; // add API URL HERE

const MarketData = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        fetch(API_URL)
            .then((response) => response.json())
            .then((data) => setData(data))
            .catch((error) => console.error("Error fetching market data:", error));
    }, []);

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
            <DataTable columns={columns} data={data} />
        </div>
    );
};

export default MarketData;
