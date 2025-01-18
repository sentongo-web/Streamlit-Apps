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
#######WIDGETS######
### Buttons
primary_btn = st.button(label="Primary", type="primary")
secondary_btn = st.button(label="Secondary", type="secondary")

if primary_btn:
    st.write("Hello from primary")

if secondary_btn:
    st.write("Hello from secondary")

# Checkbox
st.divider()

checkbox = st.checkbox("Remember me")

if checkbox:
    st.write("I will remember you")
else:
    st.write("I will forget you")

# # Radio buttons
# st.divider()

####MULTISELECT VALUES
# Buttons
# primary_btn = st.button(label="Primary", type="primary")
# secondary_btn = st.button(label="Secondary", type="secondary")

# if primary_btn:
#     st.write("Hello from primary")

# if secondary_btn:
#     st.write("Hello from secondary")

# # Checkbox
# st.divider()

# checkbox = st.checkbox("Remember me")

# if checkbox:
#     st.write("I will remember you")
# else:
#     st.write("I will forget you")

# # Radio buttons
# st.divider()

# df = pd.read_csv("data/sample.csv")

# radio = st.radio("Choose a column", options=df.columns[1:], index=1, horizontal=True)
# st.write(radio)

# # Selectbox
# st.divider()

# select = st.selectbox("Choose a column", options=df.columns[1:], index=0)
# st.write(select)

# # Mutliselect
# st.divider()

# multiselect = st.multiselect("Choose as many columns as you want", options=df.columns[1:], default=["col2"], max_selections=2)
# st.write(multiselect)

# # Slider
# st.divider()

# slider = st.slider("Pick a number", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
# st.write(slider)

# # Text input
# st.divider()

# text_input = st.text_input("What's your name?", placeholder="John Doe")
# st.write(f"Your name is {text_input}")

# # Number input
# st.divider()

# num_input = st.number_input("Pick a number", min_value=0, max_value=10, value=0, step=1)
# st.write(f"You picked {num_input}")

# # Text area
# st.divider()

# txt_area = st.text_area("What do you want to tell me?", height=500, placeholder="Write your message here")
# st.write(txt_area)

# df = pd.read_csv("data/sample.csv")

# radio = st.radio("Choose a column", options=df.columns[1:], index=1, horizontal=True)
# st.write(radio)

# # Selectbox
# st.divider()

# select = st.selectbox("Choose a column", options=df.columns[1:], index=0)
# st.write(select)

# # Mutliselect
# st.divider()


# # Slider
# st.divider()


# # Text input
# st.divider()


# # Number input
# st.divider()


# # Text area
# st.divider()
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