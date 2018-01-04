from gzip import open as gzip_open
from json import dump
from os.path import abspath, dirname, join

# ==============================================================================
# Constant Genome App paths
# ==============================================================================
PROJECT_DIRECTORY_PATH = dirname(dirname(abspath(__file__)))

OUTPUT_DIRECTORY_PATH = join(PROJECT_DIRECTORY_PATH, 'output')

# ==============================================================================


def count_variants():
    """
    Count variants per chromosome and save the result in ../output/output.json.
    Arguments:
        None
    Returns:
        None
    """

    # Count variants per chromosome
    with gzip_open(
            join(PROJECT_DIRECTORY_PATH, 'data', 'person',
                 'genome.vcf.gz')) as file_:

        counts = {}
        current_chromosome = None

        # Count variants
        for line in file_:

            line = line.decode()

            if line.startswith('#'):
                continue

            chromosome = line.split('\t')[0]

            if current_chromosome is None or current_chromosome != chromosome:

                current_chromosome = chromosome
                counts[current_chromosome] = 0

            else:
                counts[current_chromosome] += 1

    # Style results
    styled_counts = {}
    for c, n in counts.items():
        styled_counts['Chromosome {}'.format(c)] = '{} variants'.format(n)

    # Save results to ../output/output.json
    output_json_file_path = join(OUTPUT_DIRECTORY_PATH, 'output.json')

    with open(output_json_file_path, 'w') as file_:
        dump(styled_counts, file_, indent=2, sort_keys=True)

    print(
        'Counted the number of variants in each chromosome and saved the results to {}.'
    )


count_variants()
