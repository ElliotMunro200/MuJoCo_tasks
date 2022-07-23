"""Executes a defined run from the Config and passed command line args."""

import shutup;shutup.please()
from agents.Trainer import Trainer
from utilities.data_structures.Config import Config, parse_args

if __name__ == "__main__":
    args = parse_args()
    config = Config(args)
    #print(vars(config))
    trainer = Trainer(config)
    #trainer.prof()
    trainer.run_game_for_agent()

