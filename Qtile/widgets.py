from libqtile import bar, layout, widget
from libqtile.config import Screen
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

#Mouse callbacks
def rofi(qtile):
    qtile.cmd_spawn('rofi')

#Qtile extras  
powerline = {
    "decorations": [
        PowerLineDecoration(path="forward_slash")
        #path='arrow_right'
    ]
}
    
#colors
C_color3 = '#353c4a'    
C_color4 = '#54546D'    
C_color5 = '#363646'    
C_color6 = '#ffffff'    
c_black = '#000000'
c_white = '#ffffff'

layout_conf = {
    'border_focus':[C_color4, C_color4],
    'border_width': 1,
    'margin': 10
}

layout_conf2 = {
    'border_focus':[c_black, c_black],
    'border_width': 1,
    'margin': 10
}

layouts = [
    layout.Max(**layout_conf2),
    layout.MonadTall(**layout_conf),
    layout.MonadWide(**layout_conf),
]

widget_defaults = dict(
    font="UbuntuMono Nerd Font",
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [   
                widget.TextBox(
                    fmt='󰄉 ',
                    foreground=[c_white, c_white],
                    fontsize=27,
                    padding=10,
                    mouse_callbacks={'Button1': lazy.function(rofi)}
                ),
                widget.GroupBox(
                    foreground=[c_white, c_white],
                    backeground=[c_black, c_black],
                    font='UbuntuMono Nerd Font',
                    fontsize=16,
                    margin_y=4,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=2,
                    inactive=[c_black, c_black],
                    active=[C_color4, C_color4],
                    rounded=False,
                    highlight_method='text',
                    urgent_alert_method='text',
                    urgent_border=[c_white, c_white],
                    this_current_screen_border=[c_white, c_white],
                    this_screen_border=[c_white, c_white],
                    other_current_screen_border=[c_black, c_black],
                    other_screen_border=[c_black, c_black],
                    disable_drag=True
                ),
                widget.WindowName(
                    foreground=[c_black, c_black],
                    background=[c_black, c_black],
                    padding=10000,
                    **powerline
                ),
                widget.CheckUpdates(
                    distro = "Arch_checkupdates",
                    update_interval= 60,
                    display_format= '󱧘 ',
                    foreground=[C_color6, C_color6],
                    background=[C_color4, C_color4],
                    no_update_string= ' ',
                    fontsize = 16,
                    colour_no_updates=[C_color6, C_color6],
                    colour_have_updates=[C_color6, C_color6],
                    padding=5,
                    **powerline
                ),
                widget.Net(
                    prefix='M',
                    format='󰕡  {down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}',
                    foreground=[C_color6, C_color6],
                    background=[C_color5, C_color5],
                    padding=10,
                    **powerline
                ),
                 widget.Memory(
                    measure_mem='G',
                    foreground=[C_color6, C_color6],
                    background=[C_color4, C_color4],
                    format=' {MemUsed: .1f}G /{MemTotal: .1f}G',
                    padding=10,
                    **powerline
                ),
                widget.CPU(
                    format='  {load_percent}%',
                    foreground=[C_color6, C_color6],
                    background=[C_color5, C_color5],
                    padding=10,
                    **powerline
                ),
                widget.Clock(
                    foreground=[C_color6, C_color6],
                    background=[C_color4, C_color4],
                    format=" %I:%M - %d %h",
                    padding=10,
                    **powerline
                ),
                 widget.Systray(
                    **powerline
                ),
            ],
            26,
            margin=10,
        ),
    ),
]
