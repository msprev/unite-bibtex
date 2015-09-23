" define source
function! unite#sources#bibtex#define()
    return s:source
endfunction

let s:source = {
\   "name" : "bibtex",
\   "syntax" : "uniteSource__Bibtex",
\   'hooks' : {},
\   "description" : "candidates from bibtex file",
\   "action_table" : {
\       "insert" : {
\           "is_selectable" : 1,
\       },
\   },
\   "default_action" : "insert"
\}

function! s:source.action_table.insert.func(candidates)
    let l:keys = []
    for candidate in a:candidates
        call add(l:keys, candidate.action__text)
    endfor
    call sort(l:keys)
    let l:output = join(l:keys, '; ')
    execute "normal! a" . l:output . "\<esc>"
endfunction

function! s:source.hooks.on_syntax(args, context)
  syntax match uniteSource__Bibtex_Type /\[.\{-}\]$/ contained containedin=uniteSource__Bibtex
  highlight default link uniteSource__Bibtex_Type PreProc
  syntax match uniteSource__Bibtex_Id /@\S\+\ze\s/ contained containedin=uniteSource__Bibtex
  highlight default link uniteSource__Bibtex_Id Constant
endfunction

function! s:source.gather_candidates(args, context)
    " sanity check 1: cache directory is set
    if !exists('g:unite_bibtex_cache_dir')
        echoerr 'No cache directory set, please set "g:unite_bibtex_cache_dir"'
        return []
    endif
    " sanity check 2: bibtex file(s) have been set
    if !exists('b:unite_bibtex_bib_files')
        echoerr 'No bibtex file set for current buffer, please set "b:unite_bibtex_bib_files"'
        return []
    endif
    " gather the candidates
    let l:gathered = []
    python import unitebibtex; unitebibtex.vim_bridge_gather_candidates()
    return l:gathered
endfunction

