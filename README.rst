This is is the **bioconvert** pipeline from the `Sequana <https://sequana.readthedocs.org>`_ project

:Overview: TODO 
:Input: TODO
:Output: TODO
:Status: draft
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

    sequana_pipelines_bioconvert --help


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
0.8.1     **Working version**
0.8.0     **First release.**
========= ====================================================================


