import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import MarketData from "./pages/MarketData";
import TradeRecords from "./pages/TradeRecords";
import Tertiary from "./pages/TertiaryRecords";

function App() {
  return (
    <Router>
      <div style={{ display: "flex", minHeight: "100vh" }}>
        <nav
          style={{
            width: "200px",
            backgroundColor: "#6a0dad", // Purple
            color: "white",
            padding: "1rem",
            boxSizing: "border-box",
          }}
        >
          <ul style={{ listStyle: "none", padding: 0 }}>
            <li style={{ marginBottom: "1rem" }}>
              <Link to="/" style={{ color: "white", textDecoration: "none" }}>
                Market Data
              </Link>
            </li>
            <li style={{ marginBottom: "1rem" }}>
              <Link
                to="/trade-records"
                style={{ color: "white", textDecoration: "none" }}
              >
                Trade Records
              </Link>
            </li>
            <li>
              <Link
                to="/tertiary-records"
                style={{ color: "white", textDecoration: "none" }}
              >
                Tertiary Records
              </Link>
            </li>
          </ul>
        </nav>

        <main style={{ flexGrow: 1, padding: "2rem" }}>
          <Routes>
            <Route path="/" element={<MarketData />} />
            <Route path="/trade-records" element={<TradeRecords />} />
            <Route path="/tertiary-records" element={<Tertiary />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
