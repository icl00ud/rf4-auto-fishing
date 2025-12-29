# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

RF4 Auto-Fishing is a Python automation bot for Russian Fishing 4 game. It uses computer vision (template matching) to detect game states and automates fishing mechanics through keyboard/mouse control.

## Running the Project

```bash
# Install dependencies
pip install -r requirements.txt

# Run the bot
python main.py
```

**Hotkeys:**
- F3 - Start Spinning mode
- F4 - Start Twitching mode
- F8 - Stop the bot

## Architecture

### Entry Point
- `main.py` - Keyboard listener that spawns fishing mode threads

### Fishing Modes (`actions/`)
- `spinning.py` - Continuous loop for spinning fishing: check hunger -> catch -> fight -> cast -> pull
- `twitching.py` - Similar to spinning but uses ThreadPoolExecutor for parallel state checking and rapid left/right click pattern

### Subactions (`actions/subactions/`)
- `cast.py` - Bait launching (Shift+left click) and pulling mechanics
- `check_fish_catch.py` - Fish capture confirmation and trophy screenshot saving
- `fish_fight.py` - Fish fighting (hold both mouse buttons + Shift)

### Common Utilities (`common/`)
- `common_functions.py` - Image recognition using `pyautogui.locateOnScreen()` with 0.8 confidence; state detection functions (`is_fish_caught`, `is_ready_for_launch`, `is_hooked`, `is_hungry`); `eat()` function for hunger management
- `switch_to_window.py` - Game window detection and focus management; sets global `region` for screen capture bounds

### Global State
- `globals.py` - Contains `region` variable storing game window coordinates `(left, top, width, height)`

### Template Images (`screenshots/`)
Pre-captured PNG templates of game UI elements used for state detection:
- `fish-catched-*.png` - Fish caught indicators
- `ready-for-launch-*.png` - Equipment ready state
- `fish-in-line.png` - Fish hooked indicator
- `hungry.png`, `bread.png` - Hunger management
- `trophy.png` - Trophy fish detection

## Key Implementation Details

- All automation is vision-based using template matching against the `screenshots/` directory
- The `region` global restricts image search to game window bounds for performance
- State detection functions return boolean based on template matches at 0.8 confidence threshold
- Twitching mode uses concurrent futures for parallel state checking
- Trophy screenshots are saved to `~/Downloads/Russian Fishing 4`
