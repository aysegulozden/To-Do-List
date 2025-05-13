import tkinter as tk
from datetime import datetime  
from styles import Style
from task_manager import TaskManager

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.task_manager = TaskManager()
        self.root.title("To Do List")
        self.root.configure(bg=Style.BACKGROUND_COLOR)
        self.root.minsize(600, 800)

        self.container = tk.Frame(root, bg=Style.BACKGROUND_COLOR)
        self.container.place(relx=0.5, rely=0.5, anchor="center", width=400, height=650)

        self.filter_var = tk.StringVar(value="all")

        self.date_time_label = tk.Label(self.container, font=("Helvetica", 12), bg=Style.BACKGROUND_COLOR)
        self.date_time_label.pack(pady=(10, 5)) 

        self.title_label = tk.Label(self.container, text="To Do", font=Style.TITLE_FONT, bg=Style.BACKGROUND_COLOR)
        self.title_label.pack(pady=(10, 10)) 

        self.create_input_frame()
        self.create_filter_frame()

        self.task_list_frame = tk.Frame(self.container, bg=Style.BACKGROUND_COLOR)
        self.task_list_frame.pack(pady=10, fill="both", expand=True)

        self.remaining_label = tk.Label(self.container, font=("Helvetica", 10, "italic"), bg=Style.BACKGROUND_COLOR)
        self.remaining_label.pack(pady=(10, 0))

        self.update_tasks()
        self.update_date_time() 

    def create_input_frame(self):
        frame = tk.Frame(self.container, bg=Style.BACKGROUND_COLOR)
        frame.pack(pady=10)

        self.task_entry = tk.Entry(frame, width=30, font=Style.FONT, bg=Style.ENTRY_COLOR, relief="flat")
        self.task_entry.grid(row=0, column=0, ipady=6, padx=(10, 5))

        add_button = tk.Button(frame, text="+", font=("Helvetica", 14, "bold"), bg=Style.BUTTON_COLOR, fg="white",
                               command=self.add_task, relief="flat", width=2, height=1)
        add_button.grid(row=0, column=1, padx=(0, 10))

    def create_filter_frame(self):
        filter_frame = tk.Frame(self.container, bg=Style.BACKGROUND_COLOR)
        filter_frame.pack(pady=(0, 10))

        tk.Radiobutton(filter_frame, text="Tüm", variable=self.filter_var, value="all", command=self.update_tasks,
                       bg=Style.BACKGROUND_COLOR).pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(filter_frame, text="Aktif", variable=self.filter_var, value="active", command=self.update_tasks,
                       bg=Style.BACKGROUND_COLOR).pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(filter_frame, text="Tamamlanan", variable=self.filter_var, value="completed", command=self.update_tasks,
                       bg=Style.BACKGROUND_COLOR).pack(side=tk.LEFT, padx=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.task_manager.add_task(task)
            self.task_entry.delete(0, tk.END)
            self.update_tasks()

    def update_tasks(self):
        for widget in self.task_list_frame.winfo_children():
            widget.destroy()

        filter_type = self.filter_var.get()
        filtered_tasks = self.task_manager.get_filtered_tasks(filter_type)

        for index, task in enumerate(filtered_tasks):
            task_frame = tk.Frame(self.task_list_frame, bg=Style.TASK_BG_COLOR, bd=1, relief="solid")
            task_frame.pack(pady=5, padx=20, fill="x")

            task_frame.grid_columnconfigure(1, weight=1)

            checkmark = "✔️" if task["is_completed"] else "⬜"
            check_label = tk.Label(
                task_frame,
                text=checkmark,
                font=("Helvetica", 14),
                bg=Style.TASK_BG_COLOR
            )
            check_label.grid(row=0, column=0, padx=5)

            global_index = self.task_manager.tasks.index(task)
            check_label.bind("<Button-1>", lambda e, i=global_index: self.toggle_task(i))

            label = tk.Label(
                task_frame,
                text=task["task"],
                font=Style.TASK_COMPLETED_FONT if task["is_completed"] else Style.TASK_FONT,
                fg="gray" if task["is_completed"] else "black",
                bg=Style.TASK_BG_COLOR,
                anchor="w",
                justify="left",
                wraplength=250
            )
            label.grid(row=0, column=1, sticky="w", padx=5)

            del_btn = tk.Button(
                task_frame,
                text="🗑️",
                font=("Helvetica", 15),
                fg="gray",
                bg=Style.TASK_BG_COLOR,
                relief="flat",
                command=lambda i=global_index: self.delete_task(i)
            )
            del_btn.grid(row=0, column=2)

        remaining = self.task_manager.get_remaining_count()
        self.remaining_label.config(text=f"Your Tasks: {remaining}")

    def toggle_task(self, index):
        self.task_manager.toggle_task(index)
        self.update_tasks()

    def delete_task(self, index):
        self.task_manager.delete_task(index)
        self.update_tasks()

    def update_date_time(self):
        current_time = datetime.now()  
        formatted_time = current_time.strftime("%d-%m-%Y %H:%M")  
        self.date_time_label.config(text=f"{formatted_time}") 
        self.root.after(1000, self.update_date_time)
