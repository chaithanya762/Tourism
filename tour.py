import streamlit as st
# Set page configuration to dark mode
st.set_page_config(layout="wide", page_title="Mysore Tourism", page_icon=":cityscape:")

# Custom CSS for full-width container with background image
st.markdown(
    """
    <style>
    .full-width-container {
        width: 100%;
        padding: 20px;
        background-image: url('https://images.app.goo.gl/g5g5KZLPJ8Sn66qi7');
        background-size: cover;
        background-repeat: no-repeat;
        color: black; /* Text color on top of the background */
    }
    .title {
        font-family: 'Pacifico', cursive;
        font-size: 48px;
        text-align: center;
        margin-bottom: 20px;
    }
    .intro {
        font-family: 'Roboto', sans-serif;
        font-size: 20px;
        text-align: center;
        margin-bottom: 20px;
    }
    .image-caption {
        font-size: 16px;
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


# Mysore Attractions Images
images = [
    ("Mysore Palace", "https://i0.wp.com/mysuruinfrahub.com/wp-content/uploads/2023/08/mysorepalace3.jpg?fit=1200%2C675&ssl=1"),
    ("Chamundi Hills", "https://as1.ftcdn.net/v2/jpg/04/86/71/30/1000_F_486713081_QkksWuOosnIB3Q9L9hh6jPTeEPy6jf5s.jpg"),
    ("Brindavan Gardens", "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1d/1b/b7/ee/view-from-brindavan-gardens.jpg?w=1100&h=-1&s=1"),
    ("St. Philomena Church", "https://www.holidify.com/images/cmsuploads/compressed/St.-Philominas_20180124221145.jpg"),
    ("Mysore Zoo", "https://mysuruzoo.info/images/twotiger.png"),
    ("Sri Chamarajendra Park", "https://nidhi.tourism.gov.in/api/FileUpload?FilePath=null/attraction_details/gallery/638429238225389031.jpg"),
    ("Jaganmohan Palace", "https://mysuruonline.in/wp-content/uploads/2019/02/Jaganmohan-Palace.jpg"),
    ("Rail Museum", "https://images.borrbo.com/outings/Railway%20Museum%20Mysore/Railway-museum-mysore.jpg"),
    ("Karanji Lake", "https://images.borrbo.com/outings/Karanji%20Lake/Karanji-Lake-Boating.jpg"),
    ("KRS Dam", "https://tripthentic.com/wp-content/uploads/mysore-krs-dam.jpg"),
    ("Jayalakshmi Vilas Mansion", "https://www.bestbus.in/assets/images/tourist-attractions/jayalakshmi-vilas-in-mysore.jpg"),
    ("Mysore Urban Development Authority (MUDA)", "https://www.mudamysore.gov.in/Mysore%20MUDA.jpg"),
    ("Nanjangud", "https://www.nativeplanet.com/img/2023/04/srikanteshwarananjanguditemple1-1681728701.jpg"),
    ("Mysore Race Course", "https://pbs.twimg.com/media/FNt4RvKaIAE7gJn?format=jpg&name=large")
]

# Display Images
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
st.markdown("---")
st.write("Developed by Chaithanya")
st.write("Student, Dept of CSE , VVCE , MYSORE")
