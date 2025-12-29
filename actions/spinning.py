import globals
from actions.subactions.cast import launch_bait, pull_bait_spinning
from actions.subactions.check_fish_catch import catch_fish
from actions.subactions.fish_fight import fight_fish
from common.common_functions import (
    eat,
    is_fish_caught,
    is_hooked,
    is_hungry,
    is_ready_for_launch,
    release_all_keys,
)
from common.switch_to_window import switch_to_rf4_window


def start_spinning():
    print("Initializing...")
    switch_to_rf4_window()

    ready_for_launch_printed = False
    not_ready_for_launch_printed = False

    while globals.is_running:
        if is_hungry():
            eat()

        if is_fish_caught():
            catch_fish()

        if is_hooked():
            fight_fish()

        if is_ready_for_launch():
            if not ready_for_launch_printed:
                print("Equipment ready for launch.")
                ready_for_launch_printed = True

            launch_bait()
            pull_bait_spinning()
        else:
            pull_bait_spinning()
            if not not_ready_for_launch_printed:
                print("Equipment is not ready for launch.")
                not_ready_for_launch_printed = True

    release_all_keys()
