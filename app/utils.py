from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[1] / "data"

COUNTRY_FILES = {
    "Ethiopia": "ethiopia_clean.csv",
    "Kenya": "kenya_clean.csv",
    "Sudan": "sudan_clean.csv",
    "Tanzania": "tanzania_clean.csv",
    "Nigeria": "nigeria_clean.csv",
}


def load_climate_data() -> pd.DataFrame:
    frames = []

    for country, filename in COUNTRY_FILES.items():
        file_path = DATA_DIR / filename

        if not file_path.exists():
            raise FileNotFoundError(f"Missing file: {file_path}")

        df = pd.read_csv(file_path)
        df["Country"] = country
        df["Date"] = pd.to_datetime(df["Date"])
        df["Year"] = df["Date"].dt.year
        df["Month"] = df["Date"].dt.month
        frames.append(df)

    return pd.concat(frames, ignore_index=True)