import streamlit as st
from streamlit_folium import st_folium
import folium
import requests
import base64

def add_bg_from_local(image_file: str) -> None:
    """ Add background image to streamlit app.

    Args:
        image_file (str): path to the image file.
    """
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

def title() -> None:
    """ Add title to streamlit page.
    """
    st.title("Streamlit folium demo!")

def coordinates(address: str) -> tuple:
    """ Get coords of a given address.

    Args:
        address (str): A string of the address you want to display.

    Returns:
        tuple: A tuple of lat and lon as floats.
    """
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        'q': address,
        'format': 'json'
    }
    response = requests.get(url, params=params).json()
    return (response[0]['lat'], response[0]['lon'])

def plot_map(lat: float, lon: float) -> None:
    """ Given a latitude and longitude display a folium map on streamlit page.

    Args:
        lat (float): Latitude.
        lon (float): Longitude.
    """
    m = folium.Map(location=[lat, lon], zoom_start=16)
    folium.Marker(
    location=[lat, lon],
    popup="Your coords!",
    icon=folium.Icon(color="red", icon="info-sign"),
    ).add_to(m)
    st_folium(m, width = 725)

def user_input() -> None:
    """ Takes user input of an address.
    """
    address = st.text_input('Where do you want a map of?')
    if address:
        lat, lon = coordinates(address)
        plot_map(lat, lon)

def app() -> None:
    """ Call the components of the streamlit app.
    """
    add_bg_from_local("background.jpg")
    title()
    user_input()

if __name__ == "__main__":
    app()
