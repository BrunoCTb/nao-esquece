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

        self.bill_btn = ctk.CTkButton(self.sidebar, text="Adicionar conta", command=self.show_add_bill_page)
        self.bill_btn.pack(fill="x", padx=20, pady=5)

        self.bill_btn = ctk.CTkButton(self.sidebar, text="Adicionar grupo", command=self.show_add_group_page)
        self.bill_btn.pack(fill="x", padx=20, pady=5)

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

    def show_add_bill_page(self):
        self.clear_main_frame()

        title = ctk.CTkLabel(
            self.main_frame,
            text="Adicionar Nova Conta",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=15)

        form = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        form.pack(pady=10, padx=20, fill="x")

        self.bill_title = ctk.CTkEntry(form, placeholder_text="Título da conta")
        self.bill_title.pack(pady=5, fill="x")

        self.bill_value = ctk.CTkEntry(form, placeholder_text="Valor (ex: 120.90)")
        self.bill_value.pack(pady=5, fill="x")

        self.bill_type = ctk.CTkOptionMenu(form, values=["Gasto", "Ganho"])
        self.bill_type.pack(pady=5, fill="x")

        self.bill_due_date = ctk.CTkEntry(form, placeholder_text="Data de vencimento (dd/mm/aaaa)")
        self.bill_due_date.pack(pady=5, fill="x")

        self.bill_group = ctk.CTkOptionMenu(form, values=["Sem grupo"]) # get nos grupos do sqlite
        self.bill_group.pack(pady=5, fill="x")

        self.bill_card = ctk.CTkOptionMenu(form, values=["Nenhum cartão"]) # get nos cartoes do sqlite
        self.bill_card.pack(pady=5, fill="x")

        self.bill_description = ctk.CTkEntry(form, height=40, placeholder_text="descrição curta")
        self.bill_description.pack(pady=5, fill="x")

        radio_opt = ctk.IntVar();
        radio_opt.set(0)

        def set_radio_bill(opt):
            if (opt == 1):
                self.bill_total_installments.pack(pady=5, fill="x")
                self.bill_paid_installments.pack(pady=5, fill="x")
                return
            
            self.bill_total_installments.pack_forget()
            self.bill_paid_installments.pack_forget()
                
        ctk.CTkLabel(form, text='Conta parcelada:').pack()

        radio1 = ctk.CTkRadioButton(form, text="Não", variable=radio_opt, value=0, command=lambda: set_radio_bill(0))
        radio2 = ctk.CTkRadioButton(form, text="Sim", variable=radio_opt, value=1, command=lambda: set_radio_bill(1))
        radio1.pack()
        radio2.pack()

        self.bill_total_installments = ctk.CTkEntry(form, placeholder_text="Total de parcelas (ex: 12)")
        self.bill_paid_installments = ctk.CTkEntry(form, placeholder_text="Parcelas pagas (ex: 3)")
        
        submit_btn = ctk.CTkButton(
            self.main_frame,
            text="Salvar Conta",             
            fg_color="#2ecc71",
            hover_color="#27ae60"
        )
        submit_btn.pack(pady=20)

    def show_add_group_page(self): 
        self.clear_main_frame()

        title = ctk.CTkLabel(
            self.main_frame,
            text="Adicionar novo grupo",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=15)

        form = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        form.pack(pady=10, padx=20, fill="x")

        self.group_title = ctk.CTkEntry(form, placeholder_text="Nome do grupo")
        self.group_title.pack(pady=5, fill="x")

        self.group_description = ctk.CTkEntry(form, height=40, placeholder_text="descrição curta")
        self.group_description.pack(pady=5, fill="x")        
        
        submit_btn = ctk.CTkButton(
            self.main_frame,
            text="Salvar grupo",             
            fg_color="#2ecc71",
            hover_color="#27ae60"
        )
        submit_btn.pack(pady=20)

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
