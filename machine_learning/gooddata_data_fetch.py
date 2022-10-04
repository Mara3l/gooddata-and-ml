import os

from gooddata_pandas import GoodPandas

host = os.environ["GOODDATA_HOST"]
token = os.environ["GOODDATA_TOKEN"]
workspace = os.environ["WORKSPACE_ID"]
training_dataset = os.environ["TRAINING_DATASET_ID"]
validation_dataset = os.environ["VALIDATION_DATASET_ID"]

gp = GoodPandas(host, token)
frames = gp.data_frames(workspace)

training_df = frames.for_insight(training_dataset)
validation_df = frames.for_insight(validation_dataset)

training_df.to_csv("data/training_dataset.csv")
validation_df.to_csv("data/validation_dataset.csv")
