"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx

class FormInputState(rx.State):
    form_data: dict = {}
    

    def handle_submit(self, form_data: dict):        
        def numeroALetra(form_data):

            num = form_data["input"]

            '''
            Convertimos un numero entero de hasta tres dígitos a su representación en letras.
            Ejemplo: 987: Novescientos ochenta y siete
            Lo vamos a mostrar con una webapp realizada en python, con el framework Reflex.
            '''

            if num == "0":
                return'Cero'
    
            numALetra = ''
            unidades = ['','uno','dos', 'tres', 'cuatro','cinco', 'seis', 'siete', 'ocho', 'nueve']
            decenas = ['', 'dieci', 'veinti', 'treinta y ', 'cuarenta y ', 'cincuenta y ','sesenta y ', 'setenta y ', 'ochenta y ', 'noventa y ']
            centenas = ['', 'ciento', 'doscientos', 'trescientos', 'cuatroscientos', 'quinientos', 'seiscientos', 'setecientos', 'ochocientos', 'novecientos']
            num = '0' * (3-len(str(num)))+ str(num)

            unidad = int(num[-1])
            decena = int(num[-2])
            centena = int(num[-3])

            numALetra = '{} {}{}'.format(centenas[centena], decenas[decena], unidades[unidad]).strip()

            numALetra = numALetra.replace('dieciuno', 'once')
            numALetra = numALetra.replace('diecidos', 'doce')
            numALetra = numALetra.replace('diecitres', 'trece')
            numALetra = numALetra.replace('diecicuatro', 'catorce')
            numALetra = numALetra.replace('diecicinco', 'quince')  

            if numALetra.endswith('dieci'):
                numALetra = numALetra.replace('dieci', 'diez')
            elif numALetra.endswith('veinti'):
                numALetra = numALetra.replace('veinti', 'veinte') 
            elif numALetra.endswith(' y'):
                numALetra = numALetra[:-2]
            elif numALetra.endswith('ciento'):
                numALetra = numALetra.replace('ciento', 'cien')            

            return numALetra.capitalize()

        
        self.form_data = numeroALetra(form_data)
        print(numeroALetra(form_data))


def index():
    return rx.vstack(
        rx.form.root(
            rx.vstack(
                rx.text("Ingrese un número de hasta tres dígitos:", color="blue", font_size="1.5rem"  ),
                rx.input(
                    name="input",
                    default_value="search",
                    placeholder="Input number here...",
                    type="text",
                    required=True,
                ),
                rx.button("Convertir", type="submit"),
                width="100%",
                align= "center",
            ),
            on_submit=FormInputState.handle_submit,
            reset_on_submit=True,
            width="100%",
            
        ),
        
        rx.divider(width="100%"),
        rx.heading("El número en letras es: "),
        rx.text(FormInputState.form_data.to_string()),
        width="100%",
        align= "center",
    )

app = rx.App()
app.add_page(index)
