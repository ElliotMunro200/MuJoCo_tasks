
#SAC
#Reacher
python results/MuJoCo_experiment.py --env_id=Reacher-v4 --agent_name=SAC --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=1

python results/MuJoCo_experiment.py --env_id=Reacher-v4 --agent_name=SAC --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=2

python results/MuJoCo_experiment.py --env_id=Reacher-v4 --agent_name=SAC --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=3

#Hopper
python results/MuJoCo_experiment.py --env_id=Hopper-v4 --agent_name=SAC --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=1

python results/MuJoCo_experiment.py --env_id=Hopper-v4 --agent_name=SAC --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=2

python results/MuJoCo_experiment.py --env_id=Hopper-v4 --agent_name=SAC --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=3

#Walker2d
python results/MuJoCo_experiment.py --env_id=Walker2d-v4 --agent_name=SAC --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=1

python results/MuJoCo_experiment.py --env_id=Walker2d-v4 --agent_name=SAC --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=2

python results/MuJoCo_experiment.py --env_id=Walker2d-v4 --agent_name=SAC --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=3

#TD3
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

#Walker2d
python results/MuJoCo_experiment.py --env_id=Walker2d-v4 --agent_name=TD3 --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=1

python results/MuJoCo_experiment.py --env_id=Walker2d-v4 --agent_name=TD3 --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=2

python results/MuJoCo_experiment.py --env_id=Walker2d-v4 --agent_name=TD3 --num_episodes_per_run=20000 \
                                    --wandb --capture_video --GPU --seed=3
