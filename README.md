# Third-Stage Turbine Blade – Reverse Engineering & CAD Reconstruction
Reverse engineering of a third-stage turbine blade using Python-based airfoil coordinate processing and Siemens NX CAD modelling.
**CT-Assisted Geometric Data Acquisition | Python Automation | Siemens NX CAD Modelling**

## 1. Project Overview

This project involved the reverse engineering and three-dimensional CAD reconstruction of a third-stage gas turbine blade, integrating computed tomography (CT) scanning, engineering interpretation, Python-based coordinate processing and Siemens NX modelling.

The project began with the examination and digitisation of a physical turbine blade using CT scanning technology available through the Arab Organization for Industrialization (AOI) in Egypt.

The acquired measurements, together with the interpretation of available geometric information and reference turbine blade profiles studied during EgyptAir maintenance training, provided the basis for reconstructing the component.

Where complete dimensional information was unavailable, engineering judgement and estimated dimensions were used to develop the geometry, particularly for the blade attachment root and other features.

Python was subsequently used to automate the processing of airfoil coordinate data and generate sectional coordinate files for import into Siemens NX, where the final three-dimensional CAD model was constructed.

## 2. Final CAD Model

![Third-Stage Turbine Blade CAD Model](images/04-final-blade-model.png)

*Isometric view of the reconstructed third-stage turbine blade, modelled in Siemens NX.*

## 3. Project Objectives

- Investigate reverse engineering techniques using CT scanning technology.
- Acquire and interpret geometric measurements from a physical turbine blade.
- Reconstruct sectional airfoil geometry using available measurements and engineering interpretation.
- Develop a Python program to automate airfoil coordinate processing.
- Generate coordinate files for five individual airfoil sections.
- Integrate the processed coordinate data into Siemens NX.
- Construct a complete three-dimensional CAD representation of the turbine blade.

## 4. Engineering Methodology

### Stage 1 – CT Scanning and Geometric Data Acquisition

A physical turbine blade was examined using CT scanning technology available through the Arab Organization for Industrialization (AOI), Egypt.

Computed tomography provided a non-destructive method of examining the component and obtaining three-dimensional geometric information.

The objective was to obtain measurements and geometric references that could support the subsequent reconstruction process.

Particular attention was given to:
- External blade geometry.
- Airfoil profile characteristics.
- Blade height and sectional geometry.
- Platform and root configuration.
- Geometric relationships between the different component features.

The acquired information provided a reference for the subsequent dimensional interpretation and CAD reconstruction stages.

### Stage 2 – Geometric Interpretation and Engineering Reconstruction

The acquired measurements were analysed alongside reference turbine blade profiles and engineering information examined during EgyptAir aircraft maintenance training.

Reference material included turbine engine components associated with CFM and General Electric engine families.

The available geometric information was interpreted to establish the overall blade configuration and sectional airfoil profiles.

Where complete dimensional information was unavailable, estimated dimensions and engineering assumptions were introduced to reconstruct features that could not be established directly from the available measurements.

The reconstruction focused on five airfoil sections distributed along the blade height, together with the platform and fir-tree attachment geometry.

**Important:** The resulting model represents an engineering reconstruction based on available measurements and estimated dimensions. It is not presented as a dimensionally certified reproduction of an original production component.

### Stage 3 – Airfoil Coordinate Organisation

The sectional airfoil coordinate information was organised using Microsoft Excel.

The dataset contained:
- X-coordinate values describing the airfoil profile.
- Y-coordinate values for the convex surface.
- Y-coordinate values for the concave surface.
- Z-heights defining the positions of the individual airfoil sections.

Five sectional profiles were established to represent the blade geometry at different heights.

The coordinate information was organised into a structured dataset to facilitate automated processing.

### Stage 4 – Python-Based Coordinate Processing

A Python program was developed using PyCharm to automate the processing of the airfoil coordinate dataset.

The program was designed to:
- Read and parse the organised coordinate data.
- Identify the relevant coordinate values.
- Separate the convex and concave airfoil surfaces.
- Organise the coordinates according to their respective blade sections.
- Generate individual `.dat` files for subsequent import into Siemens NX.

The program generated a total of **10 DAT files**, corresponding to the two airfoil surfaces across five individual sections.

This automation reduced the need for manual coordinate-file preparation and provided a structured workflow for transferring the sectional geometry into the CAD environment.

### Stage 5 – DAT File Generation and Siemens NX Integration

The generated coordinate files were imported into Siemens NX to reconstruct the individual airfoil profiles.

The ten files were organised as follows:

| Airfoil section | Convex surface | Concave surface |
|---|---|---|
| I-I | Section_I-I_CV.dat | Section_I-I_CC.dat |
| II-II | Section_II-II_CV.dat | Section_II-II_CC.dat |
| III-III | Section_III-III_CV.dat | Section_III-III_CC.dat |
| IV-IV | Section_IV-IV_CV.dat | Section_IV-IV_CC.dat |
| V-V | Section_V-V_CV.dat | Section_V-V_CC.dat |

The profiles were positioned at their corresponding Z-heights and used as the basis for reconstructing the three-dimensional blade geometry.

### Stage 6 – Three-Dimensional CAD Reconstruction

Siemens NX was used to integrate the sectional profiles and construct the final three-dimensional model.

The modelling process incorporated:
- Airfoil profile reconstruction.
- Section positioning along the blade height.
- Three-dimensional blade surface construction.
- Platform geometry.
- Fir-tree attachment root.
- Additional geometric features represented in the reconstruction.

The final result was a complete three-dimensional CAD representation of the reconstructed third-stage turbine blade.

## 5. Project Results

The project successfully combined physical component examination, geometric interpretation, computational data processing and CAD reconstruction.

Key outcomes included:

- CT-assisted examination of a physical turbine blade.
- Reconstruction of five sectional airfoil profiles.
- Development of a Python coordinate-processing program.
- Automated generation of 10 airfoil surface coordinate files.
- Integration of the coordinate data into Siemens NX.
- Completion of a three-dimensional turbine blade CAD model incorporating the airfoil, platform and fir-tree root geometry.

## 6. Software and Technologies

| Technology | Application |
|---|---|
| Computed Tomography (CT) | Non-destructive geometric examination and data acquisition |
| Microsoft Excel | Organisation of sectional airfoil coordinate data |
| Python | Coordinate processing and automated DAT file generation |
| PyCharm | Python development environment |
| Siemens NX | Three-dimensional CAD modelling and surface reconstruction |
| Git / GitHub | Source code management and engineering documentation |

## 7. Skills Demonstrated

**Reverse Engineering and Metrology**
- CT-assisted component examination.
- Geometric data interpretation.
- Dimensional assessment.
- Engineering assumptions and reconstruction.

**Aerospace Engineering**
- Gas turbine blade geometry.
- Airfoil sectional profiles.
- Turbine blade platform and root configuration.
- Engineering drawing and reference geometry interpretation.

**CAD Modelling**
- Siemens NX.
- Section-based modelling.
- Airfoil reconstruction.
- Three-dimensional surface construction.

**Programming and Computational Engineering**
- Python programming.
- Coordinate data parsing.
- Data organisation and transformation.
- Automated file generation.
- Integration of programming workflows with CAD software.

## 8. Project Limitations

The reconstructed model is an engineering approximation developed using available CT-derived measurements, reference geometry and estimated dimensions.

It has not been independently verified against the original manufacturer's engineering drawings or certified production specifications.

The project does not claim aerodynamic performance validation, structural integrity verification, manufacturing qualification or dimensional conformity to an original production component.

## 9. Repository Structure

```text
Third-Stage-Turbine-Blade-Reverse-Engineering/
│
├── README.md
│
├── images/
│
├── CAD/
│   ├── 3rdstageturbine.prt
│   └── 3rdstageturbine.step
│
├── Python/
│   ├── airfoil_data_parser.py
│   └── requirements.txt
│
├── Data/
│   ├── input/
│   └── output/
│       └── [10 generated DAT files]
│
└── Documentation/
    ├── modelling-workflow.md
    └── engineering-notes.md
```

## 10. Author and Project Information

**Project:** Third-Stage Turbine Blade Reverse Engineering

**CAD Software:** Siemens NX

**Programming Language:** Python

**Development Environment:** PyCharm

**Data Organisation:** Microsoft Excel

**Geometric Examination:** CT Scanning

**Author:** [Your Name]
