"""Executes a defined run from execute_MuJoCo_experiments.py"""

from agents.Trainer import Trainer
from utilities.data_structures.Config import Config, parse_args

if __name__ == "__main__":
    args = parse_args()
    config = Config(args)
    trainer = Trainer(config)
    trainer.run_game_for_agent()

