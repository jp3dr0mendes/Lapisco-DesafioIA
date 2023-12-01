# Desafio IA - Lapisco

O projeto desenvolvido nesse repositório consiste no desafio prático do processo seletivo do Laboratório de Processamento de Imagens, Sinais e Computação Aplicada (LAPISCO), sendo um script desenvolvido na linguagem Python que executa a detecção de rostos usando a YOLOv8, incorporando a funcionalidade de borramento dos rostos detectados e contagem do número de pessoas presentes em cada frame do vídeo.

## Requisitos necessários para rodar o script

Para rodar o script, é necessário que o Python do computador esteja na versão 3.10.

## Como utilizar o script

### 1. Clonar o repositório

```git clone https://github.com/jp3dr0mendes/Lapisco-DesafioIA.git```

### 2. Acessar o repositório clonado

```cd Lapisco-DesafioIA```

### 3. Baixar as bibliotecas do python necessárias para rodar o script

```pip install -r requirements.txt```

### 4. Clonar o repositório do modelo de Face Detection usado no script

```git clone https://github.com/noorkhokhar99/face-detection-yolov8.git```

### 5. Rodar o arquivo main.py

```python3 main.py```

### 6. A seguinte mensagem deve ser exibida no terminal

```Digite o caminho para o vídeo: ```

### 7.Passar o caminho do vídeo em formato .mp4 ao qual se deseja aplicar o modelo de detecção facial 

ex: "C:\Users\joaop\Downloads\video (2160p).mp4"

### 8. O vídeo com a detecção facial será salvo com o sufixo "-edited" na mesma pasta que o vídeo original

ex: "C:\Users\joaop\Downloads\video (2160p)-edited.mp4"
