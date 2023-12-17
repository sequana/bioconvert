import os
import subprocess
import sys
import tempfile

from click.testing import CliRunner

from sequana_pipelines.bioconvert.main import main

from . import test_dir

sharedir = f"{test_dir}/data/"


def test_standalone_subprocess():
    directory = tempfile.TemporaryDirectory()
    cmd = """sequana_bioconvert --input-directory {}
            --input-pattern "*fastq.gz" --input-ext fastq.gz --output-ext fasta.gz
            --working-directory {} --force --command fastq2fasta
          """.format(
        sharedir, directory.name
    )
    subprocess.call(cmd.split())


def test_standalone_script():
    directory = tempfile.TemporaryDirectory()

    runner = CliRunner()
    args = [
        "--input-directory",
        sharedir,
        "--working-directory",
        directory.name,
        "--force",
        "--input-pattern",
        '"*fastq.gz"',
        "--input-ext",
        "fastq.gz",
        "--output-ext",
        "fasta.gz",
        "--command",
        "fastq2fasta",
    ]

    results = runner.invoke(main, args)
    assert results.exit_code == 0


def test_full():

    with tempfile.TemporaryDirectory() as directory:
        print(directory)
        wk = directory

        cmd = "sequana_bioconvert --input-directory {} "
        cmd += "--working-directory {}  --force --command fastq2fasta"
        cmd += '--input-pattern "*fastq.gz" --input-ext fastq.gz'
        cmd += "--output-ext fasta.gz "
        cmd = cmd.format(sharedir, wk)
        subprocess.call(cmd.split())

        stat = subprocess.call("sh bioconvert.sh".split(), cwd=wk)


def test_version():
    cmd = "sequana_bioconvert --version"
    subprocess.call(cmd.split())
