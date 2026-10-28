# USAR Ground Robotics & SLAM Sensing Benchmark

[![Benchmark CI](https://github.com/VPariz/benchmark-slam-usar/actions/workflows/ci.yml/badge.svg)](https://github.com/VPariz/benchmark-slam-usar/actions/workflows/ci.yml)
[![Paper](https://img.shields.io/badge/Paper-Springer_LNCS-blue?style=flat-square&logo=springer&logoColor=white)](https://link.springer.com/)
[![ROS 2](https://img.shields.io/badge/ROS_2-Humble%20%7C%20Galactic-22314E?style=flat-square&logo=ros&logoColor=white)](https://ros.org/)
[![Linux](https://img.shields.io/badge/Linux-Debian%20%7C%20Ubuntu-A81D33?style=flat-square&logo=debian&logoColor=white)](https://debian.org/)
[![Platforms](https://img.shields.io/badge/Robots-TurtleBot3%20%7C%20Jackal-FF6F00?style=flat-square)](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

Experimental benchmark data, sensory logs, and documentation for the research paper:  
**"Comparative Evaluation of Low-Cost Sensing and Mapping Solutions for Teleoperated Ground Robots in Urban Search and Rescue (USAR)"**  
*Presented at the 27th International Symposium on Measurement and Control in Robotics (ISMCR 2026).*  
*Published in Springer Lecture Notes in Computer Science (LNCS).*

---

## 👥 Authors & Affiliation

* Fernando P. Machado
* Kawãn F. S. Mendes
* **João Victor T. Pariz**
* Pablo C. B. Amorim
* Luiz Eduardo M. Alves
* Marlon M. López-Flores
* Paulo Fernando Ferreira Rosa

**RoboIME Robotics Laboratory — Instituto Militar de Engenharia (IME)**, Rio de Janeiro, Brazil.

---

## 🎯 Research Overview

In Urban Search and Rescue (USAR) missions, mobile robots operate in unstructured, GPS-denied environments with dense particulate matter, debris, and variable illumination.

This repository compiles empirical benchmark data gathered at IME evaluating low-cost perception sensors and Simultaneous Localization and Mapping (SLAM) algorithms deployed on autonomous and teleoperated unmanned ground vehicles (**TurtleBot3** and **Clearpath Jackal**):

1. **Depth Sensing Modalities:**
   - Stereo RGB-D: **Intel RealSense D435**
   - Monocular RGB: **Logitech C920e** paired with monocular depth estimation neural networks (**MiDaS** and **MapAnything**)
2. **LiDAR Systems:**
   - 2D Planar LiDAR: **Robotis LDS-02**
   - 3D Multibeam LiDAR: **Ouster OS1**
3. **SLAM Algorithms Evaluated:**
   - **Google Cartographer** (2D/3D Graph-based SLAM)
   - **Gmapping** (Rao-Blackwellized particle filter)
   - **ORB-SLAM3** (Visual-Inertial monocular and stereo SLAM)

---

## 🔬 Technical Contributions (João Victor Pariz)

* **Hardware Integration & Mechatronics:** Physical assembly, power distribution harness, and mechanical sensor mounting on the TurtleBot3 platform.
* **ROS 2 Driver Stack & Linux Environment:** Configuration of the Debian/Ubuntu real-time environment and parameter tuning for the LDS-02 LiDAR and Intel RealSense D435 ROS 2 nodes.
* **Empirical Trials & Data Acquisition:** Conducted standardized obstacle-course trials in a simulated USAR arena; collected raw sensor logs; measured point-cloud density, runtime latency, and CPU/RAM utilization footprints.

---

## 📂 Repository Structure

```
benchmark-slam-usar/
├── dados_experimentos/          # Raw tabular data collected during empirical trials
│   ├── mapanything_2026-08-07_1306.md
│   ├── midas_2026-08-07_0740.md
│   ├── orbslam3_2026-08-07_1316.md
│   └── realsense_2026-08-07_1322.md
├── analisar_benchmark.py        # Python CLI analyzer to process and display benchmark metrics
├── Dados Artigo.xlsx            # Consolidated quantitative metrics (latency, CPU, memory, point density)
├── Paper_ISMCR2026_Springer_LNCS.pdf # Accepted preprint paper (Springer LNCS)
└── README.md
```

---

## 📊 Quick Start

Run the analytical CLI tool to inspect the benchmark results directly in your terminal:

```bash
python analisar_benchmark.py
```

---

## 📑 Citation

If you use these benchmark datasets or findings in your academic research, please cite:

```bibtex
@inproceedings{machado2026usar,
  title={Comparative Evaluation of Low-Cost Sensing and Mapping Solutions for Teleoperated Ground Robots in Urban Search and Rescue},
  author={Machado, Fernando P. and Mendes, Kaw{\~a}n F. S. and Pariz, Jo{\~a}o Victor T. and Amorim, Pablo C. B. and Alves, Luiz Eduardo M. and L{\'o}pez-Flores, Marlon M. and Rosa, Paulo Fernando Ferreira},
  booktitle={27th International Symposium on Measurement and Control in Robotics (ISMCR 2026)},
  series={Lecture Notes in Computer Science (LNCS)},
  year={2026},
  publisher={Springer}
}
```

---

## 📜 License
The benchmark datasets and documentation in this repository are published for academic and research purposes.
