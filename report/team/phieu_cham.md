# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- **Nhóm chấm (hội đồng):** Nhóm 369 · Lớp L3B
- **Nhóm được chấm:** Nhóm 456 · Lớp L3B ([K5-L3B-DAY13-Nhom456-LaunchEconomics](https://github.com/cuakicuc4444/K5-L3B-DAY13-Nhom456-LaunchEconomics))
- **Hồ sơ đối chiếu:** [Commit `da10455`](https://github.com/cuakicuc4444/K5-L3B-DAY13-Nhom456-LaunchEconomics/commit/da10455a2bd9aa55926c990fe6d14c5cf16abaf5) · **Phạm vi chấm:** C6–C8 theo [RUBRIC.md](https://github.com/cuakicuc4444/K5-L3B-DAY13-Nhom456-LaunchEconomics/blob/da10455a2bd9aa55926c990fe6d14c5cf16abaf5/RUBRIC.md)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng (C6) | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | **10** | Nhóm đề xuất Go có điều kiện và nêu rõ rủi ro xem lại 100% làm chi phí lên **11.743–12.415 đ/việc** (`simulated`), sát hoặc vượt mốc **12.000 đ**. Hồ sơ giao Trưởng nhóm CSKH phụ trách giảm tỷ lệ xem lại theo bậc và giao Kỹ sư trưởng agent thu thập số phút thực tế ([ho_so_launch_v0.md](https://github.com/cuakicuc4444/K5-L3B-DAY13-Nhom456-LaunchEconomics/blob/da10455a2bd9aa55926c990fe6d14c5cf16abaf5/report/team/ho_so_launch_v0.md)). |
| Số giả lập và phạm vi (C7) | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | **10** | Bảng chi phí đánh dấu các kết quả mô hình là `simulated`. Hồ sơ giới hạn pilot ở nội địa (**2.696 đ/việc**) và hàng nặng (**8.221 đ/việc**). Kế hoạch ghi rõ chi phí quốc tế **1,88×** và đối tác **0,85×** so với tự làm (`simulated`). Bảng A3 cho thấy nhóm đối tác chỉ thành công **54,4%**, nên có cơ sở chọn phạm vi hẹp cho đợt đầu ([bang_chi_phi.md](https://github.com/cuakicuc4444/K5-L3B-DAY13-Nhom456-LaunchEconomics/blob/da10455a2bd9aa55926c990fe6d14c5cf16abaf5/report/team/bang_chi_phi.md)). |
| Pilot ra được quyết định (C8) | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | **10** | Chia ngẫu nhiên theo tầng depot và đối chứng song song **20 + 20**. Mục tiêu **299 yêu cầu/người** cho khoảng **859 yêu cầu hiệu dụng mỗi nhánh** ở MDE 6 điểm; nếu mức tăng thật là 5 điểm, power khoảng **64%**. Ba luật dừng có ngưỡng, thời hạn và vai phụ trách ([pilot_plan.yaml](https://github.com/cuakicuc4444/K5-L3B-DAY13-Nhom456-LaunchEconomics/blob/da10455a2bd9aa55926c990fe6d14c5cf16abaf5/report/team/pilot_plan.yaml)). |
| **Tổng** | | | | **30 / 30** | Go có điều kiện. |

**Quyết định của hội đồng:** **Go có điều kiện**

**Lý do:** Hồ sơ nhóm 456 khớp bằng chứng, gắn nhãn `simulated` đầy đủ, thu hẹp phạm vi pilot sang nội địa và hàng nặng có căn cứ số và thiết kế pilot tách được tác động. Trước khi mở pilot, hội đồng đề nghị nhóm 456 hoàn thiện hai điểm sau:

1. **Chốt thời gian thu mẫu:** Ở bước 20 người, thu đủ **299 yêu cầu/người** và chờ đủ **7 ngày theo dõi** cho các ca được đánh giá; nếu một tuần chưa đủ ca, kéo dài thời gian thu mẫu.
2. **Làm rõ ngưỡng 8.000 đ trong YAML:** Dùng chi phí biến đổi đo trong pilot (gồm token, tool và thời gian nhân viên) và đánh giá riêng khoản cố định **40 triệu đ/tháng** khi cân nhắc mở rộng.

**Một câu hỏi cho đội trình:** “Trong ba khoản tiền token, thời gian nhân viên xem lại và thời gian nhân viên làm lại, khoản nào tốn nhất? Khoản đó chiếm khoảng bao nhiêu phần trăm tổng chi phí?”

**Câu trả lời của đội trình (ghi lại tại buổi):** “Trong ba khoản chi phí, thời gian nhân viên làm lại là khoản tốn kém nhất, ngốn **2.264.000 đ** và chiếm **51,77%** tổng chi phí mô hình A2 (`simulated`). Khoản xem lại đứng thứ hai với **40,69%**, còn tiền token chiếm **5,61%**, khoảng **245.000 đ**. Chi phí làm lại cao vì lương nhân viên là **2.000 đ/phút** và mỗi ca làm lại mất trung bình khoảng **15,3 phút** để rà soát và khắc phục cho khách. Bảng độ nhạy cho thấy nếu số ca làm lại tăng gấp đôi, chi phí mỗi việc thành công tăng khoảng **51,8%**, lên **6.787 đ** (`simulated`). Vì vậy, ưu tiên kinh tế của pilot là kiểm soát lỗi và giảm thời gian nhân viên phải làm lại.”
