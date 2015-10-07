Linux & Python Notes
=========

##### General Notes
  + Suck less at vim
    + run the vimtutor command
    + Visit `http://vim-adventures.com/`
    + Practice


##### Getting started

+ Install babun
  + `http://babun.github.io/`
+ Adjust your prompt
  + `https://www.kirsle.net/wizards/ps1.html`
    + Skip this step for babun, default is fine for now
+ Create an alias or function for ports_pact
  + in babun, edit `~/.zshrc`
    + In windows, this can be found in %userprofile%\.babun\cygwin\home\%USER%\.zshrc
  + Fix the `ll` alias, set it to `alias ll='ls -lahF'`
  + Add a ports_pact alias, set it to `alias ports_pact='pact --mirror "http://mirrors.kernel.org/sources.redhat.com/cygwinports/"'`


##### Setup easy ssh login for freemont

  The following is all done in a babun shell

  + execute `ssh-keygen`
    + spam enter to accept all defaults
  + edit ``~/.ssh/config`:

  ```
  Host freemont
    HostName freemont.binarybeast.com
    User aquiyu
  ```

  + Deploy the key to allow password-less access by executing `ssh-copy-id freemont`
    + Remember that `freemont` now refers to the entry in your config, which expands to the full URL

##### Basic linux commands
+ List files / directories
  + `ls`
  + `ls -lahF`: Readable format + show hidden
+ Move around
  + `cd`: Change directory
  + `cd ~`: Move to your home directory
+ Get current working directory
  + `pwd`
+ Create / Delete directories
  + `mkdir _dirname_`
  + `rmdir _dirname`
    + Only works if the directory is empty, otherwise run `rm _dirname_ -rf`

##### Linux Aliases

Aliases allow you to define a pseudo-command that expands into a pre-defined command and arguments

+ Create an Aliases
  + `alias _aliasname_='command + args+'`
    + Example: `alias ll='ls-lahF'`
+ To view existing Aliases
  + `alias` - derp


  ##### tmux

  Tmux is a session manager, it allows pane splitting, session dettachment / re-attachment, sharing, and more

  + Launch a share-able session: `tmux start-session -s _session_name`
  + Join a session `tmux attach-session -t _session_name_`
  + Launch a private tmux: `tmux`
  + List tmux sessions running under your user: `tmux ls`
  + Dettach a session: `ctrl+b [let go] d`
