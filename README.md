# CS231.Q22 - Nhập môn Thị giác máy tính

## GIỚI THIỆU MÔN HỌC

* [cite_start]**Tên môn học:** Nhập môn Thị giác máy tính [cite: 4]
* [cite_start]**Lớp:** CS231.Q22 [cite: 4]
* **Giảng viên hướng dẫn:** TS. [cite_start]Mai Tiến Dũng [cite: 4]
* [cite_start]**Đề tài đồ án:** Phân loại vùng đất dựa trên ảnh vệ tinh [cite: 3]

## THÀNH VIÊN NHÓM

| STT | Họ tên | MSSV | Email |
| :---: | :--- | :---: | :--- |
| 1 | Nguyễn Khang | 24520749 | 24520749@gm.uit.edu.vn |
| 2 | Trần Hoài Nhân | 24521240 | 24521240@gm.uit.edu.vn |
| 3 | Lê Ngọc Tường Vy | 24522054 | 24522054@gm.uit.edu.vn |

## MÔ TẢ ĐỒ ÁN

[cite_start]Trong bối cảnh hiện nay, dữ liệu ảnh vệ tinh ngày càng được thu thập với quy mô lớn và đóng vai trò quan trọng trong quy hoạch đô thị, quản lý tài nguyên thiên nhiên, giám sát môi trường và nông nghiệp thông minh[cite: 18]. [cite_start]Việc áp dụng các phương pháp học sâu (Deep Learning), đặc biệt là các mô hình Convolutional Neural Network (CNN) giúp tự động hóa quá trình phân tích và phân loại, mang lại độ chính xác cao và tiết kiệm thời gian, chi phí[cite: 20, 21].

### 1. Tập dữ liệu (Dataset)
* [cite_start]**[EuroSAT (RGB)](https://www.kaggle.com/datasets/apollo2506/eurosat-dataset/data)**: Tập dữ liệu chứa ảnh RGB từ vệ tinh Sentinel-2[cite: 228].
* [cite_start]**Tổng số lượng mẫu**: 27.000 ảnh[cite: 230].
* [cite_start]**Phân loại**: 10 lớp vùng đất (Annual Crop, Forest, Herbaceous Vegetation, Highway, Industrial, Pasture, Permanent Crop, Residential, River, Sea Lake)[cite: 47, 48, 49, 50, 51, 52, 53, 54, 55, 56].
* [cite_start]**Phân chia dữ liệu**: Tập train (18.900 mẫu - 70%) [cite: 232][cite_start], Tập valid (5.400 mẫu - 20%) [cite: 233][cite_start], Tập test (2.700 mẫu - 10%)[cite: 234].

### 2. Phương pháp tiếp cận
* [cite_start]**Machine Learning truyền thống**: Kết hợp các đặc trưng Color Moment, LBP, HOG và huấn luyện với mô hình **XGBoost**[cite: 80, 87].
* [cite_start]**Mạng tích chập tự xây dựng**: Kiến trúc **CustomEuroSAT-CNN** gồm 4 khối tích chập[cite: 103].
* [cite_start]**Transfer Learning**: Áp dụng các kiến trúc mạng hiện đại đã được pre-train trên ImageNet[cite: 201]:
    * [cite_start]**ResNet50** [cite: 205]
    * [cite_start]**DenseNet121** [cite: 212]
    * [cite_start]**ConvNeXt-Tiny** [cite: 219]

### 3. Kết quả thực nghiệm

[cite_start]Dưới đây là bảng tổng hợp kết quả hiệu năng của các mô hình trên tập Test[cite: 967]:

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
Tải xuống file trọng số `ConvNeXt_EuroSAT_Best.pth` tại liên kết Google Drive sau:
[Tải file trọng số tại đây](https://drive.google.com/file/d/1eyADQ8CJFYmakGJ6a6xYnP1vNGfYAuLr/view?usp=sharing)

### Bước 2: Tổ chức cấu trúc thư mục
Di chuyển file trọng số vừa tải về vào trong thư mục `Web Demo` của đồ án sao cho file nằm chung cấp với file thực thi giao diện:
```text
📂 Web Demo/
├── 📄 app.py
└── 📄 ConvNeXt_EuroSAT_Best.pth
