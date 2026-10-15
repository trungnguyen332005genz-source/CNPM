-- =============================================================================
-- HỆ THỐNG QUẢN LÝ MẦM NON TƯ THỤC (KINDERGARTEN MANAGEMENT SYSTEM - KMS)
-- Database Script: DDL Schema & Initial Data
-- Chuẩn ANSI SQL / MySQL 8.0+ / MariaDB
-- =============================================================================

CREATE DATABASE IF NOT EXISTS ql_mam_non CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE ql_mam_non;

-- 1. BẢNG VAI TRÒ
CREATE TABLE IF NOT EXISTS vai_tro (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ten_vai_tro VARCHAR(50) NOT NULL UNIQUE COMMENT 'ADMIN, GIAO_VIEN, PHU_HUYNH',
    mo_ta VARCHAR(255) NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2. BẢNG TÀI KHOẢN NGƯỜI DÙNG
CREATE TABLE IF NOT EXISTS tai_khoan (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ten_dang_nhap VARCHAR(50) NOT NULL UNIQUE,
    mat_khau_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100) NULL,
    so_dien_thoai VARCHAR(20) NULL,
    vai_tro_id INT NOT NULL,
    trang_thai VARCHAR(20) DEFAULT 'ACTIVE' COMMENT 'ACTIVE, LOCKED, INACTIVE',
    ngay_tao DATETIME DEFAULT CURRENT_TIMESTAMP,
    ngay_cap_nhat DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_taikhoan_vaitro FOREIGN KEY (vai_tro_id) REFERENCES vai_tro(id) ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 3. BẢNG LỚP HỌC
CREATE TABLE IF NOT EXISTS lop_hoc (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ma_lop VARCHAR(20) NOT NULL UNIQUE,
    ten_lop VARCHAR(100) NOT NULL,
    khoi_lop VARCHAR(50) NOT NULL COMMENT 'Nhà trẻ, Mầm, Chồi, Lá',
    si_so_toi_da INT DEFAULT 25,
    nam_hoc VARCHAR(20) NOT NULL,
    phong_hoc VARCHAR(50) NULL,
    trang_thai VARCHAR(20) DEFAULT 'DANG_HOAT_DONG'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 4. BẢNG GIÁO VIÊN
CREATE TABLE IF NOT EXISTS giao_vien (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tai_khoan_id INT UNIQUE NULL,
    ma_gv VARCHAR(20) NOT NULL UNIQUE,
    ho_ten VARCHAR(100) NOT NULL,
    ngay_sinh DATE NULL,
    gioi_tinh VARCHAR(10) NULL,
    so_dien_thoai VARCHAR(20) NOT NULL,
    email VARCHAR(100) NULL,
    dia_chi VARCHAR(255) NULL,
    chuyen_mon VARCHAR(100) NULL COMMENT 'Sư phạm mầm non, Cử nhân giáo dục, v.v.',
    trang_thai VARCHAR(30) DEFAULT 'DANG_LAM_VIEC' COMMENT 'DANG_LAM_VIEC, NGHI_PHEP, DA_NGHI_VIEC',
    CONSTRAINT fk_giaovien_taikhoan FOREIGN KEY (tai_khoan_id) REFERENCES tai_khoan(id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 5. BẢNG PHÂN CÔNG GIÁO VIÊN VÀO LỚP
CREATE TABLE IF NOT EXISTS phan_cong_giao_vien (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_giao_vien INT NOT NULL,
    id_lop INT NOT NULL,
    vai_tro_lop VARCHAR(50) DEFAULT 'CHU_NHIEM' COMMENT 'CHU_NHIEM, PHO_CHU_NHIEM, BAO_MAU',
    ngay_phan_cong DATE NOT NULL,
    CONSTRAINT fk_pc_giaovien FOREIGN KEY (id_giao_vien) REFERENCES giao_vien(id) ON DELETE CASCADE,
    CONSTRAINT fk_pc_lophoc FOREIGN KEY (id_lop) REFERENCES lop_hoc(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 6. BẢNG TRẺ EM (CHỨC NĂNG TRUNG TÂM)
CREATE TABLE IF NOT EXISTS tre_em (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ma_dinh_danh VARCHAR(30) NOT NULL UNIQUE,
    ho_ten VARCHAR(100) NOT NULL,
    ngay_sinh DATE NOT NULL,
    gioi_tinh VARCHAR(10) NOT NULL,
    dia_chi VARCHAR(255) NULL,
    thong_tin_suc_khoe TEXT NULL,
    tien_su_benh TEXT NULL,
    di_ung TEXT NULL,
    ngay_nhap_hoc DATE NOT NULL,
    trang_thai VARCHAR(30) DEFAULT 'DANG_HOC' COMMENT 'DANG_HOC, NGHI_HOC, CHUYEN_TRUONG',
    id_lop INT NULL,
    CONSTRAINT fk_treem_lophoc FOREIGN KEY (id_lop) REFERENCES lop_hoc(id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 7. BẢNG PHỤ HUYNH
CREATE TABLE IF NOT EXISTS phu_huynh (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tai_khoan_id INT UNIQUE NULL,
    ho_ten VARCHAR(100) NOT NULL,
    so_dien_thoai VARCHAR(20) NOT NULL,
    email VARCHAR(100) NULL,
    cccd VARCHAR(20) NULL,
    dia_chi VARCHAR(255) NULL,
    nghe_nghiep VARCHAR(100) NULL,
    CONSTRAINT fk_phuhuynh_taikhoan FOREIGN KEY (tai_khoan_id) REFERENCES tai_khoan(id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 8. BẢNG LIÊN KẾT PHỤ HUYNH - TRẺ (QUAN HỆ 1-N & N-N)
CREATE TABLE IF NOT EXISTS phu_huynh_tre (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_phu_huynh INT NOT NULL,
    id_tre INT NOT NULL,
    quan_he VARCHAR(30) NOT NULL COMMENT 'Cha, Mẹ, Ông, Bà, Giám hộ',
    la_nguoi_giam_ho_chinh BOOLEAN DEFAULT TRUE,
    CONSTRAINT fk_pht_phuhuynh FOREIGN KEY (id_phu_huynh) REFERENCES phu_huynh(id) ON DELETE CASCADE,
    CONSTRAINT fk_pht_tre FOREIGN KEY (id_tre) REFERENCES tre_em(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 9. BẢNG MÓN ĂN
CREATE TABLE IF NOT EXISTS mon_an (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ten_mon VARCHAR(100) NOT NULL,
    loai_mon VARCHAR(50) NOT NULL COMMENT 'Chính, Canh, Phụ, Tráng miệng, Sữa',
    calo DECIMAL(8, 2) DEFAULT 0,
    thanh_phan TEXT NULL,
    don_gia_uoc_tinh DECIMAL(12, 2) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 10. BẢNG THỰC ĐƠN
CREATE TABLE IF NOT EXISTS thuc_don (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ngay_ap_dung DATE NOT NULL,
    buoi_an VARCHAR(30) NOT NULL COMMENT 'SANG, TRUA, XE_PHU',
    tuan_thu INT NOT NULL,
    nam INT NOT NULL,
    ghi_chu VARCHAR(255) NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 11. BẢNG CHI TIẾT THỰC ĐƠN - MÓN ĂN
CREATE TABLE IF NOT EXISTS thuc_don_mon_an (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_thuc_don INT NOT NULL,
    id_mon_an INT NOT NULL,
    ghi_chu VARCHAR(255) NULL,
    CONSTRAINT fk_tdma_thucdon FOREIGN KEY (id_thuc_don) REFERENCES thuc_don(id) ON DELETE CASCADE,
    CONSTRAINT fk_tdma_monan FOREIGN KEY (id_mon_an) REFERENCES mon_an(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 12. BẢNG PHIẾU HỌC PHÍ VÀ TIỀN ĂN
CREATE TABLE IF NOT EXISTS phieu_hoc_phi (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ma_phieu VARCHAR(30) NOT NULL UNIQUE,
    id_tre INT NOT NULL,
    thang INT NOT NULL,
    nam INT NOT NULL,
    hoc_phi_co_ban DECIMAL(12, 2) NOT NULL DEFAULT 1500000,
    so_ngay_an_thuc_te INT NOT NULL DEFAULT 0,
    don_gia_tien_an DECIMAL(12, 2) NOT NULL DEFAULT 30000,
    tien_an DECIMAL(12, 2) GENERATED ALWAYS AS (so_ngay_an_thuc_te * don_gia_tien_an) STORED,
    phi_dich_vu DECIMAL(12, 2) DEFAULT 0,
    phi_khac DECIMAL(12, 2) DEFAULT 0,
    giam_tru DECIMAL(12, 2) DEFAULT 0,
    tong_tien_phai_tra DECIMAL(12, 2) NOT NULL,
    trang_thai VARCHAR(30) DEFAULT 'CHUA_THANH_TOAN' COMMENT 'CHUA_THANH_TOAN, DA_THANH_TOAN, QUA_HAN',
    ngay_tao DATETIME DEFAULT CURRENT_TIMESTAMP,
    ngay_cap_nhat DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_php_tre FOREIGN KEY (id_tre) REFERENCES tre_em(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 13. BẢNG CHI TIẾT GIẢM TRỪ HỌC PHÍ
CREATE TABLE IF NOT EXISTS giam_tru_hoc_phi (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_phieu_hoc_phi INT NOT NULL,
    ly_do VARCHAR(255) NOT NULL,
    so_tien_giam DECIMAL(12, 2) NOT NULL,
    CONSTRAINT fk_gt_phieu FOREIGN KEY (id_phieu_hoc_phi) REFERENCES phieu_hoc_phi(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 14. BẢNG GIAO DỊCH THANH TOÁN (VIETQR / BANKING)
CREATE TABLE IF NOT EXISTS giao_dich_thanh_toan (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ma_giao_dich VARCHAR(50) NOT NULL UNIQUE,
    id_phieu_hoc_phi INT NOT NULL,
    id_phu_huynh INT NULL,
    phuong_thuc VARCHAR(30) DEFAULT 'VIETQR' COMMENT 'VIETQR, CHUYEN_KHOAN, TIEN_MAT',
    so_tien DECIMAL(12, 2) NOT NULL,
    noi_dung_chuyen_khoan VARCHAR(100) NOT NULL,
    ma_qr_payload TEXT NULL,
    trang_thai VARCHAR(30) DEFAULT 'KHOI_TAO' COMMENT 'KHOI_TAO, THANH_CONG, THAT_BAI',
    thoi_gian_tao DATETIME DEFAULT CURRENT_TIMESTAMP,
    thoi_gian_thanh_toan DATETIME NULL,
    CONSTRAINT fk_gd_phieu FOREIGN KEY (id_phieu_hoc_phi) REFERENCES phieu_hoc_phi(id) ON DELETE CASCADE,
    CONSTRAINT fk_gd_phuhuynh FOREIGN KEY (id_phu_huynh) REFERENCES phu_huynh(id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- DỮ LIỆU KHỞI TẠO MẪU (SEED DATA)
INSERT INTO vai_tro (id, ten_vai_tro, mo_ta) VALUES
(1, 'ADMIN', 'Quản trị viên - Toàn quyền trên toàn hệ thống'),
(2, 'GIAO_VIEN', 'Giáo viên mầm non - Quản lý trong phạm vi lớp phân công'),
(3, 'PHU_HUYNH', 'Phụ huynh học sinh - Theo dõi thông tin con, thực đơn và thanh toán');

INSERT INTO lop_hoc (id, ma_lop, ten_lop, khoi_lop, si_so_toi_da, nam_hoc, phong_hoc) VALUES
(1, 'L01', 'Lớp Lá 1', 'Lá (5-6 tuổi)', 25, '2026-2027', 'Phòng 101 - Tầng 1'),
(2, 'C01', 'Lớp Chồi 1', 'Chồi (4-5 tuổi)', 22, '2026-2027', 'Phòng 102 - Tầng 1'),
(3, 'M01', 'Lớp Mầm 1', 'Mầm (3-4 tuổi)', 20, '2026-2027', 'Phòng 201 - Tầng 2');

INSERT INTO mon_an (id, ten_mon, loai_mon, calo, thanh_phan, don_gia_uoc_tinh) VALUES
(1, 'Sữa tươi tiệt trùng Vinamilk', 'Sữa', 150, 'Sữa tươi 100%', 10000),
(2, 'Bánh mì kẹp chả lụa', 'Chính', 280, 'Bánh mì, chả lụa, dưa leo', 15000),
(3, 'Cơm trắng gạo dẻo', 'Chính', 200, 'Gạo thơm ST25', 5000),
(4, 'Thịt heo kho trứng cút', 'Chính', 320, 'Thịt nạc vai, trứng cút, nước dừa', 18000),
(5, 'Canh bí đỏ nấu tôm thịt', 'Canh', 120, 'Bí đỏ tươi, tôm sú, thịt băm', 12000),
(6, 'Chuối tiêu chín', 'Tráng miệng', 90, 'Chuối tiêu organic', 5000);
