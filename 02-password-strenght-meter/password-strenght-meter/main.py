import streamlit as st
import re
from typing import Tuple, List

def analyze_password(password: str) -> Tuple[int, List[str]]:
    """
    Analyze password strength and return score and feedback
    Returns: (score (0-100), list of feedback messages)
    """
    score = 0
    feedback = []
    
    # Length check
    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long")
    else:
        score += 20
    
    # Contains number
    if not re.search(r"\d", password):
        feedback.append("Password should contain at least one number")
    else:
        score += 20
    
    # Contains lowercase
    if not re.search(r"[a-z]", password):
        feedback.append("Password should contain at least one lowercase letter")
    else:
        score += 20
    
    # Contains uppercase
    if not re.search(r"[A-Z]", password):
        feedback.append("Password should contain at least one uppercase letter")
    else:
        score += 20
    
    # Contains special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        feedback.append("Password should contain at least one special character")
    else:
        score += 20
    
    return score, feedback

def get_strength_label(score: int) -> str:
    """Convert numerical score to strength label"""
    if score <= 20:
        return "Very Weak"
    elif score <= 40:
        return "Weak"
    elif score <= 60:
        return "Moderate"
    elif score <= 80:
        return "Strong"
    else:
        return "Very Strong"

def get_strength_color(score: int) -> str:
    """Get color based on password strength"""
    if score <= 20:
        return "red"
    elif score <= 40:
        return "orange"
    elif score <= 60:
        return "yellow"
    elif score <= 80:
        return "lightgreen"
    else:
        return "green"

def main():
    # Configure the page with custom theme and layout
    st.set_page_config(
        page_title="Password Strength Meter",
        page_icon="🔒",
        layout="centered"
    )

    # Custom CSS for better styling
    st.markdown("""
        <style>
        .main {
            padding: 2rem;
        }
        .stProgress > div > div > div {
            height: 15px;
            border-radius: 10px;
        }
        .password-header {
            text-align: center;
            padding: 1rem 0;
            color: #1E88E5;
        }
        .feedback-box {
            padding: 1rem;
            border-radius: 10px;
            background-color: #f0f2f6;
            margin: 1rem 0;
        }
        .tips-box {
            padding: 1rem;
            border-radius: 10px;
            background-color: #e3f2fd;
            margin: 1rem 0;
        }
        </style>
    """, unsafe_allow_html=True)

    # Header with animation
    st.markdown('<h1 class="password-header">🔒 Password Strength Meter</h1>', unsafe_allow_html=True)
    st.markdown("""
        <p style='text-align: center; color: #666; margin-bottom: 2rem;'>
            Create a strong password to keep your accounts secure
        </p>
    """, unsafe_allow_html=True)

    # Create columns for better layout
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Password input with better styling
        password = st.text_input(
            "Enter your password",
            type="password",
            help="Type your password to check its strength"
        )

    if password:
        # Analyze password
        score, feedback = analyze_password(password)
        strength_label = get_strength_label(score)
        color = get_strength_color(score)

        # Create columns for strength meter
        meter_col1, meter_col2 = st.columns([3, 1])
        
        with meter_col1:
            # Display strength meter with animation
            st.markdown(f"### Strength: <span style='color: {color}'>{strength_label}</span>", unsafe_allow_html=True)
            st.progress(score/100)
        
        with meter_col2:
            # Display score in a circular format
            st.markdown(f"""
                <div style='text-align: center; padding: 10px; background-color: {color}; 
                border-radius: 50%; width: 60px; height: 60px; margin: auto;'>
                    <h2 style='color: white; margin: 0; padding-top: 12px;'>{score}</h2>
                </div>
            """, unsafe_allow_html=True)

        # Display feedback in a styled box
        if feedback:
            st.markdown("<div class='feedback-box'>", unsafe_allow_html=True)
            st.markdown("#### 🔍 Suggestions for Improvement")
            for msg in feedback:
                st.warning(msg)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.success("🎉 Excellent! Your password meets all security requirements!")

        # Security tips in a styled box
        with st.expander("📌 Security Tips", expanded=False):
            st.markdown("<div class='tips-box'>", unsafe_allow_html=True)
            st.markdown("""
            - 🔑 Use a unique password for each account
            - 🚫 Avoid using personal information
            - ⚠️ Don't use common words or patterns
            - 📱 Consider using a password manager
            - 🔄 Change passwords regularly
            - 🎯 Aim for at least 12 characters
            - 🌈 Mix different types of characters
            """)
            st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()


