import streamlit as st

if 'balance' not in st.session_state:
    st.session_state.balance = 0
if 'history' not in st.session_state:
    st.session_state.history = []

st.set_page_config(page_title="My Naira Tracker")
st.title("₦ My Naira Tracker")
st.header(f"Current Balance: ₦{st.session_state.balance:,}")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Add Income")
    income_amount = st.number_input("Income Amount", min_value=0, step=1000, key="income")
    income_cat = st.text_input("Category", "Salary", key="inc_cat")
    if st.button("➕ Add Income"):
        st.session_state.balance += income_amount
        st.session_state.history.append(f"+ ₦{income_amount:,} - {income_cat}")
        st.success(f"Added ₦{income_amount:,}!")
        st.rerun()

with col2:
    st.subheader("Add Expense")
    expense_amount = st.number_input("Expense Amount", min_value=0, step=1000, key="expense")
    expense_cat = st.text_input("Category", "Food", key="exp_cat")
    if st.button("➖ Add Expense"):
        st.session_state.balance -= expense_amount
        st.session_state.history.append(f"- ₦{expense_amount:,} - {expense_cat}")
        st.error(f"Spent ₦{expense_amount:,}!")
        st.rerun()

st.subheader("📒 Last 10 Transactions")
for item in st.session_state.history[-10:]:
    st.write(item)