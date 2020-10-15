# Working with TDBX for CALPHAD Uncertainty Quantification (UQ)
Developed by

<a href="https://www.questek.com" target="_blank">
  <img alt="QuesTek Innovations LLC" src="https://imgur.com/Zy3AdNP.jpg" width=300/>
</a>
<br><br>

Funded by SBIR Award DE-SC0017234 from

<img alt="Department of Energy" src="https://imgur.com/6MPXvkq.png" width=300 />

## About TDBX (`.tdbx`) and `qt-tdbx`
TDBX (`.tdbx`) is a file format based on the commonly used `.tdb` (thermodynamic database) files, enabling UQ features in CALPHAD. The concept of TDBX is straightforward: it attaches UQ traces to the end of the original `.tdb` file as commented lines in a pre-defined format to allow convenient CALPHAD UQ calculations, like this:

```
$ ========= End of .tdb =========
$ 
$ UQ L(BCC_A2,Cr,Ni;0) {"T": [1, 2, 3, ...], "1": [1, 2, 3, ...], ...}
$ UQ L(BCC_A2,Cr,Ni;1) {"T": [1, 2, 3, ...], "1": [1, 2, 3, ...], ...}
$ ...
$ ============= EOF =============
```

TDBX (`.tdbx`) has three major advantages:
* It provides all UQ data (single source of truth) in one file to run CALPHAD UQ calculations.
* It can be used as a regular `.tdb` file, as all UQ data are commented out.
* It is human-interpretable, so users can see what's been UQ assessed.

`qt-tdbx` is QuesTek's proprietary package to cover both the assessment and calculation for CALPHAD UQ:
1. Generate a TDBX (`.tdbx`) file via CALPHAD UQ assessment.
2. Interface with a TDBX (`.tdbx`) file for high-throughput CALPHAD UQ calculations.

This demo repo contains a simplified version of the second part of the full-version of `qt-tdbx`.

## Installation
Before you decide to try this public demo package, please make sure that you have
1. Active Thermo-Calc license. (This package is tested on version 2019B.)
2. Unix environment. (This package is tested on Linux.)

To try this demo version, download this public repo:
```bash
git clone https://github.com/questek/qt-tdbx-demo.git
```

Two options to use the package:
1. Run a Jupyter Notebook within the package folder and directly `import qt_tdbx`.
2. `pip install PATH_TO_THIS_REPO` so you can `import qt_tdbx` anywhere.

## Usage

See the Jupyter Notebook file: Example.ipynb

## Citation

If you use this package, please consider citing:

* Lin, Y., Saboo, A., Frey, R. et al. CALPHAD Uncertainty Quantification and TDBX. JOM (2020). https://doi.org/10.1007/s11837-020-04405-z

## License
This project is licensed under the Apache 2.0 License, see the [LICENSE](https://github.com/questek/qt-tdbx-demo/blob/master/LICENSE) file for details.
