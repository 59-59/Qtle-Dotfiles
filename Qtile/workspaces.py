from libqtile.config import Key
from libqtile.config import Group
from libqtile.lazy import lazy

from keys import keys

#Keys
mod = 'mod4'
alt = 'mod1'

groups = [Group(f"{i+1}", label="") for i in range(6)]

for i in groups:
    keys.extend(
            [
                Key(
                    [mod],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    desc="Switch to group {}".format(i.name),
                    ),
                Key(
                    [mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name),
                    desc="Move focused window to group {}".format(i.name),
                    ),
                ]
            )
