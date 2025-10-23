import tkinter as tk
from tkinter import messagebox, filedialog
import os

# === Класс Студента ===
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = list(map(int, grades))

    def has_only_fives(self):
        return all(g == 5 for g in self.grades)

    def has_threes(self):
        return 3 in self.grades

    def has_twos(self):
        return self.grades.count(2) > 0

    def too_many_twos(self):
        return self.grades.count(2) > 1

    def __str__(self):
        return f"{self.name} {' '.join(map(str, self.grades))}"


# === Класс для работы с группой ===
class StudentGroup:
    def __init__(self, filename):
        self.filename = filename
        self.students = []
        self.load()

    def load(self):
        self.students.clear()
        if not os.path.exists(self.filename):
            open(self.filename, "w").close()
            return
        with open(self.filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 6:
                    name = " ".join(parts[:2])
                    grades = parts[2:]
                    self.students.append(Student(name, grades))

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            for s in self.students:
                f.write(str(s) + "\n")

    def add_student(self, name, grades):
        if len(grades) != 5 or not all(g.isdigit() and 2 <= int(g) <= 5 for g in grades):
            raise ValueError("Введите 5 оценок от 2 до 5")
        self.students.append(Student(name, grades))
        self.save()

    def remove_with_many_twos(self):
        self.students = [s for s in self.students if not s.too_many_twos()]
        self.save()

    def get_all(self):
        return self.students

    def get_five_students(self):
        return [s for s in self.students if s.has_only_fives()]

    def get_with_threes(self):
        return [s for s in self.students if s.has_threes()]

    def get_with_twos(self):
        return [s for s in self.students if s.has_twos()]


# === GUI ===
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Лабораторная №7 — Студенты и оценки")
        self.group = StudentGroup("students.txt")

        # Меню
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Обновить", command=self.refresh)
        filemenu.add_command(label="Добавить студента", command=self.add_student_window)
        filemenu.add_separator()
        filemenu.add_command(label="Выход", command=root.quit)
        menubar.add_cascade(label="Файл", menu=filemenu)

        viewmenu = tk.Menu(menubar, tearoff=0)
        viewmenu.add_command(label="Показать всех", command=self.show_all)
        viewmenu.add_command(label="Только отличники (все 5)", command=self.show_five_students)
        viewmenu.add_command(label="Есть тройки", command=self.show_with_threes)
        viewmenu.add_command(label="Есть двойки", command=self.show_with_twos)
        viewmenu.add_command(label="Удалить студентов с 2 двойками", command=self.remove_many_twos)
        menubar.add_cascade(label="Выборка", menu=viewmenu)

        root.config(menu=menubar)

        # Поле вывода
        self.text = tk.Text(root, width=80, height=20, wrap="word")
        self.text.pack(padx=10, pady=10)
        self.refresh()

    def refresh(self):
        self.group.load()
        self.show_all()

    def show_list(self, students, title):
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, title + "\n" + "-" * 60 + "\n")
        if not students:
            self.text.insert(tk.END, "Нет данных.\n")
        for s in students:
            self.text.insert(tk.END, str(s) + "\n")

    def show_all(self):
        self.show_list(self.group.get_all(), "Полный список студентов")

    def show_five_students(self):
        self.show_list(self.group.get_five_students(), "Студенты, сдавшие всё на 5")

    def show_with_threes(self):
        self.show_list(self.group.get_with_threes(), "Студенты, имеющие тройки")

    def show_with_twos(self):
        self.show_list(self.group.get_with_twos(), "Студенты, имеющие двойки")

    def remove_many_twos(self):
        self.group.remove_with_many_twos()
        messagebox.showinfo("Готово", "Студенты с более чем одной двойкой удалены.")
        self.refresh()

    def add_student_window(self):
        win = tk.Toplevel(self.root)
        win.title("Добавить студента")

        tk.Label(win, text="Фамилия и инициалы:").grid(row=0, column=0, padx=5, pady=5)
        name_entry = tk.Entry(win, width=30)
        name_entry.grid(row=0, column=1)

        tk.Label(win, text="5 оценок через пробел:").grid(row=1, column=0, padx=5, pady=5)
        grades_entry = tk.Entry(win, width=30)
        grades_entry.grid(row=1, column=1)

        def save_student():
            try:
                name = name_entry.get().strip()
                grades = grades_entry.get().split()
                if not name:
                    raise ValueError("Введите имя студента")
                self.group.add_student(name, grades)
                messagebox.showinfo("Успех", "Студент добавлен.")
                win.destroy()
                self.refresh()
            except Exception as e:
                messagebox.showerror("Ошибка", str(e))

        tk.Button(win, text="Сохранить", command=save_student).grid(row=2, column=0, columnspan=2, pady=10)

# === Запуск программы ===
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
