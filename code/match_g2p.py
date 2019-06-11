from os.path import abspath, dirname, exists, join

from pandas import read_csv

from kraft import (
    get_sequence_from_fasta_or_fasta_gz,
    get_variants_from_vcf_or_vcf_gz,
    get_vcf_genotype,
    get_vcf_info_ann,
    get_vcf_sample_format,
    normalize_path,
    read_json,
)

project_directory_path = dirname(dirname(abspath(__file__)))

input_directory_path = join(project_directory_path, "input")

input_g2p_tsv_file_path = join(input_directory_path, "input.g2p.tsv")

fasta_bgz_file_path = join(
    input_directory_path, "Homo_sapiens.GRCh38.dna.primary_assembly.fa.bgz"
)

vcf_gz_file_path = normalize_path(
    read_json(join(project_directory_path, "project.json"))["vcf_gz_file_path"]
)

output_directory_path = join(project_directory_path, "output")

for file_path in (input_g2p_tsv_file_path, fasta_bgz_file_path, vcf_gz_file_path):

    if not exists(file_path):

        raise FileNotFoundError(file_path)

input_g2p = read_csv(input_g2p_tsv_file_path, sep="\t", comment="#")

row_match = []

for g2p_row_index, g2p_row in input_g2p.iterrows():

    print("=" * 80)

    print(f"G2P Row #{g2p_row_index+1}")

    names, regions, genotypes = g2p_row[:3]

    row_element_match = []

    for name, region, genotype in zip(
        names.split(sep=";"), regions.split(sep=";"), genotypes.split(sep=";")
    ):

        print(f"Name {name}")

        chromosome, start_position_end_position = region.split(sep=":")

        start_position, end_position = start_position_end_position.split(sep="-")

        print(f"Region {chromosome}:{start_position}-{end_position}")

        variants = tuple(
            get_variants_from_vcf_or_vcf_gz(
                vcf_gz_file_path, chromosome, start_position, end_position
            )
        )

        print(f"Found {len(variants)} variant.")

        if genotype in ("HIGH", "MODERATE", "LOW", "MODIFIER"):

            print(f"Looking for INFO.ANN.Effect == {genotype} ...")

            row_element_match.append(
                any(
                    genotype in get_vcf_info_ann(variant[7], "impact")
                    for variant in variants
                )
            )

        elif "|" in genotype:

            print(f"Looking for genotype {genotype} ...")

            if len(variants) == 0:

                sample_genotype = (
                    get_sequence_from_fasta_or_fasta_gz(
                        fasta_bgz_file_path, chromosome, start_position, end_position
                    ),
                ) * 2

            elif len(variants) == 1:

                variant = variants[0]

                sample_genotype = get_vcf_genotype(
                    variant[3],
                    variant[4],
                    get_vcf_sample_format(variant[8], "GT", variant[9]),
                )

            else:

                raise ValueError("There are multiple variants.")


            print(f"Sample genotype: {sample_genotype}")

            row_element_match.append(
                set(sample_genotype) == set(genotype.split(sep="|"))
            )

    print(f"This row is a match: {all(row_element_match)}")

    row_match.append(all(row_element_match))

output_g2p_tsv_file_path = join(output_directory_path, "output.g2p.tsv")

input_g2p.loc[row_match].to_csv(output_g2p_tsv_file_path, sep="\t", index=None)

print()

print(f"Output {output_g2p_tsv_file_path}.")
