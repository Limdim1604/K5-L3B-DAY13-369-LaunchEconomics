# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- **Tên nhóm:** 369 · **Lớp:** L3B · **Repo nhóm:** `K5-L3B-DAY13-369-LaunchEconomics`
- **Thành viên:** xem [TEAM.md](../../TEAM.md)

## 2. Mục tiêu và cách tiếp cận

Nhóm xây dựng hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN trên mẫu giả lập (1.200 yêu cầu, 1.624 lượt chạy) để hội đồng Gate 2a xét duyệt kế hoạch pilot theo 4 câu hỏi: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao và pilot thiết kế thế nào để tách được tác động. Mọi số chi phí và cỡ mẫu được tính bằng [src/lab13.py](../../src/lab13.py), đối chiếu tay theo vai trò, gắn nhãn `simulated` cho các số suy từ cột `_simulated`, và gắn nhãn lỗi độc lập 8 phút trước khi so.

## 3. Giải pháp

- **A · Mô hình chi phí ([bang_chi_phi.md](bang_chi_phi.md), [src/lab13.py](../../src/lab13.py)):** Đạt 3/3 phép thử A1 (`1,20 · 1,25 · 1,25`); tính chi phí mọi lượt chạy chia số việc thành công (A2); tách 4 loại yêu cầu (A3) và phân bổ riêng cố định 40 triệu đ/tháng cho `noi_dia` + `hang_nang` (A4).
- **B · Độ nhạy ([bang_chi_phi.md](bang_chi_phi.md)):** Chạy 9 kịch bản đơn (B1), 1 kịch bản cặp (B2), so chi phí cả hệ thống ở giới hạn 1–3 lần chạy (B3) và kiểm tra kịch bản xem lại 100% ca đủ điều kiện (B4).
- **C · Bảng lỗi và khắc phục ([bang_loi.md](bang_loi.md)):** Hai thành viên gắn nhãn độc lập 20 ca theo 5 loại Google PAIR, giữ nguyên hai cột gốc và đồng thuận ban đầu, giải thích 17 ca lệch, viết lại định nghĩa 5 loại lỗi và lập bảng khắc phục cho 5 ca đại diện (Ca 9, 7, 18, 4, 17).
- **D · Kế hoạch pilot ([pilot_plan.yaml](pilot_plan.yaml)):** Tính 5 câu cỡ mẫu D1, kiểm 5 câu tách tác động D2, chia ngẫu nhiên 20 nhân viên/nhánh phân tầng theo depot, đặt 4 luật dừng đúng mẫu NẾU–TRONG–THÌ–KHÔNG THÌ và rollback ≤ 60 phút.
- **E · Chỉ số, rủi ro và hồ sơ v0 ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)):** Tính thử 3 chỉ số đợt chạy thử, đề xuất 2 chỉ số pilot, thiết kế 9 event có `trace_id`, tổng hợp 3 rủi ro kinh tế và ghép hồ sơ 1 trang trình Gate 2a.

- **Kiểm trên máy thứ hai.** Hà Lê Duy chạy `python -X utf8 lab13.py` từ `src/` trên bản `bb3eeff`. Mã thoát 0, A1 đạt **1,20 / 1,25 / 1,25** và chương trình in đầy đủ A1–A4, B1–B4 và D1.

## 4. Kết quả

### Con số chính và đề xuất cuối ([ho_so_launch_v0.md](ho_so_launch_v0.md))

- **Kinh tế & độ nhạy (`simulated` cho số chi phí từ cột `_simulated`):** Chi phí toàn mẫu **4.471,97 đ/việc** (`4.373.585,132 / 978`), gấp **16,28×** hóa đơn token + tool (**274,65 đ/yc**, đo từ trace); làm lại chiếm **51,77%**, xem lại **40,70%**. Phạm vi pilot còn `noi_dia` (**2.695,64 đ**, 0,22×) và `hang_nang` (**8.220,73 đ**, 0,69×); loại `quoc_te` (**22.515,17 đ**, 1,88×) và `doi_tac` (**10.214,87 đ**, 0,85×). Phân bổ riêng cố định **40 triệu đ/tháng** cho tổng **4.599,09–5.784,27 đ/việc** ở hai mức lưu lượng A4 (`simulated`). Ba yếu tố nhạy nhất: gấp đôi làm lại (**+51,77%**, lên 6.786,90 đ), gấp đôi xem lại (**+40,70%**) và lương +25% (**+23,12%**) (`simulated`). Giới hạn **2 lần chạy** có tổng chi phí hệ thống thấp nhất (**6.901.220,23 đ**, `simulated`), ít hơn giới hạn 1 lần 85 ca không thành công. Xem lại 100% ca đủ điều kiện (B4) đẩy chi phí biến đổi lên **11.742,79–12.414,79 đ/việc** (`simulated`), vượt ngưỡng biến đổi **8.000 đ**.
- **Chỉ số đợt chạy thử (không đối chứng, chỉ mô tả mẫu):** Đóng trong 24 giờ và không mở lại 7 ngày **994/1.200 = 82,83%**; sửa hoặc bỏ gợi ý **48/177 = 27,12%**; mở lại trong 7 ngày **51/1.200 = 4,25%** (`noi_dia` + `hang_nang`: 39/982 = 3,97%); đủ **9 event** có `trace_id`.
- **Lỗi, pilot & đề xuất cuối:** Đồng thuận nhãn ban đầu **3/20 (15%)** (< 80%, đã viết lại định nghĩa 5 loại). Pilot chia ngẫu nhiên **20 nhân viên/nhánh**, rollout **4 → 10 → 20**, cần **299 yêu cầu/người** (859 hiệu dụng / 5.980 thực tế mỗi nhánh, DE 6,96) cho mức tăng 6 điểm (power 80%; nếu tăng 5 điểm thì power **64,2%**). **Đề xuất chốt:** **Go có điều kiện** cho pilot `noi_dia` + `hang_nang` (tối đa 2 lần chạy).

### Kết quả duyệt chéo nhóm 369 nhận được từ hội đồng

- **Hội đồng chấm:** Nhóm **A90 — L3B** (chấm commit `cba61cc`, chạy kiểm `src/lab13.py` và hỏi–đáp trực tiếp ngày 25/11/2026).
- **Điểm chính thức & quyết định:** **30/30** (**C6:** 10/10 · **C7:** 10/10 · **C8:** 10/10) — Quyết định **Go có điều kiện** cho kế hoạch pilot `noi_dia` + `hang_nang`.
- **Câu hỏi của hội đồng:** Nếu chi phí thực tế vượt **8.000 đ/việc** trong hai tuần liên tiếp mà PM vẫn đang rà soát thì nhóm có được mở rộng pilot không, và xử lý thế nào nếu xem lại 100% đẩy chi phí lên khoảng **12.415 đ** như B4?
- **Trả lời của nhóm 369 & lý do dừng mở rộng theo kế hoạch pilot:** Không được mở rộng. Theo luật dừng chi phí trong [pilot_plan.yaml](pilot_plan.yaml), khi chi phí biến đổi đo được (token, tool, phút xem lại và làm lại; không gồm 40 triệu đ/tháng cố định) vượt **8.000 đ/việc** trong **hai cửa sổ 7 ngày liên tiếp** (tối thiểu **200 việc thành công**/cửa sổ), **Trưởng bộ phận vận hành CSKH** dừng mở rộng và giữ nguyên quy mô, không chuyển bước trong lúc **PM trợ lý hoàn phí** rà soát nguyên nhân. Mức ~**12.415 đ/việc** (`12.414,79 đ`, `simulated` ở B4 với xem lại 100% và làm lại 15,3 phút/ca) cao hơn mốc **12.000 đ** tự làm; trong pilot, nhóm đo phút xem lại/làm lại thực tế để rút ngắn bước tốn thời gian và chỉ giảm tỉ lệ xem lại khi chỉ số an toàn cho phép.
- **Nhận xét từ hội đồng A90:** Đánh giá cao tính minh bạch số bất lợi, gắn nhãn `simulated` đầy đủ và thiết kế pilot tách được tác động; đề nghị bổ sung lịch cutoff các bước rollout và cách đếm 299 yêu cầu/người, mẫu số tối thiểu Luật 1 và câu cấm chuyển bước vào vế `KHÔNG THÌ`, đồng bộ tên event giữa `bang_loi.md` và `chi_so.md`, gắn nhãn lại ≥ 80% sớm hơn bước 10 và hoàn thiện hồ sơ hành chính.

## 5. Khó khăn và cách xử lý

- **Đồng thuận gắn nhãn ban đầu thấp ở phần C (3/20 = 15% < 80%):** Do khác biệt cách tách nguyên nhân gốc và vị trí sửa; nhóm giữ nguyên 2 bộ nhãn gốc theo [RULES.md](../../RULES.md), giải thích 17 ca lệch, viết lại định nghĩa 5 loại lỗi và đặt điều kiện gắn nhãn lại đạt ≥ 80%.
- **Giới hạn cỡ mẫu 40 nhân viên:** Không đạt power 80% cho mức tăng 5 điểm; nhóm chọn 20 nhân viên/nhánh, chấp nhận MDE 6 điểm (299 yêu cầu/người), công khai power **64,2%** ở mức 5 điểm và yêu cầu xác minh phân bổ tại 12 depot trước khi mở.
- **Số phút nhân viên là `simulated` và B4 vượt 8.000 đ:** Ghi nhãn `simulated` ở mọi số suy diễn, tách riêng cố định 40 triệu đ/tháng với ngưỡng biến đổi 8.000 đ và bắt buộc đo phút thật từ bước 1.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong [TEAM.md](../../TEAM.md) và báo cáo cá nhân `report/team/MSSV_HoTen.md`.

## 7. Hạn chế và hướng cải thiện

- **Hạn chế:** (1) Thời gian xem lại/làm lại là `simulated`; (2) mẫu chạy thử chỉ có 6/12 depot và thiếu đối chứng nên ba chỉ số 82,83%, 27,12%, 4,25% chưa đo tác động nhân quả; (3) power ở mức tăng 5 điểm chỉ 64,2% và có rủi ro chia sẻ trong depot; (4) tên event chưa đồng bộ giữa [bang_loi.md](bang_loi.md) (`input_validation_failed`, `case_reopened`, `handoff_to_staff`) và [chi_so.md](chi_so.md) (`ticket_reopened`), đồng thời Luật 1 chưa ghi mẫu số tối thiểu ở bước 4 và thiếu ngày cutoff chi tiết từng bước.
- **Hướng cải thiện (tiếp thu A90):** Hoàn tất tiền kiểm (chặn Ca 7/20/17, xác minh 12 depot, chốt lịch 4→10→20, ngày cutoff đủ 7 ngày trước 20/01/2027 và quy tắc đếm 299 yêu cầu/người); thêm mẫu số tối thiểu Luật 1 và vế cấm chuyển bước trong [pilot_plan.yaml](pilot_plan.yaml); đồng bộ đầy đủ event giữa [bang_loi.md](bang_loi.md) và [chi_so.md](chi_so.md); đo thật `review_minutes`/`rework_minutes` từ tuần 1, kiểm mẫu 100 đơn/tuần và sớm kiểm chuẩn lại đồng thuận ≥ 80%.

## 8. Tài liệu tham khảo

- Đề bài, hướng dẫn Lab 13 (`docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`) và dữ liệu giả lập `src/logix_runs.csv`, `src/logix_requests.csv`.
- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models* (`arxiv.org/abs/2504.13359`).
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure" (`pair.withgoogle.com`).
- Tài liệu `statsmodels`, lớp `NormalIndPower` (`stats.power`).
