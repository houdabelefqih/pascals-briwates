from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    from operator import add

    numRows = 17
    res = [[1]]
    for _ in range(1, numRows):
        map_ = map(add, [0] + res[-1], res[-1] + [0])
        res.append(list(map_))

    pascal=  res if numRows else []

    return render_template('index.html', title='Pascal\'s Briwates', pascal=pascal)
