#Reacher
python results/MuJoCo_experiment.py --env_id=Reacher-v4 --agent_name=TD3 --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=1

python results/MuJoCo_experiment.py --env_id=Reacher-v4 --agent_name=TD3 --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=2

python results/MuJoCo_experiment.py --env_id=Reacher-v4 --agent_name=TD3 --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=3

#Hopper
python results/MuJoCo_experiment.py --env_id=Hopper-v4 --agent_name=TD3 --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=1

python results/MuJoCo_experiment.py --env_id=Hopper-v4 --agent_name=TD3 --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=2

python results/MuJoCo_experiment.py --env_id=Hopper-v4 --agent_name=TD3 --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=3
