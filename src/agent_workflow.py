import json
import os
from datetime import datetime

from src.config import AI_PROVIDER
from src.claude_client import ask_claude
from src.demo_generator import (
    create_demo_investor_memo,
    create_demo_pipeline_strategy
)
from src.prompts import (
    CAPITAL_RAISING_SYSTEM_PROMPT,
    INVESTOR_MEMO_TEMPLATE,
    PORTFOLIO_PIPELINE_PROMPT
)


def write_audit_log(event: dict, path: str = "outputs/audit_log.jsonl") -> None:
    os.makedirs("outputs", exist_ok=True)

    event["timestamp"] = datetime.utcnow().isoformat()
    event["ai_provider"] = AI_PROVIDER

    with open(path, "a") as f:
        f.write(json.dumps(event) + "\n")


def create_investor_memo(investor: dict, fund_profile: dict) -> str:
    if AI_PROVIDER == "demo":
        response = create_demo_investor_memo(investor, fund_profile)

        write_audit_log({
            "workflow": "create_investor_memo",
            "mode": "demo",
            "investor_id": investor.get("investor_id"),
            "investor_name": investor.get("name"),
            "fit_score": investor.get("fit_score"),
            "priority_tier": investor.get("priority_tier")
        })

        return response

    user_prompt = INVESTOR_MEMO_TEMPLATE.format(
        fund_profile=json.dumps(fund_profile, indent=2),
        investor_profile=json.dumps(investor, indent=2),
        call_notes=investor.get("note", "No notes available."),
        fit_score=investor.get("fit_score"),
        priority_tier=investor.get("priority_tier"),
        scoring_reasons=investor.get("scoring_reasons")
    )

    response = ask_claude(
        system_prompt=CAPITAL_RAISING_SYSTEM_PROMPT,
        user_prompt=user_prompt
    )

    if response.startswith("Claude unavailable"):
        response = create_demo_investor_memo(investor, fund_profile)

    write_audit_log({
        "workflow": "create_investor_memo",
        "mode": AI_PROVIDER,
        "investor_id": investor.get("investor_id"),
        "investor_name": investor.get("name"),
        "fit_score": investor.get("fit_score"),
        "priority_tier": investor.get("priority_tier")
    })

    return response


def create_pipeline_strategy(scored_df, fund_profile: dict) -> str:
    if AI_PROVIDER == "demo":
        response = create_demo_pipeline_strategy(scored_df, fund_profile)

        write_audit_log({
            "workflow": "create_pipeline_strategy",
            "mode": "demo",
            "num_investors": len(scored_df),
            "top_investor": scored_df.iloc[0]["name"]
        })

        return response

    compact_table = scored_df[
        [
            "name",
            "type",
            "region",
            "sector_interest",
            "known_concerns",
            "recent_signal",
            "fit_score",
            "priority_tier"
        ]
    ].to_markdown(index=False)

    user_prompt = PORTFOLIO_PIPELINE_PROMPT.format(
        fund_profile=json.dumps(fund_profile, indent=2),
        investor_table=compact_table
    )

    response = ask_claude(
        system_prompt=CAPITAL_RAISING_SYSTEM_PROMPT,
        user_prompt=user_prompt
    )

    if response.startswith("Claude unavailable"):
        response = create_demo_pipeline_strategy(scored_df, fund_profile)

    write_audit_log({
        "workflow": "create_pipeline_strategy",
        "mode": AI_PROVIDER,
        "num_investors": len(scored_df),
        "top_investor": scored_df.iloc[0]["name"]
    })

    return response