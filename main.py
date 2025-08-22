#!/usr/bin/env python3
"""
Main script for EIS Analysis Project
Run the entire project with: python main.py
"""

import numpy as np
import pandas as pd
from src.data_generation import generate_all_data, save_data
from src.visualization import create_directories, plot_nyquist, plot_bode, plot_individual_comparisons
from src.analysis import calculate_circuit_parameters, generate_report, save_analysis_results

# Import configuration
from config import get_frequencies, BASELINE_PARAMS, DEGRADATION_SCENARIOS, PLOT_SETTINGS

def main():
    """Main function to run the entire EIS analysis project."""
    print("Starting EIS Analysis Project...")
    print("=" * 50)
    
    # Get frequencies
    FREQUENCIES = get_frequencies()
    
    # Create necessary directories
    create_directories()
    
    # Step 1: Generate synthetic EIS data
    print("\n1. Generating synthetic EIS data...")
    all_data = generate_all_data(FREQUENCIES, BASELINE_PARAMS, DEGRADATION_SCENARIOS)
    save_data(all_data, 'data/synthetic_eis_data.csv')
    
    # Extract baseline data for comparisons
    baseline_data = all_data[all_data['scenario'] == 'baseline']
    
    # Step 2: Create visualizations
    print("\n2. Creating visualizations...")
    
    # Combined Nyquist plot
    plot_nyquist(all_data, PLOT_SETTINGS, 'results/nyquist_plots/all_scenarios_comparison.png')
    
    # Bode plot
    plot_bode(all_data, PLOT_SETTINGS, 'results/bode_plots/bode_plot_comparison.png')
    
    # Individual comparison plots
    plot_individual_comparisons(all_data, baseline_data, PLOT_SETTINGS)
    
    # Step 3: Perform analysis
    print("\n3. Performing analysis...")
    analysis_results = calculate_circuit_parameters(all_data)
    generate_report(analysis_results, DEGRADATION_SCENARIOS)
    save_analysis_results(analysis_results, 'results/analysis_results/circuit_parameters.csv')
    
    # Step 4: Summary
    print("\n4. Project summary:")
    print(f"   - Generated {len(all_data)} data points")
    print(f"   - Analyzed {all_data['scenario'].nunique()} scenarios")
    print(f"   - Created visualizations in results/ directory")
    print(f"   - Saved analysis results")
    
    print("\nProject completed successfully!")
    print("=" * 50)

if __name__ == "__main__":
    main()