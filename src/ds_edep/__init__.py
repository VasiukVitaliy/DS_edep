import logging
import sys
from pathlib import Path  # 1. Виправлено імпорт

# 2. Виправлено опечатку в %(asctime)s
formater = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
dirpath = "logs/logging.log"

filepath = Path(dirpath)
# 3. Виправлено parent -> parents
filepath.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=formater,
    handlers=[
        logging.FileHandler(filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

main_logger = logging.getLogger("Main dsp logger")

main_logger.info("Logger setup completed!")