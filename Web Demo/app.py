import streamlit as st
from PIL import Image
import torch
from torchvision import transforms
from torchvision.models import convnext_tiny

# 1. Khai báo cấu trúc model và tham số
num_classes = 10  # Số lượng class của dataset EuroSAT
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
MODEL_PATH = "ConvNeXt_EuroSAT_Best.pth" 
CLASSES = ['AnnualCrop', 'Forest', 'HerbaceousVegetation', 'Highway', 'Industrial',
           'Pasture', 'PermanentCrop', 'Residential', 'River', 'SeaLake']

# 2. Khởi tạo lại model
@st.cache_resource
def load_model():
    model = convnext_tiny(weights=None)
    
    # Sửa lại lớp classifier cuối cùng cho khớp với số class
    in_features = model.classifier[2].in_features
    model.classifier[2] = torch.nn.Linear(in_features, num_classes)
    
    # Load weights đã train
    try:
        model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
    except FileNotFoundError:
        st.error(f"Lỗi: Không tìm thấy file model tại {MODEL_PATH}. Vui lòng kiểm tra lại đường dẫn.")
        st.stop()
    
    model.to(DEVICE)
    model.eval()
    return model

# Thêm hiệu ứng xoay báo hiệu đang load model lần đầu
with st.spinner("Đang nạp mô hình AI lên bộ nhớ, vui lòng đợi vài giây (chỉ lâu ở lần đầu tiên)..."):
    model = load_model()

# 3. Khai báo các bước transform ảnh (giống val_transform lúc train)
mean = [0.485, 0.456, 0.406]
std  = [0.229, 0.224, 0.225]
val_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean, std),
])

# 4. Giao diện Streamlit
st.title("Demo Đồ án CS231 - Phân loại vùng đất dựa trên ảnh vệ tinh")
st.write("Bỏ một tấm ảnh dô đây để model dự đoán nhé!")

uploaded_file = st.file_uploader("Chọn một tấm ảnh...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Hiển thị ảnh đã upload
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption='Ảnh đã upload', use_container_width=True)

    # Thêm hiệu ứng xoay trong lúc chờ phân loại ảnh
    with st.spinner("Đang phân loại, vui lòng chờ..."):
        # Tiền xử lý ảnh
        input_tensor = val_transform(image).unsqueeze(0)
        input_tensor = input_tensor.to(DEVICE)

        # Đưa ảnh qua model để dự đoán
        with torch.no_grad():
            output = model(input_tensor)
            
            # Tính toán xác suất và lấy class có tỷ lệ cao nhất
            probabilities = torch.nn.functional.softmax(output[0], dim=0)
            predicted_idx = torch.argmax(probabilities).item()
            confidence = probabilities[predicted_idx].item()
            
            predicted_class = CLASSES[predicted_idx]

    # Hiển thị kết quả ra màn hình
    st.success(f"**Mô hình dự đoán:** {predicted_class}")
    st.info(f"**Độ tự tin (Confidence):** {confidence:.2%}")
# C:\Users\admin\AppData\Local\Python\pythoncore-3.14-64\python.exe -m streamlit run app.py