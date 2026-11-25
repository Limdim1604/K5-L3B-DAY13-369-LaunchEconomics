"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH_THANG = 40_000_000
SO_YEU_CAU_THANG = 45_000


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1 / p if p else math.inf
    if p == 0:
        return k
    return ti_le_thanh_cong(p, k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return float(p > 0)
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    thanh_cong = ti_le_thanh_cong(p, k)
    return so_lan_chay_ky_vong(p, k) / thanh_cong if thanh_cong else math.inf


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    cac_phep_thu = (
        ('Số lần chạy trung bình, tối đa 2 lần', so_lan_chay_ky_vong(0.8, 2), 1.20),
        ('Số lần chạy trung bình, chạy đến khi đúng', so_lan_chay_ky_vong(0.8), 1.25),
        ('Hệ số chi phí mỗi việc thành công, tối đa 3 lần', he_so_chi_phi_moi_viec_thanh_cong(0.8, 3), 1.25),
    )
    print('A1 · Ba phép thử đáp án biết trước (p = 0,8)')
    print('| Phép thử | Kết quả |')
    print('| --- | ---: |')
    for ten, ket_qua, mong_doi in cac_phep_thu:
        if not math.isclose(ket_qua, mong_doi, abs_tol=1e-9, rel_tol=0):
            raise AssertionError(f'{ten}: nhận {ket_qua}, cần {mong_doi}')
        gia_tri = f'{ket_qua:.2f}'.replace('.', ',')
        print(f'| {ten} | {gia_tri} — ĐẠT |')
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    if max_lan_chay is not None:
        raise NotImplementedError('Giới hạn số lần chạy thuộc nhiệm vụ B')

    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    tien_token = (runs['tokens_in'] * gia_vao + runs['tokens_out'] * gia_ra) / 1000
    tien_tool = runs['tool_calls'] * gia_tool
    token = tien_token.sum()
    tool = tien_tool.sum()
    chay_lai = (tien_token + tien_tool)[runs['attempt'] > 1].sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = int(reqs['ket_qua'].eq('thanh_cong').sum())
    return dict(token=token, tool=tool, chay_lai=chay_lai, xem_lai=xem_lai,
                lam_lai=lam_lai, tong=tong, thanh_cong=thanh_cong,
                cps=tong / thanh_cong if thanh_cong else math.inf,
                hoa_don_moi_yc=(token + tool) / len(reqs) if len(reqs) else math.nan)


def in_bang_a2(ket_qua):
    print('\nA2 · Mô hình chi phí từ trace')
    cac_khoan = (
        ('Token (đ)', 'token', ',.3f', 'đo từ trace'),
        ('Tool (đ)', 'tool', ',.0f', 'đo từ trace'),
        ('Trong đó, phần của lần chạy thứ 2 và 3 (đ)', 'chay_lai', ',.3f', 'đo từ trace'),
        ('Xem lại (đ)', 'xem_lai', ',.0f', 'simulated'),
        ('Làm lại (đ)', 'lam_lai', ',.0f', 'simulated'),
        ('Tổng chi phí (đ)', 'tong', ',.3f', 'simulated'),
        ('Số việc thành công', 'thanh_cong', ',d', ''),
        ('Chi phí mỗi việc thành công (đ)', 'cps', ',.2f', 'simulated'),
        ('Hoá đơn token và tool chia cho số yêu cầu (đ)', 'hoa_don_moi_yc', ',.2f', 'đo từ trace'),
    )
    print('| Khoản | Giá trị | Nhãn |')
    print('| --- | ---: | --- |')
    for ten, khoa, dinh_dang, nhan in cac_khoan:
        print(f'| {ten} | {ket_qua[khoa]:{dinh_dang}} | {nhan} |')
    print(f"Chi phí mỗi việc thành công / hoá đơn mỗi yêu cầu: "
          f"{ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.2f}× (simulated)")
    print(f"Tỉ trọng làm lại: {ket_qua['lam_lai'] / ket_qua['tong']:.2%} (simulated)")


def in_bang_a3(runs, reqs):
    print('\nA3 · Tách theo loại yêu cầu')
    print('| Loại | Số yêu cầu | Tỉ lệ thành công | Lần chạy/yêu cầu | '
          'Chi phí mỗi việc thành công (đ, simulated) | So với 12.000 đ (simulated) |')
    print('| --- | ---: | ---: | ---: | ---: | ---: |')
    for loai in ('noi_dia', 'hang_nang', 'quoc_te', 'doi_tac'):
        nhom = reqs[reqs['loai'].eq(loai)]
        ket_qua = mo_hinh(runs, nhom)
        cps = ket_qua['cps']
        print(f"| {loai} | {len(nhom)} | {ket_qua['thanh_cong'] / len(nhom):.2%} | "
              f"{nhom['so_lan_chay'].mean():.2f} | {cps:,.2f} | {cps / BASELINE:.2f}× |")

    quoc_te = reqs[reqs['loai'].eq('quoc_te')]
    runs_quoc_te = runs[runs['request_id'].isin(quoc_te['request_id'])]
    ti_le_ok = runs_quoc_te['status'].eq('ok').groupby(runs_quoc_te['attempt']).mean()
    print('Tỉ lệ status ok của quoc_te: ' + ', '.join(
        f'lần {attempt}: {ti_le:.2%}' for attempt, ti_le in ti_le_ok.items()))


def in_bang_a4(runs, reqs):
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    ket_qua = mo_hinh(runs, pham_vi)
    # Lưu lượng tháng là của toàn hệ thống, nên quy đổi theo toàn bộ mẫu.
    ti_le_thanh_cong_trong_mau = ket_qua['thanh_cong'] / len(reqs)
    print('\nA4 · Chi phí cố định (noi_dia + hang_nang)')
    print(f"Phạm vi: {len(pham_vi):,} yêu cầu, {ket_qua['thanh_cong']:,} thành công "
          f"trên {len(reqs):,} yêu cầu toàn mẫu. "
          f"Chi phí trước cố định: {ket_qua['cps']:,.2f} đ/việc (simulated).")
    print('| Yêu cầu/tháng | Việc thành công/tháng | Chi phí cố định/việc (đ) | '
          'Chi phí mỗi việc thành công + cố định (đ, simulated) | So với 12.000 đ (simulated) |')
    print('| ---: | ---: | ---: | ---: | ---: |')
    for luu_luong in (SO_YEU_CAU_THANG, SO_YEU_CAU_THANG // 2):
        thanh_cong_thang = luu_luong * ti_le_thanh_cong_trong_mau
        co_dinh = CHI_PHI_CO_DINH_THANG / thanh_cong_thang
        cps = ket_qua['cps'] + co_dinh
        print(f'| {luu_luong:,} | {thanh_cong_thang:,.0f} | {co_dinh:,.2f} | '
              f'{cps:,.2f} | {cps / BASELINE:.2f}× |')


if __name__ == '__main__':
    kiem_tra_dap_an_biet_truoc()
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    in_bang_a2(mo_hinh(runs, reqs))
    in_bang_a3(runs, reqs)
    in_bang_a4(runs, reqs)
    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
