from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import InputRequired, NumberRange


class PascalForm(FlaskForm):
    numRow = IntegerField('', validators=[InputRequired(), NumberRange(min=1, max=23, message="Row number should be in the range [1-23]")])
