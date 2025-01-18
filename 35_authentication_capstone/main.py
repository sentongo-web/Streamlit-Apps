import yaml
import streamlit as st
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

import pandas as pd
import numpy as np
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans, AgglomerativeClustering

# hashed_passwords = stauth.Hasher(['marketing', 'datascience']).generate()
# st.write(hashed_passwords)

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
)

name, authentication_status, username = authenticator.login('Login', 'sidebar')


@st.cache_data
def read_data():
    df = pd.read_csv('data/segmentation data.csv')
    return df


df = read_data()
X = df[['Sex', 'Marital status', 'Age', 'Education',
        'Income', 'Occupation', 'Settlement size']]


@st.cache_data(show_spinner="Running experiment")
def run_experiment(X):

    k_silhouettes = []
    agglo_silhouettes = []

    for i in range(2, 11):
        kmeans = KMeans(n_clusters=i)
        agglo = AgglomerativeClustering(n_clusters=i)

        kmeans.fit(X)
        agglo.fit(X)

        k_silhouettes.append(silhouette_score(X, kmeans.labels_))
        agglo_silhouettes.append(silhouette_score(X, agglo.labels_))

    metrics_df = pd.DataFrame({
        "n_clusters": np.arange(2, 11),
        "KMeans": k_silhouettes,
        "Agglo": agglo_silhouettes
    })

    return metrics_df


@st.cache_data
def display_group_metrics(df, num_clusters):
    for i in range(num_clusters):
        f_df = df[df['labels'] == i]

        male_percentage = round(len(f_df[f_df['Sex'] == 0])/len(f_df), 2)*100
        female_percentage = 100 - male_percentage

        marital_percentage = round(
            len(f_df[f_df['Marital status'] == 0])/len(f_df), 2)*100

        mean_age = round(f_df['Age'].mean(), 0)
        min_age = f_df['Age'].min()
        max_age = f_df['Age'].max()

        high_school = round(len(f_df[f_df['Education'] == 1])/len(f_df), 2)*100
        university = round(
            len(f_df[(f_df["Education"] == 2) | (f_df["Education"] == 3)])/len(f_df), 2)*100

        mean_income = round(f_df['Income'].mean(), 0)
        max_income = f_df['Income'].max()
        min_income = f_df['Income'].min()

        employment_num = f_df['Occupation'].mode().values

        if employment_num == 0:
            employment = 'Unemployed'
        elif employment_num == 1:
            employment = 'Skilled employee'
        else:
            employment = 'Highly skilled employee'

        city_num = f_df['Settlement size'].mode().values

        if city_num == 0:
            city = 'Small city'
        elif city_num == 1:
            city = "Mid-sized city"
        else:
            city = "Large city"

        with st.container():
            st.header(f"Group {i+1}")

            st.subheader("Demographics")
            st.write(f"Percentage of men: {male_percentage}%")
            st.write(f"Percentage of female: {female_percentage}%")

            st.subheader("Marital status")
            st.write(f"Percentage of married clients: {marital_percentage}%")

            st.subheader("Age")
            st.write(f"Mean age: {mean_age}")
            st.write(f"Max age: {max_age}")
            st.write(f"Min age: {min_age}")

            st.subheader("Education")
            st.write(f"High school: {high_school}%")
            st.write(f"University: {university}%")

            st.subheader("Income")
            st.write(f"Mean income: {mean_income}$")
            st.write(f"Max income: {max_income}$")
            st.write(f"Min income: {min_income}$")

            st.subheader("Employment")
            st.write(f"The majority is: {employment}")

            st.subheader("City size")
            st.write(f"The majority is: {city}")


def display_ds_content():
    st.write(df)
    exp_btn = st.button("Run experiment")

    if exp_btn:
        metrics_df = run_experiment(X)
        st.write("Silhouette scores")
        st.write(metrics_df)


def display_marketing_content():
    st.write(df)

    num_clusters = st.slider("Number of groups", 2, 10)

    run_clustering = st.button("Generate groups")

    if run_clustering:
        c_df = df.copy()

        kmeans = KMeans(n_clusters=num_clusters)
        kmeans.fit(X)

        c_df['labels'] = kmeans.predict(X)

        c_df = c_df.sort_values(by=['labels'], ascending=True)

        display_group_metrics(c_df, num_clusters)


if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'sidebar', key='unique_key')

    if username == 'marketing':
        st.write(f'Welcome *{st.session_state["name"]}*')
        st.title('Marketing content')
        display_marketing_content()

    elif username == "datascience":
        st.write(f'Welcome *{st.session_state["name"]}*')
        st.title("Data science content")
        display_ds_content()

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
