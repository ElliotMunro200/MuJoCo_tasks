#MCC
python results/MuJoCo_experiment.py --env_id=MountainCarContinuous-v0 --agent_name=TD3 --num_episodes_per_run=2000 \
                                    --wandb --capture_video --seed=1

python results/MuJoCo_experiment.py --env_id=MountainCarContinuous-v0 --agent_name=TD3 --num_episodes_per_run=2000 \
                                    --wandb --capture_video --seed=2

python results/MuJoCo_experiment.py --env_id=MountainCarContinuous-v0 --agent_name=TD3 --num_episodes_per_run=2000 \
                                    --wandb --capture_video --seed=3

#Reacher
python results/MuJoCo_experiment.py --env_id=Reacher-v4 --agent_name=TD3 --num_episodes_per_run=20000 \
                                    --wandb --capture_video --seed=1

python results/MuJoCo_experiment.py --env_id=Reacher-v4 --agent_name=TD3 --num_episodes_per_run=20000 \
                                    --wandb --capture_video --seed=2

python results/MuJoCo_experiment.py --env_id=Reacher-v4 --agent_name=TD3 --num_episodes_per_run=20000 \
                                    --wandb --capture_video --seed=3

#Hopper
python results/MuJoCo_experiment.py --env_id=Hopper-v4 --agent_name=TD3 --num_episodes_per_run=20000 \
                                    --wandb --capture_video --seed=1

python results/MuJoCo_experiment.py --env_id=Hopper-v4 --agent_name=TD3 --num_episodes_per_run=20000 \
                                    --wandb --capture_video --seed=2

python results/MuJoCo_experiment.py --env_id=Hopper-v4 --agent_name=TD3 --num_episodes_per_run=20000 \
                                    --wandb --capture_video --seed=3
