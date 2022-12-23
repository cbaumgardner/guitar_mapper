import logging
from flask import Flask, render_template, request
from scale_chart import FretBoard, ScaleChartConfig

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

def create_app():
    config = ScaleChartConfig()
    app = Flask(__name__)

    @app.route("/", methods=["POST", "GET"])
    def home():
        state = ""
        if request.method == "POST":
            key_note_input = request.form["key_note_select"]
            scale_type_input = request.form["scale_type_select"]
            state = {'scale_choice': scale_type_input, 'key_choice': key_note_input}
            fretboard = FretBoard(key_note=key_note_input, scale_type=scale_type_input)
        else:
            fretboard = FretBoard()
        logging.info(f"{request.method} - Rendering for {fretboard.key_note} {fretboard.scale_type}")
        return render_template("index.html",
                               key_note_data=config.key_notes,
                               scale_type_data=config.scale_types,
                               string=fretboard.draw_neck(),
                               state=state)

    return app


app = create_app()
