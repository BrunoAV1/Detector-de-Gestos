# Reconhecimento de Gestos com MediaPipe e OpenCV 🎥🤘

## 🚀 Visão Geral

Este projeto utiliza **Python**, junto com as bibliotecas **MediaPipe** e **OpenCV**, para criar um sistema de reconhecimento de gestos com as mãos em tempo real. Ele é capaz de identificar gestos simples como "Sim", "Não", "Paz e Amor", "Te Amo", "Ok" e até mesmo um "gesto obsceno kk". 

O objetivo do projeto é explorar técnicas de visão computacional e aprendizado de máquina, ao mesmo tempo em que oferece uma solução interativa para o reconhecimento de gestos com feedback visual.

---

## 🛠 Tecnologias Utilizadas

### **Python 3.7+**
A linguagem principal do projeto, devido à sua facilidade de uso e uma vasta gama de bibliotecas para processamento de imagens.

### **MediaPipe**
- Biblioteca do Google para soluções rápidas e eficientes de visão computacional.
- Utilizada para detectar e rastrear landmarks das mãos, o que possibilita identificar os gestos.

### **OpenCV**
- Biblioteca de código aberto para visão computacional e processamento de imagens.
- Utilizada para capturar e exibir o feed da câmera, além de desenhar os landmarks e fornecer feedback visual.

---

## 📋 Funcionalidades Implementadas

- **Reconhecimento de Gestos**:
  - **Sim**: Joinha com o polegar apontando para cima.
  - **Não**: Joinha com o polegar apontando para baixo.
  - **Paz e Amor**: Indicador e médio estendidos, outros dedos dobrados.
  - **Te Amo**: Polegar, indicador e mindinho estendidos.
  - **Ok**: Polegar e indicador formando um círculo.
  - **Gesto Obsceno kk**: Apenas o dedo médio estendido, outros dedos dobrados.

- **Feedback Visual**:
  - Nome do gesto detectado é exibido na tela com um retângulo destacando a área da mão detectada.

---

## 💡 Como Rodar o Projeto

### Pré-requisitos
- **Python 3.7+**: Certifique-se de que o Python está instalado em sua máquina. Caso não esteja, você pode baixá-lo [aqui](https://www.python.org/downloads/).
- **Câmera Integrada ou Externa**: Necessária para capturar o vídeo.

### Dependências
Certifique-se de instalar as dependências necessárias:
```bash
pip install mediapipe opencv-python
``` 
--- 
### Passos para Executar
* Clone este repositório:
```commandline
git clone https://github.com/BrunoAV1/Detector-de-Gestos.git
```
* Entre na pasta do projeto:
```commandline
 cd DetectorGestos
```
* Execute o arquivo principal:
```commandline
python main.py
```
* Acesse o feed da câmera em tempo real e experimente diferentes gestos! Pressione q para encerrar a aplicação.

---
## 📂 Estrutura do Projeto
```commandline
DetectorGestos/
│
├── main.py               # Arquivo principal da aplicação
├── README.md             # Este arquivo com a documentação do projeto
└── requirements.txt      # Lista de dependências necessárias
```
---
## 🤝 Contribuições
Este projeto foi desenvolvido como um experimento educacional e interativo. Se você deseja contribuir, fique à vontade para abrir issues ou criar pull requests. Algumas ideias de melhorias incluem:

Adicionar mais gestos personalizados.

Integrar novos gestos com comandos no sistema (como abrir páginas ou controlar dispositivos).

Melhorar a interface gráfica para exibir animações ou mensagens mais amigáveis.

--- 
## 🧑‍💻 Desenvolvedor
### Bruno Araujo de Vasconcellos.

<p>Este projeto foi criado para fins de aprendizado em visão computacional e processamento de imagens. Como estudante de Análise e Desenvolvimento de Sistemas, o objetivo foi aplicar tecnologias como MediaPipe e OpenCV para explorar os conceitos de gestos e interação com a máquina de forma criativa.</p>
=======
