import customtkinter as ctk

### App theme
# ctk.set_appearance_mode("dark")  # pode ser "light" ou "system"
# ctk.set_default_color_theme("blue")

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Nao esquece")
        self.geometry("900x600")

        ### menu config
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nswe")

        self.logo = ctk.CTkLabel(self.sidebar, text="💰 Meu Financeiro", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo.pack(pady=20)

        self.dashboard_btn = ctk.CTkButton(self.sidebar, text="Início", command=self.show_main_area)
        self.dashboard_btn.pack(fill="x", padx=20, pady=5)

        self.dashboard_btn = ctk.CTkButton(self.sidebar, text="📊 Dashboard", command=self.show_dashboard)
        self.dashboard_btn.pack(fill="x", padx=20, pady=5)

        self.tasks_btn = ctk.CTkButton(self.sidebar, text="🗓️ Tarefas", command=self.show_tasks)
        self.tasks_btn.pack(fill="x", padx=20, pady=5)

        self.cards_btn = ctk.CTkButton(self.sidebar, text="💳 Cartões", command=self.show_cards)
        self.cards_btn.pack(fill="x", padx=20, pady=5)

        self.calc_btn = ctk.CTkButton(self.sidebar, text="🧮 Calculadora", command=self.show_calc)
        self.calc_btn.pack(fill="x", padx=20, pady=5)

        self.exit_btn = ctk.CTkButton(self.sidebar, text="Sair", hover_color="#b30000", command=self.quit)
        self.exit_btn.pack(side="bottom", fill="x", padx=20, pady=20)

        self.main_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nswe")
        self.main_label = ctk.CTkLabel(self.main_frame, text="Bem-vindo ao painel financeiro 👋", font=ctk.CTkFont(size=18))
        self.main_label.pack(pady=40)

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_main_area(self):
        self.clear_main_frame()

        main_title = ctk.CTkLabel(
            self.main_frame,
            text="Resumo do mês {atual} do ano {atual}",
            anchor="w",
            justify="left",
            wraplength=650,
            font=ctk.CTkFont(size=30, weight="bold")
        )
        main_title.pack(pady=(10, 20), anchor="w")

        main_value_div = ctk.CTkFrame(self.main_frame, fg_color="#fff", corner_radius=10)
        main_value_div.pack(fill="x", padx=20, pady=10)

        tot_value = ctk.CTkFrame(main_value_div, fg_color="transparent")
        tot_value.pack(fill="x", pady=5, padx=15)
        ctk.CTkLabel(tot_value, text="Gastos previstos:", font=ctk.CTkFont(size=14)).pack(side="left")
        ctk.CTkLabel(tot_value, text="R$ 1.200,00", font=ctk.CTkFont(size=14, weight="bold")).pack(side="right")

        payed_value = ctk.CTkFrame(main_value_div, fg_color="transparent")
        payed_value.pack(fill="x", pady=5, padx=15)
        ctk.CTkLabel(payed_value, text="Total pago:", font=ctk.CTkFont(size=14)).pack(side="left")
        ctk.CTkLabel(payed_value, text="R$ 980,00", font=ctk.CTkFont(size=14, weight="bold")).pack(side="right")

        waiting_value = ctk.CTkFrame(main_value_div, fg_color="transparent")
        waiting_value.pack(fill="x", pady=5, padx=15)
        ctk.CTkLabel(waiting_value, text="Pendente:", font=ctk.CTkFont(size=14)).pack(side="left")
        ctk.CTkLabel(waiting_value, text="R$ 220,00", font=ctk.CTkFont(size=14, weight="bold")).pack(side="right")


    ### SEC MENUs
    def show_dashboard(self):
        self.clear_main_frame()
        ctk.CTkLabel(self.main_frame, text="Dashboard", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        ctk.CTkLabel(self.main_frame, text="Aqui virão os resumos financeiros.").pack(pady=5)

    def show_tasks(self):
        self.clear_main_frame()
        ctk.CTkLabel(self.main_frame, text="Tarefas", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        ctk.CTkLabel(self.main_frame, text="Aqui virá a lista de tarefas mensais.").pack(pady=5)

    def show_cards(self):
        self.clear_main_frame()
        ctk.CTkLabel(self.main_frame, text="Cartões", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        ctk.CTkLabel(self.main_frame, text="Controle de cartões de crédito.").pack(pady=5)

    def show_calc(self):
        self.clear_main_frame()
        ctk.CTkLabel(self.main_frame, text="Calculadora", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        ctk.CTkLabel(self.main_frame, text="Ferramenta para cálculos rápidos.").pack(pady=5)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
