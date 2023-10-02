from flask import Flask, render_template_string, request
import voxa

app = Flask(__name__)
translator = voxa.Translator(source='en', target='fr')

TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Translation App</title>
</head>
<body>

<div style="text-align:center; padding: 50px;">
    <h2>Text Translation (EN to FR)</h2>

    <form action="/" method="post">
        <textarea name="text_to_translate" rows="5" cols="50" placeholder="Enter English text here...">{{ original_text }}</textarea>
        <br><br>
        <input type="submit" value="Translate">
    </form>

    <h3>Translation:</h3>
    <textarea rows="5" cols="50" readonly>{{ translation }}</textarea>
</div>

</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    translation = ""
    original_text = ""

    if request.method == 'POST':
        original_text = request.form.get('text_to_translate')
        if original_text:
            translation = translator.translate(original_text)

    return render_template_string(TEMPLATE, original_text=original_text, translation=translation)

if __name__ == '__main__':
    app.run(debug=True)
