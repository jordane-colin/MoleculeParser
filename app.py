#!/usr/bin/env python3

import launch_for_test
from parser import parse_molecule
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    error = ''
    formatted_molecules = dict()
    submitted_formula = ''
    for name, item in launch_for_test.MOLECULES:
        formatted_molecules[name] = parse_molecule(item)
    if request.method == 'GET':
        formula = request.args.get('formula')
        if formula:
            try:
                submitted_formula = parse_molecule(formula)
            except ValueError as err:
                error = err

    return render_template("index.html",
                           molecules=formatted_molecules,
                           submitted_formula=submitted_formula,
                           error=error)


if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
