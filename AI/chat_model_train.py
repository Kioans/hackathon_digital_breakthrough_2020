from simpletransformers.classification import ClassificationModel
import pandas as pd
import logging
from AI import text_normalizer
from sklearn.model_selection import train_test_split
import torch


torch.multiprocessing.freeze_support()
logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)

x_data, y_data, y_labels = text_normalizer.get_normalized_words()
train_data = [[x_data[i], y_data[i]] for i in range(0, len(x_data))]

train_df, eval_df = train_test_split(train_data, test_size=0.1, random_state=42)
train_df = pd.DataFrame(train_df)

eval_df = pd.DataFrame(eval_df)

# Create a ClassificationModel
model = ClassificationModel('bert', 'bert-base-cased', num_labels=210, use_cuda=False, args={'reprocess_input_data': True, 'overwrite_output_dir': True})
# You can set class weights by using the optional weight argument

# Train the model
model.train_model(train_df)

# Evaluate the model
result, model_outputs, wrong_predictions = model.eval_model(eval_df)

predictions, raw_outputs = model.predict(["Интернет"])
