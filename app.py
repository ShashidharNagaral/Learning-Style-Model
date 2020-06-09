from flask import Flask, request, json
import utils as util
from utils import lsDictionary as d
import visualVerbalModel as VVModel
import activeReflectiveModel as ARModel
import sensingIntuitiveModel as SIModel
import sequentialGlobalModel as SGModel
app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    print(data)
    output = util.extractAttr(data, ["uid"])
    # ------visual verbal model-----#
    model_input = util.transformToModelInput(data, d['vv'])
    model_output = VVModel.predict(model_input)
    output = util.insertLS(model_output, output, 'vv')
    # ------active reflective model-----#
    model_input = util.transformToModelInput(data, d['ar'])
    model_output = ARModel.predict(model_input)
    output = util.insertLS(model_output, output, 'ar')
    # ------sensing intuitive model-----#
    model_input = util.transformToModelInput(data, d['si'])
    model_output = SIModel.predict(model_input)
    output = util.insertLS(model_output, output, 'si')
    # ------sequential global model -----#
    output = SGModel.getUserPath(data, output)
    print(output)
    response = {'model_response': json.dumps(output)}
    return response


if __name__ == '__main__':
    app.run()
