
from scale_chart import create_app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=4545)


# #TODO
# # - logging
# # - enhance CSS
# # - add more scale types (modes)
# # - dockerize
# import sqlite3
# import os
# from flask import Flask, render_template, request, current_app, g
# from flask.cli import with_appcontext
# from scale_chart import FretBoard, scale_types, key_notes
#
# # app = Flask(__name__)
#
#
#
#
# def create_app(test_config=None):
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_mapping(
#         SECRET_KEY='dev',
#         DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
#     )
#
#     if test_config is None:
#         # load the instance config, if it exists, when not testing
#         app.config.from_pyfile("config.py", silent=True)
#     else:
#         # load the test config if passed in
#         app.config.from_mapping(test_config)
#
#         # ensure the instance folder exists
#         try:
#             os.makedirs(app.instance_path)
#         except OSError:
#             pass
#
#         @app.route("/", methods=["POST", "GET"])
#         def home():
#             state = ""
#             if request.method == "POST":
#                 key_note_input = request.form["key_note_select"]
#                 scale_type_input = request.form["scale_type_select"]
#                 state = {'scale_choice': scale_type_input, 'key_choice': key_note_input}
#                 fretboard = FretBoard(key_note=key_note_input, scale_type=scale_type_input)
#             else:
#                 fretboard = FretBoard()
#
#             return render_template("index.html",
#                                    key_note_data=key_notes,
#                                    scale_type_data=scale_types,
#                                    tab=fretboard.draw_neck(),
#                                    state=state)
#
# def get_db():
#     if "db" not in g:
#         g.db = sqlite3.connect(
#             current_app.config["DATABASE"],
#             detect_types=sqlite3.PARSE_DECLTYPES
#         )
#         g.db.row_factory = sqlite3.Row
#
#     return g.db
#
# def close_db(e=None):
#     db = g.pop("db", None)
#
#     if db is not None:
#         db.close()
#
#
# if __name__ == "__main__":
#     create_app()
