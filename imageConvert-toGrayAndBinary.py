import os
import tkinter as tk
from tkinter import filedialog

def rgb_to_grayscale(image):
    # Convert an RGB image (3D) to grayscale (2D)
    height = len(image)
    width = len(image[0])
    grayscale_image = [[0 for _ in range(width)] for _ in range(height)]
    
    for i in range(height):
        for j in range(width):
            r, g, b = image[i][j]
            gray = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
            grayscale_image[i][j] = gray
    
    return grayscale_image

def grayscale_to_binary(grayscale_image, threshold=128):
    # Convert a grayscale image (2D) to a binary image (2D)
    height = len(grayscale_image)
    width = len(grayscale_image[0])
    binary_image = [[0 for _ in range(width)] for _ in range(height)]
    
    for i in range(height):
        for j in range(width):
            binary_image[i][j] = 255 if grayscale_image[i][j] >= threshold else 0
    
    return binary_image

def load_image(file_path):
    # Load an image file and return it as a 3D (RGB)
    with open(file_path, "rb") as f:
        # Skip the BMP header (assuming it's a 24-bit BMP file)
        f.read(54)
        image_data = f.read()
    
    # Parse the image data into a 3D
    ### Define the image size
    width = 512  # Example width (you need to know the actual width/height)
    height = 512  # Example height
    image = []
    index = 0
    
    for i in range(height):
        row = []
        for j in range(width):
            b = image_data[index]
            g = image_data[index + 1]
            r = image_data[index + 2]
            row.append([r, g, b])
            index += 3
        image.append(row)
    
    return image

def save_image(image, file_path, is_binary=False):
    # Save an image (2D) as a BMP file
    height = len(image)
    width = len(image[0])
    
    # BMP header (54 bytes)
    header = bytearray([
        0x42, 0x4D,             # Signature "BM"
        0x36, 0x00, 0x0C, 0x00, # File size (placeholder)
        0x00, 0x00, 0x00, 0x00, # Reserved
        0x36, 0x00, 0x00, 0x00, # Pixel data offset
        0x28, 0x00, 0x00, 0x00, # DIB header size
        width & 0xFF, (width >> 8) & 0xFF, (width >> 16) & 0xFF, (width >> 24) & 0xFF,  # Width
        height & 0xFF, (height >> 8) & 0xFF, (height >> 16) & 0xFF, (height >> 24) & 0xFF,  # Height
        0x01, 0x00,             # Planes
        0x18, 0x00,             # Bits per pixel (24-bit)
        0x00, 0x00, 0x00, 0x00, # Compression
        0x00, 0x00, 0x00, 0x00, # Image size (placeholder)
        0x00, 0x00, 0x00, 0x00, # X pixels per meter
        0x00, 0x00, 0x00, 0x00, # Y pixels per meter
        0x00, 0x00, 0x00, 0x00, # Colors in color table
        0x00, 0x00, 0x00, 0x00  # Important color count
    ])
    
    # Pixel data (24-bit BMP format)
    pixel_data = bytearray()
    for i in range(height):  # Write rows top-to-bottom
        for j in range(width):
            if is_binary:
                gray = image[i][j]
                pixel_data.extend([gray, gray, gray])  # R=G=B for binary image
            else:
                gray = image[i][j]
                pixel_data.extend([gray, gray, gray])  # R=G=B for grayscale image
    
    # Update file size in header
    file_size = len(header) + len(pixel_data)
    header[2:6] = file_size.to_bytes(4, byteorder="little")
    
    # Write to file
    with open(file_path, "wb") as f:
        f.write(header)
        f.write(pixel_data)

def main():
    # Open a file dialog to select an image
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title="Select an image", filetypes=[("BMP files", "*.bmp")])
    
    if not file_path:
        print("No file selected.")
        return
    
    # Load the image
    image = load_image(file_path)
    
    # Convert to grayscale
    grayscale_image = rgb_to_grayscale(image)
    
    
    ### Save the grayscale image
    
    # ask path to save?
    # grayscale_save_path = filedialog.asksaveasfilename(title="Save grayscale image", defaultextension=".bmp", filetypes=[("BMP files", "*.bmp")])
    
    # get file name without extension
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    
    grayscale_save_path = f"{base_name}_grayscale_image.bmp" 
    if grayscale_save_path:
        save_image(grayscale_image, grayscale_save_path, is_binary=False)
        print(f"Grayscale image saved to {grayscale_save_path}")
    
    # Convert to binary image
    binary_image = grayscale_to_binary(grayscale_image, threshold=128)
    
    ### Save the binary image
    
    # ask path to save?
    # binary_save_path = filedialog.asksaveasfilename(title="Save binary image", defaultextension=".bmp", filetypes=[("BMP files", "*.bmp")])
    
    # save binary image
    binary_save_path = f"{base_name}_binarized_image.bmp"
    if binary_save_path:
        save_image(binary_image, binary_save_path, is_binary=True)
        print(f"Binary image saved to {binary_save_path}")

if __name__ == "__main__":
    main()