<p align="left">
  <img src="https://img.shields.io/static/v1?label=Type&message=Challenge&color=8257E5&labelColor=000000" alt="Challenge" />
</p>

## Language
- [Versão em Português do conteúdo do README](README.md) <br/>
- [English version of the README content](README.us.md)
---

![Challenge](https://raw.githubusercontent.com/wekers/imageConvert-toGrayAndBinary/refs/heads/main/img/Challenge_Reduce_Img.png)

**NOTE:** The professor have say in the explanatory video of the activity, do not use external libraries, but convert the image via hardcode.
- - -
<br/>

# Let's go..
# Image Dimensionality Reduction Project

This project is a Python implementation that transforms a color image (RGB) into grayscale and then into a binarized (black and white) image. Without using external libraries, the code only utilizes the `tkinter` library to select the input image and save the processed images.

### Features

- **Grayscale Conversion**: Converts an RGB image to grayscale using the luminance formula.
- **Binary Conversion**: Applies a threshold to the grayscale image to create a binary (black and white) image.
- **Simple Interface**: Uses a graphical interface to select the input image and save the processed images.
- **No External Dependencies**: The code does not use external libraries besides `tkinter` (already included in Python).
- **Image Loading and Saving**: The project allows loading a BMP image and saving the processed images (grayscale and binarized) in the same directory as the original file, with modified names indicating the type of processing.

### Requirements

- Python 3.x
- `tkinter` library (usually included in the default Python installation)
- A BMP image for testing (the code was tested with 24-bit images).
- Without the use of external libraries, there is a restriction to using only `.bmp` format images.

### How to Use

1. **Clone the repository**:
   ```bash
   git clone git@github.com:wekers/imageConvert-toGrayAndBinary.git
   cd imageConvert-toGrayAndBinary
   ```
2. **Run the script:**
   ```bash
   python3 imageConvert-toGrayAndBinary.py
   ```
3. **Select a BMP image:**

    - A dialog window will open for you to select a BMP image for processing.

4. **Results:**

    - After processing, two new images will be saved in the same directory as the original image:

       - `image_name_grayscale_image.bmp:` Grayscale image.

       - `image_name_binarized_image.bmp:` Binarized (black and white) image. <br/><br/>


         ![Terminal](https://raw.githubusercontent.com/wekers/imageConvert-toGrayAndBinary/refs/heads/main/img/terminal_imageConvert.png)

<br/><br/>

| Image | Type |
|--------|----------|
| ![RGB](https://raw.githubusercontent.com/wekers/imageConvert-toGrayAndBinary/refs/heads/main/img/Lenna_512x512.bmp) | Original RGB Image |
| ![GRAY](https://raw.githubusercontent.com/wekers/imageConvert-toGrayAndBinary/refs/heads/main/img/Lenna_512x512_grayscale_image.bmp) | Grayscale Image |
| ![BINARY](https://raw.githubusercontent.com/wekers/imageConvert-toGrayAndBinary/refs/heads/main/img/Lenna_512x512_binarized_image.bmp) | Binary Image |


### Code Structure

   - `rgb_to_grayscale(image):` Converts an RGB image to grayscale.

   - `grayscale_to_binary(grayscale_image, threshold=128):` Converts a grayscale image to binary, using a threshold to determine if the pixel will be black or white.

   - `load_image(file_path):` Loads a BMP image and converts it into a 3D matrix (RGB).

   - `save_image(image, file_path, is_binary=False):` Saves an image (grayscale or binary) as a BMP file.

   - `main():` Main function that manages file selection, processing, and image saving.

### Limitations

   - The code is designed to work with 24-bit BMP images.

   - The example uses fixed dimensions of 512x512 pixels. For different image sizes, the code needs to be adjusted.

   - There is no support for other image formats (such as JPEG or PNG) without using external libraries.

### Usage Example

   1. Run the script `imageConvert-toGrayAndBinary.py`.

   2. Select a BMP image in the file dialog.

   3. The script will process the image and save the grayscale and binarized versions in the same directory as the original image.

---

**Note:** This project was developed as a basic implementation for educational purposes. For more advanced image processing, consider using libraries such as PIL (Pillow) or OpenCV.

 
