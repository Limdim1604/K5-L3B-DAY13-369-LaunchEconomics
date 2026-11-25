# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

**Nhóm 369 · L3B.** Pilot đề xuất cho `noi_dia` và `hang_nang`, tối đa 2 lần chạy. Chi phí có nhãn `simulated` là kết quả mô hình. Các mốc dưới đây là đề xuất.

| Mục | Con số chính | Trạng thái | Vai phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.471,97 đ/việc** toàn mẫu, gấp **16,28×** hóa đơn token và tool (**274,65 đ/yêu cầu**). Nội địa **2.695,64 đ**, hàng nặng **8.220,73 đ** (`simulated`). [A2–A3](bang_chi_phi.md) | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Gấp đôi ca làm lại **+51,77%**, gấp đôi xem lại **+40,70%**, tăng lương 25% **+23,12%** (`simulated`). [B1–B2](bang_chi_phi.md) | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Mốc **12.000 đ/yêu cầu**. Quốc tế **22.515,17 đ/việc** và đối tác **10.214,87 đ/việc** nằm ngoài phạm vi pilot. Giới hạn **2 lần** có chi phí hệ thống toàn mẫu thấp nhất, **6.901.220,23 đ**, với **85** yêu cầu không thành công ít hơn giới hạn 1 lần (`simulated` cho chi phí). [A3, B3](bang_chi_phi.md) | Giả lập | Trưởng nhóm CSKH |
| 4 · Chỉ số | Đợt chạy thử: đóng trong 24 giờ và không mở lại 7 ngày **994/1.200 = 82,83%**; sửa hoặc bỏ **48/177 = 27,12%**; mở lại **51/1.200 = 4,25%**. Có **9 event** đề xuất, mỗi event có `trace_id`. [E1](chi_so.md) | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 5 · Lỗi và khắc phục | **20 ca, 5 loại**. Đồng thuận ban đầu **3/20 (15%)** dưới mục tiêu 80%; nhóm giữ nguyên nhãn gốc và viết lại định nghĩa. [C](bang_loi.md) | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Kế hoạch pilot | Chia ngẫu nhiên **20 nhân viên/nhánh** theo tầng depot, mở **4 → 10 → 20**. Đánh giá ở bước 20 khi đủ **299 yêu cầu/người** và đủ **7 ngày** theo dõi. Thiết kế cho mức tăng **6 điểm**; nếu chỉ tăng 5 điểm, power **64,2%**. [D](pilot_plan.yaml) | Xong, có bằng chứng | Trưởng bộ phận vận hành CSKH |
| 7 · Rủi ro kinh tế | Tăng gấp đôi ca làm lại lên **6.786,90 đ/việc**. Xem lại toàn bộ ca đủ điều kiện lên **11.742,79–12.414,79 đ/việc**, vượt ngưỡng biến đổi **8.000 đ**. Phân bổ riêng **40 triệu đ/tháng** cho tổng **4.599,09–5.784,27 đ/việc** ở hai mức lưu lượng A4 (`simulated`). [A4](bang_chi_phi.md) · [E2](chi_so.md) | Giả lập | PM trợ lý hoàn phí |

## Điều kiện duyệt

- **Trước khi mở, dự kiến 05/12/2026.** Kỹ sư trưởng agent kiểm khóa chống hoàn trùng, chỉ báo hoàn khi sổ cái xác nhận, làm mới cache bảng giá, bật event và kiểm giới hạn 2 lần. Trưởng bộ phận vận hành CSKH xác minh phân bổ 40 người tại 12 depot và duyệt mục tiêu phát hiện 6 điểm.
- **Trước bước 10.** Trưởng nhóm CSKH kiểm số phút xem lại/làm lại đo thật. Kế toán trưởng đối soát 100 đơn/tuần. PM trợ lý hoàn phí tổ chức gắn nhãn độc lập lại 20 trace với mục tiêu ≥80% và chốt ngưỡng chuyển nhân viên. Tuân theo bốn luật dừng trong [kế hoạch pilot](pilot_plan.yaml).
- **Khi đủ dữ liệu, dự kiến 20/01/2027.** PM trợ lý hoàn phí đối chiếu chi phí cố định theo sản lượng thực. Trưởng bộ phận vận hành CSKH chỉ đánh giá hiệu quả khi đủ mẫu và đủ thời gian theo dõi.

**Đề xuất: Go có điều kiện.** Chỉ mở pilot cho nội địa và hàng nặng sau khi đạt điều kiện trước khi mở. Chỉ chuyển bước khi đáp ứng các điều kiện kiểm tra và luật dừng tương ứng.
