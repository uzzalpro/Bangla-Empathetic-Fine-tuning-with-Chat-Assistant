class DatasetProcessor:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.EOS = tokenizer.eos_token
        self.PROMPT = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{}

### Input:
{}

### Response:
{}"""

    def format_examples(self,batch):
        texts = []
        for inst, q, ans in zip(
            batch["Question-Title"],
            batch["Questions"],
            batch["Answers"]
        ):
            texts.append(self.PROMPT.format(inst, q, ans) + self.EOS)
        return {"text": texts}
    
    
    def preprocess(self, dataset):
        return dataset.map(
            self.format_batch,
            batched=True,
            remove_columns=dataset.column_names
        )
