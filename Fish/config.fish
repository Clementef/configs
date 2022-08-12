#RESET PATH
set -e fish_user_paths
set -U fish_user_paths $HOME/.local/bin $HOME/Applications $fish_user_path

#UNIVERSAL VARS
set -Ux PF_ASCII "Dragonfly"
set -Ux PF_COL1 4 #info names
set -Ux PF_COL3 5 #title data
set -Ux PF_COL2 9 #title data
set -Ux PF_INFO "ascii title os host kernel shell memory palette"
set -Ux TERM alacritty

#CLEAR GREETING
set fish_greeting

#SET VI BINDINGS
function fish_user_key_bindings
 fish_vi_key_bindings
end

#ON STARTUP
if status is-interactive
    # Commands to run in interactive sessions can go here
    alias config="vim ~/.config/fish/config.fish"
    alias config_starship="vim ~/.config/starship.toml"
    alias config_alacritty="vim ~/.config/alacritty/alacritty.yml"
    alias config_vim="vim ~/.vimrc"
    alias f="vifm --select ./"
    alias c="clear"
    alias py="python3" 
    alias qute="/Applications/qutebrowser.app/Contents/MacOS/qutebrowser"
    alias q="/Applications/qutebrowser.app/Contents/MacOS/qutebrowser"
    alias godesk="cd ~/Desktop/"
    alias gogit="cd ~/Git/"
    alias goconfig="cd ~/.config"
    alias godoc="cd ~/Documents/"
    alias godown="cd ~/Downloads/"
    alias gopics="cd ~/Pictures/"
    alias o="open"
    alias p="pfetch"
    alias v="vim"
    alias pico="/Applications/PICO-8.app/Contents/MacOS/pico8 -run"
    pfetch
end

#SET STARSHIP PROMPT
starship init fish | source
