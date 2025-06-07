import customtkinter as ctk
from SearchSpace import *

class FormFrame(ctk.CTkFrame):
    pady_values = (10, 15)
    input_placeholder_color = "#A8DFD3"
    input_bg_color = "#21222D"
    main_bg = "#181922"


    def __init__(self, master, results_frame, **kwargs):
        super().__init__(master, **kwargs)
        self.results_frame = results_frame

        #self.form_frame = ctk.CTkFrame(self, fg_color=self.main_bg)
        #self.form_frame.grid(row=0, column=0, padx=self.pady_values[0], pady=self.pady_values, sticky="nsew")
        
        # Writing form.
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.rowconfigure((0, 1), weight=1)
        self.body_font = ctk.CTkFont(family="Montserrat", size=14)
        self.title_font = ctk.CTkFont(family="Montserrat", size=21)

        self.title = ctk.CTkLabel(self, text="Algoritmo ACO",
                                  font=self.title_font, text_color=self.input_placeholder_color,
                                  justify="center")
        self.test_functions = ctk.CTkComboBox(self, values=["Sphere", "Rastrigin", "Rosenbrock", "Griewank"],
            font=self.body_font, fg_color=self.input_bg_color,
            border_color=""
        )
        self.ants = ctk.CTkEntry(self, placeholder_text="Número de hormigas",
                                      font=self.body_font, fg_color=self.input_bg_color,
                                      border_color="", placeholder_text_color=self.input_placeholder_color)
        self.k = ctk.CTkEntry(self, placeholder_text="Tamaño de archivo",
                                font=self.body_font, fg_color=self.input_bg_color,
                                    border_color="", placeholder_text_color=self.input_placeholder_color)
        self.itr = ctk.CTkEntry(self, placeholder_text="Número de iteraciones",
                                font=self.body_font, fg_color=self.input_bg_color,
                                border_color="", placeholder_text_color=self.input_placeholder_color)
        self.dim = ctk.CTkEntry(self, placeholder_text="Número de dimensiones",
                                font=self.body_font, fg_color=self.input_bg_color,
                                border_color="", placeholder_text_color=self.input_placeholder_color)
        self.xmin = ctk.CTkEntry(self, placeholder_text="Límite mímino",
                                 font=self.body_font, fg_color=self.input_bg_color,
                                 border_color="", placeholder_text_color=self.input_placeholder_color)
        self.xmax = ctk.CTkEntry(self, placeholder_text="Límite máximo",
                                 font=self.body_font, fg_color=self.input_bg_color,
                                 border_color="", placeholder_text_color=self.input_placeholder_color)
        self.p = ctk.CTkEntry(self, placeholder_text="Porcentaje p",
                               font=self.body_font, fg_color=self.input_bg_color,
                               border_color="", placeholder_text_color=self.input_placeholder_color)
        self.q = ctk.CTkEntry(self, placeholder_text="Peso q",
                               font=self.body_font, fg_color=self.input_bg_color,
                               border_color="", placeholder_text_color=self.input_placeholder_color)
        
        self.submit = ctk.CTkButton(
            self,
            text="Ejecutar algoritmo",
            font=self.body_font,
            command=self.execute_algorithm,
            fg_color="#388CB0",
            hover_color="#3840B0"
        ) # Button

        self.title.grid(
            row=0, column=0,
            padx=self.pady_values[0], pady=self.pady_values[1],
            sticky="nsew"
        )

        # Giving a structure to the form.
        self.k.grid(
            row = 1, column = 0,
            padx=self.pady_values[0], pady=self.pady_values,
            sticky="ew")
        self.test_functions.grid(
            row = 1, column = 1,
            padx=self.pady_values[0], pady=self.pady_values,
            sticky="ew")
        self.ants.grid(
            row = 2, column = 0,
            padx=self.pady_values[0], pady=self.pady_values,
            sticky="ew")
        self.itr.grid(
            row = 2, column = 1,
            padx=self.pady_values[0], pady=self.pady_values,
            sticky="ew")
        self.dim.grid(
            row = 3, column = 0,
            padx=self.pady_values[0], pady=self.pady_values,
            sticky="ew")
        self.p.grid(
            row = 3, column = 1,
            padx=self.pady_values[0], pady=self.pady_values,
            sticky="ew")
        self.xmin.grid(
            row = 4, column = 0,
            padx=self.pady_values[0], pady=self.pady_values,
            sticky="ew")
        self.xmax.grid(
            row = 4, column = 1,
            padx=self.pady_values[0], pady=self.pady_values,
            sticky="ew")
        self.q.grid(
            row = 5, column = 0,
            padx=self.pady_values[0], pady=self.pady_values,
            sticky="ew")
        self.submit.grid(
            row = 6, column = 0,
            padx=self.pady_values[0], pady=self.pady_values,
            sticky="nsew")

    def execute_algorithm(self):
        # Getting the parametters
        ants = int(self.ants.get())
        solutions_file = int(self.k.get())
        fitness_name = self.test_functions.get().lower()
        iterations = int(self.itr.get())
        dimensions = int(self.dim.get())
        p = float(self.p.get())
        q = float(self.q.get())
        xmin = int(self.xmin.get())
        xmax = int(self.xmax.get())
        # Initialiting the algorithm.
        print(fitness_name)
        aco = SearchSpace(k=solutions_file, p=p, q=q, n=ants, dimensions=dimensions, xmin=xmin, xmax=xmax, fitness_name=fitness_name)
        gbest, fitness = aco.search_global_minimum(iterations)
        rounded_gbest = [round(x, 6) for x in gbest]
        rounded_fitness = round(fitness, 6)

        self.results_frame.update_results(rounded_gbest, rounded_fitness)
        print(f"Mejor posición global: {rounded_gbest}")
        print(f"Entrenamiento de la mejor solución: {rounded_fitness}")

class ResultsFrame(ctk.CTkFrame):
    pady_values = (10, 15)
    text_color = "#f1f3f6"

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.body_font = ctk.CTkFont(family="Montserrat", size= 14)
        self.title_font = ctk.CTkFont(family="Montserrat", size=21)

        self.title = ctk.CTkLabel(self, text="Resultados de la ejecución",
                                  font=self.title_font, text_color=self.text_color,
                                  justify="center")
        self.best_position = ctk.CTkLabel(self, text="Mejor posición: Algoritmo aún sin ejecutar...",
                                          font=self.body_font, text_color=self.text_color,
                                          wraplength=500)
        self.best_fitness = ctk.CTkLabel(self, text="Mejor entrenamiento: Algoritmo aún sin ejecutar...",
                                         font=self.body_font, text_color=self.text_color)
        
        self.title.grid(
            row=0, column=0,
            padx=self.pady_values[0], pady=self.pady_values[1],
            sticky="nsew"
        )
        self.best_position.grid(row=1, column=0,
                                padx=self.pady_values[0], pady=self.pady_values,
                                sticky="ew")
        self.best_fitness.grid(row=2, column=0,
                               padx=self.pady_values[0], pady=self.pady_values,
                               sticky="ew")

    def update_results(self, gbest, fitness):
        self.best_position.configure(text=f"Mejor posición: {gbest}")
        self.best_fitness.configure(text=f"Mejor entrenamiento: {fitness}")

class UIApp(ctk.CTkToplevel):

    def __init__(self):
        super().__init__()
        # Defining the ui environment
        self.title("Primer servicio")
        self.geometry("800x500")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.results_frame = ResultsFrame(
            self,
            fg_color = "#131519"
        )
        self.results_frame.grid(row=0, column=1, padx=0, pady=0, sticky="nsew")

        self.form_frame = FormFrame(
            self,
            self.results_frame,
            fg_color="#181922"
        )
        self.form_frame.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

#app = UIApp()
#app.mainloop()
