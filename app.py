from contents.functions import *

st.title('Movies Recommender')


# --------------- recommendation by item similarity -----------------------
movie_name = st.selectbox(
    'Filtering by movie similarity',
    movies_list
) 

names, posters = recommender_by_item(movie_name)
plot_columns(names, posters)

# ------------------ sidebar section -----------------------
st.sidebar.title(movie_name)
with st.sidebar:
    plot_summary_image(movie_name)

