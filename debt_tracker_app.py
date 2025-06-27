import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📉 Debt Payoff Tracker with Sliders")

# 👉 User inputs
starting_debt = st.number_input("Starting Debt ($)", min_value=0, value=2500, step=100)
monthly_payment = st.slider("Monthly Payment ($)", min_value=10, max_value=1000, value=150, step=10)
interest_rate = st.slider("Interest Rate (%)", min_value=0.0, max_value=30.0, value=20.0, step=0.1)
months = st.slider("Months to Project", min_value=1, max_value=60, value=24)

# 🔍 Simulate payoff
balance = starting_debt
monthly_data = []

for month in range(1, months + 1):
    interest = balance * (interest_rate / 100) / 12
    principal = monthly_payment - interest
    balance -= principal
    balance = max(balance, 0)
    monthly_data.append({"Month": month, "Balance": round(balance, 2)})
    if balance <= 0:
        break

df = pd.DataFrame(monthly_data)

# 📊 Bar chart
st.subheader("📊 Debt Balance Over Time")
fig, ax = plt.subplots()
ax.bar(df["Month"], df["Balance"])
ax.set_xlabel("Month")
ax.set_ylabel("Remaining Balance ($)")
ax.set_title("Debt Payoff Progress")
st.pyplot(fig)
