import gradio as gr
import os

def sorted(filepath):
    return os.path.listdir(filepath)

with gr.Blocks(title="🔊",theme=gr.themes.Base(primary_hue="rose",neutral_hue="zinc")) as app:
    with gr.Row():
        weight = gr.dropdown(choices=sorted('assets/weights'))

app.launch()