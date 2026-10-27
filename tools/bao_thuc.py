"""Báo thức lặp: cửa sổ đếm ngược, hết giờ thì kêu và bật cửa sổ lên trên cùng, rồi tự đếm lại.

Chạy:  python tools/bao_thuc.py            (mặc định 20 phút)
       python tools/bao_thuc.py 15         (15 phút)
Cần Python có tkinter (bản cài từ python.org trên Windows đã kèm sẵn).
"""
import sys
import time
import tkinter as tk

try:
    import winsound
except ImportError:  # không phải Windows
    winsound = None


def beep(root):
    if winsound:
        for freq in (880, 880, 1175):
            winsound.Beep(freq, 220)
    else:
        for _ in range(3):
            root.bell()
            root.update()
            time.sleep(0.25)


class App:
    def __init__(self, root, minutes):
        self.root = root
        self.running = False
        self.ringing = False
        self.rounds = 0
        self.end = 0.0
        self.left = 0.0

        root.title("Báo thức lặp")
        root.geometry("320x260")
        root.resizable(False, False)
        root.attributes("-topmost", True)

        self.time_var = tk.StringVar()
        self.info_var = tk.StringVar(value="Chưa bắt đầu")
        self.mins_var = tk.StringVar(value=str(minutes))

        tk.Label(root, textvariable=self.time_var, font=("Consolas", 54, "bold")).pack(pady=(18, 0))
        tk.Label(root, textvariable=self.info_var, font=("Segoe UI", 11)).pack()

        row = tk.Frame(root)
        row.pack(pady=14)
        self.go_btn = tk.Button(row, text="Bắt đầu", width=10, height=2, command=self.toggle)
        self.go_btn.grid(row=0, column=0, padx=4)
        tk.Button(row, text="Đặt lại", width=10, height=2, command=self.reset).grid(row=0, column=1, padx=4)

        cfg = tk.Frame(root)
        cfg.pack()
        tk.Label(cfg, text="Mỗi").pack(side="left")
        tk.Spinbox(cfg, from_=1, to=180, width=4, textvariable=self.mins_var, command=self.on_mins).pack(side="left", padx=4)
        tk.Label(cfg, text="phút").pack(side="left")

        self.left = self.total()
        self.paint()
        root.after(250, self.loop)

    def total(self):
        try:
            return max(1, min(180, int(self.mins_var.get()))) * 60.0
        except ValueError:
            return 20 * 60.0

    def paint(self):
        s = max(0, int(self.left + 0.999))
        self.time_var.set(f"{s // 60:02d}:{s % 60:02d}")
        self.root.title(f"{self.time_var.get()} · Báo thức lặp" if self.running else "Báo thức lặp")

    def on_mins(self):
        if not self.running:
            self.left = self.total()
            self.paint()

    def toggle(self):
        if self.ringing:
            self.ringing = False
            self.info_var.set(f"Vòng {self.rounds + 1} đang chạy")
            self.go_btn.config(text="Tạm dừng")
            return
        if not self.running:
            self.running = True
            self.end = time.time() + self.left
            self.go_btn.config(text="Tạm dừng")
            self.info_var.set(f"Vòng {self.rounds + 1} đang chạy")
        else:
            self.running = False
            self.left = self.end - time.time()
            self.go_btn.config(text="Tiếp tục")
            self.info_var.set("Đang tạm dừng")
        self.paint()

    def reset(self):
        self.running = False
        self.ringing = False
        self.rounds = 0
        self.left = self.total()
        self.go_btn.config(text="Bắt đầu")
        self.info_var.set("Chưa bắt đầu")
        self.paint()

    def ring(self):
        self.rounds += 1
        self.ringing = True
        self.info_var.set(f"HẾT GIỜ! Đã qua {self.rounds} vòng")
        self.go_btn.config(text="Tắt chuông")
        self.root.deiconify()
        self.root.lift()
        self.root.attributes("-topmost", True)
        self.root.focus_force()
        self.end = time.time() + self.total()

    def loop(self):
        if self.running:
            self.left = self.end - time.time()
            if self.left <= 0:
                self.ring()
                self.left = self.total()
            self.paint()
        if self.ringing:
            beep(self.root)
        self.root.after(250 if not self.ringing else 1500, self.loop)


def main():
    minutes = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    root = tk.Tk()
    App(root, minutes)
    root.mainloop()


if __name__ == "__main__":
    main()
