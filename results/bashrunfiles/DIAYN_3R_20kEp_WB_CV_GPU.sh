
#DIAYN
#MountainCarContinuous
python results/MuJoCo_experiment.py --env_id=MountainCarContinuous-v0 --agent_name=DIAYN --num_episodes_per_run=2000 \
                                    --wandb --capture_video --GPU --seed=1

python results/MuJoCo_experiment.py --env_id=MountainCarContinuous-v0 --agent_name=DIAYN --num_episodes_per_run=2000 \
                                    --wandb --capture_video --GPU --seed=2

python results/MuJoCo_experiment.py --env_id=MountainCarContinuous-v0 --agent_name=DIAYN --num_episodes_per_run=2000 \
                                    --wandb --capture_video --GPU --seed=3

#Reacher
python results/MuJoCo_experiment.py --env_id=Reacher-v4 --agent_name=DIAYN --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=1

python results/MuJoCo_experiment.py --env_id=Reacher-v4 --agent_name=DIAYN --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=2

python results/MuJoCo_experiment.py --env_id=Reacher-v4 --agent_name=DIAYN --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=3

#Walker2d
python results/MuJoCo_experiment.py --env_id=Walker2d-v4 --agent_name=DIAYN --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=1

python results/MuJoCo_experiment.py --env_id=Walker2d-v4 --agent_name=DIAYN --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=2

python results/MuJoCo_experiment.py --env_id=Walker2d-v4 --agent_name=DIAYN --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=3

#Hopper
python results/MuJoCo_experiment.py --env_id=Hopper-v4 --agent_name=DIAYN --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=1

python results/MuJoCo_experiment.py --env_id=Hopper-v4 --agent_name=DIAYN --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=2

python results/MuJoCo_experiment.py --env_id=Hopper-v4 --agent_name=DIAYN --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=3

#HalfCheetah
python results/MuJoCo_experiment.py --env_id=HalfCheetah-v4 --agent_name=DIAYN --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=1

python results/MuJoCo_experiment.py --env_id=HalfCheetah-v4 --agent_name=DIAYN --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=2

python results/MuJoCo_experiment.py --env_id=HalfCheetah-v4 --agent_name=DIAYN --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=3

#Ant
python results/MuJoCo_experiment.py --env_id=Ant-v4 --agent_name=DIAYN --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=1

python results/MuJoCo_experiment.py --env_id=Ant-v4 --agent_name=DIAYN --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=2

python results/MuJoCo_experiment.py --env_id=Ant-v4 --agent_name=DIAYN --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=3
