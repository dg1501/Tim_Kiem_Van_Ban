
# 🔎 String Search Web Application

### So sánh thuật toán KMP và Boyer–Moore

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-WebApp-green)
![License](https://img.shields.io/badge/License-Educational-orange)

---

# 📌 Giới thiệu

Ứng dụng web này được xây dựng bằng **Python Flask** nhằm minh họa và so sánh hiệu năng của hai thuật toán tìm kiếm chuỗi nổi tiếng:

* 🔹 **Knuth–Morris–Pratt (KMP)**
* 🔹 **Boyer–Moore**

Hệ thống cho phép người dùng:

✔ Nhập văn bản trực tiếp
✔ Upload file (`.txt`, `.pdf`, `.docx`)
✔ Nhập từ khóa cần tìm
✔ So sánh **kết quả và thời gian thực thi** của hai thuật toán

Mục tiêu của chương trình là **đánh giá hiệu năng thuật toán tìm kiếm trong văn bản tiếng Việt**.

---

# ⚙️ Công nghệ sử dụng

| Công nghệ   | Vai trò                  |
| ----------- | ------------------------ |
| Python      | Ngôn ngữ lập trình chính |
| Flask       | Framework xây dựng web   |
| HTML/CSS    | Giao diện người dùng     |
| PyPDF2      | Đọc nội dung file PDF    |
| python-docx | Đọc nội dung file Word   |

---

# 📂 Cấu trúc thư mục

```
project/
│
├── app.py
├── uploads/
│
├── templates/
│   └── index.html
│
└── README.md
```

| File                   | Chức năng                     |
| ---------------------- | ----------------------------- |
| `app.py`               | Chương trình chính chạy Flask |
| `uploads/`             | Lưu file người dùng upload    |
| `templates/index.html` | Giao diện web                 |
| `README.md`            | Hướng dẫn sử dụng             |

---

# 🛠 Cài đặt chương trình

## 1️⃣ Cài đặt Python

Tải Python tại:

[https://www.python.org/downloads/](https://www.python.org/downloads/)

Kiểm tra cài đặt:

```bash
python --version
```

---

## 2️⃣ Cài đặt thư viện

Mở **Command Prompt / Terminal** và chạy:

```bash
pip install flask
pip install PyPDF2
pip install python-docx
```

Hoặc cài một lần:

```bash
pip install flask PyPDF2 python-docx
```

---

# ▶️ Chạy chương trình

Di chuyển vào thư mục project:

```bash
cd project
```

Chạy ứng dụng:

```bash
python app.py
```

Sau đó mở trình duyệt và truy cập:

```
http://127.0.0.1:5000
```

---

# 💻 Hướng dẫn sử dụng

1️⃣ Nhập **văn bản cần tìm kiếm**

hoặc

2️⃣ Upload file

* `.txt`
* `.pdf`
* `.docx`

3️⃣ Nhập **từ khóa cần tìm**

4️⃣ Nhấn **Search**

Hệ thống sẽ thực hiện:

* Tìm kiếm bằng **KMP**
* Tìm kiếm bằng **Boyer–Moore**

và hiển thị kết quả so sánh.

---

# 📊 Kết quả hiển thị

Sau khi tìm kiếm, hệ thống hiển thị:

| Thuật toán  | Kết quả          | Thời gian chạy |
| ----------- | ---------------- | -------------- |
| KMP         | vị trí xuất hiện | ms             |
| Boyer-Moore | vị trí xuất hiện | ms             |

Ví dụ:

<img width="905" height="556" alt="image" src="https://github.com/user-attachments/assets/959baf55-ca63-4ff7-9512-63b21d692a60" />

---
<img width="974" height="390" alt="image" src="https://github.com/user-attachments/assets/c35f2284-d42f-4f2d-bee1-79d183c0033c" />

---

# 📁 Định dạng file hỗ trợ

Ứng dụng hỗ trợ đọc nội dung từ các định dạng:

* `.txt`
* `.pdf`
* `.docx`

Sau khi upload, hệ thống sẽ:

1️⃣ Trích xuất văn bản từ file
2️⃣ Thực hiện tìm kiếm từ khóa trong nội dung

---

# 📚 Thuật toán sử dụng

## 🔹 KMP (Knuth–Morris–Pratt)

Đặc điểm:

* Sử dụng bảng **LPS (Longest Prefix Suffix)**
* Tránh so sánh lại các ký tự đã kiểm tra

Độ phức tạp:

```
O(n + m)
```

---

## 🔹 Boyer–Moore

Đặc điểm:

* So sánh từ **phải sang trái**
* Áp dụng **Bad Character Rule**

Độ phức tạp trung bình:

```
O(n / m)
```

---


