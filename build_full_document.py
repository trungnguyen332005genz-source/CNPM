# -*- coding: utf-8 -*-
import os
import shutil
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def create_full_document():
    doc = Document()

    # Page Margins
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Styles
    styles = doc.styles
    normal_style = styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(12)
    normal_style.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)

    # -------------------------------------------------------------
    # 1. BÌA BÁO CÁO (COVER PAGE)
    # -------------------------------------------------------------
    p_uni = doc.add_paragraph()
    p_uni.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_uni = p_uni.add_run("BỘ GIÁO DỤC VÀ ĐÀO TẠO\nTRƯỜNG ĐẠI HỌC VĂN HIẾN\nKHOA CÔNG NGHỆ THÔNG TIN\n")
    run_uni.font.name = 'Times New Roman'
    run_uni.font.size = Pt(13)
    run_uni.font.bold = True
    run_uni.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    doc.add_paragraph("\n" * 3)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_title = p_title.add_run("BÁO CÁO ĐỒ ÁN MÔN HỌC\nCÔNG NGHỆ PHẦN MỀM (CNPM)\n")
    run_title.font.name = 'Times New Roman'
    run_title.font.size = Pt(18)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(0x1E, 0x40, 0xAF)

    p_subtitle = doc.add_paragraph()
    p_subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_sub = p_subtitle.add_run("ĐỀ TÀI:\nPHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG QUẢN LÝ TRƯỜNG MẦM NON TƯ THỤC (KMS)")
    run_sub.font.name = 'Times New Roman'
    run_sub.font.size = Pt(16)
    run_sub.font.bold = True
    run_sub.font.color.rgb = RGBColor(0xDC, 0x26, 0x26)

    doc.add_paragraph("\n" * 4)

    # Student Info Box
    p_info = doc.add_paragraph()
    p_info.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_info.paragraph_format.left_indent = Inches(1.5)
    
    def add_info_line(p, label, val):
        r1 = p.add_run(f"{label}: ")
        r1.font.bold = True
        r1.font.size = Pt(12)
        r2 = p.add_run(f"{val}\n")
        r2.font.size = Pt(12)

    add_info_line(p_info, "Sinh viên thực hiện", "Trần Trung Nguyên")
    add_info_line(p_info, "Mã số sinh viên (MSSV)", "231A290096")
    add_info_line(p_info, "Môn học", "Công Nghệ Phần Mềm")
    add_info_line(p_info, "Công cụ mô hình hóa", "Astah Community / UML 2.0")
    add_info_line(p_info, "Mã nguồn dự án Git", "https://github.com/trungnguyen332005genz-source/CNPM.git")

    doc.add_paragraph("\n" * 4)

    p_footer = doc.add_paragraph()
    p_footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_foot = p_footer.add_run("TP. HỒ CHÍ MINH - NĂM 2026")
    run_foot.font.name = 'Times New Roman'
    run_foot.font.size = Pt(12)
    run_foot.font.bold = True

    doc.add_page_break()

    # -------------------------------------------------------------
    # HELPER FUNCTIONS FOR HEADINGS & CALLOUTS
    # -------------------------------------------------------------
    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(8)
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(15)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(6)
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(13)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0x03, 0x69, 0xA1)
        return p

    def add_h3(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
        return p

    def add_p(text, bold=False, italic=False):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(5)
        p.paragraph_format.line_spacing = 1.15
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        run.font.bold = bold
        run.font.italic = italic
        return p

    def add_callout(text, title="LƯU Ý NGHIỆP VỤ"):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = tbl.cell(0, 0)
        set_cell_background(cell, "EFF6FF")
        set_cell_margins(cell, 120, 120, 200, 200)
        p = cell.paragraphs[0]
        r1 = p.add_run(f"📌 {title}: ")
        r1.font.bold = True
        r1.font.color.rgb = RGBColor(0x1D, 0x4E, 0xD8)
        r2 = p.add_run(text)
        r2.font.italic = True
        doc.add_paragraph()

    def add_diagram(img_path, caption):
        if os.path.exists(img_path):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(8)
            doc.add_picture(img_path, width=Inches(6.0))
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_after = Pt(12)
            r = p_cap.add_run(f"Hình: {caption}")
            r.font.name = 'Times New Roman'
            r.font.size = Pt(10.5)
            r.font.italic = True
            r.font.bold = True
            r.font.color.rgb = RGBColor(0x47, 0x55, 0x69)
        else:
            add_p(f"*(Hình ảnh: {caption} - Chưa tìm thấy đường dẫn: {img_path})*", italic=True)

    # -------------------------------------------------------------
    # CHƯƠNG 1: TỔNG QUAN HỆ THỐNG
    # -------------------------------------------------------------
    add_h1("CHƯƠNG 1: GIỚI THIỆU VÀ TỔNG QUAN HỆ THỐNG")
    
    add_h2("1.1. Đặt vấn đề và Mục đích xây dựng")
    add_p("Trong bối cảnh các trường mầm non tư thục ngày càng phát triển về số lượng và quy mô, công tác quản lý thủ công truyền thống qua sổ sách và các file bảng tính rời rạc bộc lộ nhiều hạn chế nghiêm trọng: dữ liệu dễ thất lạc, sai sót trong tính toán tiền ăn và học phí, tra cứu hồ sơ trẻ em và giáo viên chậm chạp, đồng thời thiếu kênh kết nối minh bạch, kịp thời với phụ huynh học sinh.")
    add_p("Hệ thống Quản lý Mầm non (Kindergarten Management System - KMS) được xây dựng nhằm mục đích tin học hóa toàn diện và hỗ trợ cơ sở mầm non tư thục quản lý tập trung toàn bộ dữ liệu: thông tin trẻ em, đội ngũ giáo viên, thông tin phụ huynh, phân công lớp học, dinh dưỡng thực đơn hằng ngày, tính toán tự động học phí - tiền ăn theo số ngày ăn thực tế, và hỗ trợ thanh toán học phí trực tuyến thuận tiện qua mã QR.")

    add_h2("1.2. Mục tiêu trọng tâm của hệ thống")
    add_p("• Thay thế 100% quản lý thủ công bằng sổ sách: Tự động hóa quá trình lập hồ sơ, phân công giảng dạy, lập thực đơn và thu phát học phí.")
    add_p("• Tra cứu thông tin nhanh chóng, chính xác: Hỗ trợ tìm kiếm đa tiêu chí (theo mã định danh, họ tên, lớp học, ngày sinh, tình trạng sức khỏe...).")
    add_p("• Tăng cường tương tác Phụ huynh - Nhà trường: Cho phép phụ huynh dễ dàng theo dõi thực đơn dinh dưỡng theo tuần/ngày, theo dõi sức khỏe con em, kiểm tra chi tiết bảng tính học phí và quét mã QR chuyển khoản ngay trên thiết bị di động.")

    add_h2("1.3. Đối tượng sử dụng (Actors) và Ma trận phân quyền")
    add_p("Hệ thống xác định 3 nhóm tác nhân chính tham gia tương tác trực tiếp:")
    
    # Bảng Đối tượng
    tbl_actors = doc.add_table(rows=4, cols=3)
    tbl_actors.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ["Actor (Tác nhân)", "Mô tả nghiệp vụ", "Quyền hạn chính trên hệ thống"]
    for i, h in enumerate(headers):
        cell = tbl_actors.cell(0, i)
        set_cell_background(cell, "1E3A8A")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    actors_data = [
        ("Quản lý (Admin)", "Ban giám hiệu, chủ trường hoặc bộ phận quản trị cơ sở mầm non.", "Toàn quyền quản trị toàn bộ hoạt động, danh mục, lớp học, tài khoản, thực đơn, học phí và báo cáo thống kê."),
        ("Giáo viên (Teacher)", "Giáo viên chủ nhiệm, giáo viên bộ môn và bảo mẫu trực tiếp chăm sóc trẻ.", "Xem và quản lý hồ sơ trẻ, theo dõi sức khỏe, xem thực đơn và điểm danh trong phạm vi lớp học được phân công."),
        ("Phụ huynh (Parent)", "Cha, mẹ hoặc người giám hộ hợp pháp của trẻ theo học tại trường.", "Xem hồ sơ con, theo dõi thực đơn tuần, tra cứu bảng tính học phí & tiền ăn chi tiết, tạo và quét mã VietQR thanh toán trực tuyến.")
    ]
    for row_idx, data in enumerate(actors_data, start=1):
        for col_idx, text in enumerate(data):
            cell = tbl_actors.cell(row_idx, col_idx)
            set_cell_margins(cell, 80, 80, 100, 100)
            p = cell.paragraphs[0]
            if col_idx == 0:
                p.add_run(text).font.bold = True
            else:
                p.add_run(text)
            if row_idx % 2 == 1:
                set_cell_background(cell, "F8FAFC")

    add_callout("Các chức năng Quản lý lớp học và Quản lý tài khoản & phân quyền là nền tảng cốt lõi bắt buộc, vì tất cả các module nghiệp vụ khác (Trẻ em, Giáo viên, Thực đơn, Học phí, Thanh toán) đều có quan hệ phụ thuộc chặt chẽ vào hai module này.", "LƯU Ý CỐT LÕI HỆ THỐNG")

    # -------------------------------------------------------------
    # CHƯƠNG 2: PHÂN TÍCH CHI TIẾT 8 PHÂN HỆ NGHIỆP VỤ
    # -------------------------------------------------------------
    add_h1("CHƯƠNG 2: PHÂN TÍCH YÊU CẦU CHỨC NĂNG CHI TIẾT (8 PHÂN HỆ)")

    # 2.1 Quản lý trẻ em
    add_h2("2.1. Phân hệ 1: Quản lý trẻ em (Chức năng trung tâm)")
    add_p("Mô tả: Quản lý trẻ em là phân hệ trung tâm của toàn bộ hệ thống. Toàn bộ thông tin học tập, phân lớp, dinh dưỡng thực đơn, tiền ăn và học phí đều xoay quanh thực thể Trẻ em.")
    add_p("Các chức năng và Use Case thành phần:")
    add_p(" • Xem danh sách trẻ: Hiển thị đầy đủ danh sách học sinh theo khối, lớp, trạng thái.")
    add_p(" • Thêm trẻ mới: Tiếp nhận học sinh mới vào trường, nhập thông tin cá nhân, ngày sinh, sức khỏe ban đầu.")
    add_p(" • Xem hồ sơ chi tiết trẻ: Tra cứu lý lịch, tiền sử bệnh, dị ứng thực phẩm, danh sách phụ huynh liên kết.")
    add_p(" • Cập nhật thông tin trẻ: Điều chỉnh thông tin cá nhân, sức khỏe hoặc ghi chú của giáo viên.")
    add_p(" • Xóa / Chuyển trạng thái trẻ: Chuyển trạng thái giữa Đang học, Nghỉ học, Đã chuyển trường.")
    add_p(" • Tìm kiếm và Lọc trẻ: Tìm kiếm thông minh theo họ tên, mã định danh; lọc theo lớp học và trạng thái học.")
    add_p(" • Quản lý thông tin sức khỏe cơ bản: Chiều cao, cân nặng định kỳ, chế độ dinh dưỡng đặc biệt.")
    add_p(" • Liên kết trẻ với phụ huynh: Thiết lập quan hệ 1-N (một phụ huynh có thể có nhiều con cùng học).")

    # 2.2 Quản lý giáo viên
    add_h2("2.2. Phân hệ 2: Quản lý giáo viên")
    add_p("Mô tả: Quản lý toàn bộ hồ sơ chuyên môn và quá trình công tác của giáo viên tại cơ sở.")
    add_p("Các chức năng thành phần:")
    add_p(" • Xem danh sách giáo viên: Xem toàn bộ đội ngũ cán bộ, giáo viên đang công tác.")
    add_p(" • Thêm mới giáo viên: Tiếp nhận hồ sơ, gán mã giáo viên, số điện thoại, trình độ chuyên môn.")
    add_p(" • Cập nhật hồ sơ giáo viên: Thay đổi số điện thoại, địa chỉ, chuyên môn đào tạo.")
    add_p(" • Khóa / Đổi trạng thái làm việc: Chuyển trạng thái sang Đang làm việc, Nghỉ phép, Đã nghỉ việc.")
    add_p(" • Phân công giáo viên vào lớp học: Gán giáo viên làm Chủ nhiệm hoặc Phó chủ nhiệm của một lớp cụ thể.")

    # 2.3 Quản lý phụ huynh
    add_h2("2.3. Phân hệ 3: Quản lý phụ huynh")
    add_p("Mô tả: Lưu trữ thông tin liên lạc của phụ huynh và quản lý mối quan hệ bảo trợ đối với trẻ em.")
    add_p("Các chức năng thành phần:")
    add_p(" • Quản lý danh sách phụ huynh: Họ tên, số điện thoại, địa chỉ, CCCD, email.")
    add_p(" • Thiết lập quan hệ bảo trợ: Xác định rõ quan hệ (Bố, Mẹ, Ông, Bà, Người giám hộ hợp pháp).")
    add_p(" • Cho phép phụ huynh truy cập ứng dụng: Đăng nhập để theo dõi hồ sơ con, bảng học phí và thực đơn.")

    # 2.4 Quản lý lớp học
    add_h2("2.4. Phân hệ 4: Quản lý lớp học")
    add_p("Mô tả: Quản lý cơ cấu phòng ban học tập theo lứa tuổi (Nhà trẻ, Mầm, Chồi, Lá).")
    add_p("Các chức năng thành phần:")
    add_p(" • Quản lý danh sách lớp học: Tên lớp (Lá 1, Chồi 1...), khối lớp, sĩ số tối đa quy định.")
    add_p(" • Phân bổ học sinh vào lớp: Đảm bảo sĩ số lớp không vượt quá sĩ số tối đa.")
    add_p(" • Phân công giáo viên chủ nhiệm & giáo viên phụ trách lớp.")

    # 2.5 Quản lý thực đơn
    add_h2("2.5. Phân hệ 5: Quản lý thực đơn dinh dưỡng")
    add_p("Mô tả: Xây dựng khẩu phần ăn theo chuẩn dinh dưỡng lứa tuổi mầm non theo tuần và ngày.")
    add_p("Các chức năng thành phần:")
    add_p(" • Lập thực đơn theo ngày / tuần: Quản lý thực đơn cho từng ngày trong tuần (Thứ Hai đến Thứ Sáu).")
    add_p(" • Quản lý các bữa ăn: Bữa sáng, Bữa trưa, Bữa xế/phụ chiều.")
    add_p(" • Quản lý danh mục món ăn: Tên món, phân loại dinh dưỡng, calo, thành phần và đơn giá ước tính.")
    add_p(" • Công khai thực đơn cho Phụ huynh: Phụ huynh có thể xem thực đơn con ăn trong ngày ngay trên app.")

    # 2.6 Quản lý học phí và tiền ăn
    add_h2("2.6. Phân hệ 6: Quản lý học phí và tiền ăn")
    add_p("Mô tả: Tự động hóa quá trình tổng hợp số ngày ăn thực tế, kết hợp mức học phí và các khoản phí dịch vụ để phát hành phiếu thu học phí hằng tháng.")
    add_p("Công thức tính học phí nghiệp vụ:")
    add_callout(
        "Tổng tiền phải trả = Học phí cơ bản + Tiền ăn + Phí dịch vụ + Phí khác - Giảm trừ\n"
        "Trong đó:\n"
        " • Tiền ăn = Số ngày ăn thực tế × Đơn giá tiền ăn/ngày\n"
        " • Giảm trừ: Miễn giảm diện chính sách, con thứ 2 cùng học, v.v.\n\n"
        "Ví dụ minh họa:\n"
        " - Học phí cơ bản: 1.500.000 VNĐ\n"
        " - Tiền ăn (20 ngày × 30.000 VNĐ/ngày): 600.000 VNĐ\n"
        " - Phí dịch vụ & Phí khác: 100.000 VNĐ\n"
        " - Giảm trừ: 0 VNĐ\n"
        " => TỔNG TIỀN PHẢI THANH TOÁN: 2.200.000 VNĐ",
        "CÔNG THỨC VÀ QUY TẮC TÍNH TOÁN HỌC PHÍ"
    )

    # 2.7 Thanh toán
    add_h2("2.7. Phân hệ 7: Quản lý thanh toán học phí trực tuyến (VietQR)")
    add_p("Mô tả: Hỗ trợ phụ huynh thanh toán học phí qua mã QR động (chuẩn VietQR Napas 247). Hệ thống tự sinh mã QR chứa đầy đủ số tiền, số tài khoản nhà trường và nội dung chuyển khoản mã phiếu thu duy nhất, tự động kiểm tra và cập nhật trạng thái phiếu học phí thành 'Đã thanh toán'.")
    add_p("Quy trình 6 bước khép kín:")
    add_p(" 1. Phụ huynh đăng nhập -> Chọn chức năng 'Xem học phí & tiền ăn'.")
    add_p(" 2. Xem chi tiết các khoản phí -> Nhấn chọn 'Thanh toán trực tuyến'.")
    add_p(" 3. Hệ thống sinh mã VietQR động chứa chính xác số tiền và mã đối soát.")
    add_p(" 4. Phụ huynh mở ứng dụng Mobile Banking của bất kỳ ngân hàng nào và quét mã QR.")
    add_p(" 5. Ngân hàng xử lý chuyển khoản Napas 24/7 và gửi phản hồi trạng thái (IPN/Webhook).")
    add_p(" 6. Hệ thống tự động ghi nhận giao dịch thành công và chuyển trạng thái phiếu thu sang 'ĐÃ THANH TOÁN'.")

    # 2.8 Tài khoản & Phân quyền
    add_h2("2.8. Phân hệ 8: Quản lý tài khoản và phân quyền người dùng")
    add_p("Mô tả: Đảm bảo tính bảo mật và toàn vẹn dữ liệu cho toàn bộ hệ thống.")
    add_p(" • Quản lý xác thực: Đăng nhập bằng tài khoản/mật khẩu được mã hóa an toàn (BCrypt), đăng xuất, đổi mật khẩu.")
    add_p(" • Phân quyền vai trò: Role-Based Access Control (RBAC) với 3 vai trò Quản lý, Giáo viên, Phụ huynh.")

    # -------------------------------------------------------------
    # CHƯƠNG 3: BẢNG ĐẶC TẢ USE CASE CHI TIẾT
    # -------------------------------------------------------------
    add_h1("CHƯƠNG 3: ĐẶC TẢ USE CASE CHI TIẾT (USE CASE SPECIFICATIONS)")

    def add_uc_table(uc_id, uc_name, actor, desc, pre_cond, post_cond, main_flow, alt_flow, exc_flow):
        tbl = doc.add_table(rows=8, cols=2)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        fields = [
            ("Mã Use Case", uc_id),
            ("Tên Use Case", uc_name),
            ("Tác nhân (Actor)", actor),
            ("Mô tả tóm tắt", desc),
            ("Tiền điều kiện", pre_cond),
            ("Hậu điều kiện", post_cond),
            ("Luồng sự kiện chính (Main Flow)", main_flow),
            ("Luồng phụ & Ngoại lệ", f"Luồng phụ: {alt_flow}\nNgoại lệ: {exc_flow}")
        ]
        for idx, (label, val) in enumerate(fields):
            cell_lbl = tbl.cell(idx, 0)
            cell_val = tbl.cell(idx, 1)
            cell_lbl.width = Inches(2.0)
            cell_val.width = Inches(4.5)
            set_cell_background(cell_lbl, "F1F5F9")
            set_cell_margins(cell_lbl, 60, 60, 80, 80)
            set_cell_margins(cell_val, 60, 60, 80, 80)
            p_lbl = cell_lbl.paragraphs[0]
            p_lbl.add_run(label).font.bold = True
            p_val = cell_val.paragraphs[0]
            p_val.add_run(val)
        doc.add_paragraph()

    add_h2("3.1. Đặc tả Use Case UC01: Quản lý hồ sơ trẻ em")
    add_uc_table(
        "UC01_CHILD", "Tiếp nhận và quản lý hồ sơ trẻ em", "Quản lý (Admin), Giáo viên",
        "Thực hiện xem danh sách, thêm học sinh mới, sửa thông tin, xóa hoặc chuyển trạng thái học sinh.",
        "Người dùng đã đăng nhập hệ thống với quyền Quản lý hoặc Giáo viên.",
        "Thông tin trẻ được lưu vào CSDL; hồ sơ sức khỏe và phân lớp được cập nhật.",
        "1. Quản lý chọn menu 'Quản lý trẻ em'.\n2. Hệ thống hiển thị danh sách toàn bộ trẻ.\n3. Quản lý nhấn 'Thêm trẻ mới' và điền họ tên, ngày sinh, giới tính, tiền sử bệnh, chọn lớp học.\n4. Quản lý nhấn 'Lưu'.\n5. Hệ thống kiểm tra hợp lệ, lưu vào CSDL và thông báo thành công.",
        "Người dùng có thể tìm kiếm theo tên hoặc lọc theo lớp/trạng thái.",
        "Nếu để trống trường bắt buộc hoặc ngày sinh không hợp lệ, hệ thống báo lỗi và yêu cầu nhập lại."
    )

    add_h2("3.2. Đặc tả Use Case UC02: Quản lý giáo viên và phân công lớp")
    add_uc_table(
        "UC02_TEACHER", "Quản lý thông tin và phân công giáo viên", "Quản lý (Admin)",
        "Quản lý hồ sơ chuyên môn và phân công giáo viên vào làm chủ nhiệm hoặc phụ trách lớp học.",
        "Quản lý đã đăng nhập với quyền Quản trị.",
        "Giáo viên được gán vào lớp tương ứng; giáo viên có quyền xem danh sách trẻ của lớp đó.",
        "1. Quản lý vào menu 'Quản lý giáo viên'.\n2. Xem danh sách hoặc chọn 'Phân công lớp'.\n3. Chọn giáo viên và chọn lớp học trong danh sách.\n4. Nhấn 'Xác nhận phân công'.\n5. Hệ thống cập nhật bảng liên kết và gửi thông báo thành công.",
        "Nếu giáo viên đã được phân công lớp trước đó, hệ thống hỏi xác nhận điều chuyển.",
        "Lớp học đã đủ số lượng giáo viên phụ trách thì cảnh báo người dùng."
    )

    add_h2("3.3. Đặc tả Use Case UC03: Lập và quản lý thực đơn tuần")
    add_uc_table(
        "UC03_MENU", "Quản lý thực đơn dinh dưỡng", "Quản lý, Phụ huynh (chỉ xem)",
        "Xây dựng danh mục món ăn và lập lịch thực đơn theo ngày, tuần cho trẻ.",
        "Đã đăng nhập hệ thống.",
        "Thực đơn tuần mới được lưu trữ và hiển thị cho giáo viên và phụ huynh theo dõi.",
        "1. Quản lý vào menu 'Quản lý thực đơn'.\n2. Chọn tuần và thứ trong tuần cần lập.\n3. Thêm các món cho Bữa sáng, Bữa trưa, Bữa xế.\n4. Hệ thống tính tổng lượng Calo ước tính.\n5. Quản lý nhấn 'Lưu và Công khai'.",
        "Phụ huynh chỉ truy cập chức năng xem thực đơn tuần hiện tại của con mình.",
        "Món ăn chưa có trong danh mục: Cho phép thêm mới món ăn trước khi đưa vào thực đơn."
    )

    add_h2("3.4. Đặc tả Use Case UC04: Tính học phí và tiền ăn hằng tháng")
    add_uc_table(
        "UC04_FEE", "Tính toán và phát hành phiếu học phí", "Quản lý (Admin)",
        "Tính tiền ăn dựa trên số ngày ăn thực tế kết hợp học phí cơ bản để phát hành phiếu thu cho từng trẻ.",
        "Đến kỳ tổng kết học phí hằng tháng; dữ liệu số ngày ăn của trẻ đã được ghi nhận.",
        "Phiếu học phí được tạo với trạng thái 'Chưa thanh toán' và hiển thị cho phụ huynh.",
        "1. Quản lý chọn 'Quản lý học phí' -> Chọn 'Tạo phiếu học phí tháng'.\n2. Chọn lớp học hoặc toàn trường.\n3. Hệ thống tự động tính: Học phí cơ bản + (Số ngày ăn x Đơn giá) + Phí DV - Giảm trừ.\n4. Quản lý kiểm tra và duyệt phát hành phiếu.\n5. Hệ thống lưu phiếu học phí và gửi thông báo tới phụ huynh.",
        "Quản lý có thể nhập thêm khoản giảm trừ cá biệt cho từng học sinh cụ thể.",
        "Nếu học sinh nghỉ học dài ngày có đơn phép, hệ thống tự động hoàn trừ tiền ăn tương ứng."
    )

    add_h2("3.5. Đặc tả Use Case UC05: Thanh toán học phí trực tuyến qua VietQR")
    add_uc_table(
        "UC05_PAY", "Thanh toán học phí bằng mã QR VietQR", "Phụ huynh (Parent)",
        "Phụ huynh xem bảng tính học phí và quét mã QR động để chuyển khoản nhanh 24/7.",
        "Phụ huynh đã đăng nhập và có phiếu học phí ở trạng thái 'Chưa thanh toán'.",
        "Phiếu học phí được cập nhật sang 'Đã thanh toán', sinh biên lai thu học phí điện tử.",
        "1. Phụ huynh chọn 'Xem học phí con'.\n2. Kiểm tra chi tiết các khoản tiền -> Nhấn 'Thanh toán trực tuyến'.\n3. Hệ thống hiển thị mã VietQR động chứa số tiền và nội dung chuyển khoản.\n4. Phụ huynh mở app ngân hàng quét mã và xác nhận chuyển khoản.\n5. Ngân hàng xác nhận giao dịch -> Hệ thống đổi trạng thái sang 'ĐÃ THANH TOÁN'.",
        "Phụ huynh có thể tải hình ảnh mã QR về máy để chuyển khoản sau.",
        "Nếu quá thời gian hiệu lực của mã QR (15 phút), yêu cầu phụ huynh bấm tạo lại mã."
    )

    # -------------------------------------------------------------
    # CHƯƠNG 4: THIẾT KẾ MÔ HÌNH UML VÀ BIỂU ĐỒ ASTAH
    # -------------------------------------------------------------
    add_h1("CHƯƠNG 4: THIẾT KẾ MÔ HÌNH UML HỆ THỐNG (ASTAH COMMUNITY)")

    add_h2("4.1. Sơ đồ Use Case tổng thể và Sơ đồ phân rã")
    add_p("Sơ đồ Use Case tổng thể mô tả toàn diện sự tương tác của 3 Actor (Quản lý, Giáo viên, Phụ huynh) với 8 phân hệ chức năng:")
    add_diagram(r"e:\CNPM\CNPM\astah_export\EXTRA\UseCase_TongThe_HeThong.png", "Sơ đồ Use Case tổng thể toàn hệ thống mầm non (KMS)")

    add_p("Phân rã Use Case Quản lý trẻ em (được mô hình hóa chi tiết trên Astah Community):")
    add_diagram(r"e:\CNPM\CNPM\astah_export\CNPM\USECASE\Phân rã Use Case - Quản lý trẻ em.png", "Sơ đồ phân rã Use Case - Quản lý trẻ em (Trích xuất từ Astah Community)")

    add_p("Phân rã Use Case Quản lý giáo viên:")
    add_diagram(r"e:\CNPM\CNPM\astah_export\CNPM\USECASE\PhanRaUseCase_QuanLyGiaoVien.png", "Sơ đồ phân rã Use Case - Quản lý giáo viên (Trích xuất từ Astah Community)")

    add_h2("4.2. Sơ đồ Hoạt động (Activity Diagrams) cho các quy trình nghiệp vụ")
    add_p("Dưới đây là các sơ đồ hoạt động mô tả luồng xử lý chi tiết của từng quy trình:")

    add_diagram(r"e:\CNPM\CNPM\astah_export\CNPM\ACTIVITY\Activity_ThemTre.png", "Sơ đồ hoạt động: Quy trình Thêm trẻ mới vào trường")
    add_diagram(r"e:\CNPM\CNPM\astah_export\CNPM\ACTIVITY\Activity_CapNhatThongTinTre.png", "Sơ đồ hoạt động: Quy trình Cập nhật thông tin trẻ em")
    add_diagram(r"e:\CNPM\CNPM\astah_export\CNPM\ACTIVITY\Activity_TimKiemTre.png", "Sơ đồ hoạt động: Quy trình Tìm kiếm thông tin học sinh")
    add_diagram(r"e:\CNPM\CNPM\astah_export\CNPM\ACTIVITY\Activity_ThemGiaoVien.png", "Sơ đồ hoạt động: Quy trình Thêm mới giáo viên")
    add_diagram(r"e:\CNPM\CNPM\astah_export\EXTRA\Activity_ThanhToan_VietQR.png", "Sơ đồ hoạt động: Quy trình Tính tiền ăn và Thanh toán học phí VietQR")

    add_h2("4.3. Sơ đồ Tuần tự (Sequence Diagrams)")
    add_p("Sơ đồ tuần tự thể hiện các thông điệp truyền tải giữa Đối tượng Actor, Giao diện (Boundary), Bộ xử lý (Control) và Cơ sở dữ liệu (Entity):")

    add_diagram(r"e:\CNPM\CNPM\astah_export\CNPM\SEQUENCE\Sequence_ThemTre.png", "Sơ đồ tuần tự: Thêm học sinh mới vào hệ thống")
    add_diagram(r"e:\CNPM\CNPM\astah_export\CNPM\SEQUENCE\Sequence_CapNhatThongTinTre.png", "Sơ đồ tuần tự: Cập nhật thông tin trẻ")
    add_diagram(r"e:\CNPM\CNPM\astah_export\CNPM\SEQUENCE\Sequence_TimKiemTre.png", "Sơ đồ tuần tự: Tìm kiếm học sinh")
    add_diagram(r"e:\CNPM\CNPM\astah_export\EXTRA\Sequence_ThanhToan_VietQR.png", "Sơ đồ tuần tự: Quy trình Tạo mã QR và Thanh toán học phí VietQR Napas")

    add_h2("4.4. Sơ đồ Lớp (Class Diagram) toàn diện của hệ thống")
    add_p("Sơ đồ lớp chi tiết thể hiện đầy đủ các thuộc tính (Attributes), phương thức (Operations) và mối quan hệ kết tập, kết hợp, bội số (Multiplicity) giữa 14 thực thể:")
    add_diagram(r"e:\CNPM\CNPM\astah_export\EXTRA\ClassDiagram_ToanHeThong.png", "Sơ đồ lớp (Class Diagram) toàn diện hệ thống quản lý mầm non")

    # -------------------------------------------------------------
    # CHƯƠNG 5: THIẾT KẾ CƠ SỞ DỮ LIỆU
    # -------------------------------------------------------------
    add_h1("CHƯƠNG 5: THIẾT KẾ CƠ SỞ DỮ LIỆU (DATABASE SCHEMA)")

    add_h2("5.1. Từ điển dữ liệu (Data Dictionary)")
    add_p("Cơ sở dữ liệu được thiết kế đạt chuẩn chuẩn hóa 3NF, đảm bảo toàn vẹn dữ liệu và tối ưu hiệu năng truy vấn.")

    # Table 1: tre_em
    add_h3("Bảng 1: tre_em (Quản lý hồ sơ học sinh mầm non)")
    tbl_tre = doc.add_table(rows=6, cols=5)
    tbl_tre.alignment = WD_TABLE_ALIGNMENT.CENTER
    fields_tre = [
        ("Tên cột", "Kiểu dữ liệu", "Khóa", "Null", "Mô tả ý nghĩa"),
        ("id", "INT", "PK", "No", "Khóa chính tự tăng"),
        ("ma_dinh_danh", "VARCHAR(30)", "Unique", "No", "Mã học sinh duy nhất toàn trường"),
        ("ho_ten", "VARCHAR(100)", "", "No", "Họ và tên của trẻ"),
        ("ngay_sinh", "DATE", "", "No", "Ngày tháng năm sinh"),
        ("thong_tin_suc_khoe", "TEXT", "", "Yes", "Tình trạng sức khỏe, chiều cao, cân nặng, dị ứng")
    ]
    for r_idx, r_data in enumerate(fields_tre):
        for c_idx, val in enumerate(r_data):
            cell = tbl_tre.cell(r_idx, c_idx)
            set_cell_margins(cell, 60, 60, 80, 80)
            p = cell.paragraphs[0]
            if r_idx == 0:
                set_cell_background(cell, "1E3A8A")
                run = p.add_run(val)
                run.font.bold = True
                run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            else:
                p.add_run(val)
                if r_idx % 2 == 1:
                    set_cell_background(cell, "F8FAFC")

    doc.add_paragraph()

    # Table 2: phieu_hoc_phi
    add_h3("Bảng 2: phieu_hoc_phi (Quản lý tính toán học phí & tiền ăn)")
    tbl_hp = doc.add_table(rows=7, cols=5)
    tbl_hp.alignment = WD_TABLE_ALIGNMENT.CENTER
    fields_hp = [
        ("Tên cột", "Kiểu dữ liệu", "Khóa", "Null", "Mô tả ý nghĩa"),
        ("id", "INT", "PK", "No", "Mã khóa chính phiếu học phí"),
        ("id_tre", "INT", "FK", "No", "Khóa ngoại liên kết bảng tre_em"),
        ("hoc_phi_co_ban", "DECIMAL(12,2)", "", "No", "Học phí cố định tháng (1.500.000 VNĐ)"),
        ("so_ngay_an_thuc_te", "INT", "", "No", "Số ngày thực tế trẻ ăn tại trường"),
        ("tien_an", "DECIMAL(12,2)", "", "No", "Tiền ăn = so_ngay_an * don_gia_tien_an"),
        ("tong_tien_phai_tra", "DECIMAL(12,2)", "", "No", "Tổng = Học phí + Tiền ăn + Phí DV - Giảm trừ")
    ]
    for r_idx, r_data in enumerate(fields_hp):
        for c_idx, val in enumerate(r_data):
            cell = tbl_hp.cell(r_idx, c_idx)
            set_cell_margins(cell, 60, 60, 80, 80)
            p = cell.paragraphs[0]
            if r_idx == 0:
                set_cell_background(cell, "047857")
                run = p.add_run(val)
                run.font.bold = True
                run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            else:
                p.add_run(val)
                if r_idx % 2 == 1:
                    set_cell_background(cell, "F0FDF4")

    # -------------------------------------------------------------
    # CHƯƠNG 6: THIẾT KẾ KIẾN TRÚC VÀ KẾ HOẠCH KIỂM THỬ
    # -------------------------------------------------------------
    add_h1("CHƯƠNG 6: THIẾT KẾ KIẾN TRÚC HỆ THỐNG VÀ KIỂM THỬ")

    add_h2("6.1. Kiến trúc hệ thống (3-Tier Layered Architecture)")
    add_p("Hệ thống được thiết kế theo mô hình 3 lớp phân tách rõ ràng trách nhiệm:")
    add_p(" 1. Presentation Layer (Tầng giao diện): Xây dựng giao diện Web/Mobile responsive thân thiện cho Quản lý, Giáo viên và Phụ huynh theo dõi trên mọi thiết bị.")
    add_p(" 2. Business Logic Layer (Tầng nghiệp vụ): Chứa các module xử lý logic: công thức tính tiền ăn, sinh mã thanh toán VietQR động, phân quyền RBAC và kiểm tra tính toàn vẹn dữ liệu.")
    add_p(" 3. Data Access Layer (Tầng dữ liệu): Quản lý kết nối CSDL MySQL / MariaDB, thực thi các truy vấn và bảo đảm an toàn dữ liệu.")

    add_h2("6.2. Kế hoạch kiểm thử chức năng (Test Cases)")
    tbl_tc = doc.add_table(rows=5, cols=4)
    tbl_tc.alignment = WD_TABLE_ALIGNMENT.CENTER
    tc_data = [
        ("Mã TC", "Chức năng kiểm thử", "Dữ liệu & Thao tác kiểm thử", "Kết quả mong đợi"),
        ("TC01", "Thêm trẻ mới", "Nhập đầy đủ thông tin hợp lệ, chọn lớp còn sĩ số", "Học sinh được thêm vào CSDL và sĩ số lớp tăng 1"),
        ("TC02", "Tính học phí tự động", "Học phí 1.500.000, 20 ngày ăn x 30.000, phí khác 100.000", "Tổng tiền tự động tính ra đúng 2.200.000 VNĐ"),
        ("TC03", "Tạo mã QR thanh toán", "Nhấn nút 'Thanh toán trực tuyến' phiếu học phí 2.200.000", "Sinh mã VietQR đúng số tiền, số tài khoản nhà trường và mã phiếu"),
        ("TC04", "Phân quyền phụ huynh", "Phụ huynh truy cập xem học phí học sinh lớp khác", "Hệ thống từ chối truy cập và báo lỗi 403 Forbidden")
    ]
    for r_idx, r_data in enumerate(tc_data):
        for c_idx, val in enumerate(r_data):
            cell = tbl_tc.cell(r_idx, c_idx)
            set_cell_margins(cell, 60, 60, 80, 80)
            p = cell.paragraphs[0]
            if r_idx == 0:
                set_cell_background(cell, "1E3A8A")
                run = p.add_run(val)
                run.font.bold = True
                run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            else:
                p.add_run(val)
                if r_idx % 2 == 1:
                    set_cell_background(cell, "F8FAFC")

    # -------------------------------------------------------------
    # CHƯƠNG 7: KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN
    # -------------------------------------------------------------
    add_h1("CHƯƠNG 7: KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN")
    add_p("Đồ án đã hoàn thành toàn diện việc phân tích và thiết kế Hệ thống Quản lý Mầm non tư thục (KMS) theo đúng chuẩn môn Công Nghệ Phần Mềm:")
    add_p(" • Phân tích chi tiết 8 phân hệ nghiệp vụ bám sát thực tế hoạt động trường mầm non.")
    add_p(" • Xây dựng đầy đủ các mô hình UML chuẩn quốc tế: Sơ đồ Use Case tổng thể và phân rã, Sơ đồ Hoạt động, Sơ đồ Tuần tự và Sơ đồ Lớp chi tiết.")
    add_p(" • Thiết kế cơ sở dữ liệu quan hệ tối ưu, có script SQL DDL hoàn chỉnh và sẵn sàng triển khai.")
    add_p(" • Toàn bộ tài liệu, biểu đồ và mã nguồn đã được tích hợp đồng bộ và lưu trữ tại kho mã nguồn GitHub của dự án.")

    # Save documents
    out_workspace = r"e:\CNPM\CNPM\W.docx"
    doc.save(out_workspace)
    print("Saved to:", out_workspace)

    # Save copy to WPSDrive
    wps_target1 = r"c:\Users\NGUYEN\WPSDrive\1392229858529\WPSDrive\W.docx"
    wps_target2 = r"c:\Users\NGUYEN\WPSDrive\1392229858529\WPSDrive\YeuCauHeThong_BaoCao_HoanChinh.docx"
    shutil.copyfile(out_workspace, wps_target1)
    shutil.copyfile(out_workspace, wps_target2)
    print("Saved copies to WPSDrive successfully!")

if __name__ == "__main__":
    create_full_document()
