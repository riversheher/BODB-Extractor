import React, { useEffect, useState } from "react";
import DataTable from "../components/DataTable";

const API_URL = "http://localhost:3001/market-data?table=trades";

const TradeRecords = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        fetch(API_URL)
            .then((response) => response.json())
            .then((data) => setData(data))
            .catch((error) => console.error("Error fetching trade records:", error));
    }, []);

    const columns = [
        { field: "ticker", headerName: "Ticker Symbol" },
        { field: "timestamp", headerName: "Timestamp" },
        { field: "expiration_date", headerName: "Expiration Date" },
        { field: "strike_price", headerName: "Strike Price" },
        { field: "volume", headerName: "Volume" },
        { field: "price", headerName: "Price" },
    ];

    return (
        <div>
            <h1>Trade Records Table</h1>
            <DataTable columns={columns} data={data} />
        </div>
    );
};

export default TradeRecords;
