# Copyright (c) Facebook, Inc. and its affiliates.

from nle.minihack import MiniHack
from nle import nethack


MOVE_ACTIONS = tuple(nethack.CompassDirection)


class MiniHackNavigation(MiniHack):
    """Base class for maze-type task.

    Maze environments have
    - Restricted action space (move only by default)
    - No pet
    - One-letter menu questions are NOT allowed by default
    - Restricted observations, only glyphs by default
    - No random monster generation

    The goal is to reach the staircase.
    """

    def __init__(self, *args, des_file: str = None, **kwargs):
        # No pet
        kwargs["options"] = kwargs.pop("options", list(nethack.NETHACKOPTIONS))
        kwargs["options"].append("pettype:none")
        # Actions space - move only
        kwargs["actions"] = kwargs.pop("actions", MOVE_ACTIONS)
        # Disallowing one-letter menu questions
        kwargs["allow_all_yn_questions"] = kwargs.pop("allow_all_yn_questions", False)
        # Perform know steps
        kwargs["perform_menu_steps"] = kwargs.pop("perform_known_steps", True)
        # Play with Rogue character
        kwargs["character"] = kwargs.pop("character", "rog-hum-cha-mal")
        # Override episode limit
        kwargs["max_episode_steps"] = kwargs.pop("max_episode_steps", 100)
        # Restrict the observation space to chars only
        kwargs["observation_keys"] = kwargs.pop(
            "observation_keys", ["chars_crop", "colors_crop"]
        )
        # No random monster generation after every timestep
        self._no_rand_mon()

        super().__init__(*args, des_file=des_file, **kwargs)
