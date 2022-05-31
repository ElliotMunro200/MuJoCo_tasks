"""Defines the runs to be executed by MuJoCo_experiment.py"""

from subprocess import call
import argparse


def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--env_id", type=str, default="Walker2d-v4", help="Environment")
    parser.add_argument("--agent_name", type=str, default="DDPG", help="Agent")
    parser.add_argument("--num_runs", type=int, default=1, help="Number of experiments to perform")
    parser.add_argument("--num_episodes_per_run", type=int, default=10, help="Number of episodes to perform per run")
    parser.add_argument("--wandb", type=bool, default=False, help="Whether to perform WandB logging")
    parser.add_argument("--capture_video", type=bool, default=False, help="Whether to capture a video, send to WandB")
    runs_args = parser.parse_args()
    return runs_args


if __name__ == "__main__":
    args = arguments()
    for run in range(args.num_runs):
        call(["python", "results/MuJoCo_experiment.py",
              f"--env_id={args.env_id}",
              f"--agent_name={args.agent_name}",
              f"--seed={run+1}",
              f"--num_episodes_per_run={args.num_episodes_per_run}",
              f"--wandb={args.wandb}",
              f"--capture_video={args.capture_video}"])
