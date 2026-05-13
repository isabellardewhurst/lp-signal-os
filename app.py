import os

import plotly.express as px
import streamlit as st

from src.config import AI_PROVIDER
from src.data_loader import (
    combine_investor_data,
    load_call_notes,
    load_fund_profile,
    load_investors,
)
from src.scoring import score_all_investors
from src.agent_workflow import (
    create_investor_memo,
    create_pipeline_strategy,
)


os.makedirs("outputs", exist_ok=True)

st.set_page_config(
    page_title="LP Signal OS",
    page_icon="📈",
    layout="wide",
)

st.title("📈 LP Signal OS")
st.subheader("Agentic capital raising intelligence for investor relations teams")

if AI_PROVIDER == "demo":
    st.info("Running in free demo mode. No paid API calls are being made.")
else:
    st.warning(f"Running with AI provider: {AI_PROVIDER}")

st.markdown(
    """
    This app helps capital raising and investor relations teams prioritize investors,
    understand likely objections, and prepare evidence-based outreach.
    """
)

fund_profile = load_fund_profile()
investors = load_investors()
call_notes = load_call_notes()
combined = combine_investor_data(investors, call_notes)
scored = score_all_investors(combined, fund_profile)

tab1, tab2, tab3 = st.tabs(
    [
        "Investor Pipeline",
        "Investor Memo Agent",
        "Pipeline Strategy Agent",
    ]
)


with tab1:
    st.header("Investor Pipeline")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Target Raise", f"${fund_profile['target_raise_m']}M")

    with col2:
        st.metric("Current AUM", f"${fund_profile['current_aum_m']}M")

    with col3:
        st.metric("Track Record", f"{fund_profile['track_record_years']} years")

    st.subheader("Ranked Investors")

    display_columns = [
        "name",
        "type",
        "region",
        "sector_interest",
        "fit_score",
        "priority_tier",
        "known_concerns",
        "recent_signal",
    ]

    st.dataframe(
        scored[display_columns],
        use_container_width=True,
    )

    fig = px.bar(
        scored,
        x="name",
        y="fit_score",
        color="priority_tier",
        title="Investor Fit Scores",
    )

    st.plotly_chart(fig, use_container_width=True)


with tab2:
    st.header("Investor Memo Agent")

    investor_name = st.selectbox(
        "Choose an investor",
        scored["name"].tolist(),
    )

    selected = scored[scored["name"] == investor_name].iloc[0].to_dict()

    st.write("### Selected Investor")

    metric_col1, metric_col2, metric_col3 = st.columns(3)

    with metric_col1:
        st.metric("Investor", selected["name"])

    with metric_col2:
        st.metric("Fit Score", selected["fit_score"])

    with metric_col3:
        st.metric("Priority", selected["priority_tier"])

    st.write("#### Investor Details")

    selected_details = {
        "Field": [
            "Type",
            "Region",
            "Sector Interest",
            "Risk Appetite",
            "Liquidity Preference",
            "Known Concerns",
            "Recent Signal",
        ],
        "Value": [
            selected["type"],
            selected["region"],
            selected["sector_interest"],
            selected["risk_appetite"],
            selected["liquidity_preference"],
            selected["known_concerns"],
            selected["recent_signal"],
        ],
    }

    st.table(selected_details)

    if st.button("Generate Investor Memo"):
        with st.spinner("Generating investor memo..."):
            memo = create_investor_memo(selected, fund_profile)

        st.markdown("## Investor Intelligence Memo")
        st.markdown(memo)


with tab3:
    st.header("Pipeline Strategy Agent")

    if st.button("Generate Pipeline Strategy"):
        with st.spinner("Generating pipeline strategy..."):
            strategy = create_pipeline_strategy(scored, fund_profile)

        st.markdown("## Capital Raising Strategy")
        st.markdown(strategy)