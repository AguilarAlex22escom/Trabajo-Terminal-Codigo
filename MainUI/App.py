import customtkinter as ctk
import ACO.UI as aco_ui
import PSO.UI as pso_ui

class App(ctk.CTk):
    text_color = "#A8DFD3"
    btn_color = "#388CB0"
    btn_color_hover = "#3840B0"
    padding = 10

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Primer servicio")
        self.geometry("500x500")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        self.title_font = ctk.CTkFont(
            family="Montserrat",
            size=24)
        self.main_title = ctk.CTkLabel(
            self, text="Primer incremento",
            font=self.title_font, text_color=self.text_color)
        self.main_title.grid(
            row=0, column=0,
            padx=self.padding, pady=self.padding, sticky="nsew")

        self.subtitle_font = ctk.CTkFont(
            family="Montserrat",
            size=18)
        self.subtitle = ctk.CTkLabel(
            self, text="Seleccione un algoritmo",
            font=self.subtitle, text_color=self.text_color)
        self.subtitle.grid(
            row=1, column=0,
            padx=self.padding, pady=self.padding, sticky="nsew"
        )

        self.btns_font = ctk.CTkFont(family="Montserrat", size=14)

        self.pso_btn = ctk.CTkButton(
            self, text="PSO",
            command=self.execute_pso_algorithm,
            font=self.btns_font,
            bg_color=self.btn_color, hover_color=self.btn_color_hover
            )
        self.pso.btn.grid(
            row=2, column=0,
            padx=self.padding, pady=self.padding, sticky="nsew")
        
        self.aco_btn = ctk.CTkButton(
            self, text="ACO",
            command=self.execute_aco_algorithm,
            font=self.btns_font,
            bg_color=self.btn_color, hover_color=self.btn_color_hover
            )
        self.aco_btn.grid(
            row=3, column=0,
            padx=self.padding, pady=self.padding, sticky="nsew"
        )

    def execute_pso_algorithm(self):
        pso_ui.UIApp()
    
    def execute_aco_algorithm(self):
        aco_ui.UIApp()

main_app = App()
main_app.mainloop()