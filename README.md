<img src="stuff/omics_apps_logo.png" align="center" width="200">

<h1 align="center">Omics App Template</h1>

<p align="center">An Omics App is a <a href="https://github.com/KwatME/spro">shareable project</a> that analyzes omics data and is integrable with <a href="https://guardiome.com">Omics AI</a>.</p>

<br>

<h4 align="center"><a href="#omics-ai-api">Omics AI API</a></h4>
<h4 align="center"><a href="#get-started">Get Started</a></h4>
<p align="center">[Edit Your Omics App](#edit-your-omics-app)</p>
<p align="center">[Make a README](#make-a-readme)</p>
<p align="center">[Publish to Omics AI](#publish-to-omics-ai)</p>

<br>

## Omics AI API

Omics AI runs an Omics App by `spro run run_omics_app`.

At run time, Omics AI adds these key-value pairs to `project.json`.

```json
{
  "vcf_gz_file_path": "/path/to/sample.vcf.gz"
}
```

<br>

## Get Started

#### 1) Install Dependencies

[Download git](https://git-scm.com/downloads)

```bash
pip install spro
```

#### 2) Create an Omics App

```bash
spro create -g https://github.com/guardiome/omics_app_template my_omics_app
```

#### 3) Run it

(to see that it works)

```bash
cd my_omics_app
spro enter
spro build
spro run
```

#### 4) [Learn spro](https://github.com/kwatme/spro)

<br>

## Edit Your Omics App

Choose to:

1) [use match_g2p.py](#use-match_g2p.py) (the template code),

2) or [write your own code.](#write-your-own-code)

<br>

### Use match_g2p.py

To use `match_g2p.py`, edit `input.g2p.tsv`.

* Use the plus strand
  * [This variant is on the plus strand](https://www.snpedia.com/index.php/Rs53576).
  * [This variant is on the minus strand](https://www.snpedia.com/index.php/Rs1051730), so you would use its complement, `G|G` (the genotype on the plus strand).
* Get the genomic locations for variants from [dbSNP](https://www.ncbi.nlm.nih.gov/projects/SNP/) and the genomic locations for genes from [NCBI gene search](https://www.ncbi.nlm.nih.gov/gene/672)

<br>

### Write your own code

Outputs allowed (Omics AI will show any of these):

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

<br>

## Make a README

Link media from `stuff/` to README if you want. [Here](https://github.com/Kazyra/muscle_type) and [here](https://github.com/yaseenkady/alcohol-skin-flush) are some Omics Apps with cool READMEs.


<br>

## Publish to Omics AI

1) [Add to Github](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/).

2) Run code below to push changes to Github and create a release with the `version` you set in `project.json`.

```
cd omics_app_directory
spro share https://github.com/username/omics_app_repository_name
```

3) Add your Omics App [here](https://github.com/Guardiome/omics_apps_for_omics_ai/blob/master/omics_apps_for_omics_ai.yaml) and make a pull request. If merged, your Omics App will be available on Omics AI.

<br>

Email questions to team@guardiome.com.

<img src="stuff/guardiome_logo.png" width="150" height="150">
