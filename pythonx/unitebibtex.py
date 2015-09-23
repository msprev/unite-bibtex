import vim
import gather

def vim_bridge_gather_candidates():
    """
    Mimimal bridge function between vim and python code
    Keep this small to help with debugging
    """
    # 1. Get values from vim
    cache_dir = str(vim.eval('g:unite_bibtex_cache_dir'))
    bib_files = vim.eval('b:unite_bibtex_bib_files')
    # 2. Gather candidates
    gathered = gather.candidates(cache_dir, bib_files)
    # 3. Send results back to vim
    vim.command('let l:gathered = %s' % gathered)

