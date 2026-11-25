# Phân công Lab 13 · Nhóm 369 · L3B

Nhóm mình cần trả lời câu hỏi “Có nên thử nghiệm trợ lý hoàn phí của LogiX-VN, với loại yêu cầu nào và điều kiện gì?”. Trước 16h45, chúng ta chỉ làm **A (chi phí), B (độ nhạy), C (lỗi)**. Dùng số do code nhóm tính hoặc ghi rõ phép tính tay. Mỗi câu trả lời tối đa 3 dòng, có ít nhất một con số. Gắn nhãn `simulated` cho mọi số suy ra từ hai cột `_simulated`.

## Mỗi người nhận một vai theo TEAM.md

| Thành viên | Vai theo đề | Việc cần bàn giao |
|---|---|---|
| Hà Lê Duy · 2A202603851 · duyhale95 | Người viết code trước giải lao | Viết A và B trong [lab13.py](../src/lab13.py). Bàn giao cho Bảo bản code đang chạy, kết quả và mục còn thiếu. Sau giải lao nhận vai kiểm số. |
| Nguyễn Thiên Bảo · 2A202603861 · Limdim1604 | Người kiểm số trước giải lao, kiêm nhóm trưởng | Mình tính tay ít nhất một khoản, điền bảng A/B. Sau giải lao mình nhận vai viết code, tự chạy và kiểm lại phép tính chi phí. Mình phụ trách chốt repo và tiến độ nộp. |
| Triệu Hải Đăng Trình · 2A202603874 · DangTrinhdzZz | Người gắn nhãn 1 | Đọc điều kiện “Xong khi”, kiểm độ đầy đủ của A/B. Đến C, tự gắn đủ 20 nhãn, sau đó phụ trách đối chiếu và ghi quy tắc cho từng ca lệch. |
| Nguyễn Tấn Châu · 2A202603846 · Lmeo2h | Người gắn nhãn 2 kiêm giữ hồ sơ | Giữ đường dẫn và bằng chứng A/B/C từ đầu buổi. Đến C, tự gắn đủ 20 nhãn rồi tổng hợp bảng lỗi. Sau giờ mở khóa, ghép bằng chứng vào hồ sơ một trang. |

## Trình tự trước 16h45

1. **Khởi động — cả nhóm.** Clone hoặc pull repo nhóm 369. Mình cập nhật [TEAM.md](../TEAM.md) với email Bảo `26ai.baont5@vinuni.edu.vn`, Duy `26ai.duyhl2@vinuni.edu.vn`; Trình và Châu gửi mình email còn thiếu. Cài Python 3.10+ theo [hướng dẫn chạy](../src/README.md). Từ thư mục `src/`, chạy `python lab13.py`. Giữ nguyên bản starter và hai CSV gốc.
2. **A — Duy tính, Bảo kiểm.** A1 phải đạt cả ba giá trị 1,20 · 1,25 · 1,25 rồi mới làm tiếp. A2 cộng tiền token và tool trên mọi lần chạy, cộng thời gian nhân viên theo từng yêu cầu, rồi chia cho số yêu cầu thành công. Mình đối chiếu một khoản bằng tay và điền 9 dòng. A3 so 4 loại với mốc 12.000 đ khi nhân viên tự làm. A4 phân bổ 40 triệu đ/tháng cho phạm vi nội địa và hàng nặng ở hai mức lưu lượng. Trình so với tiêu chí, Châu lưu bằng chứng. **Bàn giao** bảng cơ sở đã kiểm trong [bảng chi phí](../report/team/bang_chi_phi.md).
3. **B — dùng lại mô hình A.** Duy chạy 9 kịch bản đổi từng yếu tố (B1), rồi đổi đồng thời giá token và tỉ lệ xem lại, xếp hạng 3 yếu tố (B2). Mình đối chiếu % thay đổi với A2. B3 so chi phí cả hệ thống ở giới hạn 1, 2, 3 lần chạy, kể cả tiền chuyển việc cho nhân viên. B4 thử xem lại 100% ca nội địa và hàng nặng. Điền kết quả vào cùng bảng. **Sau giải lao**, Duy giao bàn phím cho mình, Duy chuyển sang kiểm số. Hai người hoàn thiện B trong lúc Trình và Châu làm C.
4. **C — Trình và Châu làm độc lập trước khi so.** Mở mục “Hai mươi ca lỗi” trong [đề gốc](Ngay13_Lab13_De_bai_hoc_vien.docx). Mỗi bạn dành 8 phút tự gắn toàn bộ 20 ca vào bản riêng theo nguyên nhân gốc. Khi cả hai xong, Châu chép nguyên hai cột vào [bảng lỗi](../report/team/bang_loi.md). Trình tính số trùng/20, mục tiêu ít nhất 16/20. Giữ nguyên hai cột ban đầu, ghi nhãn thống nhất vào cột riêng. Mỗi ca lệch ghi một câu phân biệt; nếu dưới 80%, ghi lại định nghĩa đã chỉnh.
5. **Chốt A/B/C.** Trình và Châu chọn 5 ca đại diện đủ 5 loại. Mỗi ca có cách phát hiện đo được, cách khắc phục và một vai phụ trách. Mình kiểm bảng lỗi, Duy đối chiếu số A/B với slide chữa (dung sai 2%). Nếu xong sớm, cả nhóm soát A/B/C đến mốc mở khóa.

## Sau 16h45 đến lúc nộp

Mốc duyệt trong đề là **17h00**. Mình xác nhận với coach trong lúc nhóm làm A/B/C vì từ lúc mở D/E đến lúc duyệt chỉ có khoảng 15 phút. Dùng giờ mới nếu coach thông báo.

| Thứ tự | Phân công | Xong khi |
|---|---|---|
| 6 · D và E song song sau khi mở khóa | **D:** Bảo viết code tính 5 câu D1 và tỉ lệ mở lại trong 7 ngày. Trình nhận số, trả lời 5 câu D2 và điền [kế hoạch pilot](../report/team/pilot_plan.yaml). **E:** Duy tính, kiểm 3 chỉ số và điền [bảng chỉ số](../report/team/chi_so.md). Châu ghép [hồ sơ launch](../report/team/ho_so_launch_v0.md). | YAML đọc được, đủ trường và 3 luật dừng về an toàn, chi phí, sử dụng. Mỗi luật đủ NẾU – TRONG – THÌ – KHÔNG THÌ. E có thêm 1 chỉ số dùng và 1 chỉ số an toàn, ít nhất 6 event có trace_id và 2 rủi ro từ B. Hồ sơ 1 trang đủ 7 mục, có số, trạng thái, vai phụ trách và dòng cuối đề xuất Go / Go có điều kiện / No-go. |
| 7 · Duyệt chéo | Châu gửi hồ sơ cho hội đồng. Mình trình bày và giải thích đề xuất, Duy bảo vệ số liệu, Trình giải thích cách xử lý lỗi và thiết kế pilot. Khi đến lượt chấm, nhóm n chấm nhóm n + 1, nhóm cuối chấm nhóm 1. | Châu ghi điểm và nhận xét thực tế của nhóm mình về nhóm được chấm vào [phiếu chấm](../report/team/phieu_cham.md). |
| 8 · Đóng gói tại lớp, 17h45–18h00 theo đề | Duy chạy lại code từ đầu trên máy thứ hai. Trình kiểm đủ 6 file hồ sơ bằng [checklist nộp](../SUBMISSION.md). Châu tổng hợp [báo cáo nhóm](../report/team/group_report.md). Mình cập nhật đóng góp thật trong TEAM.md và push bản chốt. | Repo mở được cho giảng viên, code chạy hết, tên file đúng, không có secret, .env hay .venv trong commit. |
| 9 · Nộp LMS trước 23h59 GMT+7 ngày lab | **Cả bốn người**, mỗi người tự đăng nhập LMS, nộp cùng URL repo nhóm và báo mình sau khi đã kiểm tra trạng thái nộp. | Đủ 4 lượt nộp cá nhân. |

**Báo cáo cá nhân.** Trước khi mình push bản chốt, mỗi người copy [mẫu](../report/team/MSSV_HoTen.md) ngay trong `report/team/`, ghi phần việc thực tế, bằng chứng, công cụ AI đã dùng và cách tự kiểm. Giữ lại file mẫu.

| Bảo | Duy | Trình | Châu |
|---|---|---|---|
| `2A202603861_NguyenThienBao.md` | `2A202603851_HaLeDuy.md` | `2A202603874_TrieuHaiDangTrinh.md` | `2A202603846_NguyenTanChau.md` |

Căn cứ phân công và chấm bài nằm ở [TEAM.md](../TEAM.md), [luật lab](../RULES.md), [checkpoints](../CHECKPOINTS.md), [rubric](../RUBRIC.md) và [hướng dẫn nộp](../SUBMISSION.md).
