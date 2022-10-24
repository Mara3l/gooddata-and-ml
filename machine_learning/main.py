import os

from gooddata_pandas import GoodPandas
from pycaret.regression import *

host = os.environ["GOODDATA_HOST"]
token = os.environ["GOODDATA_TOKEN"]
workspace = os.environ["WORKSPACE_ID"]
report = os.environ["REPORT_ID"]

gp = GoodPandas(host, token)
frames = gp.data_frames(workspace)

report_data = frames.for_insight(report)

print(report_data)

s = setup(report_data, target="close")

best = compare_models()

predictions = predict_model(best, data=report_data)
print(predictions.head())
