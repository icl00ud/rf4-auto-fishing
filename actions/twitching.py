import os
from concurrent.futures import ThreadPoolExecutor

import globals
from actions.subactions.cast import launch_bait, pull_bait_twitching
from actions.subactions.check_fish_catch import catch_fish
from actions.subactions.fish_fight import fight_fish
from common.common_functions import (
    is_fish_caught,
    is_hooked,
    is_ready_for_launch,
    release_all_keys,
)
from common.switch_to_window import switch_to_rf4_window


def start_twitching():
    print("Initializing")
    switch_to_rf4_window()

    ready_for_launch_printed = False
    not_ready_for_launch_printed = False

    with ThreadPoolExecutor(max_workers=2) as executor:
        while globals.is_running:
            futures = [
                executor.submit(is_fish_caught),
                executor.submit(is_hooked),
            ]

            results = [f.result() for f in futures]

            if any(results):
                if results[0]:
                    os.system("cls")
                    print("Catching the fish...")
                    catch_fish()
                if results[1]:
                    os.system("cls")
                    print("Fighting with the fish...")
                    fight_fish()
                continue

            if is_ready_for_launch():
                if not ready_for_launch_printed:
                    os.system("cls")
                    print("Equipment ready for launch.")
                    ready_for_launch_printed = True

                launch_bait()
                pull_bait_twitching()
            else:
                pull_bait_twitching()
                if not not_ready_for_launch_printed:
                    os.system("cls")
                    print("Equipment is not ready for launch.")
                    not_ready_for_launch_printed = True

    release_all_keys()
