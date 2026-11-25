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
def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL, luong_phut=LUONG_PHUT,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'].le(max_lan_chay)]
        reqs = reqs.copy()
        vuot_gioi_han = reqs['so_lan_chay'].gt(max_lan_chay)
        reqs.loc[vuot_gioi_han, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot_gioi_han, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
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


def in_bang_b1_den_b3(runs, reqs, moc_a2):
    def thay_doi(ket_qua):
        return ket_qua['cps'] / moc_a2 - 1

    gioi_han = {k: mo_hinh(runs, reqs, max_lan_chay=k) for k in (1, 2, 3)}
    token_gap_doi = dict(gia_vao=GIA_VAO * 2, gia_ra=GIA_RA * 2)
    kich_ban = (
        ('Giá token gấp đôi', token_gap_doi),
        ('Giá token giảm một nửa', dict(gia_vao=GIA_VAO / 2, gia_ra=GIA_RA / 2)),
        ('Tỉ lệ xem lại gấp đôi', dict(he_so_xem_lai=2)),
        ('Tỉ lệ xem lại giảm một nửa', dict(he_so_xem_lai=0.5)),
        ('Số ca làm lại gấp đôi', dict(he_so_lam_lai=2)),
        ('Số ca làm lại giảm một nửa', dict(he_so_lam_lai=0.5)),
        ('Lương nhân viên tăng 25%', dict(luong_phut=LUONG_PHUT * 1.25)),
    )
    ket_qua_rieng = {ten: mo_hinh(runs, reqs, **tham_so) for ten, tham_so in kich_ban}
    ket_qua_b1 = {**ket_qua_rieng, 'Chỉ cho chạy tối đa 2 lần': gioi_han[2],
                 'Chỉ cho chạy 1 lần': gioi_han[1]}

    print(f'\nB1 · Đổi từng yếu tố (mốc A2: {moc_a2:,.2f} đ/việc thành công, simulated)')
    print('| Kịch bản | Chi phí mỗi việc thành công (đ, simulated) | Thay đổi (simulated) |')
    print('| --- | ---: | ---: |')
    for ten, ket_qua in ket_qua_b1.items():
        print(f"| {ten} | {ket_qua['cps']:,.2f} | {thay_doi(ket_qua):+.2%} |")

    cap = mo_hinh(runs, reqs, **token_gap_doi, he_so_xem_lai=2)
    yeu_to = ('Giá token gấp đôi', 'Tỉ lệ xem lại gấp đôi',
              'Số ca làm lại gấp đôi', 'Lương nhân viên tăng 25%')
    xep_hang = sorted(yeu_to, key=lambda ten: thay_doi(ket_qua_rieng[ten]), reverse=True)[:3]
    print('\nB2 · Đổi đồng thời giá token và tỉ lệ xem lại')
    print(f"Cả hai gấp đôi: {cap['cps']:,.2f} đ/việc thành công, {thay_doi(cap):+.2%} (simulated)")
    print('Ba tác động tăng mạnh nhất (simulated): ' + ' · '.join(
        f'{ten}: {thay_doi(ket_qua_rieng[ten]):+.2%}' for ten in xep_hang))

    print('\nB3 · Giới hạn số lần chạy')
    print('| Giới hạn | Tổng chi phí trợ lý (đ, simulated) | Yêu cầu không thành công | '
          'Chi phí cả hệ thống (đ, simulated) | Chi phí mỗi việc thành công (đ, simulated) |')
    print('| ---: | ---: | ---: | ---: | ---: |')
    for k, ket_qua in gioi_han.items():
        khong_thanh_cong = len(reqs) - ket_qua['thanh_cong']
        ca_he_thong = ket_qua['tong'] + BASELINE * khong_thanh_cong
        print(f"| {k} | {ket_qua['tong']:,.2f} | {khong_thanh_cong} | "
              f"{ca_he_thong:,.2f} | {ket_qua['cps']:,.2f} |")


def in_bang_b4(runs, reqs, moc_a2):
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])].copy()
    id_co_lan_ok = runs.loc[runs['status'].eq('ok'), 'request_id']
    can_xem_lai = pham_vi['request_id'].isin(id_co_lan_ok)
    can_lam_lai = pham_vi['ket_qua'].eq('lam_lai')
    so_ca_xem_lai = int(can_xem_lai.sum())
    phut_xem_lai = 5
    pham_vi['phut_xem_lai_simulated'] = can_xem_lai.astype(int) * phut_xem_lai
    # Hướng dẫn CP2 dùng trung bình làm tròn một chữ số từ ca làm lại toàn mẫu.
    phut_lam_lai_trung_binh = round(reqs.loc[reqs['ket_qua'].eq('lam_lai'),
                                          'phut_lam_lai_simulated'].mean(), 1)

    print('\nB4 · Xem lại 100% yêu cầu có lượt chạy ok (noi_dia + hang_nang)')
    print(f'{len(pham_vi)} yêu cầu, {so_ca_xem_lai} ca xem lại × {phut_xem_lai} phút, '
          f'{can_lam_lai.sum()} ca làm lại (giả định thời lượng simulated).')
    print('| Phút/ca làm lại | Chi phí mỗi việc thành công (đ) | So với 12.000 đ | '
          'Thay đổi so với A2 toàn mẫu | Phút xem lại tối đa để hòa vốn | Nhãn |')
    print('| ---: | ---: | ---: | ---: | ---: | --- |')
    for phut_lam_lai in (9, phut_lam_lai_trung_binh):
        pham_vi['phut_lam_lai_simulated'] = can_lam_lai.astype(int) * phut_lam_lai
        ket_qua = mo_hinh(runs, pham_vi)
        chi_phi_khac_xem_lai = ket_qua['token'] + ket_qua['tool'] + ket_qua['lam_lai']
        phut_hoa_von = (BASELINE * ket_qua['thanh_cong'] - chi_phi_khac_xem_lai) / (so_ca_xem_lai * LUONG_PHUT)
        cps = ket_qua['cps']
        print(f'| {phut_lam_lai:g} | {cps:,.2f} | {cps / BASELINE:.2f}× | '
              f'{cps / moc_a2 - 1:+.2%} | {phut_hoa_von:.2f} | simulated |')


if __name__ == '__main__':
    kiem_tra_dap_an_biet_truoc()
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    ket_qua_a2 = mo_hinh(runs, reqs)
    in_bang_a2(ket_qua_a2)
    in_bang_a3(runs, reqs)
    in_bang_a4(runs, reqs)
    in_bang_b1_den_b3(runs, reqs, ket_qua_a2['cps'])
    in_bang_b4(runs, reqs, ket_qua_a2['cps'])
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
