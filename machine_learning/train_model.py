from ludwig.api import LudwigModel
import pandas

df = pandas.read_csv("data/training_dataset.csv")
model = LudwigModel(config="fraud.yaml")
results = model.train(dataset=df)
