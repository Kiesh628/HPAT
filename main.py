import streamlit as st

def main():
    st.set_page_config('HPAT','♨️','wide')
    
    st.title('HPAT - Heap Pump Analysis Tool')
    st.divider()
    
    st.header('1️⃣ End Application Input')
    
    col11, col12, col13 = st.columns(3)
    
    with col11:
        Application_Type = ['Domestic','Commerical','Industrial']
        
        Domestic_Options = ['Space heating (radiators)',
                               'Domestic hot water supply (DHW)',
                               'Pool heating',
                               'Underfloor heating',
                               'Combined heating/cooling']
        
        Commercial_Options = ['DHW (hotels, etc.)',
                               'Commercial laundry/kitchens',
                               'Central heating (fan coils, etc.)',
                               'Hospital sterilization supply']
        
        Industrial_Options = ['Clean-in-place (CIP) processes',
                               'Reactor/process heating (chemical)',
                               'Steam generation (HP replacement)',
                               'Waste heat recovery and upgrade',
                               'Food pasteurization',
                               'Textile dyeing and washing',
                               'Pulp and paper drying',
                               'District heating (urban networks)']
        
        
        Application_Options = {'Domestic': Domestic_Options,
                               'Commerical':Commercial_Options,
                               'Industrial': Industrial_Options}
        
        Application_Type = st.selectbox('Application',Application_Type)
        Application = st.selectbox('Application', Application_Options[Application_Type],label_visibility='collapsed')
        
        Input_Type = st.selectbox('Select Input Type',['Volume of Water to be Heated','Required Heating Capacity (kW)'])
        st.info(" 💡 Choose one input type - all are optional but you must select one to proceed")

    
    with col12:
        Available_Cities = ['Delhi',
                            'Mumbai',
                            'Bangalore',
                            'Chennai',
                            'Nagpur',
                            'Bhopal',
                            'Guwahati',
                            'Kolkata',
                            'Lucknow',
                            'Hyderabad',
                            'Ahmedabad',
                            'Pune',
                            'Jaipur',
                            'Chandigarh',
                            'Thiruvananthapuram',
                            'Goa (Panaji)',
                            'Indore',
                            'Patna',
                            'Bhubaneswar',
                            'Raipur',
                            'Ranchi',
                            'Dehradun',
                            'Srinagar',
                            'Leh',
                            'Shillong']
        City = st.selectbox('City',Available_Cities)
    
    with col13:
        Type_of_Heat_Pump = st.selectbox('Type of Heat Pump', ['Air Source Heat Pump','Water Source Heat Pump'])
    
    col21, col22, col32 = st.columns(3)
    
    if Input_Type == 'Volume of Water to be Heated':
        with col21:
            Water_Volume = st.number_input('Volume of Water to be Heated (L)',min_value=1,step=1,placeholder='Enter water volume')
        with col22:
            Heating_Time = st.number_input('Time Required for Heating (min)', min_value=1, step=1, placeholder='Enter heating time')
    else:
        with col21:
            HP_Capacity = st.number_input('Required Heating Capacity (kW)',min_value=1,step=1, placeholder='Enter heat pump capacity')
            
    st.divider()
    
    return

if __name__ == "__main__":
    if st.runtime.exists(): #type: ignore
        main()
    else:
        import sys
        import os
        import subprocess
        cmd = [sys.executable, "-m", "streamlit", "run", os.path.abspath(__file__)]
        subprocess.run(cmd)