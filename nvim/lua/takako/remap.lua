vim.g.mapleader = " "
vim.keymap.set("n", "<leader>pv", vim.cmd.Ex)

vim.keymap.set("i", "{<CR>", "{}<Left><CR><Tab><CR><Up><Escape>A")
vim.keymap.set("i", "[<CR>", "[]<Left><CR><Tab><CR><Up><Escape>A")
vim.keymap.set("i", "(<CR>", "()<Left><CR><Tab><CR><Up><Escape>A")

vim.keymap.set("i", "(", "()<Left>")
vim.keymap.set("i", "()", "()")

vim.keymap.set("i", "{", "{}<Left>")
vim.keymap.set("i", "{}", "{}")

vim.keymap.set("i", "[", "[]<Left>")
vim.keymap.set("i", "[]", "[]")

vim.keymap.set("i", "\"", "\"\"<Left>")
vim.keymap.set("i", "\"\"", "\"\"")

vim.keymap.set("i", "<", "<><Left>")
vim.keymap.set("i", "<>", "<>")

vim.keymap.set("i", "'", "''<Left>")
vim.keymap.set("i", "''", "''")
