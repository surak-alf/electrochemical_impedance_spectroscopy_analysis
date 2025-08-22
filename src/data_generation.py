import numpy as np
import pandas as pd
import os

def calculate_impedance_RRCPE(frequencies, R_ohmic, R_ct, Q, n):
    """
    Calculate impedance for a R + (R||CPE) equivalent circuit.
    """
    omega = 2 * np.pi * frequencies
    Z_complex = np.zeros_like(frequencies, dtype=complex)
    
    for i, w in enumerate(omega):
        # CPE impedance
        Z_CPE = 1 / (Q * (1j * w) ** n)
        # Parallel combination of R_ct and CPE
        Z_parallel = 1 / (1/R_ct + 1/Z_CPE)
        # Total impedance (series with R_ohmic)
        Z_complex[i] = R_ohmic + Z_parallel
        
    return Z_complex

def calculate_impedance_with_warburg(frequencies, R_ohmic, R_ct, C_dl, sigma):
    """
    Calculate impedance for a circuit with Warburg element.
    """
    omega = 2 * np.pi * frequencies
    Z_complex = np.zeros_like(frequencies, dtype=complex)
    
    for i, w in enumerate(omega):
        # Parallel combination of R_ct and C_dl
        Z_parallel = 1 / (1/R_ct + 1j * w * C_dl)
        # Warburg impedance
        Z_warburg = sigma * (1 - 1j) / np.sqrt(w)
        # Total impedance
        Z_complex[i] = R_ohmic + Z_parallel + Z_warburg
        
    return Z_complex

def generate_scenario_data(frequencies, scenario_name, params):
    """Generate EIS data for a specific scenario."""
    if scenario_name == 'mass_transfer':
        Z = calculate_impedance_with_warburg(
            frequencies, 
            params['R_ohmic'], 
            params['R_ct'], 
            params['C_dl'], 
            params['sigma']
        )
    else:
        Z = calculate_impedance_RRCPE(
            frequencies, 
            params['R_ohmic'], 
            params['R_ct'], 
            params['Q'], 
            params['n']
        )
    
    return {
        'frequency': frequencies,
        'Z_real': Z.real,
        'Z_imag': Z.imag,
        'scenario': scenario_name,
        '|Z|': np.sqrt(Z.real**2 + Z.imag**2),
        'phase_angle': np.angle(Z, deg=True)
    }

def generate_all_data(frequencies, baseline_params, degradation_scenarios):
    """Generate all EIS data for baseline and degradation scenarios."""
    all_data = []
    
    # Generate baseline data
    baseline_df = pd.DataFrame(generate_scenario_data(
        frequencies, 'baseline', baseline_params
    ))
    all_data.append(baseline_df)
    
    # Generate degradation scenario data
    for scenario_name, params in degradation_scenarios.items():
        scenario_df = pd.DataFrame(generate_scenario_data(
            frequencies, scenario_name, params
        ))
        all_data.append(scenario_df)
    
    return pd.concat(all_data, ignore_index=True)

def save_data(data, filename):
    """Save data to CSV file."""
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    data.to_csv(filename, index=False)
    print(f"Data saved to {filename}")
    return data