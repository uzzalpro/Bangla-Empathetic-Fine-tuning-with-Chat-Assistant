from datasets import load_dataset
from src.utils.yaml_loader import load_yaml
from src.model.unsloth_strategy import UnslothStrategy
from src.dataset.processor import DatasetProcessor
from src.training.fine_tuner import LLAMAFineTuner
from src.evaluation.evaluator import Evaluator

train_cfg = load_yaml("configs/training_config.yaml")["training"]
lora_cfg = load_yaml("configs/lora_config.yaml")["lora"]
model_cfg = load_yaml("configs/model.yaml")["model"]

strategy = UnslothStrategy(model_cfg, lora_cfg)
model, tokenizer = strategy.load_model()

dataset = load_dataset("json", data_files="data/raw/bengali_empathy.json")["train"]

processor = DatasetProcessor(tokenizer, model_cfg["max_seq_length"])
tokenized_ds = processor.tokenize(dataset)

trainer = LLAMAFineTuner(model, tokenizer, train_cfg)
trainer.train(tokenized_ds)

evaluator = Evaluator(model, tokenizer, model_cfg["max_seq_length"])
ppl = evaluator.perplexity(dataset["Answers"][:50])

print("Perplexity:", ppl)
