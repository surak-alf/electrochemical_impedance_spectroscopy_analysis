import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

def create_directories():
    """Create necessary directories for results."""
    os.makedirs('results/nyquist_plots', exist_ok=True)
    os.makedirs('results/bode_plots', exist_ok=True)
    os.makedirs('results/analysis_results', exist_ok=True)
    os.makedirs('data', exist_ok=True)

def plot_nyquist(df, plot_settings, save_path=None):
    """Plot Nyquist plot for all scenarios."""
    plt.figure(figsize=plot_settings['figsize'])
    
    for scenario in df['scenario'].unique():
        scenario_data = df[df['scenario'] == scenario]
        color = plot_settings['colors'].get(scenario, 'black')
        marker = plot_settings['markers'].get(scenario, 'o')
        
        plt.plot(
            scenario_data['Z_real'], 
            -scenario_data['Z_imag'], 
            marker=marker, 
            markersize=6, 
            label=scenario.replace('_', ' ').title(),
            color=color,
            linewidth=2,
            alpha=0.8
        )
    
    plt.xlabel('Z\' (Real Impedance) / Ω', fontsize=12)
    plt.ylabel('-Z\'\' (Imaginary Impedance) / Ω', fontsize=12)
    plt.title('EIS Analysis: Nyquist Plot Comparison', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=10)
    plt.axis('equal')
    
    if save_path:
        plt.savefig(save_path, dpi=plot_settings['dpi'], bbox_inches='tight')
        print(f"Nyquist plot saved to {save_path}")
    
    plt.show()

def plot_bode(df, plot_settings, save_path=None):
    """Plot Bode plot (magnitude and phase)."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    for scenario in df['scenario'].unique():
        scenario_data = df[df['scenario'] == scenario]
        color = plot_settings['colors'].get(scenario, 'black')
        
        ax1.semilogx(
            scenario_data['frequency'], 
            scenario_data['|Z|'], 
            'o-', 
            markersize=3, 
            label=scenario.replace('_', ' ').title(),
            color=color,
            linewidth=2
        )
        
        ax2.semilogx(
            scenario_data['frequency'], 
            scenario_data['phase_angle'], 
            'o-', 
            markersize=3, 
            label=scenario.replace('_', ' ').title(),
            color=color,
            linewidth=2
        )
    
    ax1.set_ylabel('|Z| (Ω)', fontsize=12)
    ax1.set_title('Bode Plot - Magnitude', fontsize=14)
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=10)
    
    ax2.set_xlabel('Frequency (Hz)', fontsize=12)
    ax2.set_ylabel('Phase (degrees)', fontsize=12)
    ax2.set_title('Bode Plot - Phase', fontsize=14)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=plot_settings['dpi'], bbox_inches='tight')
        print(f"Bode plot saved to {save_path}")
    
    plt.show()

def plot_individual_comparisons(df, baseline_data, plot_settings):
    """Create individual comparison plots for each degradation scenario."""
    for scenario in df['scenario'].unique():
        if scenario == 'baseline':
            continue
            
        plt.figure(figsize=plot_settings['figsize'])
        
        # Plot baseline
        plt.plot(
            baseline_data['Z_real'], 
            -baseline_data['Z_imag'], 
            'o-', 
            markersize=4, 
            label='Baseline (Healthy Cell)', 
            color=plot_settings['colors']['baseline'],
            linewidth=2
        )
        
        # Plot degradation scenario
        scenario_data = df[df['scenario'] == scenario]
        plt.plot(
            scenario_data['Z_real'], 
            -scenario_data['Z_imag'], 
            's-', 
            markersize=4, 
            label=scenario.replace('_', ' ').title(),
            color=plot_settings['colors'][scenario],
            linewidth=2
        )
        
        plt.xlabel('Z\' (Real Impedance) / Ω', fontsize=12)
        plt.ylabel('-Z\'\' (Imaginary Impedance) / Ω', fontsize=12)
        plt.title(f'Nyquist Plot: Baseline vs {scenario.replace("_", " ").title()}', fontsize=14)
        plt.grid(True, alpha=0.3)
        plt.legend(fontsize=10)
        plt.axis('equal')
        
        save_path = f'results/nyquist_plots/baseline_vs_{scenario}.png'
        plt.savefig(save_path, dpi=plot_settings['dpi'], bbox_inches='tight')
        print(f"Comparison plot saved to {save_path}")
        plt.close()