

---

## 🔍 Real-Time Background Blur with YOLOv8 and Virtual Camera

This project uses YOLOv8 segmentation to apply real-time background effects (like blur, black background, or custom images) on webcam feed and streams the result via a **virtual camera** (using `pyvirtualcam`). Perfect for Google Meet, Zoom, OBS, etc.

---

### 📁 Project Structure

```
├── engine.py                # Contains YOLOv8 segmentation logic and background processing
├── main.py                  # Entry point to start the virtual camera stream
├── stream_utils.py          # Handles streaming logic and virtual camera integration
├── test.py                  # (Optional) For testing individual components
├── yolov8s-seg.pt           # YOLOv8 segmentation model (downloaded)
├── requirements.txt         # List of required Python packages
├── instruction.txt          # Project usage instructions (manual)
├── static/
│   ├── index.html           # (Optional) Frontend or placeholder
│   ├── logo.jpg             # (Optional) Logo for GUI/website
│   ├── background.jpg       # Custom background image
│   └── wallpaperflare...    # Default background image for "default" mode
```

---

### ⚙️ Features

- ✅ Real-time person segmentation using **YOLOv8-seg**
- ✅ Background Blur
- ✅ Black Background
- ✅ Custom Image Background
- ✅ Virtual Camera support (can be used in Google Meet, OBS, Zoom, etc.)

---

### 🚀 Getting Started

#### 1. Clone the Repository

```bash
git clone https://github.com/Moulik-23/Virtual-Video-Boardcaster.git
cd Virtual-Video-Boardcaster
```

#### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Make sure you have Python ≥ 3.8 and [YOLOv8 dependencies](https://docs.ultralytics.com/) set up.

#### 3. Download YOLOv8 Segmentation Model

Place `yolov8s-seg.pt` in the root directory. You can download it from [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics).

#### 4. Run the App

```bash
python main.py
```

> You can change background mode and other settings inside `main.py`.

---

### 🧪 Testing (Optional)

```bash
python test.py
```

---

### 💡 Usage Tips

- Make sure to **select the virtual camera** in Google Meet, Zoom, or any video call app.
- If the background is not applied, check the segmentation results or your camera access.
- You may need to run Python as **Administrator** for virtual camera access on some systems.

---

### 🔧 Requirements

- Python 3.11
- OpenCV
- torch
- ultralytics
- pyvirtualcam
- numpy

> All dependencies are in `requirements.txt`

---

### 🧠 Credits

- YOLOv8 by [Ultralytics](https://github.com/ultralytics)
- Virtual camera via [`pyvirtualcam`](https://github.com/letmaik/pyvirtualcam)

---

