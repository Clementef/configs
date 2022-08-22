from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import extension

mod = "mod4"
terminal = "alacritty"
browser="qutebrowser"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "x", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod], "z", lazy.layout.previous(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "space", lazy.spawn("rofi -show drun"), desc="Launch Rofi"),
    Key([mod], "b", lazy.spawn("brave"), desc="Launch Brave"),
]

groups = [Group(i) for i in "sdf"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
#            Key(
#                [mod, "shift"],
#                i.name,
#                lazy.window.togroup(i.name, switch_group=True),
#                desc="Switch to & move focused window to group {}".format(i.name),
#            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
             Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
                 desc="move focused window to group {}".format(i.name)),
        ]
    )

_cols={
        "bg":"#282a36",
        "fg":"#f8f8f2",
        "hl":"#bd93f9",
        "alt":"#44475a"
}

layout_theme = {
        "border_width":2,
        "margin":8,
        "border_focus":_cols["hl"],
        "border_normal":_cols["alt"]
}

layouts =[
    layout.MonadTall(name="tall",**layout_theme),
    layout.Max(name="max",**layout_theme),
]

widget_defaults = dict(
    font="Fira Code",
    fontsize=17,
    padding=10,
    foreground=_cols["fg"],
    background=_cols["bg"]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.Prompt(),
                widget.GroupBox(
                    highlight_method='line',
                    borderwidth=2,
                    margin_y=3,
                    margin_x=3,
                    padding_x=5,
                    padding_y=10,
                    rounded=False,
                    this_current_screen_border=_cols["hl"],
                    this_screen_border=_cols["hl"],
                    other_current_screen_border=_cols["alt"],
                    other_screen_border=_cols["alt"],
                    inactive=_cols["alt"],
                    active=_cols["fg"],
                    highlight_color=_cols["bg"],
                   ),
                widget.Sep(),
#                widget.WindowName(),
#                widget.Chord(
#                    chords_colors={
#                        "launch": (_cols["bg"],_cols["bg"])
#                    },
#                    name_transform=lambda name: name.upper(),
#                ),
                widget.WindowTabs(),
                widget.Spacer(),
                widget.Volume(fmt="Vol:{}"),
#                widget.Battery(
#                        format="{percent:2.0%} {char} ({hour:d}:{min:02d})", 
#                        discharge_char="v", 
#                        charge_char="^", 
#                        update_interval=5),
#                widget.Sep(),
#                widget.Wlan(disconnected_message="disconnected"),
#                widget.CurrentLayout(),
#                widget.Sep(),
                widget.Clock(format="%a %I:%M"),
                widget.Clock(format="%m/%d/%y"),
                widget.QuickExit(countdown_start=1,
                                 default_text='[Exit]',
                                 countdown_format='[Exit]'),
            ],
            24,
            border_width=[3, 0, 3, 0],  # Draw top and bottom borders
            border_color=[_cols["bg"],_cols["bg"],_cols["bg"],_cols["bg"]]# Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
