## takakonfig
#
from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

mod = "mod4"
terminal = "foot"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
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
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "v", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod], "m", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "m", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod], "d", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "d", lazy.spawn("fuzzel"), desc="Drun"),
    Key([mod], "s", lazy.spawn("bash /home/takako/.local/bin/screenshot"), desc="Screenshot"),

    Key([mod], "y", lazy.spawn("mpc volume -10"), desc="Mpd volume down"),
    Key([mod], "u", lazy.spawn("mpc prev"), desc="Mpd previous"),
    Key([mod], "0x2b9", lazy.spawn("mpc toggle"), desc="Mpd play-pause"), # I
    Key([mod], "o", lazy.spawn("mpc next"), desc="Mpd next"),
    Key([mod], "p", lazy.spawn("mpc volume +10"), desc="Mpd volume up"), # Ğ
    Key([mod], "0xfc", lazy.spawn("foot ncmpcpp"), desc="Launch mpd client"), # Ü

    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"), desc="Lower audio"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"), desc="Raise audio"),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"), desc="Mute audio"),
    Key([], "XF86AudioMicMute", lazy.spawn("pactl set-source-mute @DEFAULT_SINK@ toggle"), desc="Mute audio"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 20-"), desc="Lower brightness"),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +20"), desc="Raise brightness"),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [Group(i) for i in "12345"]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

# COLORS
color0="#49243e"
color1="#704264"
color2="#bb8493"
color3="#dbafa0"
transparant="#00000000"


layouts = [
    layout.Columns(
        border_focus_stack=[color3, color1],
        border_normal_stack=[color0, color0],
        border_focus=color2,
        border_normal=color0,
        border_width=3,
        border_on_single=False,
        margin=5,
    ),
    layout.Max(margin=5),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="CaskaydiaCove Nerd Font",
    fontsize=20,
    padding=10,
    background=color0
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        #background="#371b30",
        background="#261321",
        wallpaper="~/.config/qtile/background.jpg",
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.CurrentLayout(
                    background=color1,
                    padding=7,
                ),
                widget.GroupBox(
                    highlight_method="block",
                    this_screen_border=color1,
                    this_current_screen_border=color2,
                    block_highlight_text_color=color0,
                    active="#ffffff",
                    inactive=color1,
                    rounded = False,
                    padding=6,
                ),
                widget.Prompt(),
                widget.Mpd2(
                    background=color1,
                    status_format='{play_status} {artist} - {title}',
                    no_connection='',
                    play_states={
                        'pause': '',
                        'play': '',
                        'stop': ''
                    },
                    mouse_buttons={
                        1: 'toggle',
                        2: 'prev',
                        3: 'next',
                    },
                ),
                widget.Spacer(),
                widget.PulseVolume(
                    fmt='Vol: {}',
                    #emoji=True,
                ),
                widget.Wlan(
                    background=color1,
                    update_interval=3,
                    format='{essid} {percent:0.0%}'
                ),
                widget.Battery(
                    notify_below=15,
                    update_interval=3,
                    format='{char}{percent:2.0%} {watt:.2f}W',
                    charge_char="+",
                    discharge_char="",
                    full_char="",
                    low_percentage=0.25,
                    low_foreground="f4d366",
                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                #widget.TextBox("takakako", name="user"),
                widget.StatusNotifier(),
                widget.Systray(),
                widget.Clock(format="%d/%m %a %H:%M", background=color1),
            ],
            32,
            border_width=[6, 5, 1, 5],
            border_color="#00000000"
            #border_color=["ff00ff", "000000", "ff00ff", "000000"]
        ),
        # x11_drag_polling_rate = 60,
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
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=color2,
    border_normal=color1,
    border_width=0,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="Library"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
from libqtile.backend.wayland import InputConfig

wl_input_rules = {
    "*": InputConfig(pointer_accel=-1),
    "type:touchpad": InputConfig(
        accel_profile="flat",
        pointer_accel=0.5,
        scroll_factor=0.1,
        tap=True),
    "type:keyboard": InputConfig(
        kb_layout="tr",
        kb_options="caps:swapescape"),
}

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 12

# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
