import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import MarketData from "./pages/MarketData";
import TradeRecords from "./pages/TradeRecords";

function App() {
    return (
        <Router>
            <div>
                <nav>
                    <ul>
                        <li>
                            <Link to="/">Market Data</Link>
                        </li>
                        <li>
                            <Link to="/trade-records">Trade Records</Link>
                        </li>
                    </ul>
                </nav>

                <Routes>
                    <Route path="/" element={<MarketData />} />
                    <Route path="/trade-records" element={<TradeRecords />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;
