# unite-bibtex

A BibTeX source for unite.vim

The keys of the selected candidates are inserted at the cursor.

BibTeX files are listed in the variable `g:unite_bibtex_bib_files`.
    The buffer-specific variable `b:unite_bibtex_bib_files` overrides this.
    Multiple BibTeX files can be passed to both.

Citations are by default inserted in [pandoc][]'s citation format (e.g. `@SomeKey93; @AnotherKey94`).
You can change this, on a per buffer basis, by setting the variables:

- `let b:unite_bibtex_prefix = '\citet{`
- `let b:unite_bibtex_postfix = '}`
- `let b:unite_bibtex_separator = ', '`


Parsing BibTeX databases is computationally intensive, so the source caches the results.
    The cache is updated if the underlying BibTeX file has been changed.
    The cache directory is set by `b:unite_bibtex_cache_dir`.
    This variable must be set for the source to work.

# Requirements

- [unite][]
- [bibtexparser][]: A BibTeX parser in Python

# Use

1.  Install [bibtexparser][]: `pip install bibtexparser`
2.  Install [unite][]
3.  Install this plugin (e.g. via [vim-plug][])
4.  Set variable `let g:unite_bibtex_bib_files=["/path/to/your/bib/file1.bib"]`
5.  Set variable `let g:unite_bibtex_cache_dir="/path/to/your/temp_dir"`
6.  `:Unite bibtex` in vim

# Variables

The following variables can be set, shown with their default settings where applicable:

- `g:unite_bibtex_bib_files`
- `b:unite_bibtex_bib_files`
- `g:unite_bibtex_cache_dir`
- `b:unite_bibtex_prefix = '@'`
- `b:unite_bibtex_postfix = ' '`
- `b:unite_bibtex_separator = '; '`

# Troubleshooting

You can correct your .bib file with [pybtex](http://pypi.python.org/pypi/pybtex):

```
pip install pybtex
pybtex-convert /path/to/your.bib out.bib
```

# Similar projects

- <https://github.com/termoshtt/unite-bibtex> (same name, but completely different program)

# Release notes

-   1.0 (25 September 2015):
    - new: implement persistent cache
    - new: support multiple BibTex files
    - new: support buffer local and global settings
    - new: configuration variables for prefix, postfix, and separator for citations
    - fix: refactor code base
    - fix: update to work with latest version of bibtexparser
    - breaking change: BibTeX files now set with new variable `g:unite_bibtex_bib_files`

 [pandoc]: http://johnmacfarlane.net/pandoc/index.html
 [bibtexparser]: https://bibtexparser.readthedocs.org/en/latest/
 [unite]: https://github.com/Shougo/unite.vim
 [vim-plug]: https://github.com/junegunn/vim-plug
