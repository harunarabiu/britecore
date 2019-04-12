from featurerequest import app
from flask import render_template, request, flash


from .forms import FeatureRequestForm
from .models import FeatureRequest

@app.route("/", methods=['GET', 'POST'])
def feature_request():
    form = FeatureRequestForm()
    if request.method == "POST":
        if form.validate_on_submit():

            data = form.data
            if 'csrf_token' in data:
                del data['csrf_token']

            obj = FeatureRequest(**data)
            result = obj.add()
            if result:
                flash("Record Successfully Added.", "success")
        else:
            flash("Please correct the errors on the form.", "error")




    return render_template('feature-request.html', form=form)


@app.route("/requested_features")
def requested_features():
    data = FeatureRequest.query.all()
    return render_template('requested_features.html', data=data)
