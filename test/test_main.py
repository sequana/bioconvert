import easydev
import os
import tempfile
import subprocess
import sys
from sequana.pipelines_common import get_pipeline_location as getpath

sharedir = getpath('bioconvert')


def test_standalone_subprocess():
    directory = tempfile.TemporaryDirectory()
    cmd = """sequana_pipelines_bioconvert --input-directory {}
            --input-pattern "*fastq.gz" --input-ext fastq.gz --output-ext fasta.gz
            --working-directory {} --force --command fastq2fasta
          """.format(sharedir, directory.name)
    subprocess.call(cmd.split())


def test_standalone_script():
    directory = tempfile.TemporaryDirectory()
    import sequana_pipelines.bioconvert.main as m
    sys.argv = ["test", "--input-directory", sharedir,
            "--working-directory", directory.name, "--force",
            "--input-pattern", '"*fastq.gz"', "--input-ext", "fastq.gz",
            "--output-ext", "fasta.gz",
            "--command", "fastq2fasta"]
    m.main()

def test_full():

    with tempfile.TemporaryDirectory() as directory:
        print(directory)
        wk = directory

        cmd = "sequana_pipelines_bioconvert --input-directory {} "
        cmd += "--working-directory {}  --force --command fastq2fasta"
        cmd += '--input-pattern "*fastq.gz" --input-ext fastq.gz'
        cmd += "--output-ext fasta.gz "
        cmd = cmd.format(sharedir, wk)
        subprocess.call(cmd.split())

        stat = subprocess.call("sh bioconvert.sh".split(), cwd=wk)


def test_version():
    cmd = "sequana_pipelines_bioconvert --version"
    subprocess.call(cmd.split())

