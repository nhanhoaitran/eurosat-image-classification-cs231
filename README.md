# CS231.Q22 - Nhập môn Thị giác máy tính

## GIỚI THIỆU MÔN HỌC

* **Tên môn học:** Nhập môn Thị giác máy tính
* **Lớp:** CS231.Q22
* **Giảng viên hướng dẫn:** TS. Mai Tiến Dũng
* **Đề tài đồ án:** Phân loại vùng đất dựa trên ảnh vệ tinh

## THÀNH VIÊN NHÓM

| STT | Họ tên | MSSV | Email |
| :---: | :--- | :---: | :--- |
| 1 | Nguyễn Khang | 24520749 | 24520749@gm.uit.edu.vn |
| 2 | Trần Hoài Nhân | 24521240 | 24521240@gm.uit.edu.vn |
| 3 | Lê Ngọc Tường Vy | 24522054 | 24522054@gm.uit.edu.vn |

## MÔ TẢ ĐỒ ÁN

Trong bối cảnh hiện nay, dữ liệu ảnh vệ tinh ngày càng được thu thập với quy mô lớn và đóng vai trò quan trọng trong quy hoạch đô thị, quản lý tài nguyên thiên nhiên, giám sát môi trường và nông nghiệp thông minh. Việc áp dụng các phương pháp học sâu (Deep Learning), đặc biệt là các mô hình Convolutional Neural Network (CNN) giúp tự động hóa quá trình phân tích và phân loại, mang lại độ chính xác cao và tiết kiệm thời gian, chi phí.

### 1. Tập dữ liệu (Dataset)
* **[EuroSAT (RGB)](https://www.kaggle.com/datasets/apollo2506/eurosat-dataset/data)**: Tập dữ liệu chứa ảnh RGB từ vệ tinh Sentinel-2.
* **Tổng số lượng mẫu**: 27.000 ảnh.
* **Phân loại**: 10 lớp vùng đất (Annual Crop, Forest, Herbaceous Vegetation, Highway, Industrial, Pasture, Permanent Crop, Residential, River, Sea Lake).
* **Phân chia dữ liệu**: Tập train (18.900 mẫu - 70%), Tập valid (5.400 mẫu - 20%), Tập test (2.700 mẫu - 10%).

### 2. Phương pháp tiếp cận
* **Machine Learning truyền thống**: Kết hợp các đặc trưng Color Moment, LBP, HOG và huấn luyện với mô hình **XGBoost**.
* **Mạng tích chập tự xây dựng**: Kiến trúc **CustomEuroSAT-CNN** gồm 4 khối tích chập.
* **Transfer Learning**: Áp dụng các kiến trúc mạng hiện đại đã được pre-train trên ImageNet:
    * **ResNet50**
    * **DenseNet121**
    * **ConvNeXt-Tiny**

### 3. Kết quả thực nghiệm

Dưới đây là bảng tổng hợp kết quả hiệu năng của các mô hình trên tập Test:

| Mô hình | Test Accuracy | Macro F1 | Optimizer | Best LR |
| :--- | :---: | :---: | :---: | :---: |
| XGBoost (HOG+Color+LBP) | 0.9074 | 0.9070 | - | - |
| CustomEuroSAT-CNN | 0.9611 | 0.9597 | AdamW | 10^-3 |
| ConvNeXt-Tiny | 0.9856 | 0.9848 | Adam | 10^-3 |
| ResNet50 | 0.9863 | 0.9860 | AdamW | 10^-3 |
| DenseNet121 | 0.9863 | 0.9858 | Adam | 10^-3 |

## 💻 HƯỚNG DẪN CHẠY WEB DEMO

Do file trọng số (checkpoint) huấn luyện của mô hình vượt quá giới hạn dung lượng lưu trữ của GitHub, vui lòng thực hiện tuần tự theo các bước sau để thiết lập và chạy ứng dụng Web Demo:

### Bước 1: Tải file trọng số mô hình
Tải xuống file trọng số tốt nhất `ConvNeXt_EuroSAT_Best.pth` tại liên kết Google Drive sau:
👉 [Tải file trọng số tại đây](https://drive.google.com/file/d/1eyADQ8CJFYmakGJ6a6xYnP1vNGfYAuLr/view?usp=sharing)

### Bước 2: Tổ chức cấu trúc thư mục
Di chuyển file trọng số vừa tải về vào trong thư mục `Web Demo` của đồ án sao cho file nằm chung cấp với file thực thi giao diện:
```text
📂 Web Demo/
├── 📄 app.py
└── 📄 ConvNeXt_EuroSAT_Best.pth
