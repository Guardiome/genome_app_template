from gzip import open as gzip_open
from os.path import abspath, dirname, join

from kraft import write_yaml

PROJECT_DIRECTORY_PATH = dirname(dirname(abspath(__file__)))

DATA_DIRECTORY_PATH = join(PROJECT_DIRECTORY_PATH, "data")

PERSON_GENOME_VCF_GZ_FILE_PATH = join(DATA_DIRECTORY_PATH, "person", "genome.vcf.gz")

OUTPUT_DIRECTORY_PATH = join(PROJECT_DIRECTORY_PATH, "output")


def count_variants():
    """
    Counted the number of variants in each chromosome and save the results to
        ../output/output.yaml.
    Arguments:
    Returns:
    """

    with gzip_open(PERSON_GENOME_VCF_GZ_FILE_PATH) as vcf_gz_file:

        chromosome_n_variant = {}

        current_chromosome = None

        for line in vcf_gz_file:

            line = line.decode()

            if not line.startswith("#"):

                chromosome = line.split(sep="\t")[0]

                if current_chromosome is None or current_chromosome != chromosome:

                    current_chromosome = chromosome
                    chromosome_n_variant[current_chromosome] = 0

                else:
                    chromosome_n_variant[current_chromosome] += 1

    styled_chromosome_n_variant = {}

    for chromosome, n_variant in chromosome_n_variant.items():

        styled_chromosome_n_variant[
            "Chromosome {}".format(chromosome)
        ] = "{} variants".format(n_variant)

    output_yaml_file_path = join(OUTPUT_DIRECTORY_PATH, "output.yaml")

    write_yaml(styled_chromosome_n_variant, output_yaml_file_path)

    print(
        f"This Omics App counted the number of variants in each chromosome and output {output_yaml_file_path}."
    )


count_variants()
