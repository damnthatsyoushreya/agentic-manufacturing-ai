import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import compute_metrics

st.set_page_config(page_title='Manufacturing Report Generator', layout='wide')
st.title('🧠 AI-Powered Manufacturing Report Generator')

uploaded_file = st.file_uploader('📂 Upload a Manufacturing CSV File', type='csv')

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader('📄 Raw Data Sample')
    st.dataframe(df.head())

    summary = compute_metrics(df)
    st.subheader('📊 Monthly Metrics Summary')
    st.dataframe(summary)

    st.subheader('📈 Units Produced Over Time')
    fig, ax = plt.subplots()
    summary.plot(x='Month', y='Units_Produced', kind='bar', ax=ax, legend=False)
    ax.set_ylabel('Units Produced')
    ax.set_xlabel('Month')
    st.pyplot(fig)
