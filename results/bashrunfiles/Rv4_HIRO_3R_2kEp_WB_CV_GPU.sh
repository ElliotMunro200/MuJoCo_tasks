
#HIRO
python results/MuJoCo_experiment.py --env_id=Reacher-v4 --agent_name=HIRO --num_episodes_per_run=2000 \
                                    --wandb --capture_video --GPU --seed=1

python results/MuJoCo_experiment.py --env_id=Reacher-v4 --agent_name=HIRO --num_episodes_per_run=2000 \
                                    --wandb --capture_video --GPU --seed=2

python results/MuJoCo_experiment.py --env_id=Reacher-v4 --agent_name=HIRO --num_episodes_per_run=2000 \
                                    --wandb --capture_video --GPU --seed=3


