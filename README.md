sigchiproceedings-cookiecutter
====================

A [cookiecutter](https://github.com/audreyr/cookiecutter) for LaTeX documents in the [ACM SIGCHI Proceedings Format](http://sigchi.github.io/Document-Formats/).

Usage
-----
Install [cookiecutter](https://github.com/audreyr/cookiecutter):

    $ pip install cookiecutter

After installing cookiecutter, use the sigchiproceedings-cookiecutter:

    $ cookiecutter https://github.com/seclinch/sigchiproceedings-cookiecutter.git
    
As sigchiproceedings-cookiecutter runs, you will be asked for basic information about your new LaTeX document. You will be prompted for the following information:

- `working_title`: a working title for the paper you're planning to submit to an ACM SIGCHI venue,
- `paper_slug`: a name for the main LaTeX and BibTeX files (without the .tex/.bib extension) and for their containing folder,
- `figures_dir`: a name for the directory that will contain your figures,
- `sections_dir`: a name for the directory that will contain individual LaTeX files for each section of the paper,
- `inputs_dir`: a name for the directory that will contain other inputs to your LaTeX file (e.g. the macros file),
- `version_control`: your preferred version control system, and format for statements in that version control system's ignore file.

License
-------
As a derivation from the [ACM SIGCHI LaTeX template itself](https://github.com/sigchi/Document-Formats), this project is also licensed under the terms of the [GNU General Public License v2.0](/LICENSE).

More information
-------
- If you find an issue with sigchiproceedings-cookiecutter or would like to contribute an enhancement, [file an issue](https://github.com/seclinch/sigchiproceedings-cookiecutter/issues/new) at the sigchiproceedings-cookiecutter GitHub repo.