# Copyright (c) Facebook, Inc. and its affiliates.
from nle.minihack import MiniHack


class MiniHackSkill(MiniHack):
    """Base environment skill acquisition tasks."""

    def __init__(
        self,
        *args,
        des_file,
        reward_manager=None,
        **kwargs,
    ):
        """If reward_manager == None, the goal is to reach the staircase."""
        kwargs["options"] = kwargs.pop("options", [])
        kwargs["options"].append("pettype:none")
        kwargs["options"].append("!autopickup")
        kwargs["perform_menu_steps"] = kwargs.pop("perform_known_steps", True)
        kwargs["character"] = kwargs.pop("character", "cav-hum-new-mal")
        kwargs["max_episode_steps"] = kwargs.pop("max_episode_steps", 250)
        self._no_rand_mon()

        default_keys = [
            "chars_crop",
            "colors_crop",
            "screen_descriptions_crop",
            "message",
            "inv_strs",
            "inv_letters",
        ]

        kwargs["observation_keys"] = kwargs.pop("observation_keys", default_keys)
        super().__init__(
            *args, des_file=des_file, reward_manager=reward_manager, **kwargs
        )
