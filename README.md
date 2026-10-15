# ĐỒ ÁN MÔN HỌC: CÔNG NGHỆ PHẦN MỀM (CNPM)
## ĐỀ TÀI: PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG QUẢN LÝ TRƯỜNG MẦM NON TƯ THỤC (KMS)

- **Sinh viên thực hiện:** Trần Trung Nguyên
- **Mã số sinh viên:** 231A290096
- **Khoa:** Công Nghệ Thông Tin
- **Repository:** [https://github.com/trungnguyen332005genz-source/CNPM.git](https://github.com/trungnguyen332005genz-source/CNPM.git)

---

### 1. Giới thiệu tổng quan
Hệ thống quản lý trường mầm non tư thục (Kindergarten Management System - KMS) hỗ trợ cơ sở mầm non quản lý tập trung và số hóa toàn bộ quy trình:
1. **Quản lý trẻ em:** Chức năng trung tâm, hồ sơ lý lịch, tiền sử bệnh, dị ứng, phân lớp, trạng thái học.
2. **Quản lý giáo viên:** Thông tin chuyên môn, hồ sơ cán bộ, phân công lớp học.
3. **Quản lý phụ huynh:** Quản lý quan hệ 1-N với trẻ em (cha, mẹ, giám hộ), tương tác với nhà trường.
4. **Quản lý lớp học:** Tên lớp, khối (Nhà trẻ, Mầm, Chồi, Lá), sĩ số tối đa, phân bổ trẻ và giáo viên.
5. **Quản lý thực đơn:** Lập thực đơn dinh dưỡng theo tuần/ngày (bữa sáng, trưa, xế), quản lý calo và món ăn.
6. **Quản lý học phí và tiền ăn:** Tự động hóa tính toán theo công thức:
   $$\text{Tổng tiền} = \text{Học phí cơ bản} + \text{Tiền ăn (Số ngày ăn} \times \text{Đơn giá/ngày)} + \text{Phí dịch vụ} - \text{Giảm trừ}$$
7. **Thanh toán trực tuyến VietQR:** Phụ huynh quét mã VietQR Napas 24/7, cập nhật trạng thái tự động.
8. **Quản lý tài khoản & phân quyền (RBAC):** Quản lý, Giáo viên, Phụ huynh.

---

### 2. Cấu trúc thư mục dự án
```text
├── CNPM.asta                 # File mô hình UML thiết kế trên Astah Community
├── W.docx                    # Báo cáo đặc tả phân tích thiết kế hoàn chỉnh (chuẩn môn học)
├── database.sql              # Script SQL DDL & DML khởi tạo CSDL quan hệ
├── astah_export/             # Toàn bộ hình ảnh sơ đồ UML đã xuất từ Astah & công cụ
│   ├── USECASE/              # Sơ đồ Use Case tổng thể và phân rã
│   ├── ACTIVITY/             # Sơ đồ hoạt động các luồng nghiệp vụ
│   ├── SEQUENCE/             # Sơ đồ tuần tự tương tác hệ thống
│   └── EXTRA/                # Sơ đồ lớp Class Diagram & Thanh toán QR
├── build_full_document.py    # Script tự động hóa sinh file Word báo cáo
├── generate_diagrams.py      # Script sinh sơ đồ UML bổ sung chất lượng cao
└── README.md                 # Tài liệu hướng dẫn dự án
```

---

### 3. Hướng dẫn cài đặt CSDL
Hệ thống sử dụng cơ sở dữ liệu quan hệ MySQL / MariaDB (tương thích Laragon/XAMPP):
1. Mở công cụ quản lý cơ sở dữ liệu (HeidiSQL, phpMyAdmin, MySQL Workbench).
2. Tạo database và chạy script `database.sql`:
```bash
mysql -u root -p < database.sql
```
