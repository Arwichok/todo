from pathlib import Path


ROOT_PATH = Path(__file__).parent.parent
TEMPLATES_PATH = ROOT_PATH / "presentation" / "web" / "templates"

print(ROOT_PATH)
print(TEMPLATES_PATH)