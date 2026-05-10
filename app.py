import streamlit as st

# Title
st.title("Mechanical Unit Converter and Material Density Checker")

# Your Information
st.write("Name: Umair Habib Usmani")
st.write("Roll Number: 25-ME-211")

# -----------------------------
# UNIT CONVERTER
# -----------------------------

st.header("Mechanical Unit Converter")

conversion_type = st.selectbox(
    "Choose Conversion Type",
    ["Length", "Weight", "Temperature"]
)

# Length Conversion
if conversion_type == "Length":
    meters = st.number_input("Enter value in meters")

    centimeters = meters * 100
    millimeters = meters * 1000

    st.write("Centimeters:", centimeters)
    st.write("Millimeters:", millimeters)

# Weight Conversion
elif conversion_type == "Weight":
    kg = st.number_input("Enter value in kilograms")

    grams = kg * 1000

    st.write("Grams:", grams)

# Temperature Conversion
elif conversion_type == "Temperature":
    celsius = st.number_input("Enter temperature in Celsius")

    fahrenheit = (celsius * 9/5) + 32

    st.write("Fahrenheit:", fahrenheit)

# -----------------------------
# MATERIAL DENSITY CHECKER
# -----------------------------

st.header("Material Density Checker")

materials = {
    "Steel": "7850 kg/m³",
    "Aluminum": "2700 kg/m³",
    "Copper": "8960 kg/m³",
    "Brass": "8500 kg/m³"
}

selected_material = st.selectbox(
    "Select Material",
    list(materials.keys())
)

st.write(
    "Density:",
    materials[selected_material]
)