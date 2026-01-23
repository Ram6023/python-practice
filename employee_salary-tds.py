import streamlit as st

st.title("TDS Calculator")

# Input field
salary = st.number_input("Enter your Salary (in INR)", min_value=0.0, step=1000.0)

if st.button("Calculate TDS"): 
    total = 0
    sal = 0
    original_salary = salary

    if salary >= 500000:
        salary = salary - 300000

        if salary / 300000 >= 1:
            salary = salary - 300000
            tds = 300000 * 0.05
            total = total + tds
        else:
            sal = salary % 300000
            tds = sal * 0.05
            total = total + tds

        if salary / 300000 >= 1:
            salary = salary - 300000
            tds = 300000 * 0.1
            total = total + tds
        else:
            sal = salary % 300000
            tds = sal * 0.1
            total = total + tds

        if salary / 600000 >= 1:
            salary = salary - 600000
            tds = 600000 * 0.15
            total = total + tds
        else:
            sal = salary % 600000
            tds = sal * 0.15
            total = total + tds

        if salary > 0:
            tds = salary * 0.3
            total = total + tds

        st.success(f"Your total tax (TDS) is: ₹{total:,.2f}")
    else:
        st.info("No tax applicable for salary below ₹5,00,000")
