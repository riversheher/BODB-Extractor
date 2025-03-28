import axios from "axios";

// Set the API endpoint 
const API_URL = "";

export const fetchMarketData = async (page, pageSize) => {
  const response = await axios.get(`${API_URL}/market_data`, {
    params: { page, pageSize },
  });
  return response.data;
};

export const fetchTradeRecords = async (page, pageSize) => {
  const response = await axios.get(`${API_URL}/trade_record`, {
    params: { page, pageSize },
  });
  return response.data;
};
