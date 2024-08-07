import tkinter as tk
from tkinter import messagebox

# ฟังก์ชันคำนวณภาษี
def calculate_tax():
    try:
        salary = float(salary_entry.get())
        bonus = float(bonus_entry.get())
        
        total_income = salary + bonus
        
        if total_income <= 150000:
            tax = 0
        elif total_income <= 300000:
            tax = (total_income - 150000) * 0.05
        elif total_income <= 500000:
            tax = (total_income - 300000) * 0.10 + 7500
        elif total_income <= 750000:
            tax = (total_income - 500000) * 0.15 + 27500
        elif total_income <= 1000000:
            tax = (total_income - 750000) * 0.20 + 65000
        elif total_income <= 2000000:
            tax = (total_income - 1000000) * 0.25 + 115000
        elif total_income <= 5000000:
            tax = (total_income - 2000000) * 0.30 + 365000
        else:
            tax = (total_income - 5000000) * 0.35 + 1265000
        
        tax_label.config(text=f"ภาษีที่ต้องจ่าย: {tax:.2f} บาท")
    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกข้อมูลเป็นตัวเลข")

# ฟังก์ชันลบข้อมูล
def clear_entries():
    salary_entry.delete(0, tk.END)
    bonus_entry.delete(0, tk.END)
    tax_label.config(text="ภาษีที่ต้องจ่าย: ")

# ฟังก์ชันออกจากโปรแกรม
def exit_program():
    root.quit()

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("โปรแกรมคำนวณภาษี")
root.geometry('690x390')

# ตั้งค่าให้คอลัมน์และแถวขยายตัวตามขนาดหน้าต่าง
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

# สร้างและจัดวาง Label สำหรับชื่อโปรแกรม
program_label = tk.Label(root, text="โปรแกรมคำนวณภาษี", font=("Helvetica", 15))
program_label.grid(row=0, column=1, columnspan=2, pady=10)

# สร้างและจัดวาง Label และ Entry สำหรับเงินเดือน
tk.Label(root, text="เงินเดือน:").grid(row=1, column=1, padx=10, pady=5, sticky='e')
salary_entry = tk.Entry(root)
salary_entry.grid(row=1, column=2, padx=10, pady=5, sticky='w')

# สร้างและจัดวาง Label และ Entry สำหรับโบนัส
tk.Label(root, text="โบนัส:").grid(row=2, column=1, padx=10, pady=5, sticky='e')
bonus_entry = tk.Entry(root)
bonus_entry.grid(row=2, column=2, padx=10, pady=5, sticky='w')

# สร้างและจัดวาง Label สำหรับแสดงผลภาษีที่ต้องจ่าย
tax_label = tk.Label(root, text="ภาษีที่ต้องจ่าย: ")
tax_label.grid(row=3, column=1, columnspan=2, padx=10, pady=10)

# สร้างและจัดวางปุ่มคำนวณและปุ่มลบให้อยู่ข้างกัน
calculate_button = tk.Button(root, text="คำนวณ", command=calculate_tax)
calculate_button.grid(row=4, column=1, padx=10, pady=10, sticky='e')

clear_button = tk.Button(root, text="ลบข้อมูล", command=clear_entries)
clear_button.grid(row=4, column=2, padx=30, pady=10, sticky='w')

# สร้างและจัดวางปุ่มออก
exit_button = tk.Button(root, text="ออกจากโปรแกรม", command=exit_program)
exit_button.place(relx=1.0, rely=0.0, anchor='ne' , x=-100, y=50)

# เริ่มโปรแกรม
root.mainloop()
