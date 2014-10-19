IPythonTOC: Python class for IPython Notebook Table of Contents
===============================================================
IPythonTOC is a class with methods to generate markdown text that can be used to create an IPython notebook table of contents with links to referenced cells.

This work was inspired by the **Creating a table of contents with internal links in IPython Notebooks and Markdown documents** `notebook`_.

Here's how I use it\:

#. Put in the very first notebook cell, the ``import cell``\:

    +--------------------------------------------------------------------------------------+
    | from IPythonTOC import IPythonTOC                                                    |
    |                                                                                      |
    | toc = IPythonTOC()                                                                   |
    +--------------------------------------------------------------------------------------+

#. Somewhere after the ``import cell``, put in the ``genTOCEntry cell`` but don't run it yet\:

    +--------------------------------------------------------------------------------------+
    | \# if you called toc.genTOCMarkdownCell before running this cell, the title has been |
    | set in the class                                                                     |
    |                                                                                      |
    | with open('TOCEntry.txt', 'w') as outfile\:                                          |
    |                                                                                      |
    |     outfile.write(toc.genTOCEntry())                                                 |
    |                                                                                      |
    | \%load TOCEntry.txt                                                                  |
    +--------------------------------------------------------------------------------------+

#. Below the ``genTOCEntry cell```, make a ``TOC cell`` as a markdown cell\:

    +--------------------------------------------------------------------------------------+
    | #Table of Contents                                                                   |
    +--------------------------------------------------------------------------------------+

#. As the notebook is developed, put this ``genTOCMarkdownCell`` just before a new section\:

    +-------------------------------------------------------------------------------------+
    | \# a. move this cell to preceed the markdown cell you want to index                 |
    |                                                                                     |
    | \# b. put the title string as argument to genTOCMarkdownCell & run the cell         |
    |                                                                                     |
    | \# c. change the loaded cell from a code cell to a markdown cell                    |
    |                                                                                     |
    | \# d. go to the head of this notebook and run the ``genTOCEntry cell`` and          |
    | copy that output and paste into the TOC cell                                        |
    |                                                                                     |
    | with open('TOCMarkdownCell.txt', 'w') as outfile\:                                  |
    |                                                                                     |
    |     outfile.write(toc.genTOCMarkdownCell('Merge Entered Values into Dataframe'))    |
    |                                                                                     |
    | \%load TOCMarkdownCell.txt                                                          |
    +-------------------------------------------------------------------------------------+

#. Move the ``genTOCMarkdownCell`` down before starting a new section and follow the instructions. The output can be pasted into the ``TOC cell``. For example, if you change the argument to  ``genTOCMarkdownCell`` and run the  ``genTOCMarkdownCell`` cell, the output is ``[Introduction](#Introduction)`` and you can copy this link string and paste it into the ``TOC cell`` as follows\:

    +--------------------------------------------------------------------------------------+
    | #Table of Contents                                                                   |
    |                                                                                      |
    | [Introduction](#Introduction)                                                        |
    |                                                                                      |
    +--------------------------------------------------------------------------------------+

After you edit the ``TOC cell`` to insert the link string and then you press ctrl-enter, the link to your new section will appear in your notebook as a web link and clicking it will position the browser to your new section.

License
-------

::
    Do whatever you want with it. Hope it works for you but it may not. You've been warned. For technical support, call 800-477-2937.

.. _notebook: http://nbviewer.ipython.org/github/rasbt/python_reference/blob/master/tutorials/table_of_contents_ipython.ipynb
