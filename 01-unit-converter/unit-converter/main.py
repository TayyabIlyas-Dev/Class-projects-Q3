import streamlit as st

def main():
    # Custom CSS for better styling
    st.markdown("""
        <style>
        /* Main title styling */
        .main-title {
            color: #1E88E5;
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 2rem;
            text-align: center;
            padding: 1rem;
            background: linear-gradient(90deg, #E3F2FD 0%, #BBDEFB 100%);
            border-radius: 10px;
        }
        
        /* Container styling */
        .converter-container {
            background-color: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin: 1rem 0;
        }
        
        /* Formula box styling */
        .formula-container {
            background-color: #f8f9fa;
            padding: 1rem;
            border-radius: 10px;
            border-left: 4px solid #1E88E5;
            margin-top: 1rem;
        }
        
        .formula-label {
            background-color: #1E88E5;
            color: white;
            padding: 0.3rem 0.8rem;
            border-radius: 5px;
            font-weight: 500;
        }
        
        .formula-text {
            margin-left: 1rem;
            color: #424242;
        }
        
        /* Result styling */
        .result-text {
            font-size: 1.5rem;
            color: #1E88E5;
            font-weight: 600;
            text-align: center;
            padding: 1rem;
            background-color: #E3F2FD;
            border-radius: 8px;
            margin: 1rem 0;
        }
        
        /* Selectbox styling */
        .stSelectbox {
            min-width: 200px;
        }
        
        .stSelectbox > div > div {
            background-color: #f8f9fa;
            border-radius: 8px;
        }
        
        /* Number input styling */
        .stNumberInput {
            min-width: 200px;
        }
        
        .stNumberInput > div > div > input {
            border-radius: 8px;
            background-color: #f8f9fa;
        }
        
        /* Conversion type selector styling */
        .conversion-type {
            background-color: #E3F2FD;
            padding: 0.5rem;
            border-radius: 8px;
            margin-bottom: 1rem;
        }
        
        /* Equal sign styling */
        .equal-sign {
            font-size: 2rem;
            font-weight: bold;
            color: #1E88E5;
            text-align: center;
            margin: 1rem 0;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Title with custom styling
    st.markdown('<h1 class="main-title">Unit Converter</h1>', unsafe_allow_html=True)
    
    # Create a container for the converter
    with st.container():
        # st.markdown('<div class="converter-container">', unsafe_allow_html=True)
        
        # Add a selectbox for conversion type with custom styling
        st.markdown('<div class="conversion-type">', unsafe_allow_html=True)
        conversion_type = st.selectbox("Select Conversion Type", 
                                     ["Length", "Weight", "Temperature"],
                                     index=0)
        st.markdown('</div>', unsafe_allow_html=True)
        
        if conversion_type == "Length":
            # Create two columns for input and output
            col1, col2 = st.columns(2)
            
            # Input column
            with col1:
                input_value = st.number_input("Enter value", value=1.0, step=0.1)
                from_unit = st.selectbox("From", 
                    ["Metre", "Centimetre", "Millimetre", "Kilometre", "Mile", "Yard", "Foot", "Inch"])
            
            # Output column
            with col2:
                st.markdown('<div class="equal-sign">=</div>', unsafe_allow_html=True)
                to_unit = st.selectbox("To",
                    ["Centimetre", "Metre", "Millimetre", "Kilometre", "Mile", "Yard", "Foot", "Inch"])
            
            # Conversion factors (to metres first)
            conversion_factors = {
                "Metre": 1,
                "Centimetre": 0.01,
                "Millimetre": 0.001,
                "Kilometre": 1000,
                "Mile": 1609.34,
                "Yard": 0.9144,
                "Foot": 0.3048,
                "Inch": 0.0254
            }
            
            # Calculate conversion
            value_in_metres = input_value * conversion_factors[from_unit]
            result = value_in_metres / conversion_factors[to_unit]
            
            # Display result with custom styling
            st.markdown(f'<div class="result-text">{result:.4f} {to_unit}</div>', unsafe_allow_html=True)
            
            # Display formula with custom styling
            st.markdown(f"""
                <div class="formula-container">
                    <span class="formula-label">Formula</span>
                    <span class="formula-text">multiply the value by {conversion_factors[to_unit]/conversion_factors[from_unit]:.4f}</span>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    # Set page config
    st.set_page_config(
        page_title="Unit Converter",
        layout="centered",
        initial_sidebar_state="collapsed",
        page_icon="🔄"
    )
    
    # Set background color
    st.markdown("""
        <style>
        .stApp {
            background-color: #f0f2f6;
        }
        </style>
    """, unsafe_allow_html=True)
    
    main()
