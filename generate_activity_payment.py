import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

OUTPUT_DIR = r"e:\CNPM\CNPM\astah_export\EXTRA"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_activity_payment():
    fig, ax = plt.subplots(figsize=(14, 11), dpi=200)
    ax.set_xlim(0, 140)
    ax.set_ylim(0, 110)
    ax.axis('off')

    # Swimlanes
    # Lane 1: Phụ huynh (0 - 45)
    # Lane 2: Hệ thống KMS (45 - 95)
    # Lane 3: Cổng thanh toán VietQR / Ngân hàng (95 - 140)

    rect1 = patches.Rectangle((5, 5), 40, 100, facecolor='#F8FAFC', edgecolor='#CBD5E1', linewidth=1.5)
    rect2 = patches.Rectangle((45, 5), 50, 100, facecolor='#F0F9FF', edgecolor='#CBD5E1', linewidth=1.5)
    rect3 = patches.Rectangle((95, 5), 40, 100, facecolor='#F8FAFC', edgecolor='#CBD5E1', linewidth=1.5)
    ax.add_patch(rect1)
    ax.add_patch(rect2)
    ax.add_patch(rect3)

    ax.text(25, 101, "PHỤ HUYNH", fontsize=11, fontweight='bold', color='#1E40AF', ha='center')
    ax.text(70, 101, "HỆ THỐNG KMS", fontsize=11, fontweight='bold', color='#0369A1', ha='center')
    ax.text(115, 101, "CỔNG VIETQR / NGÂN HÀNG", fontsize=11, fontweight='bold', color='#15803D', ha='center')

    # Start node
    ax.plot([25], [94], marker='o', markersize=14, color='#0F172A')

    def draw_action(x, y, w, h, text, color='#FFFFFF', edge='#2563EB'):
        r = patches.FancyBboxPatch((x-w/2, y-h/2), w, h, boxstyle="round,pad=0.4,rounding_size=1.5",
                                   facecolor=color, edgecolor=edge, linewidth=1.5, zorder=3)
        ax.add_patch(r)
        ax.text(x, y, text, fontsize=8.5, fontweight='bold', color='#0F172A', ha='center', va='center', zorder=4)

    def draw_decision(x, y, w, h):
        diamond = patches.Polygon([[x, y+h/2], [x+w/2, y], [x, y-h/2], [x-w/2, y]],
                                  facecolor='#FEF3C7', edgecolor='#D97706', linewidth=1.5, zorder=3)
        ax.add_patch(diamond)

    def draw_arrow(x1, y1, x2, y2, label=""):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->", color='#334155', lw=1.5), zorder=2)
        if label:
            mx, my = (x1+x2)/2, (y1+y2)/2
            ax.text(mx+1, my+1, label, fontsize=8, fontweight='bold', color='#B45309')

    # Actions
    draw_arrow(25, 93, 25, 87)
    draw_action(25, 84, 30, 6, "Đăng nhập & Chọn\n'Xem Học Phí'")
    draw_arrow(25, 81, 70, 81)

    draw_action(70, 81, 38, 7, "Tính: Tiền ăn + Học phí cơ bản\n+ Phí DV - Giảm trừ")
    draw_arrow(70, 77.5, 25, 71)

    draw_action(25, 71, 30, 6, "Xem chi tiết phiếu thu\n& Chọn 'Thanh toán QR'")
    draw_arrow(25, 68, 70, 62)

    draw_action(70, 62, 38, 6, "Tạo mã thanh toán động\n& chuỗi VietQR NAPAS")
    draw_arrow(70, 59, 25, 53)

    draw_action(25, 53, 30, 6, "Quét mã QR qua\nApp Ngân hàng")
    draw_arrow(25, 50, 115, 50)

    draw_action(115, 50, 32, 6, "Xử lý giao dịch\nchuyển khoản 24/7")
    draw_arrow(115, 47, 115, 39)

    draw_decision(115, 36, 16, 7)
    ax.text(115, 36, "Hợp lệ?", fontsize=7.5, fontweight='bold', ha='center', va='center', zorder=4)

    # Success branch
    draw_arrow(115, 32.5, 70, 24, label="[Thành công]")
    draw_action(70, 24, 38, 6, "Cập nhật trạng thái:\n'ĐÃ THANH TOÁN'")
    draw_arrow(70, 21, 25, 15)

    draw_action(25, 15, 30, 6, "Nhận biên lai điện tử\n& hoàn tất")

    # Failure branch
    ax.plot([123, 132, 132, 25], [36, 36, 68, 68], color='#DC2626', linestyle='--', linewidth=1.5)
    ax.text(133, 50, "[Thất bại/Hết hạn]", fontsize=7.5, fontweight='bold', color='#DC2626')

    # End node
    ax.plot([25], [9], marker='o', markersize=14, color='#0F172A')
    ax.plot([25], [9], marker='o', markersize=9, color='white')
    ax.plot([25], [9], marker='o', markersize=6, color='#0F172A')
    draw_arrow(25, 12, 25, 10.5)

    plt.title("SƠ ĐỒ HOẠT ĐỘNG (ACTIVITY DIAGRAM): QUY TRÌNH THANH TOÁN VIETQR", fontsize=15, fontweight='bold', pad=25, color='#0F172A')
    out_path = os.path.join(OUTPUT_DIR, "Activity_ThanhToan_VietQR.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=200, bbox_inches='tight')
    plt.close()
    print("Exported:", out_path)

create_activity_payment()
