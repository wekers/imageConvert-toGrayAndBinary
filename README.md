<p align="left">
  <img src="https://img.shields.io/static/v1?label=Tipo&message=Desafio&color=8257E5&labelColor=000000" alt="Desafio" />
</p>


## Language
- [Versão em Português do conteúdo do README](README.md) <br/>
- [English version of the README content](README.us.md)
---

![Desafio](https://raw.githubusercontent.com/wekers/imageConvert-toGrayAndBinary/refs/heads/main/img/Desafio_Reducao_Img.png)

**ADENDO:** O professor mencionou no video explicativo da atividade a não utilizar bibliotecas externas, converter a image via harcode.
- - -
<br/>

# Let's go..
# Projeto de Redução de Dimensionalidade em Imagens

Este projeto é uma implementação em Python que realiza a transformação de uma imagem colorida (RGB) para níveis de cinza (escala de cinza) e, em seguida, para uma imagem binarizada (preto e branco). Sem o uso de bibliotecas externas, o código apenas utiliza a biblioteca `tkinter` para selecionar a imagem de entrada e salvar as imagens processadas.

### Funcionalidades

- **Conversão para Escala de Cinza**: Converte uma imagem RGB para escala de cinza usando a fórmula de luminância.
- **Conversão para Binária**: Aplica um limiar (threshold) à imagem em escala de cinza para criar uma imagem binária (preto e branco).
- **Interface Simples**: Usa uma interface gráfica para selecionar a imagem de entrada e salvar as imagens processadas.
- **Sem Dependências Externas**: O código não utiliza bibliotecas externas além do `tkinter` (já incluído no Python).
- **Carregamento e Salvamento de Imagens**: O projeto permite carregar uma imagem BMP e salvar as imagens processadas (escala de cinza e binarizada) no mesmo diretório do arquivo original, com nomes modificados para indicar o tipo de processamento.

### Requisitos

- Python 3.x
- Biblioteca `tkinter` (geralmente incluída na instalação padrão do Python)
- Uma imagem BMP para teste (o código foi testado com imagens de 24 bits).
- Sem o uso de bibliotecas externas, possui uma retrição de usar apenas imagens em formato .bmp

### Como Usar

1. **Clone o repositório**:
   ```bash
   git clone git@github.com:wekers/imageConvert-toGrayAndBinary.git
   cd imageConvert-toGrayAndBinary
   ```
2. **Execute o script:**
   ```bash
   python3 imageConvert-toGrayAndBinary.py
   ```
3. **Selecione uma imagem BMP:**

    - Uma janela de diálogo será aberta para que você selecione uma imagem BMP para processamento.

4. **Resultados:**

    - Após o processamento, duas novas imagens serão salvas no mesmo diretório da imagem original:

       - `nome_da_imagem_grayscale_image.bmp:` Imagem em tons de cinza.

       - `nome_da_imagem_binarized_image.bmp:` Imagem binarizada (preto e branco). <br/><br/>


         ![Terminal](https://raw.githubusercontent.com/wekers/imageConvert-toGrayAndBinary/refs/heads/main/img/terminal_imageConvert.png) 

<br/><br/>

| Imagem | Tipo |
|--------|----------|
| ![RGB](https://raw.githubusercontent.com/wekers/imageConvert-toGrayAndBinary/refs/heads/main/img/Lenna_512x512.bmp) | Imagem Original RGB |
| ![GRAY](https://raw.githubusercontent.com/wekers/imageConvert-toGrayAndBinary/refs/heads/main/img/Lenna_512x512_grayscale_image.bmp) | Imagem em Escala de Cinza |
| ![BINARY](https://raw.githubusercontent.com/wekers/imageConvert-toGrayAndBinary/refs/heads/main/img/Lenna_512x512_binarized_image.bmp) | Imagem Binária |


### Estrutura do Código

   - `rgb_to_grayscale(image):` Converte uma imagem RGB para escala de cinza.

   - `grayscale_to_binary(grayscale_image, threshold=128):` Converte uma imagem em escala de cinza para binária, utilizando um limiar (threshold) para determinar se o pixel será preto ou branco.

   - `load_image(file_path):` Carrega uma imagem BMP e a converte para uma matriz 3D (RGB).

   - `save_image(image, file_path, is_binary=False):` Salva uma imagem (escala de cinza ou binária) como um arquivo BMP.

   - `main():` Função principal que gerencia a seleção de arquivos, processamento e salvamento das imagens.

### Limitações

   - O código foi projetado para funcionar com imagens BMP de 24 bits.

   - As dimensões da imagem são fixas em 512x512 pixels no exemplo. Para imagens com dimensões diferentes, é necessário ajustar o código.

   - Não há suporte para outros formatos de imagem (como JPEG ou PNG) sem o uso de bibliotecas externas.

### Exemplo de Uso

   1. Execute o script `imageConvert-toGrayAndBinary.py`.

   2. Selecione uma imagem BMP no diálogo de arquivo.

   3. O script processará a imagem e salvará as versões em escala de cinza e binarizada no mesmo diretório da imagem original.

---

**Nota:** Este projeto foi desenvolvido como uma implementação básica para fins educacionais. Para processamento de imagens mais avançado, considere utilizar bibliotecas como PIL (Pillow) ou OpenCV.