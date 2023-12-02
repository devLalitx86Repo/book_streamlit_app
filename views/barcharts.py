import altair as alt
import matplotlib.pyplot as plt


def plot_availability_pie_chart(df, colors=None, size=(8, 8)):
    availability_counts = df['AVAILABILITY'].value_counts()
    labels = ['Available', 'Not Available']
    values = [availability_counts.get(True, 0), availability_counts.get(False, 0)]

    fig, ax = plt.subplots(figsize=size)
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    return fig

def bar_avgPrice_per_rating(st,df):
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Average price💶 per rating 🌟")
        #altair bar chart
        chart = alt.Chart(df).mark_bar(size=32).encode(
            x='RATING',
            y='mean(PRICE)'
        ).properties(
            width=600,
            height=400
        )
        st.altair_chart(chart, use_container_width=True)

    #divider between the charts col
        
    with col2:
        
        # availability pie chart
        st.subheader("Availability 📚")
        # Allow user to configure colors and size
        selected_color = st.color_picker("Select Pie Color", value="#0068C9")
        colors = [selected_color, "#0068C9"]
        
        fig = plot_availability_pie_chart(df, colors=colors, size=(15, 6))
        st.pyplot(fig)

    return None
        