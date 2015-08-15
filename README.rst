#IPythonTOC: Python class for IPython Notebook Table of Contents
===============================================================
IPythonTOC is a class with methods to generate markdown text that can be used to create an IPython notebook table of contents with links to referenced cells.

This work was inspired by the **Creating a table of contents with internal links in IPython Notebooks and Markdown documents** `notebook`_. 

Here's how I use it\:

Put in the very first notebook cell, the ``import cell``\:

    +--------------------------------------------------------------------------------------+
    | from IPythonTOC import IPythonTOC                                                    |
    |                                                                                      |
    | toc = IPythonTOC()                                                                   |
    +--------------------------------------------------------------------------------------+

Somewhere after the ``import cell``, put in the ``genTOCEntry cell`` but *don't run it yet*\:

    +--------------------------------------------------------------------------------------+
    | '''                                                                                  |
    | if you called toc.genTOCMarkdownCell before running this cell, the title has been    |
    | set in the class                                                                     |
    | '''                                                                                  |
    |                                                                                      |
    | print toc.genTOCEntry()                                                              |
    |                                                                                      |
    +--------------------------------------------------------------------------------------+

Below the ``genTOCEntry cell```, make a ``TOC cell`` as a markdown cell\:

    +--------------------------------------------------------------------------------------+
    | <a id='TOC'></a>                                                                     |
    |                                                                                      |
    | #TOC                                                                                 |
    |                                                                                      |
    +--------------------------------------------------------------------------------------+

As the notebook is developed, put this ``genTOCMarkdownCell`` just before a new section\:

    +-------------------------------------------------------------------------------------+
    |                                                                                     |
    | '''                                                                                 |
    | # genTOCMarkdownCell                                                                |
    |                                                                                     |
    | Move this cell to preceed the section of your notebook to add to the index          |
    |                                                                                     |
    | Add a markdown cell as the first cell in your newly indexed section                 |
    |                                                                                     |
    | Put the title of your new section as the string argument to genTOCMarkdownCell()    |
    |    & run the cell'                                                                  |
    |                                                                                     |
    | Copy the output into the markdown cell that is the first cell of your section       |
    |                                                                                     |
    | Run the ``genTOCEntry cell``near the top of this notebook                           |
    |                                                                                     |
    | Copy that output and paste into the TOC markup cell                                 |
    |                                                                                     |
    | Here is the python code:                                                            |
    | '''                                                                                   |
    |                                                                                     |
    | with open('TOCMarkdownCell.txt', 'w') as outfile\:                                  |
    |                                                                                     |
    |     outfile.write(toc.genTOCMarkdownCell('Introduction'))                           |
    |                                                                                     |
    | !cat TOCEntry.txt                                                                   |
    |                                                                                     |
    | !rm TOCEntry.txt                                                                    |
    |                                                                                     |
    +-------------------------------------------------------------------------------------+

Move the ``genTOCMarkdownCell`` down to the point in your notebook where you want to start a new section. Add a markdown cell right after it, and follow the instructions. The output can be pasted into the markdown cell you just created. Then go to the ''genTOCEntry cell'' and run it. For example, if you make the argument to  ``genTOCMarkdownCell`` as shown above and run it, you get the output:

    <a id='Introduction'></a>
    
    ###Introduction

Then when you go to the top of your notebook and run genTocEntry, you get the output:

    ``[Introduction](#Introduction)``  

Copy this link string and paste it into the ``TOC markdown cell`` as follows\:

    +--------------------------------------------------------------------------------------+
    | #Table of Contents                                                                   |
    |                                                                                      |
    | [Introduction](#Introduction)                                                        |
    |                                                                                      |
    +--------------------------------------------------------------------------------------+

After you edit the ``TOC cell`` to insert the link string and then you press ahift-enter, the link to your new section will appear in your notebook Table of Contents as a web link and clicking it will position the browser to your new section.

#License
-------

::
    Do whatever you want with it. Hope it works for you but it may not. You've been warned. For technical support, call 800-477-2937.

.. _notebook: http://nbviewer.ipython.org/github/rasbt/python_reference/blob/master/tutorials/table_of_contents_ipython.ipynb
