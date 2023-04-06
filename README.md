# Hướng dẫn cài đặt

## Bước 1: Chuẩn bị

Cài đặt `python3`, `git`, `python3-venv`

```bash
sudo apt install git python3 python3-venv
```

## Bước 2: Clone code về

Tải code từ trên github về

```bash
git clone https://github.com/patpro28/flask-D2 ~/project
```

## Bước 3: Cài đặt môi trường python cho code

```bash
cd ~/project
python3 -m venv venv
```

## Bước 4: Cài đặt các gói cần thiết cho code.

```bash
source venv/bin/activate
pip3 install -r requirements.txt
```

## Sử dụng

Sau khi cài đặt xong, chúng ta có thể chạy dự án, đầu tiên cần vào thư mục `project` để kích hoạt môi trường, sau cho chạy.

```bash
cd ~/project
source venv/bin/activate
flask run
```
