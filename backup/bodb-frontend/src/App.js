import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import MarketData from "./pages/MarketData";
import TradeRecords from "./pages/TradeRecords";
import Tertiary from "./pages/TertiaryRecords";

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
                        <li>
                            <Link to="/tertiary-records">Tertiary Records</Link>
                        </li>
                    </ul>
                </nav>

                <Routes>
                    <Route path="/" element={<MarketData />} />
                    <Route path="/trade-records" element={<TradeRecords />} />
                    <Route path="/tertiary-records" element={<Tertiary/>}/>
                </Routes>
            </div>
        </Router>
    );
}

export default App;
