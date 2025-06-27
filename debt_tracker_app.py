
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("📊 Debt Tracker Dashboard")

# Sample debt data
debt_data = {
    "Creditor": ["Apple Card", "Best Buy", "Credit One", "Capital One Savor", "Capital One Quicksilver", "Kohl's", "Target", "Carter's", "Affirm (Total)"],
    "Balance ($)": [2543.51, 2000, 500, 300, 300, 300, 300, 180, 3640],
    "Interest Rate (%)": [24.99, 25.00, 28.74, 29.74, 28.99, 30.24, 29.99, 28.00, 15.00],
    "Min Payment ($)": [87, 150, 80, 115, 115, 72, 40, 30, 300],
    "Status": ["❌"] * 9
}

df = pd.DataFrame(debt_data)

# Display table
st.subheader("💳 Debt Overview")
edited_df = st.data_editor(df, num_rows="dynamic", key="debt_table")

# Bar chart: Balances
st.subheader("📉 Balances by Creditor")
fig, ax = plt.subplots()
ax.bar(edited_df["Creditor"], edited_df["Balance ($)"])
plt.xticks(rotation=45, ha='right')
plt.ylabel("Amount ($)")
plt.tight_layout()
st.pyplot(fig)

# Summary stats
total_debt = edited_df["Balance ($)"].sum()
monthly_min = edited_df["Min Payment ($)"].sum()

st.markdown(f"### 🧮 Total Debt: ${total_debt:,.2f}")
st.markdown(f"### 💸 Total Minimum Monthly Payments: ${monthly_min:,.2f}")

# Completion Tracker
st.subheader("✅ Progress Tracker")
st.progress((edited_df["Status"].tolist().count("✅") / len(edited_df)))
