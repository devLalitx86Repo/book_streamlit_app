# Custom CSS for streamlit
app_style = """
<style>
    .card {
        background-color: #D7E4FA;
        border-radius: 5px;
        padding: 8px;
        padding-left: 20px;
        margin: 5px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .card h2 {
        font-size: 1.5em;
        font-weight: semibold;
    }
    .card p {
        font-size: 2em;
        font-weight: bold;
    }

</style>
"""

def apply_style(st):
    st.markdown(app_style, unsafe_allow_html=True)
    return None