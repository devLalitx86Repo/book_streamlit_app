def show_filter_visual(st,df):
    
    # Filters for the dataframe
    st.sidebar.header("✎ Filter data")

    # Filter by price
    st.sidebar.subheader("Filter by price")
    #price slider
    price_min = int(df['PRICE'].min())
    price_max = int(df['PRICE'].max())
    price_avg = int(df['PRICE'].mean())
    price_slider = st.sidebar.slider("Price range", price_min, price_max, (price_min, price_max))
    st.sidebar.write("Average price: €", price_avg)

    # Filter by rating
    st.sidebar.subheader("Filter by rating")
    #rating slider
    rating_min = int(df['RATING'].min())
    rating_max = int(df['RATING'].max())
    rating_avg = int(df['RATING'].mean())
    rating_slider = st.sidebar.slider("Rating range", rating_min, rating_max, (rating_min, rating_max))
    st.sidebar.write("Average rating: ", rating_avg, "★")

    
    # Filter df
    df =  df[(df['PRICE'] >= price_slider[0]) & (df['PRICE'] <= price_slider[1]) ]
    df =  df[(df['RATING'] >= rating_slider[0]) & (df['RATING'] <= rating_slider[1]) ]
    return df


