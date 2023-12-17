#
#  This file is part of Sequana software
#
#  Copyright (c) 2016-2021 - Sequana Development Team
#
#  Distributed under the terms of the 3-clause BSD license.
#  The full license is in the LICENSE file, distributed with this software.
#
#  website: https://github.com/sequana/sequana
#  documentation: http://sequana.readthedocs.io
#
##############################################################################
import os
import subprocess
import sys

import click_completion
import rich_click as click
from sequana_pipetools import SequanaManager
from sequana_pipetools.options import *

click_completion.init()
NAME = "bioconvert"


help = init_click(
    NAME,
    groups={
        "Pipeline Specific": [
            "--aligner-choice",
            "--contaminant-file",
        ],
    },
)


from bioconvert import logger as blog

# retrieve possible commands from the bioconvert registry.
from bioconvert.core.registry import Registry

blog.level = "ERROR"
r = Registry()
blog.level = "WARNING"
commands = list(r.get_converters_names())

methods = {}
smethods = set()
for command in r._fmt_registry.values():
    methods[command.__name__.lower()] = command.available_methods
    for x in command.available_methods:
        smethods.add(x)


@click.command(context_settings=help)
@include_options_from(ClickSnakemakeOptions, working_directory=NAME)
@include_options_from(ClickSlurmOptions)
@include_options_from(ClickGeneralOptions)
@click.option(
    "--input-pattern",
    "input_pattern",
    required=True,
    type=click.STRING,
    help="""The input pattern that allows you to restrict the search more specifically (default is to take all files in the input directory""",
)
@click.option(
    "--input-directory",
    "input_directory",
    required=True,
    type=click.Path(dir_okay=True, file_okay=False),
    help="""The input directory where to look for input files""",
)
@click.option(
    "--input-ext",
    "input_extension",
    required=True,
    type=click.STRING,
    help="""The extension of the files to convert. See bioconvert --help for details""",
)
@click.option(
    "--output-ext",
    "output_extension",
    required=True,
    type=click.STRING,
    help="""The extension of the output files. See bioconvert --help for details""",
)
@click.option(
    "--command",
    "command",
    required=True,
    type=click.Choice(commands),
    help="""One of the possible conversion available in bioconvert.""",
)
@click.option(
    "--method",
    "method",
    type=click.Choice(smethods),
    default=None,
    help="If you know bioconvert and method's name, you can set it here. This depends on the command used. Type 'bioconvert fastq-fasta --show--methods' to get the valid method for the command 'fastq2fasta' ",
)
def main(**options):
    """

    To convert a bunch of fastq files into fasta, initiate the pipeline using:

        sequana_bioconvert --input-directory data/ --input-ext "fastq.gz" --output-ext "fasta.gz"
            --use-apptainer --apptainer-prefix ~/images/ --command fastq2fasta --input-pattern "*"

        cd bioconvert
        sh bioconvert.sh

    """

    if options["from_project"]:
        click.echo("--from-project Not yet implemented")
        sys.exit(1)

    # the real stuff is here
    manager = SequanaManager(options, NAME)
    manager.setup()

    # aliases
    options = manager.options
    cfg = manager.config.config

    from sequana_pipetools import logger

    logger.setLevel(options.level)

    cfg.input_directory = os.path.abspath(options.input_directory)
    cfg.input_pattern = options.input_pattern
    cfg.bioconvert.method = options.method
    cfg.bioconvert.command = options.command
    cfg.bioconvert.input_extension = options.input_extension
    cfg.bioconvert.output_extension = options.output_extension

    # finalise the command and save it; copy the snakemake. update the config
    # file and save it.
    manager.teardown(check_input_files=False)


if __name__ == "__main__":
    main()
