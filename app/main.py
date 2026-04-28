import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils import load_climate_data

st.set_page_config(
    page_title="African Climate Dashboard",
    page_icon="🌍",
    layout="wide"
)

sns.set_theme(style="whitegrid")

st.title("🌍 African Climate Trend Dashboard (COP32 Analysis)")
st.markdown(
    """
    This dashboard visualizes climate trends across Ethiopia, Kenya, Sudan, Tanzania, and Nigeria.
    It supports COP32-focused climate analysis using cleaned NASA POWER climate datasets.
    """
)

@st.cache_data
def get_data():
    return load_climate_data()

df = get_data()

st.sidebar.header("Dashboard Filters")

countries = st.sidebar.multiselect(
    "Select countries",
    options=sorted(df["Country"].unique()),
    default=sorted(df["Country"].unique())
)

year_range = st.sidebar.slider(
    "Select year range",
    min_value=int(df["Year"].min()),
    max_value=int(df["Year"].max()),
    value=(int(df["Year"].min()), int(df["Year"].max()))
)

variable = st.sidebar.selectbox(
    "Select climate variable",
    options=["T2M", "PRECTOTCORR", "RH2M", "WS2M", "T2M_MAX", "T2M_MIN", "T2M_RANGE"]
)

filtered_df = df[
    (df["Country"].isin(countries)) &
    (df["Year"].between(year_range[0], year_range[1]))
]

if filtered_df.empty:
    st.warning("No data available for the selected filters.")
    st.stop()

col1, col2, col3 = st.columns(3)
col1.metric("Selected Countries", len(countries))
col2.metric("Total Records", len(filtered_df))
col3.metric("Year Range", f"{year_range[0]} - {year_range[1]}")

st.divider()

st.subheader("🌡️ Monthly Temperature Trend")

monthly_temp = (
    filtered_df
    .groupby(["Year", "Month", "Country"])["T2M"]
    .mean()
    .reset_index()
)

monthly_temp["Date"] = pd.to_datetime(
    monthly_temp["Year"].astype(str) + "-" + monthly_temp["Month"].astype(str) + "-01"
)

fig, ax = plt.subplots(figsize=(12, 5))

for country in monthly_temp["Country"].unique():
    country_data = monthly_temp[monthly_temp["Country"] == country]
    ax.plot(country_data["Date"], country_data["T2M"], label=country)

ax.set_title("Monthly Average Temperature Trend")
ax.set_xlabel("Date")
ax.set_ylabel("Temperature (°C)")
ax.legend()

st.pyplot(fig)

st.subheader("🌧️ Precipitation Distribution")

fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.boxplot(data=filtered_df, x="Country", y="PRECTOTCORR", ax=ax2)

ax2.set_title("Precipitation Distribution by Country")
ax2.set_xlabel("Country")
ax2.set_ylabel("Precipitation (mm/day)")

st.pyplot(fig2)

st.subheader(f"📊 Selected Variable Trend: {variable}")

monthly_variable = (
    filtered_df
    .groupby(["Year", "Month", "Country"])[variable]
    .mean()
    .reset_index()
)

monthly_variable["Date"] = pd.to_datetime(
    monthly_variable["Year"].astype(str) + "-" + monthly_variable["Month"].astype(str) + "-01"
)

fig3, ax3 = plt.subplots(figsize=(12, 5))

for country in monthly_variable["Country"].unique():
    country_data = monthly_variable[monthly_variable["Country"] == country]
    ax3.plot(country_data["Date"], country_data[variable], label=country)

ax3.set_title(f"Monthly Average {variable}")
ax3.set_xlabel("Date")
ax3.set_ylabel(variable)
ax3.legend()

st.pyplot(fig3)

st.subheader("📄 Filtered Data Preview")
st.dataframe(filtered_df.head(100), use_container_width=True)

st.subheader("📌 Key Insights")

st.markdown("""
- Sudan shows the highest temperature levels and extreme heat trends.
- Nigeria and Tanzania exhibit high rainfall variability.
- Ethiopia maintains moderate climate patterns compared to others.
- Climate variability differs significantly across regions.
- Sudan is the most vulnerable based on heat and drought indicators.
""")

st.markdown("---")
st.markdown("Built for COP32 Climate Analysis | Aisha Hussein")