
from huggingface_hub import login
import os
from kaggle_secrets import UserSecretsClient

try:
    # login(token=os.environ["HF_TOKEN"])
    user_secrets = UserSecretsClient()
    secret_value_0 = user_secrets.get_secret("HF_TOKEN")
    print("✓ Login successful to Hugging Face Hub")
except Exception as e:
    print(f"✗ Login failed: {e}")


from huggingface_hub import login
login()

import huggingface_hub
print(huggingface_hub.__version__)


from huggingface_hub import HfApi
api = HfApi()
api.whoami()