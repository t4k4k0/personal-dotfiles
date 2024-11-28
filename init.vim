filetype plugin on
filetype indent on

let $LANG='en'
set langmenu=en

set number
set relativenumber
set so=3

set wildmenu
set wildignore=*.o

syntax enable
set background=dark

set nobackup
set nowb
set noswapfile
set expandtab
set smarttab
set shiftwidth=2
set tabstop=2

set ai
set si

let mapleader = " "
nmap <leader>pv = :Ex<CR>

inoremap { {}<Left>
inoremap {} {}
inoremap ( ()<Left>
inoremap () ()
inoremap [ []<Left>
inoremap [] []
inoremap " ""<Left>
inoremap "" ""
inoremap ' ''<Left>
inoremap '' ''
inoremap ` ``<Left>
inoremap `` ``

inoremap {<CR> {<CR>}<Esc>O
inoremap [<CR> [<CR>]<Esc>O
inoremap (<CR> (<CR>)<Esc>O

colo retrobox
