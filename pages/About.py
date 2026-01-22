import streamlit as st

# -------------------------------
# Check if user is logged in
# -------------------------------
if not st.session_state.get("authentication_status"):
    st.warning("⚠️ Please login to access this page.")
    st.stop()  # stop rendering the page

# Optional: role-based restriction
# If you want only admin and faculty to see About page, you can use:
# allowed_roles = ["admin", "faculty"]
# if st.session_state.get("role") not in allowed_roles:
#     st.error("❌ You do not have access to this page.")
#     st.stop()

# -------------------------------
# About Page Content
# -------------------------------
st.title("About This App")

st.markdown("""
This is a **Streamlit Multi-Page Application** with role-based authentication.

**Features of this app:**
- Login and logout functionality using `streamlit-authenticator`.
- Role-based access control for different pages.
- Separate dashboards for Admin and Faculty users.
- Session management with cookies to remember logged-in users.
- Multi-page structure using Streamlit's `pages` folder.

**Purpose:**
This application is designed to demonstrate how to secure pages for different users, display metrics, and provide dashboards tailored to roles.

""")

st.subheader("Developer Info")
st.markdown("""
- **Developer:** Harjeet Singh  
- **Email:** harjeet.singh@chitkara.edu.in  
- **Organization:** Chitkara University  
""")

st.subheader("Technologies Used")
st.markdown("""
- Python 3.11  
- Streamlit  
- Streamlit-Authenticator  
- YAML for configuration  
""")
