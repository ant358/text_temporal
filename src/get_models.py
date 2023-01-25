# %%
import torch
import os
from transformers import AutoTokenizer, AutoModelForTokenClassification


def get_ner_tokenizer():
    return AutoTokenizer.from_pretrained(
        "satyaalmasian/temporal_tagger_BERT_tokenclassifier")


def get_ner_model():
    return AutoModelForTokenClassification.from_pretrained(
        "satyaalmasian/temporal_tagger_BERT_tokenclassifier")


def save_model(model, tokenizer, path):
    model.save_pretrained(path)
    tokenizer.save_pretrained(path)


if __name__ == "__main__":

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # check to see if the model is already saved
    if not os.path.exists(
            "../models/satyaalmasian/temporal_tagger_BERT_tokenclassifier"):
        model = get_ner_model()
        tokenizer = get_ner_tokenizer()
        save_model(
            model, tokenizer,
            "../models/satyaalmasian/temporal_tagger_BERT_tokenclassifier")
        print("temporal_model saved")

# %%
