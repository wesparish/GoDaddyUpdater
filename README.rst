GoDaddyUpdater
==============
Python tool used to update existing GoDaddy A-record DNS entries to current external IP address.

Source located @ https://github.com/wesparish/GoDaddyUpdater

This concept was spawned from observerss' and eXamadeus' GoDaddy libraries they have written.

Note: Check on Dockerhub for a containerized deployment that is driven by env vars.

Setup
--------

First, go to https://developer.godaddy.com/keys/ and request a production API key and secret.

*Note: Sometimes the production API keys don't seem to work correctly.  Just delete it and request another one.*

Second, install GoDaddyPy with pip.

.. code-block:: bash

    $ pip install godaddypy
..

Third, clone this repo and execute the tool.

.. code-block:: bash

    $ git clone https://github.com/wesparish/GoDaddyUpdater
..

Building
--------
.. code-block:: bash

  $ docker build --no-cache -t wesparish/godaddyupdater .
  $ docker push wesparish/godaddyupdater
..

Examples
--------

.. code-block:: bash

    $ export GODADDY_KEY=<ACCESS KEY HERE>
    $ export GODADDY_SECRET=<SECRET KEY HERE>
    $ export GODADDY_DOMAIN_LIST=mydomain.org,myotherdomain.org
    $ export GODADDY_A_RECORD_LIST=updatertest,updatertest2
    $ ./GoDaddyUpdater.py
..
