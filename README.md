🌍 African Climate Trend Analysis (COP32 Preparation)
📌 Overview

This project analyzes climate data across five African countries — Ethiopia, Kenya, Sudan, Tanzania, and Nigeria — to identify trends, variability, and climate vulnerability patterns in preparation for COP32 (Addis Ababa, 2027).

The goal is to transform raw climate data into actionable insights that support climate policy decisions and regional prioritization for climate finance.

🎯 Objectives
Analyze temperature and precipitation trends (2015–2026)
Identify extreme climate events (heatwaves & drought)
Compare climate patterns across countries
Rank countries based on climate vulnerability
Provide data-driven recommendations for COP32
🧠 Analytical Framework

This project follows a structured three-layer climate analysis approach:

What is changing?
Identify trends in temperature, rainfall, and other variables
Trend with baseline
Compare patterns over time to detect increases, decreases, or stability
Uncertainty & variability
Analyze fluctuations, extreme events, and data variability
⚙️ Project Structure
climate-challenge-week0/
│
├── notebooks/
│   ├── ethiopia_eda.ipynb
│   ├── kenya_eda.ipynb
│   ├── nigeria_eda.ipynb
│   ├── sudan_eda.ipynb
│   ├── tanzania_eda.ipynb
│   └── compare_countries.ipynb
│
├── data/                # (ignored in Git)
├── scripts/
├── tests/
├── .github/workflows/
├── README.md
└── requirements.txt
🧹 Data Processing
Replaced NASA missing values (-999) with NaN
Checked and removed duplicate rows
Handled missing values using forward fill
Converted YEAR and DOY into proper datetime format
Extracted Month and Year for time-series analysis
📊 Exploratory Data Analysis (EDA)

For each country:

Summary statistics
Monthly temperature trends
Rainfall distribution analysis
Correlation heatmaps
Scatter and bubble plots
🌡️ Cross-Country Analysis
Temperature Trends
Sudan shows consistently higher temperatures
Ethiopia and Kenya exhibit moderate climates
Nigeria and Tanzania maintain warm conditions year-round
Precipitation Patterns
Nigeria and Tanzania show high rainfall variability
Sudan has very low rainfall (dry climate)
Ethiopia and Kenya show moderate seasonal rainfall
🔥 Extreme Climate Events
Extreme Heat: Days where temperature > 35°C
Dry Days: Days with rainfall < 1 mm

Findings:

Sudan has the highest extreme heat and drought frequency
Nigeria and Tanzania show variability-driven risk
Ethiopia has moderate climate stress
📈 Statistical Analysis

A Kruskal-Wallis test confirmed that temperature differences across countries are statistically significant (p < 0.05), meaning observed variations reflect real climate differences.

⚠️ Climate Vulnerability Ranking

Countries were ranked based on:

Average temperature
Rainfall variability
Extreme heat frequency
Dry-day frequency

Most Vulnerable → Least Vulnerable:

Sudan
Nigeria
Tanzania
Ethiopia
Kenya
🌍 COP32 Key Insights
Sudan faces severe climate stress due to extreme heat and drought
Nigeria and Tanzania are vulnerable to unstable rainfall patterns
Ethiopia shows moderate but notable climate variability
Climate risks vary significantly across regions
Sudan should be prioritized for climate finance support
🚀 Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
SciPy
🔁 Reproducibility

This project is fully reproducible:

git clone <your-repo-link>
cd climate-challenge-week0
pip install -r requirements.txt