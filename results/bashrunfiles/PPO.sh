#PPO
#MountainCarContinuous
python results/MuJoCo_experiment.py --env_id=MountainCarContinuous-v0 --agent_name=PPO --num_episodes_per_run=2000 \
                                    --wandb --capture_video --seed=1

python results/MuJoCo_experiment.py --env_id=MountainCarContinuous-v0 --agent_name=PPO --num_episodes_per_run=2000 \
                                    --wandb --capture_video --seed=2

python results/MuJoCo_experiment.py --env_id=MountainCarContinuous-v0 --agent_name=PPO --num_episodes_per_run=2000 \
                                    --wandb --capture_video --seed=3