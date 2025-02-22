import copy
import random
import pickle
import os
import gym
from gym import wrappers
import numpy as np
import wandb
from torch.utils.tensorboard import SummaryWriter

class Trainer(object):
    """Runs games for given agents. Optionally will visualise and save the results"""
    def __init__(self, config):
        self.config = config
        self.env_id = config.env_id
        self.env_type = config.env_type
        self.agent_name = config.agent_name
        self.agent_group = config.agent_group
        self.agent_class = config.agent_class
        self.seed = config.seed
        self.num_episodes_per_run = config.num_episodes_per_run
        self.hyperparameters = config.hyperparameters
        self.wandb = config.wandb
        self.capture_video = config.capture_video
        self.GPU = config.GPU
        self.run_name = config.run_name

    #def prof(self):
    #    import cProfile as profile
    #    profile.runctx('self.run_game_for_agent()', globals(), locals(), 'results/cProfileDumps/reacher1k.profile')

    def run_game_for_agent(self):
        """Runs a game for a given agent, saving the results in self.results"""
        actor_str = "Actor"
        critic_str = "Critic"
        print(f"ENV ID: {self.env_id}")
        print(f"ENV TYPE: {self.env_type}")
        print(f"AGENT NAME: {self.agent_name}")
        print(f"AGENT GROUP: {self.agent_group}")
        print(f"RANDOM SEED: {self.seed}")
        print(f"NUM EPISODES PER RUN: {self.num_episodes_per_run}")
        print(f"WANDB: {self.wandb}")
        print(f"CAPTURE VIDEO: {self.capture_video}")
        print(f"GPU: {self.GPU}")
        print(f"RUN NAME: {self.run_name}")
        print(f"HYPERPARAMETERS: {self.hyperparameters}")

        agent_results = []
        agent_config = self.config
        if agent_config.wandb:
            writer = self.wandb_logger(agent_config)
        agent = agent_config.agent_class(agent_config)
        # CHECK HYPERPARAMETERS ARE WHAT THEY SHOULD BE
        game_scores, rolling_scores, time_taken = agent.run_n_episodes()
        agent_results.append([game_scores, rolling_scores, len(rolling_scores), -1 * max(rolling_scores), time_taken])
        if agent_config.wandb:
            for idx, val in enumerate(game_scores):
                writer.add_scalar("Charts/episodic_return", val, idx)
            writer.close()
            wandb.finish()
        print(f"Time taken: {round(time_taken,1)} seconds", flush=True)

    def wandb_logger(self, config):
        wandb.init(
            entity=config.wandb_entity,
            project=config.wandb_project_name,
            name=config.run_name,
            config=config,
            sync_tensorboard=True,
            monitor_gym=True,
            save_code=True,
        )
        writer = SummaryWriter(f"runs/{config.run_name}")
        writer.add_text("config", str(config))
        return writer









