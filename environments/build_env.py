"""Defines the functions used by the Config class to define a MuJoCo experiment"""

import gym
import time
import random
from agents.policy_gradient_agents.PPO import PPO
from agents.policy_gradient_agents.REINFORCE import REINFORCE
from agents.actor_critic_agents.DDPG import DDPG
from agents.actor_critic_agents.DDPG_HER import DDPG_HER
from agents.actor_critic_agents.A2C import A2C
from agents.actor_critic_agents.A3C import A3C
from agents.actor_critic_agents.SAC import SAC
from agents.actor_critic_agents.TD3 import TD3
from agents.hierarchical_agents.DIAYN import DIAYN
from agents.hierarchical_agents.HIRO import HIRO
from agents.hierarchical_agents.SNN_HRL import SNN_HRL

from environments.my_create_maze_env import create_maze_env
from environments.hyperparameters_for_agent import chosen_hyperparameters


def env_dict(env_id, key):
    e_dict = {
        "Ant-v3": {"type": "Basic", "agents": ["DDPG", "SAC", "PPO", "TD3", "DIAYN", "HIRO"]},
        "Ant-v4": {"type": "Basic", "agents": ["DDPG", "SAC", "PPO", "TD3", "DIAYN", "HIRO"]},
        "HalfCheetah-v3": {"type": "Basic", "agents": ["DDPG", "SAC", "PPO", "TD3", "DIAYN", "HIRO"]},
        "HalfCheetah-v4": {"type": "Basic", "agents": ["DDPG", "SAC", "PPO", "TD3", "DIAYN", "HIRO"]},
        "Hopper-v3": {"type": "Basic", "agents": ["DDPG", "SAC", "PPO", "TD3", "DIAYN", "HIRO"]},
        "Hopper-v4": {"type": "Basic", "agents": ["DDPG", "SAC", "PPO", "TD3", "DIAYN", "HIRO"]},
        "Humanoid-v3": {"type": "Basic", "agents": ["DDPG", "TD3"]},
        "Humanoid-v4": {"type": "Basic", "agents": ["DDPG", "TD3"]},
        "HumanoidStandup-v4": {"type": "Basic", "agents": ["DDPG", "TD3"]},
        "InvertedDoublePendulum-v4": {"type": "Basic", "agents": ["DDPG", "TD3"]},
        "InvertedPendulum-v4": {"type": "Basic", "agents": ["DDPG", "TD3"]},
        "MountainCarContinuous-v0": {"type": "Basic", "agents": ["DDPG", "SAC", "PPO", "TD3"]},
        "Pusher-v4": {"type": "Basic", "agents": ["DDPG", "TD3"]},
        "Reacher-v4": {"type": "Basic", "agents": ["DDPG", "SAC", "PPO", "TD3", "DIAYN", "HIRO"]},
        "Swimmer-v3": {"type": "Basic", "agents": ["DDPG", "TD3"]},
        "Swimmer-v4": {"type": "Basic", "agents": ["DDPG", "TD3"]},
        "Walker2d-v3": {"type": "Basic", "agents": ["DDPG", "SAC", "PPO", "TD3", "DIAYN", "HIRO"]},
        "Walker2d-v4": {"type": "Basic", "agents": ["DDPG", "SAC", "PPO", "TD3", "DIAYN", "HIRO"]},
        "AntFall": {"type": "AntNav", "agents": ["DDPG", "TD3", "DIAYN", "HIRO"]},
        "AntMaze": {"type": "AntNav", "agents": ["DDPG", "TD3", "DIAYN", "HIRO"]},
        "AntPush": {"type": "AntNav", "agents": ["DDPG", "TD3", "DIAYN", "HIRO"]},
    }
    env_info = e_dict[env_id][key]
    return env_info


def agent_dict(agent_name, key):
    """Creates a dictionary that maps an agent to their wider agent group"""
    a_dict = {
        "PPO": {"group": "Policy_Gradient_Agents", "class": PPO},
        "REINFORCE": {"group": "Policy_Gradient_Agents", "class": REINFORCE},
        "DDPG": {"group": "Actor_Critic_Agents", "class": DDPG},
        "DDPG-HER": {"group": "Actor_Critic_Agents", "class": DDPG_HER},
        "TD3": {"group": "Actor_Critic_Agents", "class": TD3},
        "A2C": {"group": "Actor_Critic_Agents", "class": A2C},
        "A3C": {"group": "Actor_Critic_Agents", "class": A3C},
        "SAC": {"group": "Actor_Critic_Agents", "class": SAC},
        "SNN-HRL": {"group": "SNN_HRL", "class": SNN_HRL},
        "HIRO": {"group": "HIRO", "class": HIRO},
        "DIAYN": {"group": "DIAYN", "class": DIAYN}
    }
    agent_info = a_dict[agent_name][key]
    return agent_info


def def_hps(env_id, env_type, agent_group):
    # need to make specific imports from a hyperparameters file that returns a dict based on args
    agent_hyperparameters = chosen_hyperparameters(env_id, env_type, agent_group)

    return agent_hyperparameters


def set_seed(randomize, given_seed):
    if randomize:
        seed = random.randint(0, 2 ** 10 - 2)
    else:
        seed = given_seed

    return seed


def env_has_changeable_goals(env):
    """Determines whether the environment is such that for each episode there is a different goal or not.
    If there is a different goal each episode, there will be no return_info,
    and env.reset() will return 'ob' in the form of a dict."""
    print(f"ENV HAS CHANGEABLE GOALS: {isinstance(env.reset(), dict)}")
    return isinstance(env.reset(), dict)


def name_of_run(env_id, agent_name, seed, given_name):
    if given_name is not None:
        name = given_name
    else:
        name = f"{env_id}__{agent_name}__{seed}__{int(time.time())}"
    return name


def build_env(env_id, env_type, agent_name, capture_video, run_name):
    def thunk():

        if env_type == "Basic":
            env = gym.make(env_id)
            print("[~~Basic~~Env~~Built~~]")
        elif env_type == "AntNav":
            # returns a wrapped AntNav gym env
            env = create_maze_env(env_id)
            print("[~~AntNav~~Env~~Built~~]")
        else:
            raise ValueError("Wrong environment name")
        env = gym.wrappers.RecordEpisodeStatistics(env)
        if capture_video:
            env = gym.wrappers.RecordVideo(env, f"videos/{run_name}")
            print("CAPTURING VIDEO...")
        # see if agent needs env flattening
        if env_has_changeable_goals(env) and ("HER" not in agent_name):
            env = gym.wrappers.FlattenDictWrapper(env, dict_keys=["observation", "desired_goal"])
            print("Flattening changeable-goal environment for agent {}".format(agent_name))

        return env

    return thunk
