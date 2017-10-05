# LinearRegression
Mô tả cách làm
1. Tìm hiểu về dữ liệu training:
Sau khi tìm hiểu một số cách chuẩn hóa dữ liệu với mong muốn đưa các giá trị của các trường dữ liệu khác nhau về cùng một miền giá trị, em vẫn không tìm được cách phù hợp. Do vậy, dữ liệu đầu vào không được chuẩn hóa, mà chỉ được đưa về cùng kiểu dữ liệu là float để tiện hơn cho phần tính toán mà không có ảnh hưởng gì đến mô hình học.
2. Xác định ngôn ngữ phù hợp sử dụng: python, sử dụng các thư viện hỗ trợ như csv, numpy, pandas, pickle,...
3. Cài đặt môi trường lập trình phát triển 
4. Tìm hiểu về thuật toán Linear Regression
5. Xây dựng class LinearRegression, class này sẽ cung cấp các method hỗ trợ quá trình học của class. Ví dụ: 
- load_raw_data(path): cho phép người dùng load file dữ liệu training, hoặc file dữ liệu test, dữ liệu cần predict và generate thành một numpy array
- split_raw_data(data, ratio): phân dữ liệu thô đầu vào thành hai phần là train_data và test_data dựa vào tỉ lệ mà người dùng mong muốn
- fit(data_set, target_set): với dữ liệu đầu vào gồm có các feature vector mỗi feature vector tương ứng là một điểm dữ liệu, và target_set là vector cột chứa những giá trị thực tương ứng với từng điểm dữ liệu.
Từ những dữ liệu đầu vào như thế, chúng ta sẽ xây dựng model học cho mô hình học máy Linear Regression
data_set khi đưa vào mô hình học sẽ được mở rộng nhờ hàm (bar_data), sau đó ta tìm tham số w (vector cột) sao cho hàm tối ưu mất mát đạt giá trị nhỏ nhất.
- save_model(path): cho phép người dùng lưu lại model học vừa được xây dựng (hay chính là lưu lại tham số w)
- load_model(path): load model đã được lưu lại lên để phục vụ công việc predict những điểm dữ liệu khác
- predict(predict_data): để phục vụ việc predict một hoặc nhiều điểm dữ liệu. Dữ liệu thô người dùng muốn predict, sau khi được mở rộng thành ma trận dữ liệu mở rộng thông qua hàm bar_data(predict_data), sẽ được predict giá trị đầu ra phụ thuộc vào tham số học w mà ta đã tính toán ở phía trên.
6. Sau khi xây dựng xong mô hình học Linear Regression, em đã test với bộ dữ liệu thầy phân, và ghi kết quả predict ra file "20141869.csv"
Những thiếu sót trong quá trình xây dựng mô hình học:
- Chưa xây dựng hàm tính điểm cho mô hình học
- Dữ liệu train còn nhỏ, kết quả predict độ chính xác thấp
