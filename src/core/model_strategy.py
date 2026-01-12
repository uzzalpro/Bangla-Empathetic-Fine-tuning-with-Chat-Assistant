from unsloth import FastLanguageModel

class UnslothStrategy:
    def load(self, model_name, max_seq_length):
        model, tokenizer = FastLanguageModel.from_pretrained(
            model_name=model_name,
            max_seq_length=max_seq_length,
            load_in_4bit=True,
        )
        tokenizer.pad_token = tokenizer.eos_token
        return model, tokenizer

    def apply_lora(self, model, lora_cfg, max_seq_length):
        return FastLanguageModel.get_peft_model(
            model,
            max_seq_length=max_seq_length,
            **lora_cfg
        )
