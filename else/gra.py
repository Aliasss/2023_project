import gradio

def greet(name):
    return 'hi, ' + name

app = gradio.Interface(
    inputs="text",
    fn=greet,
    outputs="text"
)

app.launch(share=True)