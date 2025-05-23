import yaml
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parent.parent / "config" / "config.yaml"
SECRETS_PATH = Path(__file__).resolve().parent.parent / "config" / "secrets_template.yaml"

with open(CONFIG_PATH) as f:
    config = yaml.safe_load(f)

with open(SECRETS_PATH) as f:
    secrets = yaml.safe_load(f)

class Settings:
    def __init__(self, config, secrets):
        self.__dict__.update(config)
        self.__dict__.update(secrets)

settings = Settings(config, secrets)
