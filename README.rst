==========================================================
Data Repository
==========================================================
Source code and data files for the manuscript Structure of Charge Density Waves in La1.875Ba0.125CuO4, J. Sears, Y. Shen, M. J. Krogstad, H. Miao, E. S. Bozin, I. K. Robinson, G. D. Gu, R. Osborn, S. Rosenkranz, J. M. Tranquada, and M. P. M. Dean. Execute the *.ipynb files to view the data.

How to cite
-----------
If this data is used, please cite, Structure of Charge Density Waves in La1.875Ba0.125CuO4 J. Sears, Y. Shen, M. J. Krogstad, H. Miao, E. S. Bozin, I. K. Robinson, G. D. Gu, R. Osborn, S. Rosenkranz, J. M. Tranquada, and M. P. M. Dean, Phys. Rev. B (2023)


Run locally
-----------

Work with this by installing `docker <https://www.docker.com/>`_ and pip and then running

.. code-block:: bash

       pip install jupyter-repo2docker
       jupyter-repo2docker --editable .

Change `tree` to `lab` in the URL for JupyterLab. 

The large datafile is stored using `git lfs <https://git-lfs.com/>`_. Download the files using

.. code-block:: bash

       git lfs clone https://github.com/mpmdean/Sears2023structure.git

Run remotely
------------

.. image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/mpmdean/Sears2023structure/HEAD
