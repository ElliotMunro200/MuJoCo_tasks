import argparse
from environments.build_env import env_dict, agent_dict, def_hps, set_seed, name_of_run, build_env
import copy

class Config(object):
    """Object to hold the config requirements for a MuJoCo experiment"""
    def __init__(self, args):
        self.env_id = args.env_id
        self.agent_name = args.agent_name
        assert self.agent_name in env_dict(self.env_id, "agents")
        self.env_type = env_dict(self.env_id, "type")
        self.agent_group = agent_dict(self.agent_name, "group")
        self.agent_class = agent_dict(self.agent_name, "class")
        self.hyperparameters = def_hps(self.env_id, self.env_type, self.agent_group, self.agent_name)
        self.randomise_random_seed = args.randomise_random_seed
        self.seed = set_seed(self.randomise_random_seed, args.seed)
        self.run_name = name_of_run(self.env_id, self.agent_name, self.seed, args.run_name)
        self.num_episodes_per_run = args.num_episodes_per_run
        self.capture_video = args.capture_video
        self.environment = build_env(self.env_id, self.env_type, self.agent_name, self.capture_video, self.run_name)
        self.wandb = args.wandb
        self.wandb_project_name = args.wandb_project_name
        self.wandb_entity = args.wandb_entity
        self.GPU = args.GPU
        self.save_model = args.save_model
        self.requirements_to_solve_game = args.requirements_to_solve_game
        self.debug_mode = args.debug_mode

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--env_id", type=str, default="Walker2d-v4", help="The env ID")
    parser.add_argument("--agent_name", type=str, default="DDPG", help="Agent algo name")
    parser.add_argument("--randomise_random_seed", action='store_true', help="Use unknown random seeds?")
    parser.add_argument("--seed", type=int, default=1, help="The experiment seed")
    parser.add_argument("--run_name", type=str, default=None, help="The experiment run name")
    parser.add_argument("--num_episodes_per_run", type=int, default=5, help="number of episodes per run/game/experim")
    parser.add_argument("--wandb", action='store_true', help="Whether to use WandB logging and tracking")
    parser.add_argument("--wandb_project_name", type=str, default="MuJoCo_tasks", help="WandB project name")
    parser.add_argument("--wandb_entity", type=str, default=None, help="WandB entity")
    parser.add_argument("--capture_video", action='store_true', help="Whether to capture video")
    parser.add_argument("--GPU", action='store_true', help="Whether or not to use GPU")
    parser.add_argument("--save_model", action='store_true', help="Whether or not to save the trained model")
    parser.add_argument("--requirements_to_solve_game", type=str, default=None, help="Requirements to solve?")
    parser.add_argument("--debug_mode", action='store_true', help="Debug mode?")
    arguments = parser.parse_args()
    return arguments
