![](http://d.pr/i/13kC8+ "screenshot")

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
    The cache directory is set by `g:unite_bibtex_cache_dir`.
    This variable must be set for the source to work.

# Requirements

- [unite][]
- [bibtexparser][]: A BibTeX parser in Python

# Use

1.  Install [bibtexparser][]: `pip2 install bibtexparser`
2.  Install [unite][]
3.  Install this plugin (e.g. via [vim-plug][])
4.  Set variable: `let g:unite_bibtex_bib_files=['/path/to/your/bib/file1.bib']`
5.  Set variable: `let g:unite_bibtex_cache_dir='/path/to/your/temp_dir'`
6.  `:Unite bibtex` in vim
7.  `:messages` to see any errors or warnings from the BibTeX parser

# Variables

The following variables can be set:

- `g:unite_bibtex_bib_files`, `b:unite_bibtex_bib_files` <-- at least 1 of these must be set
- `g:unite_bibtex_cache_dir` <-- must be set
- `b:unite_bibtex_prefix`, if not set assumes `'@'`
- `b:unite_bibtex_postfix`, if not set assumes `''`
- `b:unite_bibtex_separator`, if not set assumes `'; '`

# bibwatch.py

This plugin includes a separate Python executable, `bibwatch`.

bibwatch runs in the background in the terminal and watches for changes to selected BibTeX files.
    Once it detect a change, it updates the corresponding unite-bibtex cache.
    This means your Unite bibtex source in vim will be populated with zero or minimal lag, even for very large BibTeX databases.

bibwatch is in `unite-bibtex/pythonx/core` inside the unite-bibtex plugin.
    Go to this directory in the terminal to run `./bibwatch.py`
    Pass paths to any BibTeX files you want watched.
    Pass your cache directory (as defined in `g:unite_bibtex_cache_dir`) as the value of `--cache`.
    For example:

    ./bibwatch.py /path/to/your/bib/file1.bib /path/to/your/bib/file2.bib --cache /path/to/your/temp_dir

Press Control+C to terminate bibwatch.

# Troubleshooting

You can correct your .bib file with [pybtex](http://pypi.python.org/pypi/pybtex):

```
pip2 install pybtex
pybtex-convert /path/to/your.bib out.bib
```

# Similar projects

- <https://github.com/termoshtt/unite-bibtex> (same name, but completely different program)

# Release notes

-   1.0 (25 September 2015):
    - new: implement bibwatch, separate executable
    - new: implement persistent cache
    - new: support multiple BibTeX files
    - new: support buffer local and global settings
    - new: configuration variables for prefix, postfix, and separator for citations
    - fix: refactor code base
    - fix: update to work with latest version of bibtexparser
    - breaking change: BibTeX files now set with new variable `g:unite_bibtex_bib_files`

 [pandoc]: http://johnmacfarlane.net/pandoc/index.html
 [bibtexparser]: https://bibtexparser.readthedocs.org/en/latest/
 [unite]: https://github.com/Shougo/unite.vim
 [vim-plug]: https://github.com/junegunn/vim-plug
