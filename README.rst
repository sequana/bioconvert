|Logo|


This is is the **bioconvert** pipeline from the `Sequana <https://sequana.readthedocs.org>`_ project


.. image:: https://badge.fury.io/py/sequana-bioconvert.svg
     :target: https://pypi.python.org/pypi/sequana_bioconvert

.. image:: http://joss.theoj.org/papers/10.21105/joss.00352/status.svg
    :target: http://joss.theoj.org/papers/10.21105/joss.00352
    :alt: JOSS (journal of open source software) DOI

.. image:: https://github.com/sequana/bioconvert/actions/workflows/main.yml/badge.svg
   :target: https://github.com/sequana/bioconvert/actions/workflows    

|Codacy-Grade|


:Overview: convert NGS format from one to another using Bioconvert
:Input: whatever input format accepted by Bioconvert
:Output: whatever output format accepted by Bioconvert
:Status: production
:Citation: Cokelaer et al, (2017), ‘Sequana’: a Set of Snakemake NGS pipelines, Journal of Open Source Software, 2(16), 352, JOSS DOI doi:10.21105/joss.00352


Installation
~~~~~~~~~~~~

This package depends on Python only and singularity. To install **sequana_bioconvert**, just install this package as
follows::

    pip install sequana_bioconvert

For **singularity**, we recommend to use a conda environment::


    conda create --name bioconvert -y python=3.8 singularity
    conda activate bioconvert
    pip install sequana_bioconvert


Usage
~~~~~

::

    sequana_bioconvert --help

You need to provide the type of conversion you wish to perform with the
*--command* argument. You also need to tell the type of extensions expected
including the compression (gz, bz2 or dsrc recognised). Finally, the
*--input-directory* and *--input-pattern* must be used to find the input
files.::

    sequana_bioconvert --input-directory . --input-ext fastq.gz --output-ext
        fasta.gz --command fastq2fasta --input-pattern "*.fastq.gz"

This command creates a directory with the pipeline and configuration file. You will then need 
to execute the pipeline as follows::

    cd bioconvert
    sh bioconvert.sh  # for a local run

This launches a snakemake pipeline. Symbolic links to the input data are created in
the ./input directory and results stored in the ./output directory.

Some conversions require external standalones. We recommend to use our singularity image. 
To do so, add **--use-apptainer** options when you initialse the pipeline. You can also 
specify where to store the singularity image once for all using **--apptainer-prefix**::

    sequana_bioconvert --input-directory . --input-ext fastq.gz --output-ext
        fasta.gz --command fastq2fasta --input-pattern "*.fastq.gz"
        --use-apptainer --apptainer-prefix ~/images


See bioconvert.readthedocs.io for more details about **bioconvert** itself.

If you are familiar with snakemake, you can retrieve the pipeline itself and its
configuration files and then execute the pipeline yourself with specific parameters::

    snakemake -s bioconvert.rules -c config.yaml --cores 4 --stats stats.txt

Or use `sequanix <https://sequana.readthedocs.io/en/main/sequanix.html>`_ interface.

Requirements
~~~~~~~~~~~~

This pipelines requires the following executable(s) installed with sequana_bioconvert: bioconvert

All dependencies and external dependencies related to bioconvert are available through the apptainer used by this
**sequana_bioconvert** pipeline. 



Rules and configuration details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is the `latest documented configuration file <https://raw.githubusercontent.com/sequana/sequana_bioconvert/main/sequana_pipelines/bioconvert/config.yaml>`_
to be used with the pipeline. Each rule used in the pipeline may have a section in the configuration file. 

Changelog
~~~~~~~~~

========= ====================================================================
Version   Description
========= ====================================================================
1.0.0     Uses bioconvert 1.0.0
0.10.0    Add container
0.9.0     Version using new sequana/sequana_pipetools framework
0.8.1     **Working version**
0.8.0     **First release.**
========= ====================================================================


Contribute & Code of Conduct
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To contribute to this project, please take a look at the 
`Contributing Guidelines <https://github.com/sequana/sequana/blob/main/CONTRIBUTING.rst>`_ first. Please note that this project is released with a 
`Code of Conduct <https://github.com/sequana/sequana/blob/main/CONDUCT.md>`_. By contributing to this project, you agree to abide by its terms.


.. |Codacy-Grade| image:: https://app.codacy.com/project/badge/Grade/9b8355ff642f4de9acd4b270f8d14d10
   :target: https://www.codacy.com/gh/sequana/bioconvert/dashboard

.. |Logo| image:: https://github.com/sequana/sequana/blob/dev/doc/_static/logo_256x256.png
