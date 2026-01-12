merged_model = model.merge_and_unload()


merged_model.save_pretrained(
    "llama-3.1-8B-bangla-empathy",
    safe_serialization=True
)

tokenizer.save_pretrained("full-llama-3.1-8B-bangla-empathy")

## **Login to HuggingFace**



merged_model.push_to_hub(
    repo_id="uzzalHossen/full-llama-3.1-8B-bangla-empathy",
    private=False
)

tokenizer.push_to_hub(
    repo_id="uzzalHossen/full-llama-3.1-8B-bangla-empathy"
)
