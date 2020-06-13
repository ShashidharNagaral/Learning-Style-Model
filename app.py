from flask import Flask, request, json
import copy
import utils as util
from utils import lsDictionary as d
import visualVerbalModel as VVModel
import activeReflectiveModel as ARModel
import sensingIntuitiveModel as SIModel
import sequentialGlobalModel as SGModel
import confusion as Confusion
import effort as Effort
app = Flask(__name__)


def predictFunction():
    data = request.get_json()
    print(data)
    output = util.extractAttr(data, ["uid"])
    # output1 = copy.deepcopy(output)
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
    # ----- EMOTIONS -----#
    # ----- confusion -----#
    # model_input = util.transformToModelInput(data, d['conf'])
    # model_output = Confusion.predict(model_input)
    # output1 = util.insertLS(model_output, output1, 'conf')
    # print(output1)
    model_input = util.transformToModelInput(data, d['conf'])
    model_output = Confusion.predict(model_input)
    output = util.insertLS(model_output, output, 'conf')
    model_input = util.transformToModelInput(data, d['eff'])
    model_output = Effort.predict(model_input)
    output = util.insertLS(model_output, output, 'eff')
    print(output)
    response = {'model_response': json.dumps(output)}
    return response


@app.route('/predict', methods=['POST'])
def predict():
    return predictFunction()


@app.route('/predictTest', methods=['POST'])
def predictTest():
    return predictFunction()


if __name__ == '__main__':
    app.run()
