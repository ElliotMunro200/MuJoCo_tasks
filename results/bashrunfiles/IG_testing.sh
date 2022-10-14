# Ant-v4
# -m cProfile -o results/cProfileDumps/MuJoCoTasks_Antv3_SAC_GPU_1k_1.profile
python  results/MuJoCo_experiment.py --env_id=Ant-v4 --agent_name=IG --num_episodes_per_run=100 --wandb --capture_video --GPU --seed=1
