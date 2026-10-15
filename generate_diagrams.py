import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

OUTPUT_DIR = r"e:\CNPM\CNPM\astah_export\EXTRA"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_overall_usecase_diagram():
    fig, ax = plt.subplots(figsize=(16, 12), dpi=200)
    ax.set_xlim(0, 160)
    ax.set_ylim(0, 120)
    ax.axis('off')

    # Background frame - System Boundary
    rect = patches.FancyBboxPatch((35, 8), 90, 104, boxstyle="round,pad=1,rounding_size=2",
                                  facecolor='#F8FAFC', edgecolor='#1E3A8A', linewidth=2.5)
    ax.add_patch(rect)
    ax.text(80, 108, "HỆ THỐNG QUẢN LÝ MẦM NON TƯ THỤC (KMS)", 
            fontsize=15, fontweight='bold', color='#1E3A8A', ha='center', va='center')

    # Helper for Actor
    def draw_actor(x, y, name, role):
        ax.plot([x], [y+3.5], marker='o', markersize=14, color='#1E293B', fillstyle='full')
        ax.plot([x, x], [y+2.2, y-1.5], color='#1E293B', linewidth=2.5) # Body
        ax.plot([x-3, x+3], [y+1, y+1], color='#1E293B', linewidth=2.5) # Arms
        ax.plot([x, x-2.5], [y-1.5, y-5], color='#1E293B', linewidth=2.5) # Left leg
        ax.plot([x, x+2.5], [y-1.5, y-5], color='#1E293B', linewidth=2.5) # Right leg
        ax.text(x, y-7.5, name, fontsize=12, fontweight='bold', ha='center', color='#0F172A')
        ax.text(x, y-10, f"({role})", fontsize=9, fontstyle='italic', ha='center', color='#475569')

    draw_actor(15, 85, "Quản lý", "Admin")
    draw_actor(15, 35, "Giáo viên", "Teacher")
    draw_actor(145, 60, "Phụ huynh", "Parent")

    # Helper for Use Case Ellipse
    def draw_uc(cx, cy, w, h, text, color='#E0F2FE', edge='#0284C7'):
        ellipse = patches.Ellipse((cx, cy), w, h, facecolor=color, edgecolor=edge, linewidth=1.8, zorder=3)
        ax.add_patch(ellipse)
        ax.text(cx, cy, text, fontsize=9.5, fontweight='bold', color='#0F172A',
                ha='center', va='center', zorder=4, multialignment='center')

    # Draw Use Cases
    # Quản lý Trẻ em & Lớp học
    draw_uc(55, 98, 30, 8, "UC01: Quản lý\ntrẻ em")
    draw_uc(55, 84, 30, 8, "UC02: Quản lý\ngiáo viên")
    draw_uc(55, 70, 30, 8, "UC03: Quản lý\nlớp học & phân công")
    draw_uc(55, 56, 30, 8, "UC04: Quản lý\nphụ huynh")
    
    # Thực đơn & Học phí & Thanh toán
    draw_uc(105, 92, 30, 8, "UC05: Quản lý\nthực đơn dinh dưỡng")
    draw_uc(105, 76, 30, 8, "UC06: Quản lý\nhọc phí & tiền ăn")
    draw_uc(105, 60, 30, 8, "UC07: Thanh toán\nhọc phí VietQR")
    draw_uc(80, 20, 36, 9, "UC08: Quản lý tài khoản\n& phân quyền người dùng", color='#FEF3C7', edge='#D97706')

    # Helper for connection line
    def draw_line(x1, y1, x2, y2, color='#475569', style='-'):
        ax.plot([x1, x2], [y1, y2], linestyle=style, color=color, linewidth=1.5, zorder=2)

    # Actor Quản lý connects to all
    draw_line(18, 85, 40, 98) # UC01
    draw_line(18, 85, 40, 84) # UC02
    draw_line(18, 85, 40, 70) # UC03
    draw_line(18, 85, 40, 56) # UC04
    draw_line(18, 85, 90, 92) # UC05
    draw_line(18, 85, 90, 76) # UC06
    draw_line(18, 85, 62, 22) # UC08

    # Actor Giáo viên connects to
    draw_line(18, 35, 43, 94) # Xem thông tin trẻ
    draw_line(18, 35, 43, 68) # Lớp học phân công
    draw_line(18, 35, 90, 89) # Xem thực đơn
    draw_line(18, 35, 65, 23) # UC08 (Đăng nhập/đổi pass)

    # Actor Phụ huynh connects to
    draw_line(142, 60, 68, 97) # Xem hồ sơ con
    draw_line(142, 60, 118, 92) # Xem thực đơn
    draw_line(142, 60, 120, 76) # Xem chi tiết học phí
    draw_line(142, 60, 120, 60) # UC07: Thanh toán VietQR
    draw_line(142, 60, 98, 22)  # UC08: Đăng nhập/đổi pass

    plt.title("SƠ ĐỒ USE CASE TỔNG THỂ HỆ THỐNG QUẢN LÝ MẦM NON", fontsize=16, fontweight='bold', pad=25, color='#0F172A')
    out_path = os.path.join(OUTPUT_DIR, "UseCase_TongThe_HeThong.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=200, bbox_inches='tight')
    plt.close()
    print("Exported:", out_path)

def create_class_diagram():
    fig, ax = plt.subplots(figsize=(18, 14), dpi=200)
    ax.set_xlim(0, 180)
    ax.set_ylim(0, 140)
    ax.axis('off')

    def draw_class(x, y, w, h, title, attributes, methods, header_color='#1E40AF'):
        # Header Box
        header_h = 4.5
        box = patches.Rectangle((x, y + h - header_h), w, header_h, facecolor=header_color, edgecolor='#0F172A', linewidth=1.5, zorder=3)
        ax.add_patch(box)
        ax.text(x + w/2, y + h - header_h/2, title, fontsize=10, fontweight='bold', color='white', ha='center', va='center', zorder=4)

        # Body Box
        body_box = patches.Rectangle((x, y), w, h - header_h, facecolor='#FFFFFF', edgecolor='#0F172A', linewidth=1.5, zorder=3)
        ax.add_patch(body_box)

        # Attributes
        curr_y = y + h - header_h - 2.5
        for attr in attributes:
            ax.text(x + 1.2, curr_y, attr, fontsize=7.5, color='#1E293B', va='center', zorder=4)
            curr_y -= 2.2

        # Separator line
        sep_y = curr_y - 0.5
        ax.plot([x, x + w], [sep_y, sep_y], color='#CBD5E1', linewidth=1, zorder=4)

        # Methods
        curr_y = sep_y - 2.2
        for m in methods:
            ax.text(x + 1.2, curr_y, m, fontsize=7.5, color='#0369A1', va='center', zorder=4)
            curr_y -= 2.2

    # Draw Classes
    # 1. TaiKhoan & VaiTro
    draw_class(8, 105, 34, 30, "TaiKhoan", 
               ["- id: int", "- username: String", "- password_hash: String", "- role_id: int", "- status: String", "- last_login: DateTime"],
               ["+ login(pass): boolean", "+ changePassword(newPass): void", "+ lockAccount(): void"], header_color='#475569')

    draw_class(8, 70, 34, 25, "VaiTro", 
               ["- id: int", "- role_name: String", "- description: String", "- permissions: List<String>"],
               ["+ checkPermission(p): boolean", "+ getRoleName(): String"], header_color='#475569')

    # 2. LopHoc & GiaoVien
    draw_class(50, 100, 36, 35, "LopHoc", 
               ["- id: int", "- ten_lop: String", "- khoi_lop: String", "- si_so_toi_da: int", "- nam_hoc: String"],
               ["+ getSiSoHienTai(): int", "+ themTreVaoLop(tre): boolean", "+ phanCongGiaoVien(gv): void", "+ getDanhSachTre(): List<Tre>"], header_color='#0D9488')

    draw_class(50, 55, 36, 35, "GiaoVien", 
               ["- id: int", "- ho_ten: String", "- ngay_sinh: Date", "- chuyen_mon: String", "- so_dien_thoai: String", "- email: String", "- id_lop: int", "- trang_thai: String"],
               ["+ capNhatHoSo(): void", "+ xemLopPhanCong(): LopHoc", "+ diemDanhTre(idTre, st): void"], header_color='#0D9488')

    # 3. Tre & PhuHuynh
    draw_class(94, 95, 38, 40, "Tre", 
               ["- id: int", "- ma_dinh_danh: String", "- ho_ten: String", "- ngay_sinh: Date", "- gioi_tinh: String", "- thong_tin_suc_khoe: String", "- dia_chi: String", "- trang_thai: String", "- id_lop: int"],
               ["+ capNhatSucKhoe(info): void", "+ chuyenLop(lopMoi): void", "+ xemThongTinLop(): LopHoc", "+ getPhuHuynhList(): List<PhuHuynh>"], header_color='#2563EB')

    draw_class(94, 45, 38, 38, "PhuHuynh", 
               ["- id: int", "- ho_ten: String", "- so_dien_thoai: String", "- email: String", "- dia_chi: String", "- cccd: String", "- nghe_nghiep: String"],
               ["+ xemThongTinCon(): List<Tre>", "+ xemThucDon(): List<ThucDon>", "+ xemHocPhi(): List<HocPhi>", "+ thucHienThanhToan(idHP): QR"], header_color='#2563EB')

    draw_class(94, 10, 38, 25, "PhuHuynh_Tre", 
               ["- id: int", "- id_phu_huynh: int", "- id_tre: int", "- quan_he: String", "- la_nguoi_giam_ho_chinh: boolean"],
               ["+ xacNhanGiamHo(): void"], header_color='#3B82F6')

    # 4. ThucDon & MonAn
    draw_class(138, 105, 36, 30, "ThucDon", 
               ["- id: int", "- ngay_ap_dung: Date", "- buoi_an: String", "- tuan_thu: int", "- ghi_chu: String"],
               ["+ themMonAn(mon): void", "+ getMonAnList(): List<MonAn>", "+ tinhTongCalo(): double"], header_color='#EA580C')

    draw_class(138, 65, 36, 30, "MonAn", 
               ["- id: int", "- ten_mon: String", "- loai_mon: String", "- calo: double", "- thanh_phan: String", "- don_gia_uoc_tinh: double"],
               ["+ capNhatThanhPhan(): void", "+ getInfo(): String"], header_color='#EA580C')

    # 5. HocPhi, ChiTiet, ThanhToan
    draw_class(138, 12, 38, 42, "HocPhi", 
               ["- id: int", "- id_tre: int", "- thang: int", "- nam: int", "- hoc_phi_co_ban: double", "- so_ngay_an: int", "- don_gia_an_ngay: double", "- tien_an: double", "- phi_dich_vu: double", "- giam_tru: double", "- tong_tien: double", "- trang_thai: String"],
               ["+ tinhTongTien(): double", "+ taoQRThanhToan(): String", "+ xacNhanThanhToan(): void", "+ inPhieuThu(): File"], header_color='#16A34A')

    # Helper for relations
    def draw_rel(x1, y1, x2, y2, label="", mult1="", mult2="", style='-'):
        ax.plot([x1, x2], [y1, y2], linestyle=style, color='#334155', linewidth=1.5, zorder=2)
        if label:
            mx, my = (x1 + x2)/2, (y1 + y2)/2
            ax.text(mx, my + 1.2, label, fontsize=8, fontweight='bold', color='#1E293B', ha='center', bbox=dict(boxstyle="round,pad=0.2", facecolor='#F1F5F9', edgecolor='none'))
        if mult1:
            ax.text(x1 + 1, y1 + 1, mult1, fontsize=8, color='#0F172A', fontweight='bold')
        if mult2:
            ax.text(x2 + 1, y2 + 1, mult2, fontsize=8, color='#0F172A', fontweight='bold')

    # Connections
    draw_rel(25, 105, 25, 95, label="", mult1="1", mult2="1..*") # TaiKhoan - VaiTro
    draw_rel(68, 100, 68, 90, label="1..* gv", mult1="1", mult2="1..*") # Lop - GiaoVien
    draw_rel(86, 115, 94, 115, label="1 lớp chứa", mult1="1", mult2="0..*") # Lop - Tre
    draw_rel(113, 95, 113, 83, label="liên kết", mult1="1", mult2="1..*") # Tre - PhuHuynh_Tre
    draw_rel(113, 45, 113, 35, label="gồm", mult1="1", mult2="1..*") # PhuHuynh - PhuHuynh_Tre
    draw_rel(156, 105, 156, 95, label="chứa", mult1="1..*", mult2="1..*") # ThucDon - MonAn
    draw_rel(132, 110, 138, 30, label="phát sinh", mult1="1", mult2="0..*") # Tre - HocPhi

    plt.title("SƠ ĐỒ LỚP CHI TIẾT (CLASS DIAGRAM) TOÀN HỆ THỐNG MẦM NON", fontsize=16, fontweight='bold', pad=25, color='#0F172A')
    out_path = os.path.join(OUTPUT_DIR, "ClassDiagram_ToanHeThong.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=200, bbox_inches='tight')
    plt.close()
    print("Exported:", out_path)

def create_payment_sequence_diagram():
    fig, ax = plt.subplots(figsize=(15, 10), dpi=200)
    ax.set_xlim(0, 150)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Lifelines
    actors = [
        (20, "Phụ huynh\n(Parent)"),
        (55, "Giao diện Web/App\n(Frontend)"),
        (90, "Hệ thống KMS\n(Backend/API)"),
        (130, "Cổng Napas / Ngân hàng\n(VietQR Gateway)")
    ]

    for x, title in actors:
        # Box
        rect = patches.FancyBboxPatch((x-14, 88), 28, 8, boxstyle="round,pad=0.5", facecolor='#1E40AF', edgecolor='#0F172A', linewidth=1.2)
        ax.add_patch(rect)
        ax.text(x, 92, title, fontsize=9.5, fontweight='bold', color='white', ha='center', va='center')
        # Line
        ax.plot([x, x], [88, 10], linestyle='--', color='#94A3B8', linewidth=1.5)

    def draw_msg(y, x1, x2, text, is_return=False, note=""):
        style = '--' if is_return else '-'
        color = '#0284C7' if not is_return else '#059669'
        ax.annotate('', xy=(x2, y), xytext=(x1, y),
                    arrowprops=dict(arrowstyle="->", color=color, lw=1.6, linestyle=style))
        mid_x = (x1 + x2)/2
        ax.text(mid_x, y + 1.2, text, fontsize=8.5, fontweight='bold', color='#1E293B', ha='center')
        if note:
            ax.text(mid_x, y - 1.8, note, fontsize=7.5, fontstyle='italic', color='#64748B', ha='center')

    # Sequence steps
    draw_msg(80, 20, 55, "1. Chọn 'Xem học phí & tiền ăn'", note="Gửi yêu cầu tra cứu phiếu thu")
    draw_msg(73, 55, 90, "2. GET /api/v1/hoc-phi?tre_id={id}")
    draw_msg(66, 90, 55, "3. Trả về thông tin: Học phí + Tiền ăn (Số ngày x Đơn giá) - Giảm trừ", is_return=True)
    draw_msg(59, 55, 20, "4. Hiển thị tổng tiền cần thanh toán", is_return=True)
    draw_msg(52, 20, 55, "5. Nhấn nút 'Thanh toán trực tuyến VietQR'")
    draw_msg(45, 55, 90, "6. POST /api/v1/payment/create-qr (id_hoc_phi)")
    draw_msg(38, 90, 130, "7. Khởi tạo giao dịch VietQR động chuẩn EMVCo")
    draw_msg(31, 130, 90, "8. Trả về chuỗi QR Payload & mã thanh toán", is_return=True)
    draw_msg(24, 90, 55, "9. Trả về hình ảnh mã QR & thông tin chuyển khoản", is_return=True)
    draw_msg(17, 55, 20, "10. Phụ huynh quét QR bằng App Mobile Banking", is_return=True)
    draw_msg(11, 130, 90, "11. Webhook IPN: Xác nhận thanh toán thành công", note="Cập nhật trạng thái phiếu học phí -> 'Đã thanh toán'")

    plt.title("SƠ ĐỒ TUẦN TỰ (SEQUENCE DIAGRAM): QUY TRÌNH THANH TOÁN HỌC PHÍ VIETQR", fontsize=15, fontweight='bold', pad=25, color='#0F172A')
    out_path = os.path.join(OUTPUT_DIR, "Sequence_ThanhToan_VietQR.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=200, bbox_inches='tight')
    plt.close()
    print("Exported:", out_path)

create_overall_usecase_diagram()
create_class_diagram()
create_payment_sequence_diagram()
