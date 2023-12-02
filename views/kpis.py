import streamlit as st
import numpy as np
import altair as alt

# Define your CSS style for the cards




def kpi_visual(df):
    placeholder = st.empty()

    #calculate the KPIs
    # KPI 1: Total number of books in a card format
    total_books = len(df)
    average_rating  = str(np.mean(df['RATING']).round(2))+" ★"
    average_book_price = "€ "+str(np.mean(df['PRICE']).round(2))

    with placeholder.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("<div class='card'><h2>Total number of books</h2><p>{}</p></div>".format(total_books), unsafe_allow_html=True)

        with col2:
            st.markdown("<div class='card'><h2>Average rating</h2><p>{}</p></div>".format(average_rating), unsafe_allow_html=True)

        with col3:
            st.markdown("<div class='card'><h2>Average book price</h2><p>{}</p></div>".format(average_book_price), unsafe_allow_html=True)

    return None

def show_top_10_books(st,df):

    placeholder = st.empty()
    with placeholder.container():
        
        col1, col2 = st.columns(2)

        with col1:
            # Give a drop down to select rating or price
            st.subheader("Top 10 books")
            selected_metric = st.selectbox("Select metric", ["RATING", "PRICE"])

            # Sort the dataframe by the selected metric
            df = df.sort_values(by=selected_metric, ascending=False)
            # Show the top 10 books title and rating and price
            st.table(df[['TITLE', 'RATING', 'PRICE']].head(10))

        with col2:
            # Plot histogram based on the metric selected
            st.subheader("Histogram")
            # Mtric at x axis
            chart = alt.Chart(df).mark_bar(size=32).encode(
                x=selected_metric,
                y='count()'
            ).properties(
                width=600,
                height=400
            )
            st.altair_chart(chart, use_container_width=True)

    return None


            

