<div align="center">
  <img src="stuff/omics_apps_logo.png" width="250">
</div>

<h1 align="center">Omics App Template</h1>

<p align="center">An Omics App is a <a href="https://github.com/KwatME/spro">shareable project</a> that analyzes omics data and is integrable with <a href="https://guardiome.com">Omics AI</a>.</p>

<br>

<h3 align="center"><a href="#get_started">Get Started</a></h3>

<h3 align="center"><a href="#edit_your_omics_app">Edit Your Omics App</a></h3>

<h3 align="center"><a href="#learn_omics_ai_api">Learn Omics AI API</a></h3>

<h3 align="center"><a href="#make_a_readme">Make a README</a></h3>

<h3 align="center"><a href="#publish_to_omics_ai">Publish to Omics AI</a></h3>

<br>
<br>
<br>
<p id="get_started"></p>

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

```bash
cd my_omics_app
spro enter
spro build
spro run run_omics_app
```

#### 4) [Learn spro](https://github.com/kwatme/spro)

This is essential for understanding Omics Apps.

<br>
<br>
<br>
<p id="edit_your_omics_app"></p>

## Edit Your Omics App

<br>

Choose to:

1) [use the template code](#use-the-template-code),

2) or [write your own code.](#write-your-own-code)

<br>

### Use the template code

To use `code/match_g2p.py`, you'll customize `input/input.g2p.tsv`.

`input.g2p.tsv` is basically a genomic lookup table. `match_g2p.py` checks the given vcf for the items in `input.g2p.tsv` and writes any matches it finds to `output.g2p.tsv`.

<br>

#### `input.g2p.tsv`

- `input.g2p.tsv` has 5 required columns: `NAME`, `REGION`, `GENOTYPE`, `PHENOTYPE`, and `SOURCE`.

- For each row in `input.g2p.tsv`, if `match.g2p.py` finds the `GENOTYPE` in the `REGION` of the given vcf, the row is added to `output.g2p.tsv`.


- If there are multiple regions and genotypes like below, they all must be true for the row to be added to `ouput.g2p.tsv`.


| NAME                  | REGION                               | GENOTYPE      | PHENOTYPE | SOURCE  |
| :-------------------- | :----------------------------------- | :------------ | :-------- | :------ |
| WASH7P;TPRXL          | 1:12362-29570;3:14064384-14064385    | MODIFIER;HIGH | True.     | Source. |


- `match.g2p.py` searches for two types of `GENOTYPE`s in `input.g2p.tsv`: [SNPeff putative impact](http://snpeff.sourceforge.net/SnpEff_manual.html) (MODIFIER, MODERATE, or HIGH) and actual genotype (A/T, for example). Checkout the template `input.g2p.tsv`, which  contains all possible uses of `input.g2p.tsv` rows.

<br>

#### Tips
* `REGION`s must be for GRCH38.
* Use the plus strand for variants.
  * [This variant is on the minus strand](https://www.snpedia.com/index.php/Rs1051730), so you would use its complement, `G|G` (the plus strand genotype) to look for normal smoker behavior.

<br>

### Write your own code

Add software your code depends on with `spro install`.

Omics AI expects your code to produce one of the following:

- `output/output.html`
- `output/output.json` (1 level only)
- `ouput/output.g2p.tsv`

In `project.json`

  1. Dont change data file path keys.
  2. Set `command/run_omics_app/` to your entry code file.

<br>

### Run Your Omics App

```
cd omics_app
spro enter
spro run run_omics_app
```

<br>
<br>
<br>
<p id="learn_omics_ai_api"></p>

## Learn Omics AI API

Omics AI runs an Omics App by `spro run run_omics_app`.

At run time, Omics AI adds these key-value pairs to `project.json`.

```json
{
  "vcf_gz_file_path": "/path/to/sample.vcf.gz"
}
```

<br>
<br>
<br>
<p id="make_a_readme"></p>

## Make a README

Link things from `stuff/` to README if you want. [Here](https://github.com/kwatme/muscle_type) and [here](https://github.com/yaseenkady/alcohol-skin-flush) are some Omics Apps with cool READMEs.


<br>
<br>
<br>
<p id="publish_to_omics_ai"></p>

## Publish to Omics AI

1) [Add to Github](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/).

2) Run code below to push changes to Github and create a release with the `version` you set in `project.json`.

```
cd omics_app_directory
spro share https://github.com/username/omics_app_repository_name
```

3) Add your Omics App [here](https://github.com/Guardiome/omics_apps_for_omics_ai/blob/master/omics_apps_for_omics_ai.yaml) and make a pull request. If merged, your Omics App will be available on Omics AI.

<br>
<br>
<br>

Feel free to [create an issue](https://github.com/Guardiome/omics_app_template/issues/new).

<img src="stuff/guardiome_logo.png" width="150" height="150">
