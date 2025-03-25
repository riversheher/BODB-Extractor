import React, { useEffect, useState } from "react";
import DataTable from "../components/DataTable";

const API_URL = process.env.API_URL + "/trade-records";

const TradeRecords = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        fetch(API_URL)
            .then((response) => response.json())
            .then((data) => setData(data))
            .catch((error) => console.error("Error fetching trade records:", error));
    }, []);

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
            <h1>Trade Records Table</h1>
            <DataTable columns={columns} data={data} />
        </div>
    );
};

export default TradeRecords;
