import hydra
import os
import sys
from omegaconf import DictConfig
from importlib import import_module
from pathlib import Path
import logging
import torch
from utils.random_seed import setup_seed
import warnings
import torch.multiprocessing as mp

warnings.filterwarnings("ignore")
torch.autograd.set_detect_anomaly(True)

os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":16:8"

# Config primit din linia de comandă:
# python3 run.py "./configs/training&infer_img_folder.yaml"
if len(sys.argv) < 2:
    raise ValueError('Usage: python3 run.py "./configs/training&infer_img_folder.yaml"')

config_file = sys.argv[1]
config_dir = os.path.dirname(config_file)
config_name = os.path.basename(config_file)

# Scoatem argumentul cu yaml-ul ca Hydra să nu îl trateze ca override
sys.argv = [sys.argv[0]] + sys.argv[2:]


@hydra.main(version_base=None, config_path=config_dir, config_name=config_name)
def main(cfg: DictConfig) -> None:
    setup_seed(cfg.random_seed)

    working_dir = str(Path.cwd())
    logging.info(f"The current working directory is {working_dir}")

    runner_module_cfg = cfg.runner_module
    module_path, attr_name = runner_module_cfg.split(" - ")
    module = import_module(module_path)
    runner_module = getattr(module, attr_name)
    runner = runner_module(cfg, working_dir)

    runner.run()


if __name__ == "__main__":
    main()