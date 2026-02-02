import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="Researcher Profile and STEM Data Explorer", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "Publications", "STEM Data Explorer", "Contact"],
)

# Dummy STEM data

Physicochemical_Parameters_data = pd.DataFrame({
    "River": ["Black", "Juskei", "Vaal", "Umgeni", "Olifants", "GaSelati", "Modder"],
    "Temperature (°C)": [19, 23, 20, 28, 29, 22, 24],
    "pH": [6.5, 7.1, 5.5, 8.0, 5.0, 6.0, 7.4],
    "EC (uS/cm)": [403, 530, 135, 215, 305, 640, 721],
     "As (ug/L)": [0.5, 2.2, 1.7, 3.4, 2.2, 5.8, 10.4],
    "Recorded Date": pd.date_range(start="2024-01-01", periods=7),
})

# Sections based on menu selection
if menu == "Researcher Profile":
    st.title("Researcher Profile")
    st.sidebar.header("Profile Options")

    # Collect basic information
    name = "Dr. Innocentia Pilane"
    field = "Chemistry"
    institution = "University of Johannesburg"

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")
    
    st.image(
    "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg",
    caption="Nature (Pixabay)"
)

elif menu == "Publications":
    st.title("Publications")
    st.sidebar.header("Upload and Filter")

    # Upload publications file
    uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)

        # Add filtering for year or keyword
        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            filtered = publications[
                publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
            ]
            st.write(f"Filtered Results for '{keyword}':")
            st.dataframe(filtered)
        else:
            st.write("Showing all publications")

        # Publication trends
        if "Year" in publications.columns:
            st.subheader("Publication Trends")
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)
        else:
            st.write("The CSV does not have a 'Year' column to visualize trends.")

elif menu == "STEM Data Explorer":
    st.title("STEM Data Explorer")
    st.sidebar.header("Data Selection")
    
    # Tabbed view for STEM data
    data_option = st.sidebar.selectbox(
        "Choose a dataset to explore", 
        ["Physicochemical Parameters Data"]
    )

    if data_option == "Physicochemical_Parameters_data":
        st.write("### Physicochemical parameters Data")
        st.dataframe(Physicochemical_Parameters_data)
        # Add widgets to filter by temperature, pH, EC and As
        temp_filter = st.slider("Filter by Temperature (°C)", 0, 50.0, (0, 50.0))
        pH_filter = st.slider("Filter by pH", 0, 10, (0, 10))
        EC_filter = st.slider("Filter by EC (uS/cm)", 0, 800, (0, 800))
        As_filter = st.slider("Filter by As (ug/L)", 0, 20, (0, 20))
        filtered_physicochemical_parameters = Physicochemical_Parameters_data[
            Physicochemical_Parameters_data["Temperature (°C)"].between(temp_filter[0], temp_filter[1]),
            Physicochemical_Parameters_data["pH"].between(pH_filter[0], pH_filter[1]),
            Physicochemical_Parameters_data["EC (uS/cm)"].between(pH_filter[0], pH_filter[1])&
            Physicochemical_Parameters_data["As (ug/L)"].between(pH_filter[0], pH_filter[1])
        ]
        st.write(f"Filtered Results for Temperature {temp_filter},pH {pH_filter}, EC {EC_filter} and Humidity {pH_filter}:")
        st.dataframe(filtered_physicochemical_parameters)
        
        

elif menu == "Contact":
    # Add a contact section
    st.header("Contact Information")
    email = "inno.p@uj.com"
    st.write(f"You can reach me at {email}.")