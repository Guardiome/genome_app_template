# Omics App Template

An Omics App is a [shareable project](https://github.com/KwatME/spro) that is integrable with [Omics AI](https://guardiome.com).

Omics AI runs an Omics App by `spro run run_omics_app`.

At run time, Omics AI adds these key-value pairs to `project.json`.

```json
{
  "vcf_gz_file_path": "/path/to/sample.vcf.gz"
}
```


## Make an Omics App

### Install Dependencies

[Download git](https://git-scm.com/downloads)

```bash
pip install spro
```

### Make

```bash
spro create -g https://github.com/guardiome/omics_app_template my_omics_app
```

### Run

(to see that it works)

```bash
cd my_omics_app
spro enter
spro build
spro run
```

### [Learn spro](https://github.com/kwatme/spro)

----------------------------------------------------------------------

### Edit

Either:

1) [use `match_g2p.py`](#use-match-g2p.py) by editing `input.g2p` to make `output.g2p`,

2) or [write your own code.](#write-your-own-code)

<br>
#### Use match_g2p.py

To use `match_g2p.py`, edit `input.g2p.tsv`.

* Use the plus strand
  * [This variant is on the plus strand](https://www.snpedia.com/index.php/Rs53576).
  * [This variant is on the minus strand](https://www.snpedia.com/index.php/Rs1051730), so you would use its complement, `G|G` (the genotype on the plus strand).
* Get the genomic locations for variants from [dbSNP](https://www.ncbi.nlm.nih.gov/projects/SNP/) and the genomic locations for genes from [NCBI gene search](https://www.ncbi.nlm.nih.gov/gene/672)

<br>
#### Write your own code

Outputs allowed:

- `output/output.html`
- `output/output.json` (1 level only)
- `ouput/output.g2p.tsv`

In `project.json`

    1) Dont change data file path keys.
    2) Set `command/run_omics_app/` to your entry code file.

<br>
#### Run Your Omics App

```
cd omics_app
spro enter
spro run run_omics_app
```

---------------------------------------------------------------------------

### Make README

Link media from `stuff/` to README if you want. [Here](https://github.com/Kazyra/muscle_type) and [here](https://github.com/yaseenkady/alcohol-skin-flush) are some Omics Apps with cool READMEs.


----------------------------------------------------------------------------------------------

### Share to Omics AI

#### [Add to Github](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/)

#### Share

```
cd omics_app_directory
spro share https://github.com/username/omics_app_repository_name
```


If you have any questions or concerns about publishing your Omics App, email team@guardiome.com.


<br>

Omics App powered by [Guardiome](https://guardiome.com)

<img src="stuff/guardiome_logo.png" width="150" height="150">
