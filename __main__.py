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


def enter_text(words: str, wpm: int):
    """Enter the string"""
    word_count = len(words.split(' '))
    letter_count = len(words)
    interval = ((word_count / wpm) / letter_count) * 60
    pyautogui.typewrite(words, interval=interval)


def alt_tab():
    """Alt + Tab"""
    pyautogui.hotkey('alt', 'tab')

def crop_image(image: Image) -> Image:
    """Resize the image"""
    return image.crop((1950, 1250, 3750, 1700)) ## Coordinate of image (Change based on monitor used)

def ocr(image: Image) -> str:
    return pytesseract.image_to_string(image, lang=tesseract_language, config=tesseract_config)

def greyscale(image: Image) -> Image:
    return image.convert("1")


def main():
    img = screenshot()
    img = crop_image(img)
    img = greyscale(img)

    typed_string = ocr(img)
    temp = typed_string.split("\n\n")
    typed_str = " ".join(temp[0].split("\n"))
    print(f"Detected string: {typed_str}")

    wpm = int(input("WPM wanted: "))
    ## Comment these 2 when testing ##
    alt_tab()
    enter_text(typed_str, wpm)
    ##                              ##
    
    img.show()


if __name__ == '__main__':
    main()
