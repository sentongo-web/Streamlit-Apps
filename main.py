import streamlit as st
import pandas as pd
df = pd.read_csv("patient_data.csv")
st.dataframe(df)

# line charts
st.line_chart(df, x="AdmissionYear", y= ["VisitCount", "Age"])

###area charts
st.area_chart(df, x="AdmissionYear", y= ["VisitCount", "Age"])

###bar charts
st.bar_chart(df, x="AdmissionYear", y= ["VisitCount", "Age"])

##streamlit map
# Load the dataset
map_data = pd.read_csv("map_data.csv")
st.map(map_data)
# Display the map

# st.table(df)

# st.text("Hello streamlit- We are learning streamlit")
# st.header("This is a header")
# st.subheader("This is a subheader")
# st.markdown("This is a markdown")
# st.markdown("#This is a markdown1")
# st.markdown("##This is a markdown2")
# st.markdown("###This is a markdown3")
# st.caption("This is a caption")
# st.code("import pandas")