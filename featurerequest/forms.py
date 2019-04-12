from flask_wtf import FlaskForm
from wtforms import  StringField
from wtforms.validators import DataRequired



class FeatureRequestForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(message="Title is required")])
    description = StringField('Description', validators=[DataRequired(message="Decription is required")])
    client = StringField('Client', validators=[DataRequired(message="Client is required")])
    client_priority = StringField('Client Priority', validators=[DataRequired(message="Client Priority is required")])
    target_date = StringField('Target Date', validators=[DataRequired(message="Target Date is required")])
    product_area = StringField('Product Area', validators=[DataRequired(message="Product Area is required")])
