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
import sys
import os
import argparse
import subprocess

from sequana_pipetools.options import *
from sequana_pipetools.options import before_pipeline
from sequana_pipetools.misc import Colors
from sequana_pipetools.info import sequana_epilog, sequana_prolog
from sequana_pipetools import SequanaManager


col = Colors()

NAME = "bioconvert"


# retrieve possible commands from the bioconvert registry.
from bioconvert.core.registry import Registry
from bioconvert import logger as blog
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




class Options(argparse.ArgumentParser):
    def __init__(self, prog=NAME, epilog=None):
        usage = col.purple(sequana_prolog.format(**{"name": NAME}))

        usage += """\nTo convert a bunch of fastq files into fasta, initiate the pipeline using:

    sequana_bioconvert --input-directory data/ --input-ext "fastq.gz" --output-ext "fasta.gz" 
 --use-apptainer --apptainer-prefix ~/images/ --command fastq2fasta --input-pattern "*"

    cd bioconvert
    sh bioconvert.sh


"""

        super(Options, self).__init__(usage=usage, prog=prog, description="",
            epilog=epilog,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )

        # add a new group of options to the parser
        so = SlurmOptions()
        so.add_options(self)

        # add a snakemake group of options to the parser
        so = SnakemakeOptions(working_directory=NAME)
        so.add_options(self)

        so = GeneralOptions()
        so.add_options(self)

        pipeline_group = self.add_argument_group("pipeline")

        pipeline_group.add_argument("--input-pattern", dest="input_pattern",
            required=True, type=str, help="""The input pattern that allows you to restrict the search more specifically
(default is to take all files in the input directory""")
        pipeline_group.add_argument("--input-directory", dest="input_directory",
            required=True, type=str, help="""The input directory where to look for input files""")
        pipeline_group.add_argument("--input-ext", dest="input_extension",
            required=True, type=str, help="""The extension of the files to convert. See bioconvert --help for details""")
        pipeline_group.add_argument("--output-ext", dest="output_extension", 
            required=True, type=str, help="""The extension of the output files. See bioconvert --help for details""")
        pipeline_group.add_argument("--command", dest="command",
            required=True, type=str, help="""One of the possible conversion available in bioconvert.""",
choices=commands)
        pipeline_group.add_argument("--method", dest="method",
            type=str,
            default=None,
            choices=smethods,
            help="If you know bioconvert and method's name, you can set it here. This depends on the command used. Type 'bioconvert fastq-fasta --show--methods' to get the valid method for the command 'fastq2fasta' ")


def main(args=None):

    if args is None:
        args = sys.argv

    # whatever needs to be called by all pipeline before the options parsing
    before_pipeline(NAME)

    # option parsing including common epilog
    options = Options(NAME, epilog=sequana_epilog).parse_args(args[1:])

    # the real stuff is here
    manager = SequanaManager(options, NAME)

    # create the beginning of the command and the working directory
    manager.setup()
    from sequana_pipetools import logger
    logger.setLevel(options.level)
    logger.name = "sequana_bioconvert"
    logger.info(f"#Welcome to sequana_bioconvert pipeline.")

    # fill the config file with input parameters
    cfg = manager.config.config
    # EXAMPLE TOREPLACE WITH YOUR NEEDS
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
