import pandas as pd


def score_investor_fit(investor: pd.Series, fund_profile: dict) -> dict:
    score = 0
    reasons = []

    target_types = fund_profile.get("target_investor_types", [])

    if investor["type"] in target_types:
        score += 25
        reasons.append("Investor type matches the fund's target investor profile.")
    else:
        reasons.append("Investor type is not a primary target for this fund.")

    if investor["preferred_stage"] == "Emerging Manager":
        score += 20
        reasons.append("Investor is open to emerging managers.")
    elif investor["preferred_stage"] == "Established Manager":
        score += 8
        reasons.append("Investor prefers established managers, which may create friction.")

    sector_interest = str(investor["sector_interest"]).lower()

    if "ai" in sector_interest or "technology" in sector_interest or "b2b saas" in sector_interest:
        score += 20
        reasons.append("Investor sector interests overlap with the fund's AI/technology strategy.")
    elif "hedge funds" in sector_interest or "global macro" in sector_interest:
        score += 12
        reasons.append("Investor has alternatives interest, though not a direct sector match.")
    else:
        reasons.append("Sector interest does not strongly match the fund strategy.")

    if investor["liquidity_preference"] == fund_profile["liquidity_terms"].split(" with ")[0]:
        score += 15
        reasons.append("Liquidity preference appears aligned with fund terms.")
    else:
        reasons.append("Liquidity preference may not fully align with fund terms.")

    risk_appetite = str(investor["risk_appetite"]).lower()
    fund_risk = str(fund_profile["risk_profile"]).lower()

    if risk_appetite in fund_risk:
        score += 15
        reasons.append("Risk appetite appears aligned.")
    elif risk_appetite == "high" and "medium" in fund_risk:
        score += 10
        reasons.append("Investor may tolerate the fund's risk profile.")
    else:
        reasons.append("Risk appetite may be a mismatch.")

    recent_signal = str(investor["recent_signal"]).lower()

    if any(word in recent_signal for word in ["allocating", "allocation", "seeking", "launching", "increasing"]):
        score += 5
        reasons.append("Recent signal suggests possible allocation activity.")

    score = min(score, 100)

    if score >= 75:
        tier = "High Priority"
    elif score >= 50:
        tier = "Medium Priority"
    else:
        tier = "Low Priority"

    return {
        "fit_score": score,
        "priority_tier": tier,
        "scoring_reasons": reasons
    }


def score_all_investors(investors: pd.DataFrame, fund_profile: dict) -> pd.DataFrame:
    results = []

    for _, row in investors.iterrows():
        scoring = score_investor_fit(row, fund_profile)
        combined = row.to_dict()
        combined.update(scoring)
        results.append(combined)

    return pd.DataFrame(results).sort_values(
        by="fit_score",
        ascending=False
    )