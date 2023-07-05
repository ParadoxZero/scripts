# Use this script to sync dependent branches
# E.g. when you divide a features into smaller part - A,B,C
# and you don't want to wait for A to be merged before starting B
#
# You finish A in branch_a, then raise the PR. Immediately create branch_b from
# branch_a and start working on B. Then if branch_b is ready, you create a PR
# for branch_b with target as branch_a. Similarly for branch_c.
# When you get a PR comment on branch_a, you can fix it in branch_a and then
# call this script. It will rebase branch_b and branch_c respectively on top of
# the previous branch automatically.
# Once the branches are merged one by one, update the target of the next PR.


branch_list = [
    "branch_a",
    "branch_b",
    "branch_c",
]

import os

def command(command_string):
    if os.system(command_string) != 0:
        raise Exception(f"Command failed: {command_string}")

total_branches = len(branch_list)
try:
    for i, branch in enumerate(branch_list):
        print(f"Syncing ({i+1}/{total_branches}) {branch} ")
        command(f"git checkout {branch}")
        command("git pull")
        if i > 0:
            command(f"git rebase {branch_list[i-1]}")
            command("git push -f")
        else:
            command("git push")
        
        print()
except Exception as e:
        print(f"Failed at Syncing ({i+1}/{total_branches}) {branch}: {e}")
