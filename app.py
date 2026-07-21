import streamlit as st
from board_service import BoardService
from data_processor import process_deals
from ai_assistant import answer_question


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Founder Copilot",
    page_icon="🚀",
    layout="wide"
)


# -----------------------------
# Title
# -----------------------------

st.title("🚀 Founder Copilot")

st.caption(
    "AI Business Intelligence Agent for Founders"
)


# -----------------------------
# Connect Monday Board
# -----------------------------

service = BoardService()


try:

    deals = service.get_deals()

    st.success(
        "Connected to Monday.com Deals board"
    )


    # -----------------------------
    # Data Processing
    # -----------------------------

    processed_deals = process_deals(deals)



    # -----------------------------
    # Intelligence Calculation
    # -----------------------------

    def calculate_insights(deals):

        total_pipeline = 0

        stage_count = {}

        sector_value = {}

        owner_value = {}


        for deal in deals:

            value = deal.get("value")


            if value:

                value = float(value)

                total_pipeline += value

            else:

                value = 0



            stage = deal.get(
                "stage",
                "Unknown"
            )


            sector = deal.get(
                "sector",
                "Unknown"
            )


            owner = deal.get(
                "owner",
                "Unknown"
            )


            stage_count[stage] = (
                stage_count.get(stage,0)+1
            )


            sector_value[sector] = (
                sector_value.get(sector,0)+value
            )


            owner_value[owner] = (
                owner_value.get(owner,0)+value
            )



        return {

            "total_pipeline": total_pipeline,

            "stage_breakdown": stage_count,

            "sector_analysis": sector_value,

            "owner_analysis": owner_value
        }



    insights = calculate_insights(
        processed_deals
    )



    # -----------------------------
    # Dashboard
    # -----------------------------

    st.divider()

    st.header(
        "📊 Founder Intelligence Dashboard"
    )


    col1,col2,col3 = st.columns(3)



    with col1:

        st.metric(

            "Total Pipeline",

            f"₹ {insights['total_pipeline']/10000000:.2f} Cr"

        )



    with col2:

        st.metric(

            "Active Deals",

            len(processed_deals)

        )



    with col3:

        st.metric(

            "Sectors Covered",

            len(insights["sector_analysis"])

        )




    # -----------------------------
    # Analytics
    # -----------------------------


    st.subheader(
        "📈 Pipeline Analysis"
    )


    st.write(
        "Deal Stage Distribution"
    )


    st.bar_chart(
        insights["stage_breakdown"]
    )



    st.write(
        "Sector Pipeline"
    )


    st.bar_chart(
        insights["sector_analysis"]
    )



    st.write(
        "Owner Performance"
    )


    st.bar_chart(
        insights["owner_analysis"]
    )




    # -----------------------------
    # AI Assistant
    # -----------------------------


    st.divider()


    st.header(
        "🤖 Ask your Business Assistant"
    )


    st.write(
        "Ask questions about your sales pipeline."
    )



    st.info(
        """
Example questions:

• What is our biggest opportunity?

• Which deals are risky?

• Which owner has the highest pipeline?

• Which sector should we focus on?

• Give me founder actions for this week.
        """
    )



    question = st.text_input(
        "Ask a business question..."
    )



    if question:


        with st.spinner(
            "AI Assistant is analyzing..."
        ):


            response = answer_question(

                question,

                processed_deals,

                insights

            )


        st.success(
            "Founder Intelligence"
        )


        st.write(
            response
        )



except Exception as e:


    st.error(
        f"Error: {e}"
    )
