# LP Signal OS

LP Signal OS is an agentic capital raising intelligence platform for investor relations, fundraising, and institutional sales teams.

It helps teams prioritize potential investors, generate investor-specific memos, identify likely objections, and create capital raising strategy recommendations.

## Live Demo Mode

This app runs in free demo mode by default. No paid API key is required.

The app supports provider routing:

- `AI_PROVIDER=demo` uses local deterministic memo and strategy generation.
- `AI_PROVIDER=anthropic` can be used later to call Claude through the Anthropic API.

## Why This Project Matters

Capital raising teams often work across fragmented CRM notes, investor preferences, call notes, and subjective judgment. LP Signal OS shows how AI-assisted workflows can support a more structured investor relations process.

## Core Features

- Investor pipeline scoring
- Investor-fit ranking
- Investor memo generation
- Capital raising strategy generation
- Demo-mode agentic workflow
- Claude-ready provider routing
- Audit logging
- Streamlit dashboard

## Technical Stack

- Python
- Streamlit
- Pandas
- Plotly
- Anthropic API-ready architecture
- Local fallback generation
- Config-driven model routing

## AI Engineering Concepts Demonstrated

- Agentic workflow design
- Provider routing
- Local fallback generation
- Human-in-the-loop decision support
- Auditability
- Investor-fit scoring
- Compliance-aware generation
- Separation of deterministic scoring and language generation

## How to Run Locally

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app.py