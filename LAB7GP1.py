from guizero import App, Text, Picture
app= App("WANTED!", height=600, width=900)
app.bg = "#A0A0A0"
wanted_text = Text(app, "MR GOPHER")
wanted_text.text_size = 50
wanted_text.font = "Times New Roman"
cat = Picture(app, image="Gopher.jpg")
app.display()