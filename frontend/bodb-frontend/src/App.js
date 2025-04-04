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
            backgroundColor: "#6a0dad",
            color: "white",
            padding: "0",
            boxSizing: "border-box",
          }}
        >
          <ul style={{ listStyle: "none", margin: 0, padding: 0 }}>
            <li>
              <Link
                to="/"
                style={{
                  display: "block",
                  padding: "1rem",
                  borderTop: "1px solid white",
                  borderBottom: "1px solid white",
                  textDecoration: "none",
                  color: "white",
                  fontWeight: "bold",
                  width: "100%",
                }}
              >
                Market Data
              </Link>
            </li>
            <li>
              <Link
                to="/trade-records"
                style={{
                  display: "block",
                  padding: "1rem",
                  borderTop: "1px solid white",
                  borderBottom: "1px solid white",
                  textDecoration: "none",
                  color: "white",
                  fontWeight: "bold",
                  width: "100%",
                }}
              >
                Trade Records
              </Link>
            </li>
            <li>
              <Link
                to="/tertiary-records"
                style={{
                  display: "block",
                  padding: "1rem",
                  borderTop: "1px solid white",
                  borderBottom: "1px solid white",
                  textDecoration: "none",
                  color: "white",
                  fontWeight: "bold",
                  width: "100%",
                }}
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
