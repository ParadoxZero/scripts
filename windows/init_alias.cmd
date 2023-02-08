@echo off

REM the script assumed following utilities are available in your PATH -
REM ripgrep -   https://github.com/BurntSushi/ripgrep
REM fzf -       https://github.com/junegunn/fzf
REM rush -      https://github.com/shenwei356/rush
REM Add this script to the PATH and/or set CMD's autorun to run this at startup.


REM set your prefered editor for opening files
set EDITOR=code


REM Alias for effecient fzf  usage
DOSKEY f=fzf -q $*
DOSKEY fc=fzf -q $* $B rush %EDITOR% "{}"
DOSKEY fbranch=git branch $B fzf $B rush git checkout

REM Combine ripgrep with fzf to search and open files in huge codebases
REM 
DOSKEY frg=rg $* $B fzf $B rush %EDITOR% "{}"
DOSKEY rcpp=rg -tcpp $* $B fzf $B rush %EDITOR% "{}"
DOSKEY rjs=rg -tjs $* $B fzf $B rush %EDITOR% "{}"

REM Small git based productivity alias
DOSKEY ls=dir $*
DOSKEY branch=git branch $*
DOSKEY checkout=git checkout $*
DOSKEY status=git status

DOSKEY config_alias=code d:\path\init_alias.bat
