import evaluate, math, torch

class Evaluator:
    def __init__(self):
        self.bleu = evaluate.load("bleu")
        self.rouge = evaluate.load("rouge")

    def bleu_rouge(self, preds, refs):
        return {
            "bleu": self.bleu.compute(predictions=preds, references=refs),
            "rouge": self.rouge.compute(predictions=preds, references=refs)
        }

    def perplexity(self, model, tokenizer, texts, max_len):
        losses = []
        for t in texts:
            enc = tokenizer(
                t, return_tensors="pt",
                truncation=True, max_length=max_len
            ).to(model.device)

            with torch.no_grad():
                loss = model(
                    input_ids=enc["input_ids"],
                    labels=enc["input_ids"]
                ).loss
            losses.append(loss.item())

        return math.exp(sum(losses)/len(losses))
