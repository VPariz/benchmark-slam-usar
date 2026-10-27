# Benchmark de SLAM e Sensoriamento para Robôs USAR

Dados experimentais, logs de sensoriamento e documentação do artigo científico:  
**"Comparative Evaluation of Low-Cost Sensing and Mapping Solutions for Teleoperated Ground Robots in Urban Search and Rescue (USAR)"**  
*Apresentado no 27th International Symposium on Measurement and Control in Robotics (ISMCR 2026).*  
*Publicado na Springer Lecture Notes in Computer Science (LNCS).*

[![Springer](https://img.shields.io/badge/Springer-LNCS-blue?style=flat-square&logo=springer&logoColor=white)](https://link.springer.com/)
[![ROS 2](https://img.shields.io/badge/ROS-2-22314E?style=flat-square&logo=ros&logoColor=white)](https://ros.org/)
[![Linux](https://img.shields.io/badge/Linux-Debian-A81D33?style=flat-square&logo=debian&logoColor=white)](https://debian.org/)
[![Robôs](https://img.shields.io/badge/Rob%C3%B4s-TurtleBot3%20%7C%20Jackal-FF6F00?style=flat-square)](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/)

---

## Autores e Afiliação

* Fernando P. Machado
* Kawãn F. S. Mendes
* **João Victor T. Pariz**
* Pablo C. B. Amorim
* Luiz Eduardo M. Alves
* Marlon M. López-Flores
* Paulo Fernando Ferreira Rosa

**Laboratório de Robótica RoboIME — Instituto Militar de Engenharia (IME)**, Rio de Janeiro, Brasil.

---

## Visão Geral da Pesquisa

Em operações de Busca e Salvamento Urbano (USAR - *Urban Search and Rescue*), robôs móveis precisam navegar em ambientes colapsados, sem sinal de GPS, com obstáculos desestruturados, fumaça e baixa luminosidade.

Este repositório reúne os dados do benchmark experimental realizado no IME comparando soluções de sensoriamento de baixo custo e algoritmos de mapeamento espacial (SLAM) embarcados em plataformas terrestres autônomas e teleoperadas (**TurtleBot3** e **Clearpath Jackal**):

1. **Sensores de Profundidade Avaliados:**
   - Câmera Estéreo RGB-D: **Intel RealSense D435**
   - Câmera Monocular RGB: **Logitech C920e** acoplada a redes neurais de estimativa de profundidade (**MiDaS** e **MapAnything**)
2. **Sistemas LiDAR:**
   - LiDAR Planar 2D: **Robotis LDS-02**
   - LiDAR Multifeixe 3D: **Ouster OS1**
3. **Algoritmos de SLAM Avaliados:**
   - **Google Cartographer** (SLAM 2D/3D baseado em grafo)
   - **Gmapping** (Filtro de partículas Rao-Blackwellizado)
   - **ORB-SLAM3** (Visual-Inercial monocular/estéreo)

---

## Minhas Contribuições Técnicas (João Victor Pariz)

* **Integração das Plataformas Físicas:** Montagem mecânica, distribuição de alimentação e acoplamento dos sensores na plataforma TurtleBot3.
* **Ambiente e Drivers em ROS 2:** Configuração do ambiente em Linux Debian/Ubuntu e parametrização dos nós do LiDAR LDS-02 e da câmera RealSense D435.
* **Ensaios Experimentais e Coleta de Dados:** Execução das baterias de testes em pista de obstáculos USAR, coleta de logs brutos, medição de densidade de nuvens de pontos e consumo de CPU/RAM em tempo de execução.

---

## Estrutura do Repositório

```
benchmark-slam-usar/
├── dados_experimentos/          # Tabelas geradas durante os ensaios práticos
│   ├── mapanything_2026-08-07_1306.md
│   ├── midas_2026-08-07_0740.md
│   ├── orbslam3_2026-08-07_1316.md
│   └── realsense_2026-08-07_1322.md
├── Dados Artigo.xlsx            # Métricas quantitativas consolidadas (latência, CPU, memória e pontos)
├── Paper_ISMCR2026_Springer_LNCS.pdf # Preprint do artigo completo aceito na Springer
└── README.md
```

---

## Como Citar este Trabalho

Caso utilize os dados deste benchmark em sua pesquisa, por favor cite:

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

## Licença
Os dados e documentação deste repositório estão disponibilizados para fins acadêmicos e de pesquisa.
