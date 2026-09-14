# Source this in interactive zsh so the selected SSH command enters its history.
ssh-fzf() {
    emulate -L zsh
    if [[ "$1" == --clip || "$1" == -c || "$1" == --print-target ]]; then
        command ssh-fzf "$@"
        return $?
    fi

    local target
    target=$(command ssh-fzf --print-target) || return $?
    [[ -n "$target" ]] || return 1

    # Quote the destination so recalling the command reproduces the same argument.
    print -s -- "ssh ${(q)target}"
    print -r -- "running ssh $target"
    ssh "$target"
}
