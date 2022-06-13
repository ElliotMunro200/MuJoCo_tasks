

python results/MuJoCo_experiment.py --env_id=MountainCarContinuous-v0 --agent_name=PPO --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=1

python results/MuJoCo_experiment.py --env_id=MountainCarContinuous-v0 --agent_name=PPO --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=2

python results/MuJoCo_experiment.py --env_id=MountainCarContinuous-v0 --agent_name=PPO --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=3


