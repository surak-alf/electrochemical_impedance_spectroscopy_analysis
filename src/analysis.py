import pandas as pd
import numpy as np
import os

def calculate_circuit_parameters(df):
    """Calculate estimated circuit parameters from EIS data."""
    results = {}
    
    for scenario in df['scenario'].unique():
        scenario_data = df[df['scenario'] == scenario]
        
        # Estimate R_ohmic from high-frequency intercept
        high_freq_data = scenario_data[scenario_data['frequency'] > 1000]  # > 1kHz
        if len(high_freq_data) > 0:
            R_ohmic = high_freq_data['Z_real'].mean()
        else:
            R_ohmic = scenario_data['Z_real'].min()
        
        # Estimate R_ct from low-frequency data
        low_freq_data = scenario_data[scenario_data['frequency'] < 1]  # < 1Hz
        if len(low_freq_data) > 0:
            R_total = low_freq_data['Z_real'].max()
            R_ct = R_total - R_ohmic
        else:
            R_total = scenario_data['Z_real'].max()
            R_ct = R_total - R_ohmic
        
        results[scenario] = {
            'R_ohmic': R_ohmic,
            'R_ct': R_ct,
            'R_total': R_total
        }
    
    return results

def generate_report(analysis_results, degradation_scenarios):
    """Generate a summary report of the analysis."""
    print("=" * 60)
    print("EIS ANALYSIS REPORT")
    print("=" * 60)
    
    baseline = analysis_results['baseline']
    print(f"\nBASELINE (Healthy Cell):")
    print(f"  Ohmic Resistance (R_ohmic): {baseline['R_ohmic']:.3f} Ω")
    print(f"  Charge Transfer Resistance (R_ct): {baseline['R_ct']:.3f} Ω")
    print(f"  Total Resistance: {baseline['R_total']:.3f} Ω")
    
    print("\nDEGRADATION ANALYSIS:")
    for scenario, params in analysis_results.items():
        if scenario == 'baseline':
            continue
        
        degradation = degradation_scenarios.get(scenario, {})
        print(f"\n{scenario.replace('_', ' ').upper()}:")
        print(f"  Description: {degradation.get('description', 'N/A')}")
        print(f"  R_ohmic: {params['R_ohmic']:.3f} Ω (Change: {params['R_ohmic'] - baseline['R_ohmic']:+.3f} Ω)")
        print(f"  R_ct: {params['R_ct']:.3f} Ω (Change: {params['R_ct'] - baseline['R_ct']:+.3f} Ω)")
        print(f"  Total Resistance: {params['R_total']:.3f} Ω (Change: {params['R_total'] - baseline['R_total']:+.3f} Ω)")
    
    print("\n" + "=" * 60)

def save_analysis_results(analysis_results, filename):
    """Save analysis results to CSV."""
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    results_df = pd.DataFrame.from_dict(analysis_results, orient='index')
    results_df.to_csv(filename)
    print(f"Analysis results saved to {filename}")