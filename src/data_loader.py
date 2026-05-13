import json
import pandas as pd


def load_investors(path: str = "data/investors.csv") -> pd.DataFrame:
    return pd.read_csv(path)


def load_call_notes(path: str = "data/call_notes.csv") -> pd.DataFrame:
    return pd.read_csv(path)


def load_fund_profile(path: str = "data/fund_profile.json") -> dict:
    with open(path, "r") as f:
        return json.load(f)


def combine_investor_data(
    investors: pd.DataFrame,
    call_notes: pd.DataFrame
) -> pd.DataFrame:
    notes_grouped = (
        call_notes
        .groupby("investor_id")["note"]
        .apply(lambda notes: " | ".join(notes))
        .reset_index()
    )

    combined = investors.merge(
        notes_grouped,
        on="investor_id",
        how="left"
    )

    combined["note"] = combined["note"].fillna("No call notes available.")
    return combined