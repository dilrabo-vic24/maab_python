import  numpy as np
from PIL import Image

def flip_image(img_array):
    horizontal_flip = img_array[:, ::-1, :]
    
    vertical_flip = img_array[::-1, :, :]
    
    return horizontal_flip, vertical_flip

def add_noise(img_array, noise_level=25):
    noise = np.random.randint(-noise_level, noise_level, img_array.shape)
    
    noisy_img = np.clip(img_array + noise, 0, 255).astype(np.uint8)
    
    return noisy_img

def brighten_channels(img_array, channel=0, value=40):
    brightened = img_array.copy()
    
    brightened[:, :, channel] = np.clip(brightened[:, :, channel] + value, 0, 255)
    
    return brightened

def apply_mask(img_array, top_left=(0, 0), size=(100, 100)):
    masked = img_array.copy()
    
    x, y = top_left
    width, height = size
    
    masked[y:y+height, x:x+width, :] = 0
    
    return masked

def process_image(image_path):
    try:
        img = Image.open(image_path)
        
        img_array = np.array(img)
        
        print(f"Image loaded: Shape {img_array.shape}, Type {img_array.dtype}")
        
        horizontal_flip, vertical_flip = flip_image(img_array)
        Image.fromarray(horizontal_flip).save('horizontal_flip.jpg')
        Image.fromarray(vertical_flip).save('vertical_flip.jpg')
        
        noisy_img = add_noise(img_array)
        Image.fromarray(noisy_img).save('noisy_image.jpg')
        
        brightened_img = brighten_channels(img_array, channel=0, value=40)
        Image.fromarray(brightened_img).save('brightened_red.jpg')
        
        center_x = img_array.shape[1] // 2 - 50
        center_y = img_array.shape[0] // 2 - 50
        masked_img = apply_mask(img_array, (center_x, center_y), (100, 100))
        Image.fromarray(masked_img).save('masked_image.jpg')
        
        print("All image manipulations completed and saved")
        
    except Exception as e:
        print(f"Error processing image: {e}")