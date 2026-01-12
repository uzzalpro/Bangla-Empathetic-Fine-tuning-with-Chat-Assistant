

from logger import logging
from exception import BangliEmpathyException
from trl import SFTTrainer
from transformers import TrainingArguments

class LLAMAFineTuner:
    def __init__(self, model, tokenizer, train_cfg):
        self.model = model
        self.tokenizer = tokenizer
        self.train_cfg = train_cfg

    def train(self, dataset):
        try:
            trainer = SFTTrainer(
                model=self.model,
                tokenizer=self.tokenizer,
                train_dataset=dataset,
                dataset_text_field="text",
                max_seq_length=self.train_cfg["max_seq_length"],
                packing=False,
                args=TrainingArguments(**self.train_cfg)
            )
            trainer.train()
            return trainer
        except Exception as e:
            raise BangliEmpathyException(e, sys) from e

model.save_pretrained("llama-3.1-8B-bangla-empathy")
tokenizer.save_pretrained("llama-3.1-8B-bangla-empathy")
