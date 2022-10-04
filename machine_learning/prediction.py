from ludwig.api import LudwigModel

model = LudwigModel.load('results/api_experiment_run/model')

predictions, _ = model.predict(dataset='data/fraud_input.csv')
print(predictions.head())

eval_stats, _, _ = model.evaluate(dataset='data/validation_dataset.csv')

print(eval_stats)
