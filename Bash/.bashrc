#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

#starship prompt
eval "$(starship init bash)"

#aliases
alias c="clear"
alias g="cd ~/Git && echo 'moving to ~/Git' && ls"
alias h="cd ~ && echo 'moving to ~' && ls"
alias conf="cd ~/.config && echo 'moving to ~/.config' && ls"
alias sleep="systemctl suspend"
alias sp="systemctl suspend"
alias sd="shutdown -h now"
alias hibernate="systemctl hibernate"
alias hb="systemctl hibernate"
alias randombg="feh --bg-scale --no-fehbg --randomize ~/Documents/Wallpapers"

#run programs
pfetch
