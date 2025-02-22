
#MCC-v0 across algos (non-GPU)
#DIAYN
python results/MuJoCo_experiment.py --env_id=MountainCarContinuous-v0 --agent_name=DIAYN --num_episodes_per_run=2000 \
                                    --wandb --capture_video --seed=1

python results/MuJoCo_experiment.py --env_id=MountainCarContinuous-v0 --agent_name=DIAYN --num_episodes_per_run=2000 \
                                    --wandb --capture_video --seed=2

python results/MuJoCo_experiment.py --env_id=MountainCarContinuous-v0 --agent_name=DIAYN --num_episodes_per_run=2000 \
                                    --wandb --capture_video --seed=3


#HIRO
python results/MuJoCo_experiment.py --env_id=MountainCarContinuous-v0 --agent_name=HIRO --num_episodes_per_run=20000 \
                                    --wandb --capture_video --seed=1

python results/MuJoCo_experiment.py --env_id=MountainCarContinuous-v0 --agent_name=HIRO --num_episodes_per_run=20000 \
                                    --wandb --capture_video --seed=2

python results/MuJoCo_experiment.py --env_id=MountainCarContinuous-v0 --agent_name=HIRO --num_episodes_per_run=20000 \
                                    --wandb --capture_video --seed=3


