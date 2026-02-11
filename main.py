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
    
    default_refrigs_dict = {'Domestic': dict(zip(Domestic_Options,[['R410A','R32','R290','R1234ze(E)'],
                                                              ['R134a','R290','R1234ze(E)','R600a'],
                                                              ['R134a','R290','R1234yf','R600a'],
                                                              ['R32','R290','R1234yf','R134a'],
                                                              ['R32','R290','R1234yf','R410A']])),
                       'Commerical': dict(zip(Commercial_Options,[['R290','R134a','R1234ze(E)','R600a'],
                                                                  ['R600a','R717','R1234ze(E)','R1233zd(E)'],
                                                                  ['R410A','R32','R290','R1234ze(E)'],
                                                                  ['R1234ze(E)','R600','R717','R245fa'],])),
                       'Industrial': dict(zip(Industrial_Options,[['1233zd(E)','R717','R245fa','R600a'],
                                                                  ['R600a','R1233zd(E)','R245fa','R718'],
                                                                  ['R245fa','R601','R1233zd(E)','R601a'],
                                                                  ['R245fa','R1233zd(E)','R600','R717'],
                                                                  ['R1234ze(E)','R1234yf','R290','R245fa'],
                                                                  ['R717','R1234ze(Z)','R245fa','R600'],
                                                                  ['R600','R245fa','R601','R1233zd(E)'],
                                                                  ['R290','R134a','R1234ze(Z)','R717']]))
                       }
    
    max_cond_temp = {'R717': 122,
                     'CarbonDioxide': 21,
                     'CycloHexane': 270,
                     'Cyclopentane': 228,
                     'CycloPropane': 116,
                     'IsoButane': 124,
                     'R601a': 177,
                     'n-Butane': 143,
                     'n-Octane': 286,
                     'R601': 186,
                     'R290': 87,
                     'Neopentane': 151,
                     'R11': 188,
                     'R12': 102,
                     'R13': 19,
                     'R21': 169,
                     'R22': 86,
                     'R23': 16,
                     'R32': 68,
                     'R40': 134,
                     'R113': 204,
                     'R114': 136,
                     'R115': 70,
                     'R116': 10,
                     'R123': 174,
                     'R1233zd(E)': 156,
                     'R1234yf': 85,
                     'R1234ze(E)':99,
                     'R1234ze(Z)': 160,
                     'R124': 112,
                     'R1243zf': 87,
                     'R125': 57,
                     'R134a': 92,
                     'R141b': 194,
                     'R142b': 128,
                     'R143a': 63,
                     'R152A': 104,
                     'R161': 92,
                     'R218': 62,
                     'R227EA': 93,
                     'R236EA': 129,
                     'R236FA': 115,
                     'R245ca': 164,
                     'R245fa': 144,
                     'R365MFC': 151,
                     'R404A': 63,
                     'R407C': 77,
                     'R410A': 62,
                     'R507A': 61,
                     'SulfurDioxide': 310,
                     'R718': 364
                     }
    
    refrigs_list = list(max_cond_temp.keys())
    
    emojis = ['1️⃣','2️⃣','3️⃣','4️⃣']
    
    st.session_state.setdefault('selected_refrigs',default_refrigs_dict[Application_Type][Application])
    st.session_state.setdefault('edit_mode',None)
    
    st.header(f'3️⃣ Select Refrigerants (up to 4)')

    if len(st.session_state['selected_refrigs']) > 0:
        for i, current_refrig in enumerate(st.session_state['selected_refrigs']):
            with st.container():
                col51, col52, col53, col54 = st.columns([0.2,2,0.5,0.5])
                
                with col51:
                    st.subheader(emojis[i])
                    
                with col52:
                    if st.session_state['edit_mode'] == i:
                        taken_refrigs = [r for idx, r in enumerate(st.session_state['selected_refrigs']) if idx != i]
                        available_refrigs = [r for r in refrigs_list if r not in taken_refrigs]
                        new_refrig = st.selectbox('Refrigerant', available_refrigs,index=available_refrigs.index(current_refrig),key=f'{i}_dropdown',label_visibility='collapsed')
                    else:
                        st.subheader(current_refrig)

                with col53:
                    if st.session_state['edit_mode'] == i:
                        if st.button('Save', key=f'{i}_save', icon='✅'):
                            st.session_state['selected_refrigs'][i] = new_refrig #type:ignore
                            st.session_state['edit_mode'] = None
                            st.rerun()
                    else:
                        if st.button('Edit', key=f'{i}_edit', icon='✏️'):
                            st.session_state['edit_mode'] = i
                            st.rerun()
                
                with col54:
                    if st.button('Remove', key=f'{i}_remove', icon='❌', type='primary'):
                        st.session_state['selected_refrigs'].pop(i)
                        st.session_state['edit_mode'] = None
                        st.rerun()
    else:
        st.header('📦', text_alignment='center')
        st.subheader('No refrigerants selected', text_alignment='center')
        st.caption('Click "Add Refrigerant" to get started', text_alignment='center')
    
    if len(st.session_state['selected_refrigs']) < 4:
        if st.button(f'➕ Add Refrigerant ({len(st.session_state['selected_refrigs'])}/4)',width='stretch'):
            st.selectbox('Select',refrigs_list,placeholder='🔎 Search refrigerants...')
            
      
    if len(st.session_state['selected_refrigs']) == 4:
        st.caption('4/4 refrigerants selected • Maximum reached')
    else:
        st.caption(f'{len(st.session_state['selected_refrigs'])}/4 refrigerants selected')
                
        
            
        
    
    
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