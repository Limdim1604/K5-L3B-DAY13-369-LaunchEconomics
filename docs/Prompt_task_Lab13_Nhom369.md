# Prompt làm Lab 13 cho nhóm 369

Duy, Trình, Châu mở repo nhóm trong agent của mình. Mỗi bạn **dán prompt khởi động một lần**, rồi dán **từng prompt mang tên mình** khi đến lượt. Nếu mở chat mới, dán lại prompt khởi động. Bảo dùng cột cuối bảng để điều phối. Các mục “sau 16h45” dưới đây là việc giao trước để đọc lịch.

| Lượt | Ai bắt đầu | Bảo cần làm để bàn giao |
|---|---|---|
| 1 · A | Duy tính, Trình so tiêu chí, Châu giữ bằng chứng | Tự kiểm tay một khoản, điền A1–A4 trong bảng chi phí rồi báo Duy số cơ sở A2 đã kiểm. |
| 2 · B và C | Duy chuyển sang B sau A. Trình và Châu có thể làm C độc lập trong lúc hai người còn lại chốt B. | Sau giải lao nhận code từ Duy, tự chạy lại, hoàn thiện phần code B còn thiếu. Bàn giao quyền sửa bảng chi phí cho Duy kiểm và chốt B. |
| 3 · Ghép C | Khi có đủ hai bộ nhãn gốc, Trình đối chiếu, Châu ghi bảng | Kiểm đủ 20 cặp nhãn và 5 dòng khắc phục. Trước 16h45 dừng ở A/B/C. |
| 4 · D và E | **Chỉ sau 16h45**. Duy làm E, Trình làm D2, Châu giữ hồ sơ | Bảo giữ quyền sửa lab13.py, tính 5 câu D1 và tỉ lệ mở lại trong 7 ngày, chuyển output cho Trình. Chốt lựa chọn pilot và đề xuất cùng nhóm. |
| 5 · Hội đồng và nộp | Châu ghi nhận xét thực tế. Từng người hoàn tất báo cáo riêng. | Xác nhận mốc duyệt 17h00 với coach vì giờ mở khóa sát giờ duyệt. Sau duyệt, kiểm repo, push bản chốt, gửi cùng một URL cho cả nhóm nộp LMS. |

## Prompt khởi động dùng chung

```text
Tôi là thành viên nhóm 369 lớp L3B, đang làm Lab 13 về trợ lý hoàn phí LogiX-VN. Hãy hỗ trợ tôi trong repo K5-L3B-DAY13-369-LaunchEconomics. Đọc TEAM.md, RULES.md, CHECKPOINTS.md, RUBRIC.md, SUBMISSION.md và docs/Phan_cong_Lab13_Nhom369.md. Tôi sẽ gửi từng lượt bên dưới. Trước mắt chỉ xác nhận đã tìm đúng repo và có thể bắt đầu lượt tôi giao.

Khi nhận lượt, xem trạng thái Git và mẫu file liên quan. Chỉ sửa file được giao trong lượt; giữ nguyên CSV và file starter. Giải thích cách làm, gợi ý code và giúp tôi chạy kiểm tra để chính tôi hiểu, thực hiện và bảo vệ kết quả. Mọi số phải truy được về output của lab13.py hoặc phép tính tay có ghi cách tính. Ghi nhãn simulated cho số suy ra từ cột _simulated. Không điền nhãn lỗi, hoạt động cá nhân hoặc kết quả hội đồng thay người thật. D/E chỉ bắt đầu khi đã qua 16h45 giờ Việt Nam và tôi gửi prompt lượt tương ứng.

Cuối mỗi lượt, viết cho tôi một tin nhắn ngắn để gửi Bảo gồm phần đã làm, file hoặc commit chứa thay đổi, lệnh kiểm và kết quả thật, phần còn thiếu và người nhận tiếp theo. Nếu thay đổi còn ở máy tôi, nhắc tôi chia sẻ commit hoặc gửi output trước khi báo người khác dùng. Không tự nhận rằng đồng đội đã nhận file hoặc nộp LMS.
```

## Duy · Người viết code rồi chuyển sang kiểm số

**Duy 1 — bắt đầu A ngay khi đã có repo.**

```text
Tôi là Hà Lê Duy, MSSV 2A202603851, GitHub duyhale95. Tôi phụ trách code A trong src/lab13.py. Đọc src/README.md và mẫu report/team/bang_chi_phi.md. Từ src/, hướng dẫn tôi viết và chạy 3 phép thử A1 đến khi đạt 1,20 / 1,25 / 1,25. Tiếp theo giúp tôi xây mo_hinh và kiểm cách tính A2 trên mọi lượt chạy, còn mẫu số chỉ đếm yêu cầu thành công. Kiểm việc cộng phút nhân viên đúng một lần trên mỗi yêu cầu. Chạy A3 theo 4 loại và A4 cho noi_dia + hang_nang ở cả hai mức lưu lượng. Xuất kết quả đủ để Bảo điền từng dòng và chọn một khoản Bảo có thể tính tay. Bảo đang giữ file bảng chi phí. Dừng sau A để Bảo xác nhận số cơ sở.
```

**Duy 2 — sau khi Bảo xác nhận A2.**

```text
Giúp tôi dùng lại mô hình A để làm B1–B4 theo đúng 9 kịch bản của mẫu, thêm kịch bản đổi một cặp, xếp hạng 3 yếu tố, so giới hạn chạy 1/2/3 theo cả chi phí công ty và chi phí mỗi việc thành công, rồi xét xem lại 100% ca nội địa và hàng nặng. So từng % thay đổi với cùng số cơ sở A2. Đến giờ đổi vai sau giải lao, liệt kê mục đã chạy, mục còn dở và gửi code cho Bảo. Từ khi Bảo nhận code, tôi giữ vai kiểm số: dùng output mới nhất của Bảo, kiểm chéo một kịch bản bằng tay và hoàn tất mục B trong report/team/bang_chi_phi.md khi Bảo đã giao file. Không sửa đồng thời lab13.py với Bảo.
```

**Duy 3 — sau 16h45, khi có bảng B.**

```text
Tôi phụ trách report/team/chi_so.md. Theo mẫu E1, giúp tôi kiểm công thức, tử số, mẫu số và số tính thử cho 3 chỉ số. Nếu cần thêm output từ lab13.py, soạn yêu cầu gửi Bảo, người đang giữ file code. Hỗ trợ tôi chọn thêm 1 chỉ số dùng và 1 chỉ số an toàn, mô tả ít nhất 6 event có trace_id, chỉ rõ mỗi chỉ số lấy từ event nào. Điền ít nhất 2 rủi ro kinh tế bằng số thật từ bảng B, có dấu hiệu, hành động và vai phụ trách. Chuyển bảng số đã kiểm cho Châu. Khi có commit chốt code, tôi chạy python lab13.py từ src/ trên máy thứ hai và gửi Bảo output cùng mã commit đã kiểm.
```

## Trình · Người gắn nhãn 1

**Trình 1 — lúc Duy làm A/B và khi bắt đầu C.**

```text
Tôi là Triệu Hải Đăng Trình, MSSV 2A202603874, GitHub DangTrinhdzZz. Trước hết tóm tắt điều kiện hoàn thành A/B từ rubric để tôi đối chiếu với Bảo và Duy. Đến C, chỉ cho tôi vị trí mục “Hai mươi ca lỗi” trong docs/Ngay13_Lab13_De_bai_hoc_vien.docx và tạo trong chat danh sách trống từ 1 đến 20. Nhắc tên 5 loại lỗi theo mẫu. Tôi sẽ tự đọc và ghi nhãn cho cả 20 ca trong 8 phút ở bản riêng. Không phân tích từng ca, gợi ý nhãn hay đọc bản của Châu. Dừng tại đây cho tới khi tôi xác nhận cả hai đã chốt bản gốc.
```

**Trình 2 — chỉ khi cả hai đã gắn xong.**

```text
Tôi sẽ dán hai bộ nhãn gốc của Trình và Châu, mỗi bộ đủ ca 1–20. Kiểm số ca, đối chiếu theo mã ca, xuất số trùng/20, phần trăm và danh sách ca lệch. Giữ nguyên cả hai cột. Với mỗi ca lệch, để tôi và Châu thống nhất nguyên nhân gốc rồi mới ghi nhãn cuối và một câu quy tắc. Nếu dưới 80%, nhắc chúng tôi viết lại định nghĩa và giữ kết quả đồng thuận ban đầu. Gửi bảng đối chiếu cho Châu, người duy nhất nhập report/team/bang_loi.md. Tôi cùng Châu chọn mỗi loại một ca và kiểm cách phát hiện có event, ngưỡng, tần suất.
```

**Trình 3 — sau 16h45, nhận số D1 từ Bảo.**

```text
Tôi phụ trách report/team/pilot_plan.yaml. Đọc yêu cầu D và mẫu YAML. Dùng 5 kết quả D1 và tỉ lệ mở lại 7 ngày do Bảo gửi, kiểm xem bằng chứng có ủng hộ cách chia nhóm đối chứng không. Nếu thiếu số, liệt kê đúng đầu ra cần Bảo bổ sung. Hỗ trợ tôi giải thích 5 câu D2 và so lựa chọn trước khi nhóm chốt. Ghi D1/D2 vào chú thích, điền các trường và 3 luật dừng về an toàn, chi phí, mức sử dụng theo NẾU – TRONG – THÌ – KHÔNG THÌ. Kiểm parse bằng yaml.safe_load và tìm dấu ? còn lại ngoài chú thích. Gửi Châu phạm vi, cỡ mẫu, đánh đổi, luật dừng. Trước khi nộp, đối chiếu 6 file hồ sơ với SUBMISSION.md và báo Bảo file còn thiếu.
```

## Châu · Người gắn nhãn 2 kiêm giữ hồ sơ

**Châu 1 — giữ bằng chứng A/B và tự làm C.**

```text
Tôi là Nguyễn Tấn Châu, MSSV 2A202603846, GitHub Lmeo2h. Giúp tôi giữ danh sách trong chat gồm mục A/B/C, file chứa bằng chứng và người đã kiểm để dùng sau. Khi bắt đầu C, chỉ mục “Hai mươi ca lỗi” trong docs/Ngay13_Lab13_De_bai_hoc_vien.docx, nhắc 5 loại lỗi và đưa 20 ô trống theo mã ca. Tôi tự gắn cả 20 nhãn trong 8 phút ở bản riêng. Không suy nhãn, không đọc nhãn của Trình. Chỉ sau khi cả hai xác nhận đã xong tôi mới chuyển nguyên bộ nhãn của mình cho Trình đối chiếu.
```

**Châu 2 — nhận bảng đối chiếu từ Trình.**

```text
Tôi giữ report/team/bang_loi.md. Tôi sẽ cung cấp hai bộ nhãn thật, kết quả đối chiếu của Trình và các quyết định hai người đã thống nhất. Giúp tôi nhập nguyên hai cột nhãn, số trùng/20, tỉ lệ đồng thuận, cột thống nhất và quy tắc cho từng ca lệch. Với 5 ca hai người đã chọn, kiểm đủ 5 loại, cách phát hiện đo được, hành động khắc phục và một vai phụ trách mỗi dòng. Thiếu quyết định nào thì hỏi tôi đúng mục đó. Chuyển tên file và bằng chứng hoàn tất C cho Bảo.
```

**Châu 3 — chỉ mở sau 16h45, rồi cập nhật khi có D/E.**

```text
Tôi giữ report/team/ho_so_launch_v0.md. Từ bằng chứng A/B/C đã kiểm, điền các mục tương ứng. Khi nhận pilot_plan.yaml từ Trình và chi_so.md từ Duy, giúp tôi hoàn thiện 1 trang theo 7 mục của mẫu. Mỗi mục có số chính, trạng thái và một vai phụ trách. Chỉ ghi đề xuất cuối sau khi nhóm chốt Go / Go có điều kiện / No-go. Nêu số bất lợi, cách xử lý và phạm vi pilot. Kiểm nhãn simulated. Báo Bảo bản sẵn sàng để nhóm gửi hội đồng vào mốc coach xác nhận.
```

**Châu 4 — tại buổi duyệt và sau khi nhận phản hồi.**

```text
Tôi sẽ nhập tên nhóm đối tác, điểm từng tiêu chí, bằng chứng, quyết định, câu hỏi và câu trả lời thực tế tại buổi duyệt. Hỗ trợ ghi phiếu nhóm mình chấm nhóm khác vào report/team/phieu_cham.md. Phân biệt phiếu đó với phản hồi do hội đồng chấm nhóm mình, dùng phản hồi nhận được cho mục kết quả của report/team/group_report.md. Giữ báo cáo nhóm tối đa 2 trang, dẫn các file và đóng góp thật. Nội dung nào hội đồng chưa cung cấp thì liệt kê để tôi hỏi tại buổi. Chuyển hai file cho Bảo kiểm bản nộp.
```

## Prompt cuối cho từng người

Dán vào chat của **chính mình**, sau khi xong phần được giao và trước khi Bảo chốt repo. Bảo cũng dùng được prompt này.

```text
Tôi chuẩn bị nộp bài cá nhân Lab 13. Hãy copy report/team/MSSV_HoTen.md thành file của tôi theo danh sách dưới đây, giữ nguyên mẫu. Dùng bằng chứng thực tế trong chat và repo để hỗ trợ tôi điền phần việc, đóng góp, file/commit/output, công cụ AI và cách tự kiểm. Hỏi tôi về email còn thiếu, việc tự đánh giá hoặc phần chưa có bằng chứng. Chỉ sửa báo cáo của người đang dùng chat. Gửi Bảo đường dẫn và commit chứa báo cáo. Sau khi Bảo gửi URL repo bản chốt, tôi tự nộp URL đó trên LMS bằng tài khoản cá nhân trước 23h59 GMT+7 ngày lab, kiểm tra trạng thái và báo Bảo.

Bảo   2A202603861_NguyenThienBao.md
Duy   2A202603851_HaLeDuy.md
Trình 2A202603874_TrieuHaiDangTrinh.md
Châu  2A202603846_NguyenTanChau.md
```
