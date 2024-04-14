import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit.components.v1 as components
# Page configs
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(layout="wide")
hide_decoration_bar_style = '''<style>header {visibility: hidden;}</style>'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)
# Design hide "made with streamlit" footer menu area
hide_streamlit_footer = """<style>#MainMenu {visibility: hidden;}
                        footer {visibility: hidden;}</style>"""
st.markdown(hide_streamlit_footer, unsafe_allow_html=True)
#title and description page
st.title("Crime monitoring/prediction model 🚨")
#with st.popover("About Us"):
#    st.write("Introducing our cutting-edge Crime Prediction and Monitoring System (CPMS) – a revolutionary machine learning model designed to forecast crime-prone regions and effectively monitor criminal activities. By analyzing historical crime data, socio-economic factors, demographic information, and real-time inputs such as weather and local events, CPMS generates predictive insights to identify areas at high risk of criminal incidents.Utilizing advanced algorithms, CPMS not only predicts potential crime hotspots but also continuously monitors and updates its predictions based on evolving data patterns. Through integration with law enforcement databases and surveillance systems, CPMS provides actionable intelligence to law enforcement agencies, enabling proactive deployment of resources for crime prevention and rapid response.With its proactive approach and real-time monitoring capabilities, CPMS empowers communities to enhance public safety, allocate resources efficiently, and combat crime effectively in today's dynamic urban environments.")
#with st.popover("Github"):
#    st.write("Repo link : ")
#tabs

tab1, tab2, tab3 = st.tabs(["About Us", "Github", "Dataset"])

with tab1:
   st.write("Introducing our cutting-edge Crime Prediction and Monitoring System (CPMS) – a revolutionary machine learning model designed to forecast crime-prone regions and effectively monitor criminal activities. By analyzing historical crime data, socio-economic factors, demographic information, and real-time inputs such as weather and local events, CPMS generates predictive insights to identify areas at high risk of criminal incidents.Utilizing advanced algorithms, CPMS not only predicts potential crime hotspots but also continuously monitors and updates its predictions based on evolving data patterns. Through integration with law enforcement databases and surveillance systems, CPMS provides actionable intelligence to law enforcement agencies, enabling proactive deployment of resources for crime prevention and rapid response.With its proactive approach and real-time monitoring capabilities, CPMS empowers communities to enhance public safety, allocate resources efficiently, and combat crime effectively in today's dynamic urban environments.")


with tab2:
   st.write("Github link")
   st.write("[Github Repository] (https://github.com/Rishav-Raj-Sinha/hack2skill)")


with tab3:
   st.write("Kaggle")
   st.write("[Kaggle link] (https://www.kaggle.com/datasets/luxmikant2254/predictive-crime-analysis/settings)")


st.divider()
# #selection widgets
# districts_karnataka = [
#     "Bangalore Urban",
#     "Bangalore Rural",
#     "Belgaum",
#     "Bellary",
#     "Bidar",
#     "Bijapur (Vijayapura)",
#     "Chamarajanagar",
#     "Chikballapur",
#     "Chikmagalur",
#     "Chitradurga",
#     "Dakshina Kannada",
#     "Davanagere",
#     "Dharwad",
#     "Gadag",
#     "Gulbarga (Kalaburagi)",
#     "Hassan",
#     "Haveri",
#     "Kodagu (Coorg)",
#     "Kolar",
#     "Koppal",
#     "Mandya",
#     "Mysore (Mysuru)",
#     "Raichur",
#     "Ramanagara",
#     "Shimoga (Shivamogga)",
#     "Tumkur (Tumakuru)",
#     "Udupi",
#     "Uttara Kannada (Karwar)",
#     "Yadgir"
# ]
# st.header("Please select your district")
# selected_district = st.selectbox("Karnataka districts :", districts_karnataka)
# # columns
# col1,col2,col3 = st.columns(3)

# with col1:
    
# with col2:

#     st.image("/home/rishav/code/streamlit/hack2skill/assets/5.jpeg")

#     st.image("/home/rishav/code/streamlit/hack2skill/assets/6.jpeg")

# with col3:
#     st.image("/home/rishav/code/streamlit/hack2skill/assets/7.jpeg")

#     st.image("/home/rishav/code/streamlit/hack2skill/assets/8.jpeg")

#     st.image("/home/rishav/code/streamlit/hack2skill/assets/9.jpeg")   

tab11, tab22, tab33, tab44, tab55, tab66 ,tab77 = st.tabs(["Crime Trends Forecast", "Time series plots", "Most common crimes", "Victim segregation", "Crime rate by area", "Time period plots", "Crime prone areas"])

with tab11:
    col1,col2,col3 = st.columns(3)
    with col1:
        st.image("assets/1.jpeg")
        st.image("assets/2.jpeg")
        st.image("assets/3.jpeg")
        st.image("assets/4.jpeg")
        st.image("assets/tr.jpeg")

    with col2:
        st.image("assets/5.jpeg")
        st.image("assets/6.jpeg")
        st.image("assets/trends.jpeg")

    with col3:
        st.image("assets/tr3end.jpeg")
        st.image("assets/trend.jpeg")

with tab22:
    col1,col2 = st.columns(2)
    with col1:
        st.image("assets/8.jpeg")
        st.image("assets/9.jpeg")
        st.image("assets/ts.jpeg")
    with col2:
        st.image("assets/tss.jpeg")
        st.image("assets/tsss.jpeg")

with tab33:
    col1,col2 = st.columns(2)
    with col1:
        st.image("assets/c.jpeg",width=800)
        st.image("assets/c1.jpeg",width=800)
        st.image("assets/c2.jpeg",width=800)
    with col2:
        st.image("assets/r.jpeg",width=800)
        st.image("assets/r1.jpeg",width=800)
    

with tab44:
    col1,col2 = st.columns(2)
    with col1:
        st.image("assets/vicbyprof.jpeg")
        st.image("assets/dist-by-sex.jpeg")
    with col2:
        st.image("assets/firbycaste.jpeg")
        st.image("assets/firbycaste1.jpeg")

with tab55:
    st.image("assets/crimeratebyareaname.jpeg")

with tab66:
    col1,col2 = st.columns(2)
    with col1:
        st.image("assets/dayofweek.jpeg")
    with col2:
        st.image("assets/permperh.jpeg")

with tab77:
    st.image("assets/7.jpeg")
