# Configuration parameters for EIS simulation

# Frequency range (we'll define this as a function since we can't use numpy here directly)
def get_frequencies():
    import numpy as np
    return np.logspace(-1, 4, 100)  # 0.1 Hz to 10 kHz

# Baseline parameters (healthy cell)
BASELINE_PARAMS = {
    'R_ohmic': 0.1,    # Ω
    'R_ct': 0.5,       # Ω
    'Q': 1e-3,         # S·s^n
    'n': 0.9,          # CPE exponent
    'scenario': 'baseline'
}

# Degradation scenarios
DEGRADATION_SCENARIOS = {
    'increased_ohmic': {
        'R_ohmic': 0.5,    # Increased from 0.1 Ω
        'R_ct': 0.5,       # Same as baseline
        'Q': 1e-3,         # Same as baseline
        'n': 0.9,          # Same as baseline
        'description': 'Membrane contamination or contact issues'
    },
    'increased_ct': {
        'R_ohmic': 0.1,    # Same as baseline
        'R_ct': 2.0,       # Increased from 0.5 Ω
        'Q': 1e-3,         # Same as baseline
        'n': 0.9,          # Same as baseline
        'description': 'Catalyst degradation'
    },
    'mass_transfer': {
        'R_ohmic': 0.1,    # Same as baseline
        'R_ct': 0.5,       # Same as baseline
        'C_dl': 1e-3,      # F
        'sigma': 5.0,      # Warburg coefficient
        'description': 'Mass transfer limitations'
    }
}

# Plot settings
PLOT_SETTINGS = {
    'figsize': (10, 8),
    'dpi': 300,
    'colors': {
        'baseline': 'blue',
        'increased_ohmic': 'red',
        'increased_ct': 'green',
        'mass_transfer': 'purple'
    },
    'markers': {
        'baseline': 'o',
        'increased_ohmic': 's',
        'increased_ct': '^',
        'mass_transfer': 'd'
    }
}