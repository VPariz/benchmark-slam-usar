#!/usr/bin/env python3
"""
analisar_benchmark.py - Utilitário de Visualização de Métricas do Artigo ISMCR 2026.
Carrega os dados experimentais de sensoriamento 3D e SLAM em robôs USAR
(TurtleBot3 e Clearpath Jackal) e exibe tabelas comparativas consolidadas.
"""

import os
import sys

def exibir_tabela_resumo():
    print("=" * 78)
    print("   BENCHMARK ISMCR 2026: AVALIAÇÃO DE SENSORES 3D E SLAM EM ROBÔS USAR")
    print("   Artigo aceito na Springer Lecture Notes in Computer Science (LNCS)")
    print("   Laboratório de Robótica RoboIME — Instituto Militar de Engenharia (IME)")
    print("=" * 78)
    print()
    print("1. LATÊNCIA E TAXA DE ATUALIZAÇÃO DOS SENSORES:")
    print("-" * 78)
    print(f"{'Sensor / Solução':<30} | {'Frequência (Hz)':<16} | {'Latência Média (ms)':<18}")
    print("-" * 78)
    print(f"{'Intel RealSense D435 (Estéreo)':<30} | {'30.0 Hz':<16} | {'33.3 ms':<18}")
    print(f"{'LiDAR Ouster OS1 (3D)':<30} | {'10.0 / 20.0 Hz':<16} | {'50.0 ms':<18}")
    print(f"{'Robotis LDS-02 (2D)':<30} | {'5.0 Hz':<16} | {'200.0 ms':<18}")
    print(f"{'C920e + MiDaS (Profundidade IA)':<30} | {'8.5 Hz (GPU)':<16} | {'117.6 ms':<18}")
    print(f"{'C920e + MapAnything (IA)':<30} | {'4.2 Hz (GPU)':<16} | {'238.1 ms':<18}")
    print("-" * 78)
    print()
    print("2. CONSUMO COMPUTACIONAL DOS ALGORITMOS DE SLAM (Embarcado):")
    print("-" * 78)
    print(f"{'Algoritmo SLAM':<25} | {'Uso de CPU Médio':<18} | {'Consumo de RAM':<18} | {'Estabilidade':<12}")
    print("-" * 78)
    print(f"{'Google Cartographer 2D':<25} | {'38% (Cortex-A72)':<18} | {'420 MB':<18} | {'Alta':<12}")
    print(f"{'Gmapping (Rao-Blackwell)':<25} | {'28% (Cortex-A72)':<18} | {'290 MB':<18} | {'Média/Alta':<12}")
    print(f"{'ORB-SLAM3 (Visual-Inercial)':<25} | {'65% (Cortex-A72)':<18} | {'780 MB':<18} | {'Média':<12}")
    print("-" * 78)
    print("\nPara aprofundamento metodológico e equações, consulte o PDF no repositório:")
    print(" -> Paper_ISMCR2026_Springer_LNCS.pdf\n")

if __name__ == '__main__':
    exibir_tabela_resumo()
