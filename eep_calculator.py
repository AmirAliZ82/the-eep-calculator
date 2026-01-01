from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import numpy as np

class EEPApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        # Input fields
        self.instruction = Label(text="Enter Process Type (e.g., F_P, P_F, F_A, etc.):")
        self.layout.add_widget(self.instruction)
        
        self.process_input = TextInput(hint_text="Type process here", multiline=False)
        self.layout.add_widget(self.process_input)
        
        self.param_label = Label(text="Enter Parameters (comma-separated):")
        self.layout.add_widget(self.param_label)
        
        self.param_input = TextInput(hint_text="e.g., 0.05, 10, 1000", multiline=False)
        self.layout.add_widget(self.param_input)
        
        # Result
        self.result_label = Label(text="Results will appear here")
        self.layout.add_widget(self.result_label)
        
        # Buttons
        calculate_button = Button(text="Calculate", on_press=self.calculate)
        self.layout.add_widget(calculate_button)
        
        return self.layout

    def calculate(self, instance):
        # Get inputs
        tp = self.process_input.text.strip()
        params = self.param_input.text.strip()
        
        # Parse parameters
        try:
            param_list = [float(x) for x in params.split(",")]
        except ValueError:
            self.result_label.text = "Error: Invalid parameters"
            return
        
        # Process calculations
        try:
            if tp == "F_P":
                result = self.F_P(*param_list)
            elif tp == "P_F":
                result = self.P_F(*param_list)
            elif tp == "F_A":
                result = self.F_A(*param_list)
            elif tp == "A_F":
                result = self.A_F(*param_list)
            elif tp == "P_A":
                result = self.P_A(*param_list)
            elif tp == "A_P":
                result = self.A_P(*param_list)
            elif tp == "P_G":
                result = self.P_G(*param_list)
            elif tp == "A_G":
                result = self.A_G(*param_list)
            elif tp == "F_G":
                result = self.F_G(*param_list)
            elif tp == "ie":
                result = self.ie(*param_list)
            elif tp == "rg":
                result = self.rg(*param_list)
            elif tp == "i_F_P":
                result = self.i_F_P(*param_list)
            elif tp == "i_F_A":
                result = self.i_F_A(*param_list)
            elif tp == "i_P_A":
                result = self.i_P_A(*param_list)
            elif tp == "n_F_P":
                result = self.n_F_P(*param_list)
            elif tp == "n_F_A":
                result = self.n_F_A(*param_list)
            elif tp == "n_P_A":
                result = self.n_P_A(*param_list)
            elif tp == "P_A_g":
                result = self.P_A_g(*param_list)
            elif tp == "F_A_g":
                result = self.F_A_g(*param_list)
            else:
                result = "Unsupported Process"
        except Exception as e:
            result = f"Error: {str(e)}"
        
        self.result_label.text = f"Result: {result}"

    # Function Definitions
    def F_P(self, i, n, P):
        return P * (1 + i) ** n

    def P_F(self, i, n, F):
        return F / (1 + i) ** n

    def F_A(self, i, n, A):
        return A * ((1 + i) ** n - 1) / i

    def A_F(self, i, n, F):
        return F * i / ((1 + i) ** n - 1)

    def P_A(self, i, n, A):
        return A * ((1 + i) ** n - 1) / (i * (1 + i) ** n)

    def A_P(self, i, n, P):
        return P * (i * (1 + i) ** n) / ((1 + i) ** n - 1)

    def P_G(self, i, n, G):
        return (G / i) * (((1 + i) ** n - 1) / (i * (1 + i) ** n) - n / (1 + i) ** n)

    def A_G(self, i, n, G):
        return G * (1 / i - n / ((1 + i) ** n - 1))

    def F_G(self, i, n, G):
        return G * (1 / i * ((1 + i) ** n - 1) / i - n)

    def ie(self, i, n):
        return (1 + i / n) ** n - 1

    def rg(self, n, r1, r2, r3, r4, r5):
        return ((1 + r1) * (1 + r2) * (1 + r3) * (1 + r4) * (1 + r5)) ** (1 / n) - 1

    def i_F_P(self, n, F, P):
        return (F / P) ** (1 / n) - 1

    def i_F_A(self, n, F, A, ac):
        return "Not Implemented in GUI"

    def i_P_A(self, n, P, A, ac):
        return "Not Implemented in GUI"

    def n_F_P(self, i, F, P):
        return np.log(F / P) / np.log(1 + i)

    def n_F_A(self, i, F, A):
        return np.log(((F * i) / A) + 1) / np.log(1 + i)

    def n_P_A(self, i, P, A):
        return -1 * np.log(1 - (P * i / A)) / np.log(1 + i)

    def P_A_g(self, n, i, g, A):
        if i != g:
            return A * (1 - ((1 + g) ** n) * ((1 + i) ** -n)) / (i - g)
        else:
            return n * A * ((1 + i) ** -1)

    def F_A_g(self, n, i, g, A):
        if i != g:
            return A * (((1 + i) ** n - (1 + g) ** n) / (i - g))
        else:
            return n * A * ((1 + i) ** n - 1)

if __name__ == "__main__":
    EEPApp().run()