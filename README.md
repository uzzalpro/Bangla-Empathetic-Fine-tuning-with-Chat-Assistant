
# **Project: Bangla Empathetic Fine-tuning with Chat Assistant**

This notebook implements a complete pipeline for fine-tuning LLaMA 3.1-8B-Instruct using parameter-efficient fine-tuning (LoRA/Unsloth) for empathetic response generation.
### Requirements Implemented:
1. Preprocess dataset for LLM fine-tuning
2. Fine-tune LLaMA 3.1-8B-Instruct using LoRA/Unsloth
3. Evaluation pipeline (Perplexity, BLEU, ROUGE, Human evaluation)
4. Database logging system
5. OOP Design with Strategy Pattern
6. Resource optimization (gradient checkpointing, mixed precision)

### **DatasetProcessor** 


* We load Bengali empathetic conversations from CSV and clean them.
* We convert raw Q&A into instruction–response format.
* We make Dataset splitting

**“DatasetProcessor isolates data representation logic so changes in prompts or cleaning don’t affect training code or experimental validity.”**


## **Load the Model**
- We abstract model loading using a Strategy Pattern.
- How the base model is loaded
- Backend-specific optimizations
- Hardware-aware configuration

*“The Strategy pattern decouples model selection and optimization from training logic, enabling backend or configuration changes without modifying the core pipeline.”*

**Using Unsloth (which is highly recommended for Llama 3.1 in notebooks due to speed), the loading process looks like this**

### **LoRA Adaptation (Core Algorithm)**
* Apply LoRA to attention layers only.
* Low-rank matrices injected into attention.

**WHY**
- ✔ Parameter-efficient
- ✔ Attention controls reasoning + empathy
- ✔ Train <1% parameters
- ✔ Faster, cheaper, safer

*This is the algorithmic heart of the system*

### **LLAMAFineTuner**
1. LoRA injection
2. Tokenization policy
3. Training loop
4. Memory optimization
5. Most OOMs happen
6. Most performance decisions live 

*“LLAMAFineTuner centralizes all learning-related decisions, ensuring training behavior is controlled, debuggable, and reproducible.”*

**Fine-tuning is not just optimization — it’s system orchestration.**

### **Training Loop (SFTTrainer)**
* Supervised fine-tuning using TRL.
* Requirement: sequence length not reduced

*TRL handles causal LM correctly, Supports instruction tuning, Stable training with LoRA*

**The “same model” behaves differently depending on how it’s loaded.**

## **Evaluator**
Evaluate with BLEU, ROUGE, Perplexity.

**BLEU** → N-gram overlap,   **ROUGE** → Recall-oriented overlap,   **Perplexity** → Language fluency

* Metric computation
* Text generation for evaluation
* Model comparison logic

“*Evaluator separates model assessment from optimization, enabling unbiased metric computation and consistent comparison across experiments.”*

**Metrics are not model quality — they are signals.**

### **Human Evaluation (Empathy)**  

**Empathy**, **Tone**, **Helpfulness** (1–5 scale)

*Manual scoring of emotional quality.*

**WHY**
* Empathy is subjective
* Metrics miss emotional nuance
* Shows real-world ML thinking


## Workflow
- constant
- config_entity
- adaptor_entity
- core
- pipeline
- app.py / demo.py