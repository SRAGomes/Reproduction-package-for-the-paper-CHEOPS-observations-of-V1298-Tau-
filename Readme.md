
# Reproduction package for the paper "CHEOPS observations of V1298 Tau: updated planetary densities and implications on the early evolution of the young system"


This is a basic reproduction package for the paper "CHEOPS observations of V1298 Tau: updated planetary densities and
implications on the early evolution of the young system" 
by [Shivkumar, Gomes, et al (2026)](in revision).


## Software  prerequisites

To run the scripts in this package, the following software has been used:
* OS: macOS Tahoe v26.4.1
* python v3.13.3
* numpy v2.2.3
* matplotlib v3.10.1
* Jupyter core v5.7.2
* Rebound v4.4.6 (https://rebound.hanno-rein.de)



## End-to-End analysis scripts
* The analysis.ipynb script is divided in two sections: 
    * The conservative section, where the forced eccentricities; the NAMD (Normalized angular momentum deficit); and the present resonance state can be calculated. It need the "forced_eccentricity.py" file.
    * The dissipative section, where the contribution from the stellar and planetary contributions; the past and future evolutionary tracks considering a toy model for the radial contraction.
* The forced_eccentricity.py script contains the functions fot the conservative section of the paper, using the Rebound N-body code.



https://github.com/SRAGomes/Reproduction-package-for-the-paper-CHEOPS-observations-of-V1298-Tau-.git