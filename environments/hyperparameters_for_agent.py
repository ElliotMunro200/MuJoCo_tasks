"""Defines a function that takes experiment arguments and returns dictionaries of agent hyperparameters"""

# define the logic of choosing hyperparameters here.
# 1. start by looking through sets of hyperparameters for my chosen envs e.g. Walker/Hopper/Reacher etc. and compare.
# 2. determine some logic to define the hyperparameters based on the most important experiment arguments.
# 3. build the mega-dictionary or if-statement logic flow.
import copy

actor_critic_agent_hyperparameters = {
    "Actor": {
        "learning_rate": 0.0003,
        "linear_hidden_units": [64, 64],
        "final_layer_activation": None,
        "batch_norm": False,
        "tau": 0.005,
        "gradient_clipping_norm": 5,
        "initialiser": "Xavier"
    },

    "Critic": {
        "learning_rate": 0.0003,
        "linear_hidden_units": [64, 64],
        "final_layer_activation": None,
        "batch_norm": False,
        "buffer_size": 1000000,
        "tau": 0.005,
        "gradient_clipping_norm": 5,
        "initialiser": "Xavier"
    },

    "min_steps_before_learning": 400,
    "batch_size": 256,
    "discount_rate": 0.99,
    "mu": 0.0,  # for O-H noise
    "theta": 0.15,  # for O-H noise
    "sigma": 0.25,  # for O-H noise
    "action_noise_std": 0.2,  # for TD3
    "action_noise_clipping_range": 0.5,  # for TD3
    "update_every_n_steps": 1,
    "learning_updates_per_learning_session": 1,
    "automatically_tune_entropy_hyperparameter": True,
    "entropy_term_weight": None,
    "add_extra_noise": False,
    "do_evaluation_iterations": True,
    "clip_rewards": False
}

dqn_agent_hyperparameters = {
    "learning_rate": 0.005,
    "batch_size": 128,
    "buffer_size": 40000,
    "epsilon": 1.0,
    "epsilon_decay_rate_denominator": 3,
    "discount_rate": 0.99,
    "tau": 0.01,
    "alpha_prioritised_replay": 0.6,
    "beta_prioritised_replay": 0.1,
    "incremental_td_error": 1e-8,
    "update_every_n_steps": 3,
    "linear_hidden_units": [30, 15],
    "final_layer_activation": "None",
    "batch_norm": False,
    "gradient_clipping_norm": 5,
    "clip_rewards": False,
    "learning_iterations": 1
}

manager_hyperparameters = dqn_agent_hyperparameters
manager_hyperparameters.update({"timesteps_to_give_up_control_for": 5})

config_hyperparameters = {
    # From Hopper.py
    "Policy_Gradient_Agents": {
        "learning_rate": 0.05,
        "linear_hidden_units": [30, 15],
        "final_layer_activation": "TANH",
        "learning_iterations_per_round": 10,
        "discount_rate": 0.9,
        "batch_norm": False,
        "clip_epsilon": 0.2,
        "episodes_per_learning_round": 10,
        "normalise_rewards": True,
        "gradient_clipping_norm": 5,
        "mu": 0.0,
        "theta": 0.15,
        "sigma": 0.2,
        "epsilon_decay_rate_denominator": 1,
        "clip_rewards": False
    },

    # From Hopper.py
    "Actor_Critic_Agents": actor_critic_agent_hyperparameters,

    # From Hopper.py
    "DIAYN": {
        "DISCRIMINATOR": {
            "learning_rate": 0.001,
            "linear_hidden_units": [32, 32],
            "final_layer_activation": None,
            "gradient_clipping_norm": 5
        },

        "AGENT": actor_critic_agent_hyperparameters,
        "MANAGER": manager_hyperparameters,
        "num_skills": 10,
        "num_unsupservised_episodes": 500 # Walker.py has = 100
    },

    # From Reacher.py
    "HIRO": {
        "LOWER_LEVEL": {
            "Actor": {
                "learning_rate": 0.001,
                "linear_hidden_units": [20, 20],
                "final_layer_activation": "TANH",
                "batch_norm": False,
                "tau": 0.005,
                "gradient_clipping_norm": 5
            },

            "Critic": {
                "learning_rate": 0.01,
                "linear_hidden_units": [20, 20],
                "final_layer_activation": "None",
                "batch_norm": False,
                "buffer_size": 100000,
                "tau": 0.005,
                "gradient_clipping_norm": 5
            },

            "batch_size": 256,
            "discount_rate": 0.9,
            "mu": 0.0,  # for O-H noise
            "theta": 0.15,  # for O-H noise
            "sigma": 0.25,  # for O-H noise
            "action_noise_std": 0.2,  # for TD3
            "action_noise_clipping_range": 0.5,  # for TD3
            "update_every_n_steps": 20,
            "learning_updates_per_learning_session": 10,
            "clip_rewards": False,
            "max_lower_level_timesteps": 5
        },

        "HIGHER_LEVEL": {

            "Actor": {
                "learning_rate": 0.001,
                "linear_hidden_units": [20, 20],
                "final_layer_activation": "TANH",
                "batch_norm": False,
                "tau": 0.005,
                "gradient_clipping_norm": 5
            },

            "Critic": {
                "learning_rate": 0.01,
                "linear_hidden_units": [20, 20],
                "final_layer_activation": "None",
                "batch_norm": False,
                "buffer_size": 100000,
                "tau": 0.005,
                "gradient_clipping_norm": 5
            },

            "batch_size": 256,
            "discount_rate": 0.9,
            "mu": 0.0,  # for O-H noise
            "theta": 0.15,  # for O-H noise
            "sigma": 0.25,  # for O-H noise
            "action_noise_std": 0.2,  # for TD3
            "action_noise_clipping_range": 0.5,  # for TD3
            "update_every_n_steps": 20,
            "learning_updates_per_learning_session": 10,
            "clip_rewards": False,
            "max_lower_level_timesteps": 5,
            "number_goal_candidates": 5 # What should this value be?

        }
    },

    # From Long_Corridor.py
    "SNN_HRL": {
        "SKILL_AGENT": {
            "num_skills": 2,
            "regularisation_weight": 1.5,
            "visitations_decay": 0.99,
            "episodes_for_pretraining": 2000,
            # "batch_size": 256,
            # "learning_rate": 0.01,
            # "buffer_size": 40000,
            # "linear_hidden_units": [20, 10],
            # "final_layer_activation": "None",
            # "columns_of_data_to_be_embedded": [0, 1],
            # "embedding_dimensions": [[config.environment.observation_space.n,
            #                           max(4, int(config.environment.observation_space.n / 10.0))],
            #                          [6, 4]],
            # "batch_norm": False,
            # "gradient_clipping_norm": 5,
            # "update_every_n_steps": 1,
            # "epsilon_decay_rate_denominator": 50,
            # "discount_rate": 0.999,
            # "learning_iterations": 1

            "learning_rate": 0.05,
            "linear_hidden_units": [20, 20],
            "final_layer_activation": "SOFTMAX",
            "learning_iterations_per_round": 5,
            "discount_rate": 0.99,
            "batch_norm": False,
            "clip_epsilon": 0.1,
            "episodes_per_learning_round": 4,
            "normalise_rewards": True,
            "gradient_clipping_norm": 7.0,
            "mu": 0.0,  # only required for continuous action games
            "theta": 0.0,  # only required for continuous action games
            "sigma": 0.0,  # only required for continuous action games
            "epsilon_decay_rate_denominator": 1.0
        },

        "MANAGER": {
            "timesteps_before_changing_skill": 4,
            "linear_hidden_units": [10, 5],
            "learning_rate": 0.01,
            "buffer_size": 40000,
            "batch_size": 256,
            "final_layer_activation": "None",
            "columns_of_data_to_be_embedded": [0],
            #"embedding_dimensions": [[config.environment.observation_space.n, #needs to be solved!
            #                          max(4, int(config.environment.observation_space.n / 10.0))]],
            "batch_norm": False,
            "gradient_clipping_norm": 5,
            "update_every_n_steps": 1,
            "epsilon_decay_rate_denominator": 1000,
            "discount_rate": 0.999,
            "learning_iterations": 1

        }
    }
}

config_hyperparameters_reacher_AC = {
    "Actor_Critic_Agents": {
        "Actor": {
            "learning_rate": 0.001,
            "linear_hidden_units": [400, 300],
            "final_layer_activation": "TANH",
            "batch_norm": False,
            "tau": 0.01,
            "gradient_clipping_norm": 5
        },

        "Critic": {
            "learning_rate": 0.01,
            "linear_hidden_units": [400, 300],
            "final_layer_activation": "None",
            "batch_norm": False,
            "buffer_size": 100000,
            "tau": 0.01,
            "gradient_clipping_norm": 5
        },

        "batch_size": 64,
        "discount_rate": 0.99,
        "mu": 0.0,  # for O-H noise
        "theta": 0.15,  # for O-H noise
        "sigma": 0.2,  # for O-H noise
        "action_noise_std": 0.2,  # for TD3
        "action_noise_clipping_range": 0.5,  # for TD3
        "update_every_n_steps": 1,
        "learning_updates_per_learning_session": 1,
        "clip_rewards": False,
	"automatically_tune_entropy_hyperparameter": True,
	"min_steps_before_learning": 400,
        "entropy_term_weight": None,
        "add_extra_noise": False,
        "do_evaluation_iterations": True
    }
}


def chosen_hyperparameters(env_id, env_type, agent_group):
    # Can use env_type later to refine hyperparameter choices further.
    assert env_type is not None
    default_hypers = copy.deepcopy(config_hyperparameters[agent_group])
    if env_id == "MountainCarContinuous-v0" and agent_group == "Actor_Critic_Agents":
        default_hypers["Actor"]["learning_rate"] = 0.003
        default_hypers["Actor"]["linear_hidden_units"] = [20, 20]
        default_hypers["Critic"]["learning_rate"] = 0.02
        default_hypers["Critic"]["linear_hidden_units"] = [20, 20]
        default_hypers["min_steps_before_learning"] = 1000
        default_hypers["update_every_n_steps"] = 20
        default_hypers["learning_updates_per_learning_session"] = 10
        default_hypers["add_extra_noise"] = True
    elif env_id == "Reacher-v4" and agent_group == "Actor_Critic_Agents":
        default_hypers = copy.deepcopy(config_hyperparameters_reacher_AC[agent_group])
    specific_hypers = default_hypers

    return specific_hypers
