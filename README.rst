This is is the **bioconvert** pipeline from the `Sequana <https://sequana.readthedocs.org>`_ project


.. image:: https://badge.fury.io/py/sequana-bioconver.svg
     :target: https://pypi.python.org/pypi/sequana_bioconvert

.. image:: http://joss.theoj.org/papers/10.21105/joss.00352/status.svg
    :target: http://joss.theoj.org/papers/10.21105/joss.00352
    :alt: JOSS (journal of open source software) DOI

.. image:: https://github.com/sequana/bioconvert/actions/workflows/main.yml/badge.svg
   :target: https://github.com/sequana/bioconvert/actions/workflows    



:Overview: convert NGS format from one to another using bioconvert
:Input: whatever input format accepted by bioconvert
:Output: whatever output format accepted by bioconvert
:Status: production
:Citation: Cokelaer et al, (2017), ‘Sequana’: a Set of Snakemake NGS pipelines, Journal of Open Source Software, 2(16), 352, JOSS DOI doi:10.21105/joss.00352


Installation
~~~~~~~~~~~~

You must install Sequana first::

    pip install sequana

Then, just install this package::

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


This creates a directory with the pipeline and configuration file. You will then need 
to execute the pipeline::

    cd bioconvert
    sh bioconvert.sh  # for a local run

This launch a snakemake pipeline. Symboli links to the input data are created in
the ./input directory and results stored in the ./output directory.

See bioconvert.readthedocs.io for more details about **bioconvert** itself.

If you are familiar with snakemake, you can retrieve the pipeline itself and its 
configuration files and then execute the pipeline yourself with specific parameters::

    snakemake -s bioconvert.rules -c config.yaml --cores 4 --stats stats.txt

Or use `sequanix <https://sequana.readthedocs.io/en/master/sequanix.html>`_ interface.

Requirements
~~~~~~~~~~~~

This pipelines requires the following executable(s):

- bioconvert

.. image:: https://raw.githubusercontent.com/sequana/sequana_bioconvert/master/sequana_pipelines/bioconvert/dag.png


Details
~~~~~~~~~

This pipeline runs **bioconvert** in parallel on the input fastq files (paired or not). 
A brief sequana summary report is also produced.


Rules and configuration details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is the `latest documented configuration file <https://raw.githubusercontent.com/sequana/sequana_bioconvert/master/sequana_pipelines/bioconvert/config.yaml>`_
to be used with the pipeline. Each rule used in the pipeline may have a section in the configuration file. 

Changelog
~~~~~~~~~

========= ====================================================================
Version   Description
========= ====================================================================
0.9.0     Version using new sequana/sequana_pipetools framework
0.8.1     **Working version**
0.8.0     **First release.**
========= ====================================================================


Contribute & Code of Conduct
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To contribute to this project, please take a look at the 
`Contributing Guidelines <https://github.com/sequana/sequana/blob/master/CONTRIBUTING.rst>`_ first. Please note that this project is released with a 
`Code of Conduct <https://github.com/sequana/sequana/blob/master/CONDUCT.md>`_. By contributing to this project, you agree to abide by its terms.

