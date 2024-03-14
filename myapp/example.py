import cv2
import pytesseract
from PIL import Image

# Установите путь к исполняемому файлу Tesseract
pytesseract.pytesseract.tesseract_cmd = r':/Program Files/Tesseract-OCR/tesseract.exe'

def enhance_image(image_path, output_path):
    # Загрузите изображение с использованием OpenCV
    image = cv2.imread(image_path)

    # Преобразуйте изображение в оттенки серого
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Увеличьте контрастность изображения с использованием адаптивной гистограммной эквализации
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced_image = clahe.apply(gray_image)

    # Примените медианный фильтр для уменьшения шума
    filtered_image = cv2.medianBlur(enhanced_image, 3)

    # Сохраните улучшенное изображение
    cv2.imwrite(output_path, filtered_image)

input_image = 'C:/Users/Papech/Desktop/baza.jpg'
enhanced_image = 'C:/Users/Papech/Desktop/baza2.jpg'

enhance_image(input_image, enhanced_image)

# Выполните OCR на улучшенном изображении
text = pytesseract.image_to_string(Image.open(enhanced_image))
print(text)