def answer_question(question, deals, insights):

    question = question.lower()

    if "biggest opportunity" in question:
        biggest = max(
            deals,
            key=lambda x: float(x["value"]) if x["value"] else 0
        )

        return f"""
🚀 Biggest Opportunity

Client:
{biggest['client']}

Sector:
{biggest['sector']}

Deal Value:
₹ {float(biggest['value'])/10000000:.2f} Cr

Stage:
{biggest['stage']}

Founder Action:
Prioritize this deal and ensure executive-level follow-up.
"""


    elif "risky" in question:

        risky=[]

        for d in deals:
            if "hold" in d["stage"].lower():
                risky.append(d)

        if risky:
            return f"""
⚠️ Risk Alert

{len(risky)} deals are currently on hold.

Recommended Action:
- Review blockers
- Contact clients
- Revalidate timelines
"""
        else:
            return "No major risks detected."


    elif "owner" in question:

        best=max(
            insights["owner_analysis"],
            key=insights["owner_analysis"].get
        )

        return f"""
🏆 Top Performing Owner

{best}

Pipeline Managed:

₹ {insights['owner_analysis'][best]/10000000:.2f} Cr
"""


    elif "sector" in question:

        best=max(
            insights["sector_analysis"],
            key=insights["sector_analysis"].get
        )

        return f"""
📈 Sector Recommendation

Focus Sector:

{best}

Pipeline:

₹ {insights['sector_analysis'][best]/10000000:.2f} Cr

Founder Action:
Increase sales investment in this segment.
"""


    elif "action" in question:

        return """
🧠 Founder Actions This Week

1. Follow up with high-value proposals.
2. Revive projects currently on hold.
3. Review feasibility stage deals.
4. Push negotiation-stage opportunities.
5. Assign owners clear closing targets.
"""


    else:

        return """
I can answer questions about:

• Biggest opportunities
• Risky deals
• Owner performance
• Sector strategy
• Founder actions

Please ask a pipeline question.
"""