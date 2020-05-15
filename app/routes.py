from app import app
from flask import render_template
from app.forms import PascalForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PascalForm()

    if form.validate_on_submit():
        row_number = form.numRow.data
        pascal = pascalsTriangle(row_number)
        return render_template('index.html', form=form, pascal=pascal)

    return render_template('index.html', title='Pascal\'s Briwates',form=form)


def pascalsTriangle(row_number):
    from operator import add

    res = [[1]]
    for _ in range(1, row_number):
        map_ = map(add, [0] + res[-1], res[-1] + [0])
        res.append(list(map_))

    return res if row_number else []
