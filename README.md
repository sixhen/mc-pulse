<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,12,24,35&height=210&section=header&text=mc-pulse&fontSize=64&fontAlignY=38&desc=Real-Time%20Minecraft%20Server%20Telemetry%20%26%20Heartbeat&descAlignY=58&descSize=17&fontColor=ffffff" width="100%"/>

<p align="center">
  <img src="https://img.shields.io/badge/LANGUAGE-PYTHON_3-0f172a?style=for-the-badge&logo=python&logoColor=38bdf8" alt="Python 3" />
  <img src="https://img.shields.io/badge/METRICS-TPS_%7C_RAM_%7C_PING-022c22?style=for-the-badge&logoColor=6ee7b7" alt="Metrics" />
  <img src="https://img.shields.io/badge/LICENSE-MIT-1e1b4b?style=for-the-badge&logoColor=a5b4fc" alt="MIT License" />
  <img src="https://img.shields.io/badge/AI--CRAFTED-100%25-8A2BE2?style=for-the-badge" alt="AI Crafted" />
</p>

</div>

---

## ⚡ Tổng quan (Overview)

**mc-pulse** là công cụ telemetry siêu nhẹ viết bằng Python, chuyên trách theo dõi nhịp tim (heartbeat), lượng người chơi, biến động TPS và mức tiêu thụ RAM của các máy chủ Minecraft (Java / Bedrock) theo thời gian thực.

> 🏛️ **Tiêu chuẩn thiết kế:** Tối giản trong tư duy, tinh tế trong cấu trúc, chuẩn xác tuyệt đối trong thực thi. 100% kiến tạo & đồng bộ cùng AI.

---

## 🚀 Tính năng chính (Key Capabilities)

- **📈 Giám sát thời gian thực:** Quét thông số TPS (Ticks Per Second) và độ trễ ping liên tục.
- **🔔 Cảnh báo tức thì:** Tích hợp webhook phát thông báo qua Discord/Telegram khi máy chủ có dấu hiệu lag hoặc tụt TPS.
- **📊 Báo cáo chỉ số RAM/CPU:** Đọc trực tiếp mức tiêu hao tài nguyên từ tiến trình JVM.
- **⚡ Tiêu thụ tài nguyên tối thiểu:** Thiết kế asynchronous non-blocking, chiếm dưới 0.1% CPU của host.

---

## 💻 Cài đặt & Khởi chạy (Usage)

```bash
git clone https://github.com/sixhen/mc-pulse.git
cd mc-pulse
pip install -r requirements.txt
python pulse.py --host 127.0.0.1 --port 25565
```

---

## 📄 Bản quyền (License)

Phát hành theo giấy phép **MIT License**. Tự do sử dụng và tùy biến.
