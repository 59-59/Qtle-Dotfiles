from libqtile.utils import guess_terminal
from libqtile.config import Key
from libqtile.lazy import lazy

#Keys
mod = 'mod4'
alt = 'mod1'

terminal = guess_terminal()

keys = [

    #Displacement
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([alt], "Tab", lazy.layout.next(), desc="Move window focus to other window"),

    #Changing the location of windows
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    #Fit size
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "f", lazy.window.toggle_floating(), desc="Reset all window sizes & change type off windows"),
    
    #Qtile Config
    Key([mod, "shift"],"Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    #Rofi
    Key([mod], "d", lazy.spawn("launcher.sh")),
    
    #Lockscreen
    Key([mod], "l", lazy.spawn("dm-tool switch-to-greeter")),

    #Audio
    Key([], "f10", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")), #Boton
    Key([], "f11", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")), #Boton
    Key([], "f9", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([], "f8", lazy.spawn("playerctl next")),
    Key([], "f6", lazy.spawn("playerctl previous")),
    Key([], "f7", lazy.spawn("playerctl play-pause")),
    
    #Screenshot
    Key([], "Print", lazy.spawn("flameshot gui")),
    Key([mod, "shift"] , "s" , lazy.spawn("flameshot gui")),
    
    #terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
]
