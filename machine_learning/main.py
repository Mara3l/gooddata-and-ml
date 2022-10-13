import os

from gooddata_pandas import GoodPandas
from pycaret.regression import *

host = os.environ["GOODDATA_HOST"]
token = os.environ["GOODDATA_TOKEN"]
workspace = os.environ["WORKSPACE_ID"]
insight = os.environ["INSIGHT_ID"]

gp = GoodPandas(host, token)
frames = gp.data_frames(workspace)

insight_data = frames.for_insight(insight)

print(insight_data)

s = setup(insight_data, target="close")

best = compare_models()

predict_model(best)

predictions = predict_model(best, data=insight_data)
print(predictions.head())
