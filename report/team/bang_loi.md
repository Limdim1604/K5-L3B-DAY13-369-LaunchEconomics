# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Triệu Hải Đăng Trình · Người gắn nhãn 2: Nguyễn Tấn Châu (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Giới hạn hệ thống | Do người dùng | Không | Do người dùng |
| 2 | Do người dùng | Hệ thống | Không | Hệ thống |
| 3 | Giới hạn hệ thống | Ngữ cảnh | Không | Ngữ cảnh |
| 4 | Do người dùng | Giới hạn hệ thống | Không | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Ngữ cảnh | Do người dùng | Không | Do người dùng |
| 7 | Ngữ cảnh | Hệ thống | Không | Hệ thống |
| 8 | Giới hạn hệ thống | Hệ thống | Không | Hệ thống |
| 9 | Hệ thống | Do người dùng | Không | Do người dùng |
| 10 | Do người dùng | Ngữ cảnh | Không | Ngữ cảnh |
| 11 | Ngữ cảnh | Giới hạn hệ thống | Không | Giới hạn hệ thống |
| 12 | Ngữ cảnh | Ngầm | Không | Ngầm |
| 13 | Ngữ cảnh | Giới hạn hệ thống | Không | Giới hạn hệ thống |
| 14 | Ngữ cảnh | Do người dùng | Không | Do người dùng |
| 15 | Giới hạn hệ thống | Hệ thống | Không | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Do người dùng | Ngầm | Không | Ngầm |
| 18 | Do người dùng | Ngữ cảnh | Không | Ngữ cảnh |
| 19 | Hệ thống | Giới hạn hệ thống | Không | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 3 / 20 = 15%

*Ghi chú: Giữ nguyên hai bộ nhãn độc lập ban đầu và tỉ lệ đồng thuận thực tế 15% (trùng 3 ca: 5, 16, 20; bất đồng 17 ca). Sau khi đối chiếu và rà soát lại định nghĩa, hai thành viên thống nhất sử dụng bộ nhãn của Nguyễn Tấn Châu làm nhãn cuối theo lựa chọn của Triệu Hải Đăng Trình.*

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

### Giải thích nguyên nhân gốc cho 17 ca không trùng

- **Ca 01 – Do người dùng:** Nguyên nhân gốc xuất phát từ việc khách hàng nhập số tài khoản nhận hoàn tiền thiếu hai chữ số, khiến ngân hàng từ chối giao dịch; đây là lỗi dữ liệu đầu vào do khách cung cấp, không phải lỗi tính toán hay xử lý của trợ lý.
- **Ca 02 – Hệ thống:** Trợ lý sử dụng sai tham số khi tra bảng giá, áp dụng mức phí hàng thường cho kiện hàng nặng 28 kg dẫn đến hoàn thiếu 45.000 đồng; nguyên nhân gốc là hệ thống thực hiện sai quy tắc tính phí đã thiết kế.
- **Ca 03 – Ngữ cảnh:** Trợ lý đã hoàn tiền đúng thiết kế vào ví LogiX, nhưng khách hàng lại kỳ vọng nhận tiền qua tài khoản ngân hàng; vấn đề xuất phát từ sự khác biệt giữa cách hệ thống hoạt động và kỳ vọng thực tế của khách hàng.
- **Ca 04 – Giới hạn hệ thống:** Yêu cầu hoàn phí liên quan đến chặng giao hàng của hãng nước ngoài mà LogiX không có dữ liệu, nên do thiếu thông tin cần thiết trợ lý không thể xác định trạng thái và phải chuyển cho nhân viên xử lý.
- **Ca 06 – Do người dùng:** Khách hàng chọn nhầm mục hoàn phí giao trễ trong khi vấn đề thực tế là hàng hóa bị vỡ, khiến trợ lý xử lý theo quy trình không phù hợp.
- **Ca 07 – Hệ thống:** API sổ cái trả về lỗi 503 (giao dịch chưa được xác nhận thành công) nhưng trợ lý vẫn thông báo đã hoàn tiền; nguyên nhân gốc là hệ thống không kiểm tra chính xác trạng thái giao dịch trước khi phản hồi.
- **Ca 08 – Hệ thống:** Trợ lý trích dẫn Điều 7.2 làm căn cứ hoàn phí trong khi điều khoản này không tồn tại trong chính sách hiện hành; mặc dù số tiền hoàn đúng, hệ thống vẫn cung cấp thông tin căn cứ không chính xác.
- **Ca 09 – Do người dùng:** Khách hàng nhập mã đơn hàng của sàn thương mại điện tử thay vì mã vận đơn theo yêu cầu; nguyên nhân gốc là sử dụng sai loại mã đầu vào khiến trợ lý không thể tra cứu thông tin.
- **Ca 10 – Ngữ cảnh:** Trợ lý từ chối hoàn phí đúng theo điều khoản bất khả kháng do bão, nhưng ứng dụng vẫn hiển thị cam kết giao hàng trong 24 giờ, tạo mâu thuẫn giữa kỳ vọng của khách và chính sách áp dụng khiến khách thấy kết quả không hợp lý.
- **Ca 11 – Giới hạn hệ thống:** Khách hàng gửi tin nhắn thoại dài 40 giây nhưng trợ lý không có khả năng xử lý dữ liệu âm thanh; đây là giới hạn về định dạng đầu vào mà hệ thống hỗ trợ.
- **Ca 12 – Ngầm:** Tool tra cứu trả về thiếu dữ liệu khiến trợ lý phải thực hiện nhiều lần gọi làm chi phí token tăng gấp ba trong ba tuần, nhưng vì kết quả cuối cùng vẫn chính xác nên bất thường về chi phí không được phát hiện trong quá trình vận hành.
- **Ca 13 – Giới hạn hệ thống:** Khách hàng yêu cầu hoàn phí bảo hiểm hàng hóa (sản phẩm của công ty bảo hiểm đối tác, ngoài phạm vi hỗ trợ của trợ lý); việc trợ lý trả lời chung chung là điểm cần cải thiện, nhưng nguyên nhân gốc vẫn là giới hạn phạm vi xử lý.
- **Ca 14 – Do người dùng:** Khách hàng bấm nhầm nút xác nhận đã nhận tiền khi thực tế chưa nhận được khiến yêu cầu bị đóng; nguyên nhân gốc là thao tác không chính xác của khách hàng.
- **Ca 15 – Hệ thống:** Theo chính sách, đơn giao trễ 26 giờ chỉ được hoàn 50% nhưng trợ lý tính hoàn 100%; nguyên nhân gốc là hệ thống áp dụng sai quy tắc hoàn phí và lỗi đã được nhân viên phát hiện trước khi gửi.
- **Ca 17 – Ngầm:** Sau khi bảng giá thay đổi, trợ lý vẫn sử dụng phiên bản cũ trong bộ nhớ đệm gây sai lệch số tiền của 212 đơn trong chín ngày, và các sai sót này không được khách hàng phản ánh hoặc hệ thống cảnh báo nên thuộc lỗi ngầm.
- **Ca 18 – Ngữ cảnh:** Trợ lý tính đúng số tiền hoàn là 15.000 đồng (50% phí giao hàng 30.000 đồng) nhưng không giải thích cách tính trong tin nhắn, khiến khách hàng hiểu nhầm rằng số tiền hoàn không đầy đủ.
- **Ca 19 – Giới hạn hệ thống:** Khách hàng yêu cầu tra cứu đơn hàng từ 14 tháng trước trong khi trợ lý chỉ truy cập được dữ liệu 12 tháng gần nhất; đây là giới hạn dữ liệu của hệ thống nên trợ lý không thể tự xử lý yêu cầu.

### Định nghĩa năm loại lỗi viết lại sau khi rà soát (đồng thuận ban đầu 15% < 80%)

Do tỉ lệ đồng thuận ban đầu giữa hai người gắn nhãn chỉ đạt 15%, thấp hơn yêu cầu 80%, nhóm đã rà soát và làm rõ lại định nghĩa của năm loại lỗi nhằm thống nhất cách phân loại dựa trên nguyên nhân gốc:

- **Do người dùng:** Là những trường hợp nguyên nhân trực tiếp xuất phát từ dữ liệu hoặc thao tác không chính xác của khách hàng, chẳng hạn nhập sai mã vận đơn, lựa chọn nhầm loại yêu cầu hoặc xác nhận sai trạng thái giao dịch. Khi phân loại, cần xác định lỗi có bắt nguồn từ hành động của người dùng hay không; dù hệ thống có thể bổ sung tính năng kiểm tra hoặc hướng dẫn để phòng tránh, điều này không làm thay đổi nguyên nhân gốc.
- **Hệ thống:** Xảy ra khi trợ lý có đủ dữ liệu và khả năng xử lý nhưng thực hiện không đúng thiết kế, quy trình hoặc chính sách đã quy định (liên quan đến tính toán, tra cứu, thông báo trạng thái hoặc trích dẫn thông tin). Điểm phân biệt quan trọng là lỗi đã được phát hiện trong quá trình vận hành hoặc thể hiện rõ qua kết quả xử lý.
- **Ngữ cảnh:** Xảy ra khi trợ lý hoạt động đúng theo thiết kế và chính sách nhưng kết quả không phù hợp với hoàn cảnh, kỳ vọng hoặc cách hiểu của khách hàng, thường do sự thiếu đồng nhất giữa thông tin khách nhận được và giả định mà hệ thống sử dụng. Cần phân biệt giữa việc trợ lý thực hiện sai quy tắc và việc trợ lý thực hiện đúng nhưng truyền đạt chưa phù hợp.
- **Giới hạn hệ thống:** Là những trường hợp yêu cầu vượt quá khả năng xử lý, phạm vi nghiệp vụ hoặc dữ liệu mà trợ lý có thể truy cập (đối tác ngoài phạm vi hỗ trợ, dữ liệu quá thời hạn lưu trữ, định dạng đầu vào chưa hỗ trợ). Ngay cả khi trợ lý phản hồi chưa rõ ràng, nguyên nhân gốc vẫn là giới hạn về năng lực hoặc dữ liệu của hệ thống.
- **Ngầm:** Là những sai sót đã xảy ra nhưng không được người dùng hoặc cơ chế giám sát phát hiện trong quá trình vận hành thông thường (có thể liên quan đến kết quả xử lý, dữ liệu, chi phí hoặc hiệu suất hoạt động). Điểm phân biệt với lỗi hệ thống là trạng thái phát hiện: sai sót chỉ được nhận diện thông qua kiểm tra mẫu, đối soát hoặc phân tích sau đó.

**Nguyên tắc chung sau rà soát:** Ưu tiên xác định **nguyên nhân gốc** thay vì hậu quả hoặc vị trí cần sửa. Nếu lỗi xuất phát từ thao tác khách hàng thì thuộc **Do người dùng**; nếu hệ thống thực hiện sai quy định và lỗi đã lộ ra thì thuộc **Hệ thống**; nếu kết quả đúng nhưng không phù hợp kỳ vọng thì thuộc **Ngữ cảnh**; nếu yêu cầu vượt quá năng lực xử lý thì thuộc **Giới hạn hệ thống**; còn những sai sót không được nhận ra cho đến khi kiểm tra sẽ thuộc **Ngầm**.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Ghi nhận sự kiện `input_validation_failed` mỗi khi khách nhập mã không hợp lệ; theo dõi tỷ lệ lỗi hằng ngày và cảnh báo nếu vượt 2% tổng số yêu cầu. | Bổ sung chức năng nhận diện sự khác biệt giữa mã đơn thương mại điện tử và mã vận đơn, hướng dẫn khách nhập đúng hoặc tự chuyển đổi khi có dữ liệu phù hợp. | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát trạng thái giao dịch giữa thông báo của trợ lý và API sổ cái theo `trace_id` mỗi giờ; ngưỡng cho phép bằng 0 trường hợp báo hoàn tiền thành công khi chưa có xác nhận từ sổ cái. | Chỉ thông báo thành công sau khi nhận xác nhận giao dịch hợp lệ; nếu API tiếp tục trả lỗi 503 sau số lần thử giới hạn thì thông báo đang xử lý và chuyển yêu cầu cho nhân viên. | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Theo dõi sự kiện `case_reopened` đối với các trường hợp khách mở lại yêu cầu vì cho rằng số tiền hoàn không chính xác dù kết quả tính toán đúng; tổng hợp hằng tuần và cảnh báo khi tỷ lệ này vượt 1% số yêu cầu hoàn thành. | Bổ sung phép tính chi tiết vào thông báo (số tiền ban đầu, tỷ lệ hoàn và kết quả cuối cùng) giúp khách hiểu rõ căn cứ hoàn phí. | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Ghi nhận sự kiện `handoff_to_staff` cùng lý do thiếu dữ liệu của hãng vận chuyển nước ngoài; theo dõi hằng ngày các yêu cầu vượt phạm vi xử lý. | Thông báo rõ giới hạn dữ liệu và chuyển cho nhân viên kèm tóm tắt thông tin đã thu thập; trong giai đoạn pilot ban đầu loại các yêu cầu quốc tế khỏi phạm vi tự động xử lý. | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra ngẫu nhiên 100 đơn mỗi tuần, đối chiếu phiên bản bảng giá được sử dụng trong từng trace với bảng giá hiện hành; cảnh báo nếu tỷ lệ đơn sai lệch đạt từ 1% trở lên. | Tự động làm mới bộ nhớ đệm mỗi khi bảng giá thay đổi, ghi nhận phiên bản bảng giá trong lịch sử xử lý và đối soát lại những đơn có khả năng sử dụng dữ liệu cũ. | Kế toán trưởng |

*Lưu ý: Các ngưỡng và tần suất giám sát trên là phương án đề xuất cho pilot, chưa phải kết quả đã đo được.*
