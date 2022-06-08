"""Defines the runs to be executed by MuJoCo_experiment.py"""

from subprocess import call
import argparse


def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--env_id", type=str, default="Walker2d-v4", help="Environment")
    parser.add_argument("--agent_name", type=str, default="DDPG", help="Agent")
    parser.add_argument("--num_runs", type=int, default=1, help="Number of experiments to perform")
    parser.add_argument("--num_episodes_per_run", type=int, default=10, help="Number of episodes to perform per run")
    parser.add_argument("--wandb", action='store_true', help="If to perform WandB logging")
    parser.add_argument("--capture_video", action='store_true', help="If to capture a video, send to WandB")
    parser.add_argument("--use_GPU", action='store_true', help="If to use GPU or not")
    runs_args = parser.parse_args()
    return runs_args


"""In the call to this script from the command line, only specify --wandb, --capture_video, --use_GPU when want True."""

if __name__ == "__main__":
    args = arguments()
    call_list = ["python", "results/MuJoCo_experiment.py",
                 f"--env_id={args.env_id}",
                 f"--agent_name={args.agent_name}",
                 f"--num_episodes_per_run={args.num_episodes_per_run}"]
    if args.wandb:
        call_list.append("--wandb")
    if args.capture_video:
        call_list.append("--capture_video")
    if args.use_GPU:
        call_list.append("--GPU")
    for run in range(args.num_runs):
        call_list.append(f"--seed={run+1}")
        call(call_list)
