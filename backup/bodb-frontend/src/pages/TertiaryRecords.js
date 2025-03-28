import React, { useEffect, useState } from "react";
import DataTable from "../components/DataTable";

const API_URL = "http://localhost:3001/market-data?table=tertiary_records"; 

const Tertiary = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        fetch(API_URL)
            .then((response) => response.json())
            .then((data) => setData(data))
            .catch((error) => console.error("Error fetching market data:", error));
    }, []);

    const columns = [
        { field: "ticker", headerName: "Ticker Symbol" },
        { field: "record_type", headerName: "Record Type" },
        { field: "timestamp", headerName: "Timestamp" },
        { field: "raw_line", headerName: "Data Line" },
    ];

    return (
        <div>
            <h1>Tertiary Records Table</h1>
            <DataTable columns={columns} data={data} />
        </div>
    );
};

export default Tertiary;
