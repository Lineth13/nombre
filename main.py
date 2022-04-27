def pulsador_a():
    basic.show_string("Mi nombre es Lineth")

def pulsador_b():
    basic.show_string("Mi edad es 16")

input.on_button_pressed(Button.A, pulsador_a)
input.on_button_pressed(Button.B, pulsador_b)
