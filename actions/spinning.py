from actions.subactions.check_fish_catch import is_fish_caught, catch_fish
from actions.subactions.fish_fight import is_hooked, fight_fish
from actions.subactions.cast import is_ready_for_launch, launch_bait, pull_bait
from actions.switch_to_window import switch_to_rf4_window


def start_spinning():
    print("Iniciando o bot...")
    switch_to_rf4_window()

    while True:
        if is_fish_caught():
            catch_fish()

        if is_hooked():
            fight_fish()

        if is_ready_for_launch():
            launch_bait()
            pull_bait()
