
#SAC
#Ant-v3
python -m cProfile -o results/cProfileDumps/MuJoCoTasks_Antv3_SAC_GPU_1k_1.profile results/MuJoCo_experiment.py --env_id=Ant-v3 --agent_name=SAC --num_episodes_per_run=20000 --wandb --GPU --seed=1

python -m cProfile -o results/cProfileDumps/MuJoCoTasks_Antv3_SAC_GPU_1k_2.profile results/MuJoCo_experiment.py --env_id=Ant-v3 --agent_name=SAC --num_episodes_per_run=20000 --wandb --GPU --seed=2
