import streamlit as st

def main():
    st.set_page_config('HPAT','♨️','wide')
    
    st.title('HPAT - Heap Pump Analysis Tool')
    st.divider()
    
    st.header('1️⃣ End Application Input')
    
    col11, col12, col13 = st.columns(3)
    
    with col11:
        Application_Types = ['Domestic','Commerical','Industrial']
        
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
        
        Application_Type = st.selectbox('Application',Application_Types)
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
    
    col21, col22, col23 = st.columns(3)
    
    if Input_Type == 'Volume of Water to be Heated':
        with col21:
            Water_Volume = st.number_input('Volume of Water to be Heated (L)',min_value=1,step=1,placeholder='Enter water volume')
        with col22:
            Heating_Time = st.number_input('Time Required for Heating (min)', min_value=1, step=1, placeholder='Enter heating time')
    else:
        with col21:
            HP_Capacity = st.number_input('Required Heating Capacity (kW)',min_value=1,step=1, placeholder='Enter heat pump capacity')
            
    st.divider()
    
    st.header('2️⃣ Heat Pump Technical Inputs')
    
    default_cond_temps = {'Domestic': dict(zip(Domestic_Options,[60.0,65.0,35.0,40.0,55.0])),
                          'Commerical': dict(zip(Commercial_Options,[65.0,80.0,55.0,75.0])),
                          'Industrial': dict(zip(Industrial_Options,[85.0,120.0,140.0,110.0,72.0,90.0,130.0,90.0]))}
    
    col31, col32, col33, col34 = st.columns(4)
    
    
    
    #TODO: format
    with col31:
        Cond_Temp = st.number_input('Condensing Temperature (°C)',min_value=0.0,value=default_cond_temps[Application_Type][Application],step=0.1,placeholder='Auto-filled',format='%0f')
        Desired_Water_Temp = st.slider('Desired Water Temperature (°C)',min_value=Cond_Temp-9.0, max_value=Cond_Temp-5.0,step=1.0,format='%0f')

        col41, col42 = st.columns(2)
        
        with col41:
            st.text(f'Selected: {round(Desired_Water_Temp)}°C')
        with col42:
            st.caption(f'(Range: {round(Cond_Temp-9)}-{round(Cond_Temp-5)}°C)')
        
    with col32:
        Evap_Temp = st.number_input('Evaporating Temperature (°C)', min_value=0.0,value=20.0,step=0.1,placeholder='Auto-filled',format='%0f')
    with col33:
        Subcool = st.number_input('Degree of Subcooling (°C)', min_value=0.0, value=8.0, step=0.1,placeholder='Auto-filled',format='%0f')
    with col34:
        Supheat = st.number_input('Degree of Superheat (°C)',min_value=0.0, value=11.0, step=0.1, placeholder='Auto-filled',format='%0f')
        
    
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