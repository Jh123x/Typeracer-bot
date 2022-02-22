import pyautogui
from PIL import ImageGrab, Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def screenshot() -> Image:
    """Screenshot"""
    image = ImageGrab.grab()
    return image


def enter_text(words: str):
    """Enter the string"""
    pyautogui.typewrite(words)


def alt_tab():
    """Alt + Tab"""
    pyautogui.hotkey('alt', 'tab')


def crop_image(image: Image) -> Image:
    """Resize the image"""
    return image.crop((1950, 1400, 3750, 1700))

def ocr(image: Image) -> str:
    return pytesseract.image_to_string(image)


def main():
    img = screenshot()
    img = crop_image(img)

    typed_string = ocr(img)
    print(typed_string)
    alt_tab()
    enter_text(''.join(typed_string))


if __name__ == '__main__':
    main()
