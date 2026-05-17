# Adidas Interactive Sales Dashboard
**Category:** Data Science  
**Tech Stack:** Python, Streamlit, Plotly, Pandas, Pillow  
**Status:** Complete  
**Thumbnail:** assets/thumbnail.png
## Overview
An interactive Streamlit dashboard for exploring Adidas store sales data. Visualize sales performance by retailer, track monthly revenue trends, and download filtered data — all through an intuitive web interface with real-time chart rendering.
## Features
- **Retailer Sales Chart**: Bar chart showing total sales by retailer
- **Monthly Trend Analysis**: Line graph tracking revenue over time
- **Data Download**: Export filtered sales data as CSV
- **Interactive Filtering**: Expandable sections for detailed data views
- **Real-Time Updates**: Auto-refreshes with current date display
- **Responsive Layout**: Wide-screen optimized with multi-column design
## Project Structure
```
Adidas_store_sales/
├── app.py                        # Streamlit dashboard application
├── Adidas.xlsx                   # Sales dataset
└── README.md
```
## Dataset
**Adidas Sales Data**
- Retailer information
- Invoice dates
- Product details
- Total sales amounts
- Monthly and yearly aggregations
## Getting Started
### Prerequisites
- Python 3.8+
- Streamlit
### Installation
```bash
git clone https://github.com/Dr-Aniekan-Udo/Adidas_store_sales.git
cd Adidas_store_sales
pip install streamlit pandas plotly openpyxl pillow
```
### Run the Dashboard
```bash
streamlit run app.py
```
The app opens at `http://localhost:8501`
## Dashboard Sections
| Section | Visualization |
|---------|---------------|
| **Retailer Sales** | Bar chart of total sales by retailer |
| **Monthly Trends** | Line graph of revenue over time |
| **Data Export** | Downloadable CSV of sales data |
## Tech Stack
- **Framework**: Streamlit
- **Visualization**: Plotly Express, Plotly Graph Objects
- **Data Processing**: Pandas
- **Image**: Pillow
## Contact
- **Email**: [Aniekan Udo @Gmail](mailto:aniekanetimudo+reachout@gmail.com)
- **LinkedIn**: [Aniekan Udo @Linkedin](https://www.linkedin.com/in/aniekan-etim-udo)
## License
MIT
