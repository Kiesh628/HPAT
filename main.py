import streamlit as st

def main():    
    st.set_page_config('HPAT','♨️','wide')
    
    st.title('HPAT - Heap Pump Analysis Tool')

    fixed = st.toggle('Use fixed version', value=False, help="The default is a model replica of ISHRAE's Heat Pump Analysis Tool, with all of its bugs and issues transfered over. Select this option to use the fixed version, which is a more accurate model.")
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
    
    default_cond_temps = {'Domestic': dict(zip(Domestic_Options,[60.0,65.0,35.0,40.0,55.0])),
                          'Commerical': dict(zip(Commercial_Options,[65.0,80.0,55.0,75.0])),
                          'Industrial': dict(zip(Industrial_Options,[85.0,120.0,140.0,110.0,72.0,90.0,130.0,90.0]))}

    if Input_Type == 'Volume of Water to be Heated':
        with col21:
            Water_Volume = st.number_input('Volume of Water to be Heated (L)',min_value=1,step=1,placeholder='Enter water volume')
        with col22:
            Heating_Time = st.number_input('Time Required for Heating (min)', min_value=1, step=1, placeholder='Enter heating time')
    else:
        with col21:
            HP_Capacity = st.number_input('Required Heating Capacity (kW)',min_value=1.0,step=1.0, placeholder='Enter heat pump capacity')
    inlet_water_temp = 26.0
    if fixed:
        with col23:
            inlet_water_temp = st.number_input('Inlet Water Temperature (°C)', value=26.0, min_value=-273.15, max_value=default_cond_temps[Application_Type][Application]-6.0, step=1.0, placeholder='Enter inlet water temperature')
    
    st.divider()
    
    st.header('2️⃣ Heat Pump Technical Inputs')
    
    
    
    col31, col32, col33, col34 = st.columns(4)
    
    
    
    #TODO: format
    with col31:
        Cond_Temp = st.number_input('Condensing Temperature (°C)',min_value=0.0,value=default_cond_temps[Application_Type][Application],step=0.1,placeholder='Auto-filled',format='%0f')
        if fixed:
            Desired_Water_Temp = st.number_input('Desired Water Temperature (°C)', value=Cond_Temp-9.0,min_value=inlet_water_temp+1.0, max_value=Cond_Temp-5.0,step=1.0,format='%0f') # +1 so it has something to heat
        else:
            Desired_Water_Temp = st.slider('Desired Water Temperature (°C)',min_value=Cond_Temp-9.0, max_value=Cond_Temp-5.0,step=1.0,format='%0f')
        
        if not fixed:
            col41, col42 = st.columns(2)
            with col41:
                st.text(f'Selected: {round(Desired_Water_Temp)}°C')
            with col42:
                st.caption(f'(Range: {round(Cond_Temp-9)}-{round(Cond_Temp-5)}°C)')
        
    with col32:
        Evap_Temp = st.number_input('Evaporating Temperature (°C)', min_value=0.0,value=21.0,step=0.1,placeholder='Auto-filled',format='%0f')
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

    refrigerant_data = {
        "R410A":      {"gwp": 1924, "safety": "A1",  "score": 9.6, "max_temp": 62.0},
        "R134a":      {"gwp": 1300, "safety": "A1",  "score": 9.6, "max_temp": 92.0},
        "R404A":      {"gwp": 3943, "safety": "A1",  "score": 9.6, "max_temp": 63.0},
        "R507A":      {"gwp": 3985, "safety": "A1",  "score": 9.6, "max_temp": 61.0},
        "R407C":      {"gwp": 1774, "safety": "A1",  "score": 9.6, "max_temp": 77.0},
        "R218":       {"gwp": 8830, "safety": "A1",  "score": 9.6, "max_temp": 62.0},
        "R227EA":     {"gwp": 3220, "safety": "A1",  "score": 9.6, "max_temp": 93.0},
        "R236FA":     {"gwp": 9810, "safety": "A1",  "score": 9.6, "max_temp": 115.0},
        "R236EA":     {"gwp": 1370, "safety": "A1",  "score": 9.6, "max_temp": 129.0},
        "R245fa":     {"gwp": 858,  "safety": "B1",  "score": 9.6, "max_temp": 144.0},
        "R245ca":     {"gwp": 693,  "safety": "A1",  "score": 9.6, "max_temp": 164.0},
        "R365MFC":    {"gwp": 794,  "safety": "N/A", "score": 1.2, "max_temp": 151.0},
        "R32":        {"gwp": 677,  "safety": "A2L", "score": 6.8, "max_temp": 68.0},
        "R1234yf":    {"gwp": 1,    "safety": "A2L", "score": 6.8, "max_temp": 85.0},
        "R1234ze(E)": {"gwp": 1,    "safety": "A2L", "score": 6.8, "max_temp": 99.0},
        "R1234ze(Z)": {"gwp": 1,    "safety": "A2L", "score": 6.8, "max_temp": 140.0},
        "R1233zd(E)": {"gwp": 1,    "safety": "A1",  "score": 9.6, "max_temp": 156.0},
        "R142b":      {"gwp": 2310, "safety": "A2",  "score": 6.8, "max_temp": 128.0},
        "R143a":      {"gwp": 4470, "safety": "A2L", "score": 6.8, "max_temp": 63.0},
        "R152A":      {"gwp": 138,  "safety": "A2",  "score": 6.8, "max_temp": 104.0},
        "R290":       {"gwp": 3,    "safety": "A3",  "score": 1.2, "max_temp": 87.0},
        "R600a":      {"gwp": 3,    "safety": "A3",  "score": 1.2, "max_temp": 124.0},
        "R600":       {"gwp": 4,    "safety": "A3",  "score": 1.2, "max_temp": 143.0},
        "R601":       {"gwp": 5,    "safety": "A3",  "score": 1.2, "max_temp": 186.0},
        "R601a":      {"gwp": 5,    "safety": "A3",  "score": 1.2, "max_temp": 177.0},
        "R1270":      {"gwp": 2,    "safety": "A3",  "score": 1.2, "max_temp": 83.0},
        "CycloPropane": {"gwp": 0,  "safety": "A3",  "score": 1.2, "max_temp": 116.0},
        "R717":       {"gwp": 0,    "safety": "B2L", "score": 6.8, "max_temp": 122.0},
        "R744":       {"gwp": 1,    "safety": "A1",  "score": 9.6, "max_temp": 21.0},
        "R718":       {"gwp": 0,    "safety": "A1",  "score": 9.6, "max_temp": 364.0},
        "R22":        {"gwp": 1760, "safety": "A1",  "score": 9.6, "max_temp": 86.0},
        "R123":       {"gwp": 77,   "safety": "B1",  "score": 9.6, "max_temp": 174.0},
        "R141b":      {"gwp": 725,  "safety": "N/A", "score": 1.2, "max_temp": 194.0},
        "R113":       {"gwp": 6130, "safety": "A1",  "score": 9.6, "max_temp": 204.0},
        "R114":       {"gwp": 10000,"safety": "A1",  "score": 9.6, "max_temp": 136.0}
    }

    refrigs_list = sorted(list(refrigerant_data.keys()))
    
    
    emojis = ['1️⃣','2️⃣','3️⃣','4️⃣']
    
    st.session_state.setdefault('selected_refrigs',default_refrigs_dict[Application_Type][Application])
    st.session_state.setdefault('edit_mode',None)
    
    st.header(f'3️⃣ Select Refrigerants (up to 4)')

    refrigs_valid = True
    error_string = None
    if len(st.session_state['selected_refrigs']) > 0 and min(refrigerant_data[refrig]['max_temp'] for refrig in st.session_state['selected_refrigs']) < Cond_Temp:
        refrigs_valid = False
        error_string = f"The following refrigerant(s) cannot operate at the selected condensing temperature ({Cond_Temp}°C):  \n"
        for refrig in st.session_state['selected_refrigs']:
            if refrigerant_data[refrig]['max_temp'] < Cond_Temp:
                excess = Cond_Temp - refrigerant_data[refrig]['max_temp']
                error_string += f"- **{refrig}** — Max: {refrigerant_data[refrig]['max_temp']}°C (exceeds by {excess:.0f}°C)  \n"
    
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
                        if refrigerant_data[current_refrig]['max_temp'] < Cond_Temp:
                            st.subheader(f"{current_refrig} ⚠️")
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
    
    st.session_state.setdefault('adding_refrig', False)

    if len(st.session_state['selected_refrigs']) < 4:
        if not st.session_state['adding_refrig']:
            if st.button(f'➕ Add Refrigerant ({len(st.session_state["selected_refrigs"])}/4)', width='stretch'):
                st.session_state['adding_refrig'] = True
                st.rerun()
        else:
            available = [r for r in refrigs_list if r not in st.session_state['selected_refrigs']]
            col_sel, col_confirm, col_cancel = st.columns([3, 1, 1])
            with col_sel:
                chosen = st.selectbox('Select refrigerant to add', available,
                                      placeholder='🔎 Search refrigerants...', label_visibility='collapsed')
            with col_confirm:
                if st.button('✅ Add', width='stretch'):
                    st.session_state['selected_refrigs'].append(chosen)
                    st.session_state['adding_refrig'] = False
                    st.rerun()
            with col_cancel:
                if st.button('✖ Cancel', width='stretch', type='primary'):
                    st.session_state['adding_refrig'] = False
                    st.rerun()

    if len(st.session_state['selected_refrigs']) == 4:
        st.caption('4/4 refrigerants selected • Maximum reached')
    else:
        st.caption(f'{len(st.session_state['selected_refrigs'])}/4 refrigerants selected')
    
    if not refrigs_valid:
        st.error(error_string)
    
    st.divider()
    
    st.header(f'4️⃣ Other Inputs')
    
    col61, col62, col63, col64 = st.columns(4)
    
    fuel_sources_list = ['Electrical',
                         'Diesel',
                         'Biomass',
                         'Natural Gas',
                         'Wood',
                         'LPG',
                         'Bituminous coal']
    
    Compressor_types_list = ['Rotary','Reciprocating','Scroll','Screw']
    
    operating_hours_list = ['4 hours','8 hours','12 hours','16 hours']
    
    with col61:
        fuel_source = st.selectbox('Existing Heating Fuel Source',fuel_sources_list)
    if not fixed:
        with col62:
            compressor_type = st.selectbox('Type of Compressor',Compressor_types_list, help='Does absolutely nothing') # dont ask me what this does, I don't know either
    with col63:
        safety = st.selectbox('Refrigerant Ranking Preference',['With Safety Class','Without Safety Class'], help='TOPSIS Method: Technique for Order of Preference by Similarity to Ideal Solution. TOPSIS is a multi-criteria decision analysis method that ranks alternatives based on their geometric distance from the ideal solution. In this tool, it helps identify the best refrigerant choice by considering multiple performance criteria simultaneously.')
    with col64:
        operating_hours = st.selectbox('Daily Operating Hours',operating_hours_list,index=1)
    st.info('Note: Emission factor for electricity is from Central Electricity Authority (CEA), India. For TEWI calculations of the heat pump, the following assumptions are considered: operating life of 15 years, 300 days of operation per year.')
    
    st.divider()
    
    if st.button('Calculate Results', type="primary") and refrigs_valid:
        
        with st.spinner('Processing your request...', show_time=True):
            import pandas as pd
            import numpy as np
            import plotly.graph_objects as go
            import CoolProp.CoolProp as cp
            
            Cp_water = 4.2

            _ETA_A, _ETA_B, _ETA_C = 0.395831, 0.176590, -0.027411
            def get_eta_is(cond_t, evap_t, ref):
                P1 = cp.PropsSI('P', 'T', evap_t + 273.15, 'Q', 1, ref)
                P2 = cp.PropsSI('P', 'T', cond_t + 273.15, 'Q', 0, ref)
                PR = P2 / P1
                return max(0.50, min(0.95, _ETA_A + _ETA_B * PR + _ETA_C * PR * PR))

            grid_ef    = 0.913 
            leak_rate  = 0.02
            recovery   = 0.70
            life_years = 15
            days_year  = 300

            charge_per_kw = {
                "R410A":        0.2314, "R134a":        0.2181, "R404A":        0.2113,
                "R507A":        0.2125, "R407C":        0.2089, "R218":         0.2082,
                "R245fa":       0.2172, "R245ca":       0.2233, "R32":          0.2146,
                "R1234yf":      0.9821, "R1234ze(E)":   1.6369, "R1234ze(Z)":   0.3274,
                "R1233zd(E)":   0.3274, "R142b":        0.2202, "R143a":        0.2293,
                "R290":         0.2579, "R600a":        0.2579, "R600":         0.2455,
                "R601":         0.5000, "R601a":        0.4583, "R1270":        0.2679,
                "CycloPropane": 0.2200, "R717":         0.2200, "R718":         0.2200,
                "R22":          0.2177, "R123":         0.2192, "R141b":        0.2186,
                "R113":         0.2052, "R114":         0.1881,
                "R227EA":       0.2245, "R236FA":       0.1787, "R236EA":       0.2110,
                "R365MFC":      0.2170, "R152A":        0.2202,
                "DEFAULT":      0.2200,
            }

            BASE_EF = {
                'Electrical':      0.7343,
                'Diesel':          0.3181,
                'Natural Gas':     0.2418,
                'LPG':             0.2715,  
                'Bituminous coal': 0.4048,
                'Biomass':         0.4278,
                'Wood':            0.0000,   # The ISHRAE people didnt bother to implement wood so neither will I 
            }

            if Input_Type == 'Required Heating Capacity (kW)':
                Heating_Capacity = float(HP_Capacity) #type:ignore
            else:
                Heating_Capacity = (Water_Volume * Cp_water * (Desired_Water_Temp - inlet_water_temp)) / (60.0 * Heating_Time) #type:ignore
            def get_cycle(refrig: str):
                try:
                    T_cond_K = Cond_Temp + 273.15
                    T_evap_K = Evap_Temp + 273.15
                    
                    P1 = cp.PropsSI('P', 'T', T_evap_K, 'Q', 1, refrig)
                    T1 = T_evap_K + Supheat
                    h1 = cp.PropsSI('H', 'T', T1, 'P', P1, refrig)
                    s1 = cp.PropsSI('S', 'T', T1, 'P', P1, refrig)
                    rho1 = cp.PropsSI('D', 'T', T1, 'P', P1, refrig)
                    s1_sup = s1

                    P2 = cp.PropsSI('P', 'T', T_cond_K, 'Q', 0, refrig)
                    h2s = cp.PropsSI('H', 'P', P2, 'S', s1_sup, refrig)
                    eta_is = get_eta_is(Cond_Temp, Evap_Temp, refrig)
                    h2 = h1 + ((h2s - h1) / eta_is)
                    T2 = cp.PropsSI('T', 'P', P2, 'H', h2, refrig)

                    P3 = P2 
                    T3 = T_cond_K - Subcool
                    h3 = cp.PropsSI('H', 'T', T3, 'P', P3, refrig)
                    
                    P4 = P1
                    h4 = h3 
                    T4 = cp.PropsSI('T', 'P', P4, 'H', h4, refrig)

                    q_cond = (h2 - h3) / 1000.0
                    w_comp = (h2 - h1) / 1000.0
                    cop_actual = q_cond / w_comp
                    
                    mass_flow = Heating_Capacity / q_cond
                    vhc = (q_cond * rho1) / 1000.0
                    displacement = (mass_flow / rho1) * 3600.0
                    evap_cap = mass_flow * ((h1 - h4) / 1000.0)
                    comp_power = mass_flow * w_comp
                    
                    cop_carnot = T_cond_K / (T_cond_K - T_evap_K)
                    exergy_eff = (cop_actual / cop_carnot) * 100.0

                    T_crit = cp.PropsSI('Tcrit', refrig)
                    T_trip = cp.PropsSI('Tmin', refrig)
                    T_range = np.linspace(T_trip, T_crit - 0.1, 300)
                    
                    dome = {
                        'T': T_range - 273.15,
                        'P': [cp.PropsSI('P','T',t,'Q',0,refrig)/1e5 for t in T_range],
                        's_liq': [cp.PropsSI('S','T',t,'Q',0,refrig)/1000 for t in T_range],
                        's_vap': [cp.PropsSI('S','T',t,'Q',1,refrig)/1000 for t in T_range],
                        'h_liq': [cp.PropsSI('H','T',t,'Q',0,refrig)/1000 for t in T_range],
                        'h_vap': [cp.PropsSI('H','T',t,'Q',1,refrig)/1000 for t in T_range]
                    }

                    if fixed:
                        def _isobar_ts(P_pa, T_start_K, T_end_K, n=20):
                            Ts = np.linspace(T_start_K, T_end_K, n)
                            return [cp.PropsSI('S','P',P_pa,'T',T,refrig)/1000 for T in Ts], [T-273.15 for T in Ts], \
                                   [cp.PropsSI('H','P',P_pa,'T',T,refrig)/1000 for T in Ts], [P_pa/1e5]*n

                        s2_act = cp.PropsSI('S','P',P2,'H',h2,refrig)/1000
                        c12 = ([s1_sup/1000, s2_act], [T1-273.15, T2-273.15], [h1/1000, h2/1000], [P1/1e5, P2/1e5])
                        dsh = _isobar_ts(P2, T2, T_cond_K + 0.5, 15)
                        h_gC_val = cp.PropsSI('H','T',T_cond_K,'Q',1,refrig)
                        h_fC_val = cp.PropsSI('H','T',T_cond_K,'Q',0,refrig)
                        h_cond_arr = np.linspace(h_gC_val, h_fC_val, 25)
                        cond_s = [cp.PropsSI('S','P',P2,'H',h,refrig)/1000 for h in h_cond_arr]
                        cond_T_arr = [cp.PropsSI('T','P',P2,'H',h,refrig)-273.15 for h in h_cond_arr]
                        cond = (cond_s, cond_T_arr, [h/1000 for h in h_cond_arr], [P2/1e5]*25)
                        sc = _isobar_ts(P2, T_cond_K - 0.5, T3, 10)
                        s3 = cp.PropsSI('S','T',T3,'P',P3,refrig)/1000
                        s4 = cp.PropsSI('S','P',P1,'H',h4,refrig)/1000
                        c34 = ([s3, s4], [T3-273.15, T4-273.15], [h3/1000, h4/1000], [P2/1e5, P1/1e5])
                        h_gE_val = cp.PropsSI('H','T',T_evap_K,'Q',1,refrig)
                        h_evap_arr = np.linspace(h4, h_gE_val, 25)
                        evap_s = [cp.PropsSI('S','P',P1,'H',h,refrig)/1000 for h in h_evap_arr]
                        evap_T_arr = [cp.PropsSI('T','P',P1,'H',h,refrig)-273.15 for h in h_evap_arr]
                        evap = (evap_s, evap_T_arr, [h/1000 for h in h_evap_arr], [P1/1e5]*25)
                        sh = _isobar_ts(P1, T_evap_K + 0.5, T1, 15)

                        path_s = list(c12[0]) + list(dsh[0])[1:] + list(cond[0])[1:] + list(sc[0])[1:] + list(c34[0])[1:] + list(evap[0])[1:] + list(sh[0])[1:]
                        path_T = list(c12[1]) + list(dsh[1])[1:] + list(cond[1])[1:] + list(sc[1])[1:] + list(c34[1])[1:] + list(evap[1])[1:] + list(sh[1])[1:]
                        path_h = list(c12[2]) + list(dsh[2])[1:] + list(cond[2])[1:] + list(sc[2])[1:] + list(c34[2])[1:] + list(evap[2])[1:] + list(sh[2])[1:]
                        path_P = list(c12[3]) + list(dsh[3])[1:] + list(cond[3])[1:] + list(sc[3])[1:] + list(c34[3])[1:] + list(evap[3])[1:] + list(sh[3])[1:]

                        cycle = {'T': path_T, 'P': path_P, 'h': path_h, 's': path_s,
                                 'states': {'s': [s1_sup/1000, s2_act, s3, s4],
                                            'T': [T1-273.15, T2-273.15, T3-273.15, T4-273.15],
                                            'h': [h1/1000, h2/1000, h3/1000, h4/1000],
                                            'P': [P1/1e5, P2/1e5, P2/1e5, P1/1e5]}}
                        def _seg_x(p1, p2, q1, q2):
                            d = p2 - p1; e = q2 - q1
                            c = d[0]*e[1] - d[1]*e[0]
                            if abs(c) < 1e-12: return None
                            r = q1 - p1
                            t = (r[0]*e[1] - r[1]*e[0]) / c
                            u = (r[0]*d[1] - r[1]*d[0]) / c
                            if 0.0 < t < 1.0 and 0.0 < u < 1.0:
                                return p1 + t * d
                            return None
                        def _all_ints(cyc, dom):
                            xs, ys = [], []
                            for i in range(len(cyc)-1):
                                for j in range(len(dom)-1):
                                    pt = _seg_x(cyc[i], cyc[i+1], dom[j], dom[j+1])
                                    if pt is not None:
                                        xs.append(float(pt[0])); ys.append(float(pt[1]))
                            return xs, ys
                        T_d = np.array(dome['T'])
                        dom_ts = np.column_stack([np.concatenate([dome['s_liq'], dome['s_vap'][::-1]]), np.concatenate([T_d, T_d[::-1]])])
                        dom_ph = np.column_stack([np.concatenate([dome['h_liq'], dome['h_vap'][::-1]]), np.concatenate([dome['P'], dome['P'][::-1]])])
                        cyc_ts = np.column_stack([np.array(path_s), np.array(path_T)])
                        cyc_ph = np.column_stack([np.array(path_h), np.array(path_P)])
                        ts_x, ts_y = _all_ints(cyc_ts, dom_ts)
                        ph_x, ph_y = _all_ints(cyc_ph, dom_ph)
                        inters = {'ts': {'s': ts_x, 'T': ts_y}, 'ph': {'h': ph_x, 'P': ph_y}}
                    else:
                        cycle = {
                            'T': [T1-273.15, T2-273.15, T3-273.15, T4-273.15, T1-273.15],
                            'P': [P1/1e5, P2/1e5, P3/1e5, P1/1e5, P1/1e5],
                            'h': [h1/1000, h2/1000, h3/1000, h4/1000, h1/1000],
                            's': [s1_sup/1000, cp.PropsSI('S','P',P2,'H',h2,refrig)/1000, cp.PropsSI('S','T',T3,'P',P3,refrig)/1000, cp.PropsSI('S','P',P1,'H',h4,refrig)/1000, s1_sup/1000]
                        }
                        def _seg_x(p1, p2, q1, q2):
                            d = p2 - p1; e = q2 - q1
                            c = d[0]*e[1] - d[1]*e[0]
                            if abs(c) < 1e-12: return None
                            r = q1 - p1
                            t = (r[0]*e[1] - r[1]*e[0]) / c
                            u = (r[0]*d[1] - r[1]*d[0]) / c
                            if 0.0 < t < 1.0 and 0.0 < u < 1.0:
                                return p1 + t * d
                            return None
                        def _all_ints(cyc, dom):
                            xs, ys = [], []
                            for i in range(len(cyc)-1):
                                for j in range(len(dom)-1):
                                    pt = _seg_x(cyc[i], cyc[i+1], dom[j], dom[j+1])
                                    if pt is not None:
                                        xs.append(float(pt[0])); ys.append(float(pt[1]))
                            return xs, ys
                        T_d  = np.array(dome['T'])
                        dom_ts = np.column_stack([np.concatenate([dome['s_liq'], dome['s_vap'][::-1]]), np.concatenate([T_d, T_d[::-1]])])
                        dom_ph = np.column_stack([np.concatenate([dome['h_liq'], dome['h_vap'][::-1]]), np.concatenate([dome['P'], dome['P'][::-1]])])
                        cyc_ts = np.column_stack([np.array(cycle['s']), np.array(cycle['T'])])
                        cyc_ph = np.column_stack([np.array(cycle['h']), np.array(cycle['P'])])
                        ts_x, ts_y = _all_ints(cyc_ts, dom_ts)
                        ph_x, ph_y = _all_ints(cyc_ph, dom_ph)
                        inters = {'ts': {'s': ts_x, 'T': ts_y}, 'ph': {'h': ph_x, 'P': ph_y}}

                    metrics = {
                        "Refrigerant": refrig,
                        "Volumetric Heating Capacity (MJ/m\u00b3)": vhc,
                        "Displacement of Compressor (m\u00b3/hr)": displacement,
                        "Condenser Capacity (kW)": Heating_Capacity,
                        "Evaporator Capacity (kW)": evap_cap,
                        "Actual COP": cop_actual,
                        "Carnot COP": cop_carnot,
                        "Exergy Efficiency (%)": exergy_eff,
                        "_comp_power": comp_power
                    }

                    return metrics, {'dome': dome, 'cycle': cycle, 'inters': inters}

                except Exception as e:
                    st.error(f"[DEBUG] get_cycle failed for {refrig}: {type(e).__name__}: {e}")
                    return None, None

            results_list = []
            plotting_data = {}
            for ref in st.session_state['selected_refrigs']:
                metrics, plots = get_cycle(ref)
                if metrics:
                    results_list.append(metrics)
                    plotting_data[ref] = plots
                else:
                    st.warning(f"[DEBUG] {ref} returned None from get_cycle")

            if results_list:
                df = pd.DataFrame(results_list)
                
                base_ef = BASE_EF.get(fuel_source, BASE_EF['Electrical'])
                base_emissions_hourly = Heating_Capacity * base_ef

                try:
                    HOURS_DAY = int(str(operating_hours).split()[0])
                except:
                    HOURS_DAY = 8

                topsis_matrix = []
                
                for i, row in df.iterrows():
                    ref = row['Refrigerant']
                    gwp = refrigerant_data[ref]['gwp']
                    power = row['_comp_power']
                    
                    indirect_tons = (power * HOURS_DAY * days_year * life_years * grid_ef) / 1000.0
                    
                    charge_pkw  = charge_per_kw.get(ref, charge_per_kw['DEFAULT'])
                    charge      = Heating_Capacity * charge_pkw
                    loss_frac   = (leak_rate * life_years) + (1 - recovery)
                    direct_tons = (charge * loss_frac * gwp) / 1000.0
                    
                    hp_emissions_hourly = power * grid_ef
                    reduction_kg = base_emissions_hourly - hp_emissions_hourly
                    
                    df.at[i, 'Direct Emissions (Tons CO₂)'] = direct_tons #type:ignore
                    df.at[i, 'Indirect Emissions (Tons CO₂)'] = indirect_tons #type:ignore
                    df.at[i, 'Total Emissions (Tons CO₂)'] = indirect_tons + direct_tons #type:ignore
                    df.at[i, 'CO₂ Reduction (KG)'] = reduction_kg #type:ignore
                    df.at[i, 'CO₂ Reduction (kg per kW)'] = reduction_kg / Heating_Capacity if Heating_Capacity > 0 else 0 #type:ignore
                    
                    topsis_matrix.append([
                        row['Actual COP'],
                        row['Volumetric Heating Capacity (MJ/m³)'],
                        gwp,
                        refrigerant_data[ref]['score']
                    ])

                mat = np.array(topsis_matrix)
                
                is_ind = "Industrial" in Application_Type or "Steam" in Application
                if safety == 'With Safety Class':
                    w = [0.25, 0.65, 0.00, 0.10] if is_ind else [0.231, 0.636, 0.006, 0.127]
                else:
                    w = [0.28, 0.72, 0.00, 0.00] if is_ind else [0.50, 0.50, 0.00, 0.00]
                
                norm_mat = np.zeros_like(mat)
                for i in range(4):
                    denom = np.sqrt(np.sum(mat[:, i]**2))
                    norm_mat[:, i] = mat[:, i] / denom if denom > 0 else 0
                    
                w_mat = norm_mat * np.array(w)
                best = np.array([w_mat[:,0].max(), w_mat[:,1].max(), w_mat[:,2].min(), w_mat[:,3].max()])
                worst = np.array([w_mat[:,0].min(), w_mat[:,1].min(), w_mat[:,2].max(), w_mat[:,3].min()])
                
                d_pos = np.sqrt(np.sum((w_mat - best)**2, axis=1))
                d_neg = np.sqrt(np.sum((w_mat - worst)**2, axis=1))
                
                scores = np.divide(d_neg, (d_pos + d_neg), out=np.zeros_like(d_neg), where=(d_pos+d_neg)!=0)
                
                df['TOPSIS Score'] = scores
                
                ranked_df = df.sort_values(by='TOPSIS Score', ascending=False).reset_index(drop=True)
                
                st.divider()
                col71, col72 = st.columns([0.7, 0.3])
                with col71:
                    st.header('📊 Analysis Results')
                with col72:
                    st.button("📥 Download PDF Report", disabled=True, help="PDF Generation coming soon")
                
                st.subheader('TOPSIS Ranking')
                top_refs = ranked_df['Refrigerant'].tolist() 
                while len(top_refs) < 4: top_refs.append("-")
                
                ranking_display = pd.DataFrame({
                    "Condensing Range": [f"{int(Cond_Temp-9)}°C – {int(Cond_Temp-5)}°C"],
                    "Rank 1": [top_refs[0]], "Rank 2": [top_refs[1]], "Rank 3": [top_refs[2]], "Rank 4": [top_refs[3]]
                })
                st.dataframe(ranking_display, hide_index=True, width='stretch')
                
                st.subheader('Required Heating Capacity')
                c81, c82 = st.columns([0.6,0.4])
                c81.text('Heating Capacity')
                c82.text(f'{Heating_Capacity:.2f} kW')
                
                st.header('📈 Performance Results')
                
                if fixed:
                    final_cols = [
                        'Refrigerant',
                        'Volumetric Heating Capacity (MJ/m³)',
                        'Displacement of Compressor (m³/hr)',
                        'Condenser Capacity (kW)',
                        'Evaporator Capacity (kW)',
                        'Actual COP',
                        'CO₂ Reduction (KG)',
                        'Carnot COP',
                        'Exergy Efficiency (%)',
                        'Direct Emissions (Tons CO₂)',
                        'Indirect Emissions (Tons CO₂)',
                        'Total Emissions (Tons CO₂)',
                        'CO₂ Reduction (kg per kW)'
                    ]
                    format_dict = {
                        'Volumetric Heating Capacity (MJ/m³)': '{:.4f}',
                        'Displacement of Compressor (m³/hr)': '{:.2f}',
                        'Condenser Capacity (kW)': '{:.2f}',
                        'Evaporator Capacity (kW)': '{:.2f}',
                        'Actual COP': '{:.2f}',
                        'CO₂ Reduction (KG)': '{:.2f}',
                        'Carnot COP': '{:.2f}',
                        'Exergy Efficiency (%)': '{:.1f}',
                        'Direct Emissions (Tons CO₂)': '{:.3f}',
                        'Indirect Emissions (Tons CO₂)': '{:.3f}',
                        'Total Emissions (Tons CO₂)': '{:.3f}',
                        'CO₂ Reduction (kg per kW)': '{:.2f}'
                    }
                    st.dataframe(df[final_cols].style.format(format_dict), width='stretch', hide_index=True) #type:ignore
                else:
                    final_cols = [
                        'Refrigerant',
                        'Volumetric Heating Capacity (MJ/m³) (fake)',
                        'Displacement of Compressor (m³/hr)',
                        'Condenser Capacity (kW)',
                        'Evaporator Capacity (kW)',
                        'Actual COP',
                        'CO₂ Reduction (KG)',
                        'Carnot COP',
                        'Exergy Efficiency (%)',
                        'Direct Emissions (Tons CO₂)',
                        'Indirect Emissions (Tons CO₂)',
                        'Total Emissions (Tons CO₂)',
                        'CO₂ Reduction (kg per kW)'
                    ]
                    format_dict = {
                        'Volumetric Heating Capacity (MJ/m³) (fake)': '{:.2f}',
                        'Displacement of Compressor (m³/hr)': '{:.2f}',
                        'Condenser Capacity (kW)': '{:.2f}',
                        'Evaporator Capacity (kW)': '{:.2f}',
                        'Actual COP': '{:.2f}',
                        'CO₂ Reduction (KG)': '{:.2f}',
                        'Carnot COP': '{:.2f}',
                        'Exergy Efficiency (%)': '{:.1f}',
                        'Direct Emissions (Tons CO₂)': '{:.3f}',
                        'Indirect Emissions (Tons CO₂)': '{:.3f}',
                        'Total Emissions (Tons CO₂)': '{:.3f}',
                        'CO₂ Reduction (kg per kW)': '{:.2f}'
                    }
                    df_display = df.rename(columns={'TOPSIS Score': 'Volumetric Heating Capacity (MJ/m³) (fake)'})
                    st.dataframe(df_display[final_cols].style.format(format_dict), width='stretch', hide_index=True) #type:ignore
                
                st.header('📊 Performance Graphs')
                
                for i, row in df.iterrows(): 
                    ref = row['Refrigerant']
                    if ref in plotting_data:
                        d = plotting_data[ref]
                        dome, cycle = d['dome'], d['cycle']
                        
                        with st.container(border=True):
                            st.subheader(f"{ref} - Performance Curves")
                            c1, c2 = st.columns(2)
                            
                            with c1:
                                st.markdown("**Temperature vs Entropy**")
                                fig_ts = go.Figure()
                                fig_ts.add_trace(go.Scatter(x=np.concatenate([dome['s_liq'], dome['s_vap'][::-1]]), y=np.concatenate([dome['T'], dome['T'][::-1]]), mode='lines', name='Saturation', line=dict(color='gray', width=1)))
                                if fixed and 'states' in cycle:
                                    fig_ts.add_trace(go.Scatter(x=cycle['s'], y=cycle['T'], mode='lines', name='Cycle', line=dict(color='blue', width=2)))
                                    st_pts = cycle['states']
                                    fig_ts.add_trace(go.Scatter(x=st_pts['s'], y=st_pts['T'], mode='markers+text', name='States',
                                        text=['1','2','3','4'], textposition='top right',
                                        marker=dict(color='blue', size=8), showlegend=False))
                                else:
                                    fig_ts.add_trace(go.Scatter(x=cycle['s'], y=cycle['T'], mode='lines+markers+text', name='Cycle', text=['1','2','3','4',''], textposition="top left", line=dict(color='blue', width=3), marker=dict(color='blue', size=8)))
                                if 'inters' in d and d['inters']['ts']['s']:
                                    it = d['inters']['ts']
                                    fig_ts.add_trace(go.Scatter(x=it['s'], y=it['T'], mode='markers', name='Intersections',
                                        marker=dict(color='red', size=10, symbol='circle'),
                                        text=[f"({s:.2f}, {t:.1f})" for s, t in zip(it['s'], it['T'])],
                                        textposition='top right', textfont=dict(color='red', size=10)))
                                fig_ts.update_layout(xaxis_title="Entropy (kJ/kg·K)", yaxis_title="Temperature (°C)", height=400, margin=dict(l=20, r=20, t=20, b=20))
                                st.plotly_chart(fig_ts, width='stretch')

                            with c2:
                                st.markdown("**Pressure vs Enthalpy**")
                                fig_ph = go.Figure()
                                fig_ph.add_trace(go.Scatter(x=np.concatenate([dome['h_liq'], dome['h_vap'][::-1]]), y=np.concatenate([dome['P'], dome['P'][::-1]]), mode='lines', name='Saturation', line=dict(color='gray', width=1)))
                                if fixed and 'states' in cycle:
                                    fig_ph.add_trace(go.Scatter(x=cycle['h'], y=cycle['P'], mode='lines', name='Cycle', line=dict(color='purple', width=2)))
                                    st_pts = cycle['states']
                                    fig_ph.add_trace(go.Scatter(x=st_pts['h'], y=st_pts['P'], mode='markers+text', name='States',
                                        text=['1','2','3','4'], textposition='top right',
                                        marker=dict(color='purple', size=8), showlegend=False))
                                else:
                                    fig_ph.add_trace(go.Scatter(x=cycle['h'], y=cycle['P'], mode='lines+markers+text', name='Cycle', text=['1','2','3','4',''], textposition="top left", line=dict(color='purple', width=3), marker=dict(color='purple', size=8)))
                                if 'inters' in d and d['inters']['ph']['h']:
                                    ip = d['inters']['ph']
                                    fig_ph.add_trace(go.Scatter(x=ip['h'], y=ip['P'], mode='markers', name='Dome crossings',
                                        marker=dict(color='red', size=10, symbol='circle'),
                                        text=[f"({h:.2f}, {p:.2f})" for h, p in zip(ip['h'], ip['P'])],
                                        textposition='top right', textfont=dict(color='red', size=10)))
                                fig_ph.update_layout(xaxis_title="Enthalpy (kJ/kg)", yaxis_title="Pressure (bar)", yaxis_type='log' if upgraded else 'linear', height=400, margin=dict(l=20, r=20, t=20, b=20))
                                st.plotly_chart(fig_ph, width='stretch')
    
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