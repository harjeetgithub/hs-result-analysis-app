import streamlit as st
import streamlit_authenticator as stauth
import yaml

# Load config
with open("config.yaml") as file:
    config = yaml.safe_load(file)

authenticator = stauth.Authenticate(
    credentials=config["credentials"],
    cookie_name=config["cookie"]["name"],
    cookie_key=config["cookie"]["key"],
    cookie_expiry_days=config["cookie"]["expiry_days"],
)

# Render login widget
authenticator.login(location="main", key="login_form")

# Check auth status from session state
if st.session_state.get("authentication_status"):
    st.success(f"Welcome {st.session_state.get('name')} 👋")
    
    # Get the username and role
    username = st.session_state.get("username")
    # credentials = stauth.Credentials(config["credentials"])
    # role = credentials.users[username].get("role", "faculty")  # default role if missing

    user_info = config["credentials"]["usernames"].get(username, {})
    st.session_state["role"] = user_info.get("role", "faculty")


    #st.session_state["role"] = role  # save role in session state
    # -------------------------------
    # Sidebar: Display role and logout
    # -------------------------------
    with st.sidebar:
        st.write("## User Info")
        st.write(f"**Name:** {st.session_state.get('name')}")
        #st.write(f"**Username:** {st.session_state.get('username')}")
        #st.write(f"**Role:** {st.session_state.get('role')}")
        authenticator.logout(location="sidebar", key="logout_btn")
    #authenticator.logout(location="sidebar", key="logout_btn")

    # Dashboard content
    st.write("Welcome to the dashboard")
 
elif st.session_state.get("authentication_status") is False:
    st.error("Invalid username or password 😬")

elif st.session_state.get("authentication_status") is None:
    st.info("Please enter your credentials")
