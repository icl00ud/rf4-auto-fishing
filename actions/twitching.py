from actions.subactions.check_fish_catch import catch_fish
from actions.subactions.cast import launch_bait, pull_bait_twitching
from actions.subactions.fish_fight import fight_fish
from common.switch_to_window import switch_to_rf4_window
from common.common_functions import eat, is_fish_caught, is_hooked, is_hungry, is_ready_for_launch
from concurrent.futures import ThreadPoolExecutor

def start_twitching():
    print("Iniciando o bot...")
    switch_to_rf4_window()

    ready_for_launch_printed = False
    not_ready_for_launch_printed = False

    while True:
        with ThreadPoolExecutor() as executor:
            futures = [
                executor.submit(is_fish_caught),
                executor.submit(is_hooked),
            ]

            results = [f.result() for f in futures]

            if any(results):
                if results[0]:
                    print("Capturando peixe...")
                    catch_fish()
                if results[1]:
                    print("Puxando peixe...")
                    fight_fish()
                continue

        if is_ready_for_launch():
            if not ready_for_launch_printed:
                print("Equipamento pronto para lançamento.")
                ready_for_launch_printed = True
                
            launch_bait()
            pull_bait_twitching()
        else:
            pull_bait_twitching()
            if not not_ready_for_launch_printed:
                print("Equipamento não está pronto para lançamento.")
                not_ready_for_launch_printed = True
