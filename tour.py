import streamlit as st

# Set page configuration to dark mode
st.set_page_config(layout="wide", page_title="Mysore Tourism", page_icon=":cityscape:")

# Custom CSS for title and introduction
st.markdown(
    """
    <style>
    .title {
        font-family: 'Pacifico', cursive;
        font-size: 48px;
        color: #FFFFFF;
    }
    .intro {
        font-family: 'Roboto', sans-serif;
        font-size: 20px;
        color: #CCCCCC;
    }
    .image-container {
        padding: 10px;
        border-radius: 10px;
        border: 2px solid #FFFFFF;
        margin-bottom: 20px;
    }
    .image-caption {
        font-size: 14px;
        color: #FFFFFF;
        text-align: center;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Introduction
st.markdown("<h1 class='title'>Mysore Tourism</h1>", unsafe_allow_html=True)
st.markdown("<p class='intro'>Welcome to the Mysore Tourism app! Explore the beauty of Mysore through this gallery.</p>", unsafe_allow_html=True)

# Image Gallery
st.write("## Image Gallery")

# Mysore Attractions Images
images = [
    ("Mysore Palace", "https://cdn.pixabay.com/photo/2015/12/02/14/54/mysore-palace-1079933_960_720.jpg"),
    ("Chamundi Hills", "https://cdn.pixabay.com/photo/2016/01/08/05/09/chamundi-hills-1129608_960_720.jpg"),
    ("Brindavan Gardens", "https://cdn.pixabay.com/photo/2014/12/15/13/08/brindavan-gardens-569296_960_720.jpg"),
    ("St. Philomena Church", "https://cdn.pixabay.com/photo/2017/11/16/21/35/st-philomena-church-2951443_960_720.jpg"),
    ("Mysore Zoo", "https://cdn.pixabay.com/photo/2017/05/10/07/43/mysore-2308128_960_720.jpg"),
    ("Sri Chamarajendra Park", "https://cdn.pixabay.com/photo/2015/12/02/14/52/sri-chamarajendra-park-1079931_960_720.jpg"),
    ("Jaganmohan Palace", "https://cdn.pixabay.com/photo/2015/08/10/01/24/jaganmohan-palace-882128_960_720.jpg"),
    ("Rail Museum", "https://cdn.pixabay.com/photo/2018/01/19/18/17/indian-railway-museum-3094770_960_720.jpg"),
    ("Karanji Lake", "https://cdn.pixabay.com/photo/2014/12/09/22/25/karanji-lake-562314_960_720.jpg"),
    ("KRS Dam", "https://cdn.pixabay.com/photo/2017/12/04/16/43/krishna-raja-sagara-2992020_960_720.jpg"),
    ("Jayalakshmi Vilas Mansion", "https://cdn.pixabay.com/photo/2016/09/29/11/38/india-1700112_960_720.jpg"),
    ("Mysore Urban Development Authority (MUDA)", "https://cdn.pixabay.com/photo/2015/03/17/14/05/river-677442_960_720.jpg"),
    ("St. Thomas Church", "https://cdn.pixabay.com/photo/2017/12/11/14/07/st-thomas-church-3013465_960_720.jpg"),
    ("Mysore Race Course", "https://cdn.pixabay.com/photo/2014/11/06/15/09/mysore-race-course-520219_960_720.jpg")
]

# Display Images
col_width = 200
col_count = 5
num_images = len(images)
num_cols = min(col_count, num_images)
col_spacing = 10
col_style = f"width: calc((100% - {col_spacing}px * {col_count - 1}) / {col_count});"

for i in range(0, num_images, num_cols):
    cols = st.beta_columns(num_cols)
    for j, (caption, url) in enumerate(images[i:i+num_cols]):
        with cols[j]:
            st.image(url, caption=caption, use_column_width=True)
            st.markdown(f"<p class='image-caption'>{caption}</p>", unsafe_allow_html=True)
            st.markdown("<style>.stImg {padding: 0 !important;}</style>", unsafe_allow_html=True)

# Footer
st.write("Developed by Chaithanya")

