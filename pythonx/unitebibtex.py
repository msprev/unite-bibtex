import vim
from core import gather

def vim_bridge_gather_candidates():
    """
    Mimimal bridge function between vim and python code
    Keep this small to help with debugging
    """
    # 1. Get values from vim
    bib_files = vim.eval('b:unite_bibtex_bib_files')
    cache_dir = str(vim.eval('g:unite_bibtex_cache_dir'))
    prefix = vim.eval('l:prefix')
    postfix = vim.eval('l:postfix')
    # 2. Gather candidates
    gathered = gather.candidates(bib_files, cache_dir)
    # 3. Make commands to transmit candidates back to vim
    vim_cmds = gather.make_vim_commands(gathered, 'l:gathered', prefix, postfix)
    # 4. Send candidates back to vim
    for cmd in vim_cmds:
        vim.command(cmd)
