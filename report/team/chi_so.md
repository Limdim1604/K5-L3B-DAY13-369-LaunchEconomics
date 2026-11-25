# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | Đếm yêu cầu có `dong_trong_24h = 1` và `mo_lai_trong_7_ngay = 0`, chia tổng số yêu cầu | **994 / 1.200 = 82,83%** |
| Dùng | Tỉ lệ sửa hoặc bỏ gợi ý | Trong các yêu cầu có `duoc_xem_lai = 1`, đếm yêu cầu có `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **(41 sửa + 7 bỏ) / 177 = 48 / 177 = 27,12%** |
| An toàn | Tỉ lệ mở lại trong 7 ngày (dấu hiệu lỗi lọt đến khách) | Đếm yêu cầu có `mo_lai_trong_7_ngay = 1`, chia tổng số yêu cầu | **51 / 1.200 = 4,25%** |
| Dùng (đề xuất) | Tỉ lệ yêu cầu của nhánh trợ lý được nhân viên mở bằng trợ lý | Số yêu cầu khác nhau thuộc nhánh trợ lý và có lượt mở giao diện trợ lý, chia tổng số yêu cầu thuộc nhánh trợ lý trong cùng kỳ | Đo trong pilot |
| An toàn (đề xuất) | Tỉ lệ hoàn sai tiền trong mẫu kiểm tra hằng tuần | Số yêu cầu đã kiểm tra có số tiền thực hoàn khác số tiền đúng theo chính sách, chia tổng số yêu cầu có kết quả kiểm tra mẫu trong tuần | Đo trong pilot |

Đây là các chỉ số trong đợt chạy thử. Các tử số và mẫu số đếm trực tiếp từ [logix_requests.csv](../../src/logix_requests.csv) theo điều kiện trong bảng. Đợt chạy thử chưa có nhóm đối chứng nên kết quả mô tả mẫu và chưa cho biết tác động của trợ lý.

## Danh sách event

Hệ thống tạo `trace_id` khi tiếp nhận yêu cầu và truyền cùng `request_id` qua các event của pilot. Dùng `run_id` và `attempt` để phân biệt các lượt chạy. Trong CSV đợt chạy thử, mỗi lượt chạy có `trace_id` riêng và hai CSV nối bằng `request_id`. Đã kiểm sáu lượt đầu (`run_00001`–`run_00006`) và xác nhận cả **1.624/1.624** lượt đều có `trace_id`. [logix_runs.csv](../../src/logix_runs.csv)

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Dịch vụ tiếp nhận và phân tuyến | `trace_id`, `request_id`, `created_at`, `loai`, `arm`, `staff_id`, `depot` | Khi tiếp nhận và ghi nhận nhánh theo phân công nhân viên |
| `staff_assistant_opened` | Giao diện nhân viên | `trace_id`, `request_id`, `staff_id`, `opened_at` | Khi nhân viên mở trợ lý cho yêu cầu |
| `agent_run_completed` | Agent | `trace_id`, `request_id`, `run_id`, `attempt`, `status`, `tokens_in`, `tokens_out`, `tool_calls`, `completed_at` | Sau mỗi lượt chạy, kể cả lượt lỗi |
| `staff_review_decision` | Giao diện nhân viên | `trace_id`, `request_id`, `staff_id`, `decision` (`giu`, `sua`, `bo`), `review_minutes`, `decided_at` | Khi nhân viên hoàn tất xem lại và xác nhận quyết định |
| `staff_rework_completed` | Giao diện nhân viên | `trace_id`, `request_id`, `staff_id`, `rework_minutes`, `reason`, `completed_at` | Khi nhân viên hoàn tất xử lý lại |
| `ticket_closed` | Hệ thống ticket | `trace_id`, `request_id`, `closed_at` | Mỗi lần ticket chuyển sang trạng thái đóng |
| `ticket_reopened` | Hệ thống ticket | `trace_id`, `request_id`, `reopened_at`, `reason` | Mỗi lần ticket được mở lại |
| `audit_sample_checked` | Kế toán đối soát | `trace_id`, `request_id`, `audit_week`, `amount_refunded_vnd`, `amount_expected_vnd`, `checked_at` | Khi hoàn tất đối soát một yêu cầu trong mẫu tuần |
| `refund_outcome_finalized` | Hệ thống đối soát kết quả yêu cầu | `trace_id`, `request_id`, `ket_qua`, `finalized_at` | Khi đủ thời gian theo dõi và đã phân loại kết quả cuối |

**Kiểm tra chéo.** Nối event theo `trace_id` và đếm yêu cầu duy nhất theo `request_id`. Với chỉ số chính và tỉ lệ mở lại, so sánh theo nhánh đã phân ban đầu và chỉ dùng yêu cầu đủ thời gian theo dõi. [Kế hoạch pilot](pilot_plan.yaml)

| Chỉ số | Event dùng tính tử số và mẫu số |
| --- | --- |
| Đóng trong 24 giờ và không mở lại trong 7 ngày | Mẫu số từ `refund_request_created`. Tử số lấy `ticket_closed` lần đầu trong 24 giờ từ `created_at` và kiểm tra không có `ticket_reopened` trong 7 ngày sau lần đóng đó. |
| Sửa hoặc bỏ gợi ý | Mẫu số là yêu cầu có `staff_review_decision` hợp lệ. Lấy quyết định cuối của mỗi yêu cầu và đếm `sua` hoặc `bo` vào tử số. |
| Mở lại trong 7 ngày | Mẫu số từ `refund_request_created`. Tử số là yêu cầu có `ticket_reopened` trong 7 ngày sau lần đóng đầu tiên xác định từ `ticket_closed`. |
| Mở yêu cầu bằng trợ lý | Mẫu số từ `refund_request_created` với `arm` là nhánh trợ lý. Tử số là yêu cầu trong tập này có ít nhất một `staff_assistant_opened` trong kỳ đo. |
| Hoàn sai tiền trong mẫu kiểm tra | Mẫu số là yêu cầu có `audit_sample_checked` hoàn tất trong tuần. Tử số đếm yêu cầu có `amount_refunded_vnd` khác `amount_expected_vnd` ở kết quả kiểm tra cuối của tuần. |

## E2 · Rủi ro kinh tế

Tác động lấy từ B1, B4 và A4. Quy tắc dừng mở rộng lấy từ kế hoạch pilot. [Bảng chi phí](bang_chi_phi.md) · [Kế hoạch pilot](pilot_plan.yaml)

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi (B1) | **6.786,90 đ/việc thành công, +51,77%** so với A2 (simulated) | Theo dõi số yêu cầu có `staff_rework_completed` chia số yêu cầu trong phạm vi và số phút làm lại mỗi tuần. Mốc đợt chạy thử là **48/982 = 4,89%** theo `ket_qua = lam_lai` của `noi_dia` + `hang_nang`. | Rà trace làm lại theo loại yêu cầu, xác định nhóm lỗi và sửa luồng trước khi đề xuất mở rộng. | PM trợ lý hoàn phí |
| Phải xem lại 100% ca đủ điều kiện kéo dài (B4) | **11.742,79 đ/việc thành công** nếu làm lại 9 phút/ca và **12.414,79 đ** nếu làm lại 15,3 phút/ca (simulated). Cả hai vượt ngưỡng biến đổi **8.000 đ**. | Theo tuần, đếm yêu cầu có quyết định xem lại trên số yêu cầu có lượt `agent_run_completed` với `status = ok`, đồng thời đo `review_minutes`. | Rà bước xem lại tốn thời gian và thử rút ngắn thao tác. Chỉ giảm tỉ lệ xem lại khi kết quả giám sát an toàn cho phép. | Trưởng nhóm CSKH |
| Lưu lượng thấp làm tăng chi phí cố định mỗi việc (A4) | **40 triệu đ/tháng** tương ứng **1.185,19 đ/việc** khi có **33.750** việc thành công/tháng và **2.370,37 đ/việc** khi còn **16.875**. Tổng sau phân bổ là **4.599,09 đ** và **5.784,27 đ/việc thành công** (simulated). | Đối chiếu số việc thành công thực tế từ `refund_outcome_finalized` với sản lượng tháng dự báo. | Xem lại hiệu quả kinh tế và chi phí cố định trước quyết định mở rộng nếu sản lượng thấp hơn dự báo. | PM trợ lý hoàn phí |

- **Khoản cố định A4.** Phân bổ `40.000.000 / số việc thành công trong tháng`. A4 dự báo số việc thành công bằng lưu lượng toàn hệ thống nhân `900 / 1.200`, cho hai mức **45.000** và **22.500 yêu cầu/tháng**. Dùng tổng đã phân bổ để đánh giá hiệu quả kinh tế khi mở rộng.
- **Ngưỡng biến đổi D.** Tính `(token + tool + tiền xem lại + tiền làm lại) / số việc thành công` từ `agent_run_completed`, `staff_review_decision`, `staff_rework_completed` và `refund_outcome_finalized`. Khoản **40 triệu đ/tháng** được theo dõi ở phép tính A4 riêng. Trưởng bộ phận vận hành CSKH dừng mở rộng nếu chi phí biến đổi **vượt 8.000 đ/việc** trong **hai cửa sổ 7 ngày liên tiếp**, mỗi cửa sổ có **ít nhất 200 việc thành công**. B4 là kịch bản simulated để đối chiếu ngưỡng. Quy tắc dừng dùng số đo trong pilot.
