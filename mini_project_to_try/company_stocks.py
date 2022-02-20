import streamlit as st
import yfinance as finance

def get_ticker(name):
    company = finance.Ticker(name) #google
    return company

st.title("Build and Deploy Stock Market App Using Streamlit")
st.header("A Basic Data Science Web Application")

st.sidebar.header("Geeksforgeeks \n TrueGeeks")

company1 = get_ticker("GOOGL")
company2 = get_ticker("MSFT")

google = finance.download("GOOGL", start="2021-10-01", end="2021-10-01")
microsoft = finance.download("MSFT", start="2021-10-01", end="2021-10-01")

data1 = company1.history(period="3mo")
data2 = company2.history(period="3mo")

company2.history()
st.write(company1.info)
st.write("""
### Google
""")
st.write(company1.info['longBusinessSummary'])
st.write(google)
st.line_chart(data1.values)

st.write("""
### Microsoft
""")
st.write(company2.info['longBusinessSummary'],"\n",microsoft)
st.line_chart(data2.values)