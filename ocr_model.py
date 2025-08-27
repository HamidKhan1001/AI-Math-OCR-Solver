# ocr_model.py
import torch
import torchvision.transforms as T
from PIL import Image

# Assume you have a PyTorch model class `HandwrittenMathOCR`
from your_model_definition import HandwrittenMathOCR

# Load weights once at startup
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
OCR_MODEL = HandwrittenMathOCR()
OCR_MODEL.load_state_dict(torch.load("models/handwritten_math_ocr.pth", map_location=DEVICE))
OCR_MODEL.to(DEVICE)
OCR_MODEL.eval()

# Preprocessing pipeline: grayscale, resize, normalize
TRANSFORMS = T.Compose([
    T.Grayscale(num_output_channels=1),
    T.Resize((32, 128)),             # height=32, width=128
    T.ToTensor(),
    T.Normalize(mean=[0.5], std=[0.5])
])

def recognize_math_expression(image_pil: Image.Image) -> str:
    """
    Given a PIL image of a handwritten equation (cropped to just the equation line),
    return a LaTeX-like string, e.g. '2x^2+3x-5=0'.
    """
    # 1) Convert to grayscale, resize
    img = TRANSFORMS(image_pil).unsqueeze(0).to(DEVICE)  # [1,1,32,128]
    # 2) Run through model → sequence of token IDs
    with torch.no_grad():
        token_ids = OCR_MODEL(img)  # shape [1, seq_len]
    # 3) Decode token IDs to symbols (digits, variables, operators)
    latex_str = OCR_MODEL.decode(token_ids.squeeze(0).cpu().tolist())
    return latex_str
