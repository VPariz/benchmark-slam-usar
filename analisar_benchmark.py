#!/usr/bin/env python3
"""
analisar_benchmark.py - ISMCR 2026 Benchmark Metrics CLI Viewer.
Loads and displays empirical 3D sensing & SLAM benchmark tables for USAR robots
(TurtleBot3 and Clearpath Jackal) published in Springer LNCS.
"""

import sys
import argparse

def display_summary_en():
    print("=" * 80)
    print("   ISMCR 2026 BENCHMARK: 3D SENSING & SLAM EVALUATION FOR USAR ROBOTICS")
    print("   Published in Springer Lecture Notes in Computer Science (LNCS)")
    print("   RoboIME Robotics Laboratory — Instituto Militar de Engenharia (IME)")
    print("=" * 80)
    print()
    print("1. SENSOR REFRESH RATE AND LATENCY CHARACTERISTICS:")
    print("-" * 80)
    print(f"{'Sensor / Solution':<32} | {'Frequency (Hz)':<16} | {'Mean Latency (ms)':<18}")
    print("-" * 80)
    print(f"{'Intel RealSense D435 (Stereo)':<32} | {'30.0 Hz':<16} | {'33.3 ms':<18}")
    print(f"{'Ouster OS1 LiDAR (3D)':<32} | {'10.0 / 20.0 Hz':<16} | {'50.0 ms':<18}")
    print(f"{'Robotis LDS-02 (2D)':<32} | {'5.0 Hz':<16} | {'200.0 ms':<18}")
    print(f"{'C920e + MiDaS (Monocular AI)':<32} | {'8.5 Hz (GPU)':<16} | {'117.6 ms':<18}")
    print(f"{'C920e + MapAnything (AI)':<32} | {'4.2 Hz (GPU)':<16} | {'238.1 ms':<18}")
    print("-" * 80)
    print()
    print("2. COMPUTATIONAL FOOTPRINT OF EMBEDDED SLAM PIPELINES:")
    print("-" * 80)
    print(f"{'SLAM Algorithm':<26} | {'Mean CPU Load':<18} | {'RAM Footprint':<18} | {'Stability':<12}")
    print("-" * 80)
    print(f"{'Google Cartographer 2D':<26} | {'38% (Cortex-A72)':<18} | {'420 MB':<18} | {'High':<12}")
    print(f"{'Gmapping (Rao-Blackwell)':<26} | {'28% (Cortex-A72)':<18} | {'290 MB':<18} | {'Medium/High':<12}")
    print(f"{'ORB-SLAM3 (Visual-Inertial)':<26} | {'65% (Cortex-A72)':<18} | {'780 MB':<18} | {'Medium':<12}")
    print("-" * 80)
    print("\nFor full methodology, benchmark trials, and formulas, inspect:")
    print(" -> Paper_ISMCR2026_Springer_LNCS.pdf\n")

def display_summary_pt():
    print("=" * 80)
    print("   BENCHMARK ISMCR 2026: AVALIAÇÃO DE SENSORES 3D E SLAM EM ROBÔS USAR")
    print("   Artigo aceito na Springer Lecture Notes in Computer Science (LNCS)")
    print("   Laboratório de Robótica RoboIME — Instituto Militar de Engenharia (IME)")
    print("=" * 80)
    print()
    print("1. LATÊNCIA E TAXA DE ATUALIZAÇÃO DOS SENSORES:")
    print("-" * 80)
    print(f"{'Sensor / Solução':<30} | {'Frequência (Hz)':<16} | {'Latência Média (ms)':<18}")
    print("-" * 80)
    print(f"{'Intel RealSense D435 (Estéreo)':<30} | {'30.0 Hz':<16} | {'33.3 ms':<18}")
    print(f"{'LiDAR Ouster OS1 (3D)':<30} | {'10.0 / 20.0 Hz':<16} | {'50.0 ms':<18}")
    print(f"{'Robotis LDS-02 (2D)':<30} | {'5.0 Hz':<16} | {'200.0 ms':<18}")
    print(f"{'C920e + MiDaS (Profundidade IA)':<30} | {'8.5 Hz (GPU)':<16} | {'117.6 ms':<18}")
    print(f"{'C920e + MapAnything (IA)':<30} | {'4.2 Hz (GPU)':<16} | {'238.1 ms':<18}")
    print("-" * 80)
    print()
    print("2. CONSUMO COMPUTACIONAL DOS ALGORITMOS DE SLAM (Embarcado):")
    print("-" * 80)
    print(f"{'Algoritmo SLAM':<25} | {'Uso de CPU Médio':<18} | {'Consumo de RAM':<18} | {'Estabilidade':<12}")
    print("-" * 80)
    print(f"{'Google Cartographer 2D':<25} | {'38% (Cortex-A72)':<18} | {'420 MB':<18} | {'Alta':<12}")
    print(f"{'Gmapping (Rao-Blackwell)':<25} | {'28% (Cortex-A72)':<18} | {'290 MB':<18} | {'Média/Alta':<12}")
    print(f"{'ORB-SLAM3 (Visual-Inercial)':<25} | {'65% (Cortex-A72)':<18} | {'780 MB':<18} | {'Média':<12}")
    print("-" * 80)
    print("\nPara aprofundamento metodológico e equações, consulte o PDF no repositório:")
    print(" -> Paper_ISMCR2026_Springer_LNCS.pdf\n")

def main():
    parser = argparse.ArgumentParser(description="ISMCR 2026 SLAM & 3D Sensing Benchmark Metrics Viewer")
    parser.add_argument("--pt", action="store_true", help="Display output in Portuguese")
    args = parser.parse_args()

    if args.pt:
        display_summary_pt()
    else:
        display_summary_en()

if __name__ == '__main__':
    main()
