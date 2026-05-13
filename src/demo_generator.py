def create_demo_investor_memo(investor: dict, fund_profile: dict) -> str:
    return f"""
## Executive Summary

**{investor["name"]}** is ranked as **{investor["priority_tier"]}** with a fit score of **{investor["fit_score"]}/100**.

This recommendation is based on the investor's type, sector interest, liquidity preference, risk appetite, known concerns, and recent allocation signal.

## Why This Investor May Be a Fit

- **Investor type:** {investor["type"]}
- **Sector interest:** {investor["sector_interest"]}
- **Recent signal:** {investor["recent_signal"]}
- **Fit score:** {investor["fit_score"]}/100
- **Priority tier:** {investor["priority_tier"]}

The investor may be relevant for **{fund_profile["fund_name"]}** because the fund focuses on:

> {fund_profile["strategy"]}

## Why This Investor May Not Be a Fit

The main concern is:

> {investor["known_concerns"]}

Before outreach, the capital raising team should prepare a clear response to this concern.

## Likely Objections

The investor may ask about:

1. The depth and quality of the track record.
2. How the fund controls drawdowns.
3. Whether the AI infrastructure thesis is differentiated.
4. Whether the fund terms match their liquidity needs.
5. Whether the fund has enough operational maturity for institutional allocation.

## Best Outreach Angle

Lead with a specific AI infrastructure thesis rather than generic AI excitement.

A strong angle would be:

> “We focus on the picks-and-shovels layer of AI infrastructure: semiconductor supply chains, cloud software, data-center beneficiaries, and related public-market opportunities.”

## Suggested Email Draft

Subject: AI infrastructure strategy discussion

Hi,

I wanted to reach out because your current investment focus appears potentially aligned with **{fund_profile["fund_name"]}**.

The fund focuses on AI infrastructure, semiconductor supply chains, cloud software, and data-center beneficiaries through a long/short equity strategy.

Given your interest in **{investor["sector_interest"]}**, I thought it could be worth a brief introductory conversation.

Best,  
Aster Capital Team

## Meeting Preparation Questions

1. What role are you looking for new managers to play in the portfolio?
2. How do you evaluate emerging manager risk?
3. What liquidity profile is appropriate for this allocation?
4. What would make an AI infrastructure strategy credible to your team?
5. What concerns would prevent this from moving forward?

## Evidence Used

- Investor name: {investor["name"]}
- Investor type: {investor["type"]}
- Sector interest: {investor["sector_interest"]}
- Risk appetite: {investor["risk_appetite"]}
- Liquidity preference: {investor["liquidity_preference"]}
- Known concerns: {investor["known_concerns"]}
- Recent signal: {investor["recent_signal"]}
- Call notes: {investor.get("note", "No call notes available.")}

## Inferences Made

- The investor may be worth outreach if the team can address the known concern.
- The outreach should be tailored around the investor's stated sector interest and recent signal.
- The team should avoid making performance promises or implying guaranteed downside protection.

## Compliance Notes

This memo does not promise returns, does not imply the investment is safe, and does not provide personalized investment advice.

## Confidence Level

**3 out of 5**

The confidence level is moderate because the app has useful investor profile data and call notes, but it does not yet include full CRM history, actual allocation history, ticket size, decision-maker identity, or prior meeting transcripts.
"""


def create_demo_pipeline_strategy(scored_df, fund_profile: dict) -> str:
    top_targets = scored_df.head(3)
    low_targets = scored_df.tail(3)

    top_target_text = "\n".join(
        [
            f"- **{row['name']}**: {row['fit_score']}/100, {row['priority_tier']}. Reason: {row['recent_signal']}"
            for _, row in top_targets.iterrows()
        ]
    )

    low_target_text = "\n".join(
        [
            f"- **{row['name']}**: {row['fit_score']}/100, {row['priority_tier']}. Concern: {row['known_concerns']}"
            for _, row in low_targets.iterrows()
        ]
    )

    return f"""
## Capital Raising Strategy

### Executive Summary

The strongest near-term capital raising opportunity is to prioritize investors whose profile, stated interests, and recent signals align with **{fund_profile["fund_name"]}**.

The fund is raising **${fund_profile["target_raise_m"]}M** and currently has **${fund_profile["current_aum_m"]}M** in AUM.

The strategy is:

> {fund_profile["strategy"]}

## Top 3 Investor Targets

{top_target_text}

## Investors to Deprioritize

{low_target_text}

## Common Objections Across the Pipeline

The most likely objections are:

1. Track record length.
2. Operational maturity.
3. Liquidity terms.
4. Fee sensitivity.
5. Whether the AI thesis is differentiated or too crowded.
6. Whether the fund can clearly explain risk management.

## Recommended Capital Raising Strategy

The team should prioritize investors who are:

- open to emerging managers,
- interested in AI, technology, hedge funds, or alternatives,
- showing recent allocation activity,
- able to tolerate medium-to-high risk,
- compatible with quarterly liquidity.

The message should avoid generic AI hype and instead emphasize:

- AI infrastructure,
- semiconductor supply chains,
- cloud software,
- data-center beneficiaries,
- fundamental research,
- risk-managed exposure.

## 30-Day Action Plan

### Week 1

- Prioritize the top 3 investor targets.
- Prepare objection-handling notes for each.
- Create a two-minute explanation of the fund strategy.

### Week 2

- Send tailored outreach emails.
- Schedule introductory meetings.
- Collect missing information on liquidity needs, target ticket size, and prior hedge fund exposure.

### Week 3

- Hold investor calls.
- Record objections and buying signals.
- Update pipeline scores based on new information.

### Week 4

- Follow up with tailored materials.
- Identify which investors should move to diligence.
- Deprioritize investors with clear structural mismatches.

## Risks in the Current Pipeline

- Some investors may require a longer track record.
- Some investors may prefer lower-volatility or credit-oriented products.
- Some investors may need a simpler advisor-friendly story.
- Some investors may require more operational due diligence before allocating.

## Missing Information to Collect

The IR team should collect:

1. Target ticket size.
2. Prior hedge fund allocation history.
3. Decision-maker names.
4. Investment committee timeline.
5. Liquidity requirements.
6. Fee sensitivity.
7. Current manager roster.
8. Specific objections from first calls.

## Compliance Notes

The strategy should not promise returns, imply guaranteed downside protection, or describe the fund as risk-free.
"""