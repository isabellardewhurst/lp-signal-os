# LP Signal OS

LP Signal OS is an agentic capital raising intelligence platform for investor relations, fundraising, and institutional sales teams.

It helps teams prioritize potential investors, generate investor-specific memos, identify likely objections, and create capital raising strategy recommendations.

## Live Demo

Add your deployed Streamlit link here:

```text
https://your-app-name.streamlit.app
```

## Live Demo Mode

This app runs in free demo mode by default. No paid API key is required.

The app supports provider routing:

- `AI_PROVIDER=demo` uses local deterministic memo and strategy generation.
- `AI_PROVIDER=anthropic` can be used later to call Claude through the Anthropic API.

## Why This Project Matters

Capital raising teams often work across fragmented CRM notes, investor preferences, call notes, and subjective judgment.

LP Signal OS shows how AI-assisted workflows can support a more structured investor relations process by combining:

- deterministic scoring,
- configurable AI provider routing,
- investor-specific memo generation,
- pipeline strategy recommendations,
- audit logging,
- and compliance-aware language generation.

## Core Features

- Investor pipeline scoring
- Investor-fit ranking
- Investor memo generation
- Capital raising strategy generation
- Demo-mode agentic workflow
- Claude-ready provider routing
- Audit logging
- Streamlit dashboard
- Free local fallback generation

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
- Production-style configuration management

## Example Use Case

A fund manager wants to raise capital and has a list of potential LPs.

LP Signal OS ranks investors, explains why each investor is or is not a fit, identifies likely objections, and generates investor-specific talking points.

Example questions the app helps answer:

- Which investors should the capital raising team prioritize?
- Why is a specific investor a strong or weak fit?
- What objections is this investor likely to raise?
- What should the outreach angle be?
- What information is missing before a meeting?
- Which investors should be deprioritized?

## Project Structure

```text
lp-signal-os/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
├── data/
│   ├── investors.csv
│   ├── fund_profile.json
│   └── call_notes.csv
│
├── src/
│   ├── config.py
│   ├── data_loader.py
│   ├── scoring.py
│   ├── claude_client.py
│   ├── prompts.py
│   ├── demo_generator.py
│   └── agent_workflow.py
```

## How to Run Locally

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/lp-signal-os.git
cd lp-signal-os
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

On macOS:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the app:

```bash
python -m streamlit run app.py
```

## Environment Variables

Create a `.env` file in the main project folder.

For free demo mode:

```env
AI_PROVIDER=demo
ANTHROPIC_API_KEY=
```

To use Claude through the Anthropic API later:

```env
AI_PROVIDER=anthropic
ANTHROPIC_API_KEY=your_api_key_here
```

## Streamlit Cloud Configuration

For Streamlit Community Cloud, add the following secrets in the app settings:

```toml
AI_PROVIDER = "demo"
ANTHROPIC_API_KEY = ""
```

If you later want to use Claude in production, update the Streamlit secrets to:

```toml
AI_PROVIDER = "anthropic"
ANTHROPIC_API_KEY = "your_api_key_here"
```

Do not commit real API keys to GitHub.

## Data Files

The app currently uses sample data stored in the `data/` folder.

### `investors.csv`

Contains investor profile information such as:

- investor name,
- investor type,
- AUM,
- region,
- preferred stage,
- sector interest,
- risk appetite,
- liquidity preference,
- known concerns,
- recent allocation signal.

### `fund_profile.json`

Contains the sample fund profile used for scoring and memo generation.

### `call_notes.csv`

Contains sample call notes linked to each investor.

## How Investor Scoring Works

The app uses a deterministic scoring system before any memo or strategy is generated.

Investors receive points based on:

- whether their investor type matches the fund’s target investor profile,
- whether they are open to emerging managers,
- whether their sector interests match the fund strategy,
- whether their liquidity preferences align with the fund terms,
- whether their risk appetite is compatible,
- whether their recent signal suggests possible allocation activity.

This creates a repeatable investor-fit score from 0 to 100.

Priority tiers are assigned as:

```text
75 to 100: High Priority
50 to 74: Medium Priority
0 to 49: Low Priority
```

## Provider Routing

The app supports two AI provider modes.

### Demo Mode

```env
AI_PROVIDER=demo
```

This mode uses local deterministic generation. It does not make paid API calls.

### Anthropic Mode

```env
AI_PROVIDER=anthropic
```

This mode sends prompts to Claude through the Anthropic API.

If Claude is unavailable, the app can fall back to demo generation rather than crashing.

## Audit Logging

When a memo or pipeline strategy is generated, the app writes an audit event to:

```text
outputs/audit_log.jsonl
```

The audit log records:

- workflow name,
- selected investor,
- fit score,
- priority tier,
- AI provider mode,
- timestamp.

The `outputs/` folder is ignored by Git because it is generated locally.

## Security Notes

This repository should not contain real API keys.

The following files and folders are ignored by Git:

```text
.env
.venv/
__pycache__/
outputs/
.streamlit/secrets.toml
```

Use `.env.example` to show required environment variable names without exposing private secrets.

## Current Project Status

Current version includes:

- Working Streamlit dashboard
- Free demo mode
- Investor scoring
- Investor memo generation
- Pipeline strategy generation
- Audit logging
- Claude-ready provider routing

Planned upgrades:

- Evaluation Lab
- CSV upload
- CRM-style pipeline stages
- Meeting prep mode
- Compliance red-team tests
- Prompt/model regression tracking
- Exportable investor memos
- Investor pipeline editing
- Persistent database storage

## Portfolio Positioning

This project demonstrates the ability to build an AI product, not just a chatbot.

It combines:

- structured data,
- deterministic business logic,
- AI-style generation,
- provider routing,
- Streamlit product design,
- auditability,
- and capital markets workflow knowledge.

## Suggested GitHub Repo Description

```text
Agentic capital raising intelligence platform for investor relations teams, with investor-fit scoring, memo generation, pipeline strategy, audit logging, and demo-mode AI provider routing.
```

## Suggested GitHub Topics

```text
streamlit
python
ai-engineering
agentic-ai
investor-relations
capital-raising
fundraising
fintech
```

## Disclaimer

This project uses sample data and is intended for educational and portfolio purposes.

It does not provide investment advice, does not recommend securities, and does not guarantee investment outcomes.