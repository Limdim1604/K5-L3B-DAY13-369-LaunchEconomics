# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 — ĐẠT |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 — ĐẠT |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 — ĐẠT |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585,132 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804,488 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585,132 | Token + tool + xem lại + làm lại | simulated |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.471,97 | Tổng chi phí / 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,65 | (Token + tool) / 1.200 | đo từ trace |

- Kiểm khoản tool trực tiếp từ CSV: cộng `tool_calls` trên 1.624 lượt chạy được 5.600, nhân 15 đ/lượt gọi được 84.000 đ.
- Chi phí mỗi việc thành công gấp **16,28 lần** hoá đơn chia số yêu cầu (simulated).
- Nhân viên làm lại là khoản lớn nhất, chiếm **51,77%** tổng chi phí (simulated).

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công (đ, simulated) | So với 12.000 đ (simulated) |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,02% | 1,11 | 2.695,64 | 0,22× |
| hang_nang | 158 | 74,05% | 1,47 | 8.220,73 | 0,69× |
| quoc_te | 150 | 27,33% | 2,32 | 22.515,17 | 1,88× |
| doi_tac | 68 | 54,41% | 1,88 | 10.214,87 | 0,85× |

- Loại quốc tế tốn **22.515,17 đ/việc thành công** (simulated). Trong các lượt chạy quốc tế, tỉ lệ `status=ok` ở lần 2 và 3 chỉ là **11,43%** và **2,15%**, nên dữ liệu cho thấy ít lượt chạy lại có kết quả OK.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc (đ) | Chi phí mỗi việc thành công + cố định (đ, simulated) | So với 12.000 đ (simulated) |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185,19 | 4.599,09 | 0,38× |
| Một nửa khối lượng (22.500 yêu cầu/tháng) | 16.875 | 2.370,37 | 5.784,27 | 0,48× |

- Sau khi phân bổ 40 triệu đ/tháng theo tỉ lệ 900/1.200 việc thành công trong phạm vi, cả hai mức vẫn dưới 12.000 đ/việc, lần lượt **4.599,09 đ** và **5.784,27 đ** (simulated).

## B1 · Đổi từng yếu tố

Mốc A2 là **4.471,97 đ/việc thành công** (simulated). Phần trăm thay đổi được tính trước khi làm tròn.

| Kịch bản | Cách tính | Chi phí mỗi việc thành công (đ, simulated) | Thay đổi so với A2 (simulated) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token, giữ giá tool | 4.723,08 | +5,62% |
| Giá token giảm một nửa | 13 đ và 65 đ cho 1.000 token, giữ giá tool | 4.346,41 | −2,81% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292,01 | +40,70% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.561,95 | −20,35% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.786,90 | +51,77% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.314,50 | −25,88% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.505,71 | +23,12% |
| Chỉ cho chạy tối đa 2 lần | Bỏ `attempt > 2`. Yêu cầu có `so_lan_chay > 2` chuyển cho nhân viên, đặt phút xem lại và làm lại về 0 | 4.237,29 | −5,25% |
| Chỉ cho chạy 1 lần | Áp dụng cùng quy tắc với giới hạn 1 | 4.110,99 | −8,07% |

## B2 · Đổi một cặp và xếp hạng

- Gấp đôi cả giá token và tỉ lệ xem lại cho **6.543,12 đ/việc thành công (+46,31%)** (simulated). Mức tăng bằng tổng hai tác động riêng trước khi làm tròn.
- Ba mức tăng mạnh nhất lần lượt là gấp đôi số ca làm lại (**+51,77%**), gấp đôi tỉ lệ xem lại (**+40,70%**) và tăng lương 25% (**+23,12%**) (simulated).

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống bằng tổng chi phí trợ lý cộng 12.000 đ cho mỗi yêu cầu không thành công.

| Giới hạn | Tổng chi phí trợ lý (đ, simulated) | Số yêu cầu không thành công | Chi phí cả hệ thống (đ, simulated) | Chi phí mỗi việc thành công (đ, simulated) |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.780,64 | 319 | 7.449.780,64 | **4.110,99** |
| 2 lần | 4.093.220,23 | 234 | **6.901.220,23** | 4.237,29 |
| 3 lần | 4.373.585,13 | 222 | 7.037.585,13 | 4.471,97 |

- Giới hạn **2 lần** có tổng chi phí hệ thống thấp nhất (**6.901.220,23 đ**), còn giới hạn **1 lần** có chi phí mỗi việc thành công thấp nhất (**4.110,99 đ**) (simulated). Giới hạn 1 lần có thêm **85 yêu cầu không thành công** so với 2 lần.

## B4 · Nếu phải xem lại tất cả

- Trong `noi_dia` + `hang_nang`, xem lại 5 phút cho mỗi ca trong số **948 ca có lượt `ok`**, với **48 ca làm lại** và **900 việc thành công**. Nếu làm lại mất **9 phút/ca**, chi phí là **11.742,79 đ/việc thành công (0,98×)**. Dùng **15,3 phút/ca** từ trung bình toàn mẫu (`1.132 / 74`, làm tròn) thì chi phí là **12.414,79 đ (1,03×)** (simulated).
- Để hòa vốn ở mốc **12.000 đ/việc thành công**, thời gian xem lại tối đa là **5,12 phút/ca** với giả định làm lại 9 phút và **4,80 phút/ca** với mức 15,3 phút (simulated). Pilot cần đo thời gian xem lại và mức có thể giảm tỉ lệ xem lại mà vẫn giữ an toàn.
