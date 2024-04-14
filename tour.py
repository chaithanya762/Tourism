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
        color: black;
    }
    .intro {
        font-family: 'Roboto', sans-serif;
        font-size: 20px;
        color: black;
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
    ("Mysore Palace", "https://images.app.goo.gl/geGQirfLz9gFqrhU9"),
    ("Chamundi Hills", "https://images.app.goo.gl/iiunDd2qEwWTgLmb6"),
    ("Brindavan Gardens", "https://images.app.goo.gl/Umi9X4EQ1fVEV7RCA"),
    ("St. Philomena Church", "https://images.app.goo.gl/cG5WbsEcREn26T4e9"),
    ("Mysore Zoo", "https://images.app.goo.gl/CyMrWiuczm2UTMms9"),
    ("Sri Chamarajendra Park", "https://images.app.goo.gl/FQrZx4d3ZNfuQcDK6"),
    ("Jaganmohan Palace", "https://images.app.goo.gl/Uzu8DVuUGgCqm4BA8"),
    ("Rail Museum", "https://images.app.goo.gl/esXMyEaer6d4AwWcA"),
    ("Karanji Lake", "https://images.app.goo.gl/76Cpm4VepedThfPi7"),
    ("KRS Dam", "https://images.app.goo.gl/HToQ9UqTPbZdFAaEA"),
    ("Jayalakshmi Vilas Mansion", "https://images.app.goo.gl/DLtj1dbu1jQTCPo69"),
    ("Mysore Urban Development Authority (MUDA)", "https://images.app.goo.gl/LcfQVb6j6XmKzgFRA"),
    ("Nanjangud", "https://images.app.goo.gl/ZdwQdnwJPQNv5dMMA"),
    ("Mysore Race Course", "https://images.app.goo.gl/TYMJWKvs9Stuw5T76")
]

# Display Images
col_width = 200
col_count = 5
num_images = len(images)
num_cols = min(col_count, num_images)
col_spacing = 10
col_style = f"width: calc((100% - {col_spacing}px * {col_count - 1}) / {col_count});"

for i in range(0, num_images, num_cols):
    cols = st.columns(num_cols)
    for j, (caption, url) in enumerate(images[i:i+num_cols]):
        with cols[j]:
            st.image(url, caption=caption, use_column_width=True)
            st.markdown(f"<p class='image-caption'>{caption}</p>", unsafe_allow_html=True)
            st.markdown("<style>.stImg {padding: 0 !important;}</style>", unsafe_allow_html=True)

# Footer
st.write("Developed by Chaithanya")


