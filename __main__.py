import pyautogui
from PIL import ImageGrab, Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
tesseract_config = r"""-c tessedit_char_whitelist="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,:.-'?" """
tesseract_language = "eng"

def screenshot() -> Image:
    """Screenshot"""
    image = ImageGrab.grab()
    return image


def enter_text(words: str):
    """Enter the string"""
    pyautogui.typewrite(words, interval=0.05)


def alt_tab():
    """Alt + Tab"""
    pyautogui.hotkey('alt', 'tab')


def crop_image(image: Image) -> Image:
    """Resize the image"""
    return image.crop((1950, 1250, 3750, 1700))

def ocr(image: Image) -> str:
    return pytesseract.image_to_string(image.convert("1"), lang=tesseract_language, config=tesseract_config)


def main():
    img = screenshot()
    img = crop_image(img)

    typed_string = ocr(img)
    # print(typed_string)
    temp = typed_string.split("\n\n")
    typed_str = " ".join(temp[0].split("\n"))
    print(typed_str)
    alt_tab()
    enter_text(typed_str)
    img.show()


if __name__ == '__main__':
    main()
