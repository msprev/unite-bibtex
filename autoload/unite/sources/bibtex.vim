" define source
function! unite#sources#bibtex#define()
    return s:source
endfunction

let s:source = {
\   "name" : "bibtex",
\   "syntax" : "uniteSource__Bibtex",
\   'hooks' : {},
\   "description" : "minimal unite-source",
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

function! s:source.gather_candidates(args, context)
    if !exists('g:unite_bibtex_gathered')
        let l:candidates = []
        python import unitebibtex; unitebibtex.populate_list()
        let g:unite_bibtex_gathered = map(l:candidates,'{
                    \   "word": v:val[1],
                    \   "action__text": "@" . v:val[0],
                    \ }')
    endif
    return g:unite_bibtex_gathered
endfunction

function! s:source.hooks.on_syntax(args, context)
  syntax match uniteSource__Bibtex_Type /\[.\{-}\]$/ contained containedin=uniteSource__Bibtex
  highlight default link uniteSource__Bibtex_Type PreProc
endfunction


