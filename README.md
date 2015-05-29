# unite-bibtex

a BibTeX source for unite.vim

The keys of the selected candidates are inserted at the cursor.

Citations are inserted in pandoc's citation format (e.g. `@SomeKey93; @AnotherKey94`).

It is possible to change to a different citation format (e.g. `\cite{SomeKey93}`) (just tweak `bibtex.vim`).

# Requirements

- [unite.vim](https://github.com/Shougo/unite.vim)
- [bibtexparser](https://bibtexparser.readthedocs.org/en/latest/): A BibTeX parser in Python

# Use

1.  Install [bibtexparser](https://bibtexparser.readthedocs.org/en/latest/): `pip install bibtexparser`
2.  Install [unite.vim](https://github.com/Shougo/unite.vim)
3.  Install this plugin
4.  Set variable `let g:unite_bibtex_bib_file="/path/to/your/bib/file.bib"`
5.  `:Unite bibtex` in vim

# Troubleshooting

You can correct your .bib file with [pybtex](http://pypi.python.org/pypi/pybtex):

```
pip install pybtex
pybtex-convert /path/to/your.bib out.bib
```

# Similar projects

- <https://github.com/termoshtt/unite-bibtex> (same name, but different approach)
