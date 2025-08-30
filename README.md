# Electrochemical Impedance Spectroscopy Analysis of Electrolyzer Degradation

## 📖 Project Overview

This project implements a computational framework for generating and analyzing synthetic Electrochemical Impedance Spectroscopy (EIS) data to simulate and diagnose degradation mechanisms in proton exchange membrane (PEM) electrolyzers. The system produces realistic Nyquist and Bode plots that visually distinguish between different degradation modes, enabling better understanding of EIS interpretation for electrolyzer health monitoring.

## 🎯 Key Objectives

- **Synthetic Data Generation**: Create realistic EIS spectra mimicking PEM electrolyzer behavior
- **Degradation Simulation**: Model three primary degradation mechanisms with distinct impedance signatures
- **Visualization**: Generate clear Nyquist and Bode plots for pattern recognition
- **Quantitative Analysis**: Extract circuit parameters to quantify degradation severity
- **Educational Tool**: Provide a framework for learning EIS interpretation principles

## ⚙️ Degradation Mechanisms Modeled

1. **Increased Ohmic Resistance** (R₀: 0.1 Ω → 0.5 Ω)
   - Membrane contamination or dehydration
   - Contact resistance increases
   - *Visual signature: Rightward shift of entire curve*

2. **Increased Charge Transfer Resistance** (R_ct: 0.5 Ω → 2.0 Ω)
   - Catalyst degradation or poisoning
   - Electrode surface passivation
   - *Visual signature: Semicircle diameter expansion*

3. **Mass Transfer Limitations** (σ: 5.0 Ω·s⁻⁰·⁵)
   - Gas bubble accumulation
   - Diffusion limitations
   - *Visual signature: 45° low-frequency diffusion tail*

## 📊 Key Results Summary

| Scenario | R_ohmic (Ω) | R_ct (Ω) | Total R (Ω) | % Increase |
|----------|-------------|----------|-------------|------------|
| **Baseline** | 0.164 | 0.436 | 0.600 | - |
| **Ohmic** | 0.564 (+244%) | 0.436 | 1.000 | +67% |
| **Charge Transfer** | 0.138 | 1.961 (+350%) | 2.100 | +250% |
| **Mass Transfer** | 0.146 | 6.762 | 6.908 | +1051% |

## 🗂️ Project Structure

```
eis_analysis_project/
│
├── main.py                 # Main execution script
├── config.py              # Configuration parameters
├── requirements.txt       # Python dependencies
├── Report       # Pdf document detailing about the project
│
├── src/                   # Source code
│   ├── __init__.py
│   ├── data_generation.py # Synthetic data generation
│   ├── equivalent_circuit.py # Circuit model implementations
│   ├── visualization.py   # Plotting functions
│   └── analysis.py        # Data analysis routines
│
├── data/                  # Generated data
│   └── synthetic_eis_data.csv
│
└── results/               # Output files
    ├── nyquist_plots/
    │   ├── all_scenarios_comparison.png
    │   ├── baseline_vs_increased_ohmic.png
    │   ├── baseline_vs_increased_ct.png
    │   └── baseline_vs_mass_transfer.png
    ├── bode_plots/
    │   └── bode_plot_comparison.png
    └── analysis_results/
        └── circuit_parameters.csv
```

## 🚀 Installation & Usage

### Prerequisites
- Python 3.8+
- pip package manager

### Installation
```bash
# Clone or download the project
git clone <https://github.com/surak-alf/electrochemical_impedance_spectroscopy_analysis>
cd eis_analysis_project

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Project
```bash
# Execute the complete analysis pipeline
python main.py

# Expected output:
# - Synthetic EIS data generation
# - Nyquist and Bode plot creation
# - Quantitative analysis report
# - CSV files with results
```

### Output Files
After successful execution, the following files will be generated:
- `data/synthetic_eis_data.csv`: All generated impedance data
- `results/nyquist_plots/`: Comparative Nyquist diagrams
- `results/bode_plots/`: Frequency response plots
- `results/analysis_results/circuit_parameters.csv`: Extracted circuit parameters

## 🧪 Methodology

### Equivalent Circuit Models
- **Baseline**: R₀ + (R_ct || CPE) circuit
- **Mass Transfer**: R₀ + (R_ct || CPE) + Warburg element
- **CPE Parameters**: Q = 1e-3 S·sⁿ, n = 0.9 (accounting for surface heterogeneity)

### Frequency Range
- 0.1 Hz to 10 kHz (100 points, logarithmically spaced)
- Covers complete electrochemical response spectrum

### Analysis Approach
1. **Visual Inspection**: Pattern recognition in Nyquist/Bode plots
2. **Parameter Extraction**: 
   - R_ohmic from high-frequency intercept (>1 kHz)
   - R_ct from semicircle diameter
   - Warburg coefficient from low-frequency slope
3. **Comparative Assessment**: Quantitative degradation severity analysis

## 📈 Key Findings

1. **Ohmic Degradation**: Pure rightward shift (+244% R_ohmic), unaffected electrochemical kinetics
2. **Charge Transfer Degradation**: Radial expansion (+350% R_ct), specific to electrode processes
3. **Mass Transfer Limitations**: Severe impact (+1051% total R), diffusion-controlled behavior
4. **Frequency Separation**: Clear mechanistic discrimination through frequency-domain analysis

## 🎓 Educational Value

This project serves as an excellent resource for:
- Learning EIS principles and equivalent circuit modeling
- Understanding Nyquist plot interpretation for fuel cells/electrolyzers
- Recognizing visual patterns associated with different degradation mechanisms
- Developing skills in electrochemical diagnostics

## 🔧 Customization

Parameters can be easily modified in `config.py`:
- Circuit parameters (R_ohmic, R_ct, CPE values)
- Degradation severity factors
- Frequency range and resolution
- Visualization settings

## 👥 Contributing

Contributions to enhance this project are welcome:
- Additional equivalent circuit models
- Experimental data validation
- Machine learning integration for pattern recognition
- GUI interface for educational use

**Note**: This project uses synthetic data for educational purposes. For real-world applications, it must be validate with experimental data and consider additional factors like temperature effects, aging, and measurement artifacts.