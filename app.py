import streamlit as st
import pandas as pd
import networkx as nx

# -------------------------
# Load data
# -------------------------
df = pd.read_csv("services.csv")

# -------------------------
# Build Knowledge Graph
# -------------------------
G = nx.DiGraph()

for index, row in df.iterrows():
    service = row["Service"]
    price = f"₹{row['Price']}"
    city = row["City"]

    G.add_edge(service, price, relation="HAS_PRICE")
    G.add_edge(service, city, relation="AVAILABLE_IN")
    G.add_edge(city, service, relation="HAS_SERVICE")

# -------------------------
# Chatbot Logic
# -------------------------
def chatbot_response(question):
    question = question.lower()

    # PRICE query
    if "price" in question or "cost" in question:
        for u, v, d in G.edges(data=True):
            if d["relation"] == "HAS_PRICE":
                if u.lower() in question:
                    return f"The price of {u} is {v}"

    # LOCATION query
    elif "where" in question or "available" in question:
        for u, v, d in G.edges(data=True):
            if d["relation"] == "AVAILABLE_IN":
                if u.lower() in question:
                    return f"{u} is available in {v}"

    # SERVICES IN CITY
    elif "services" in question or "what" in question:
        for u, v, d in G.edges(data=True):
            if d["relation"] == "HAS_SERVICE":
                if u.lower() in question:
                    return f"Services available in {u}: {v}"

    return "Sorry, I couldn't understand. Please ask about services, price, or location."


# -------------------------
# Streamlit UI
# -------------------------
st.title("🧠 Knowledge Graph Chatbot")

user_input = st.text_input("Ask your question:")

if user_input:
    response = chatbot_response(user_input)
    st.write("🤖:", response)