IPythonTOC: Python class for IPython Notebook Table of Contents
===============================================================
IPythonTOC is a class with methods to generate markdown text that can be used to create an IPython notebook table of contents with links to indexeded notebook cells.

This work was inspired by the **Creating a table of contents with internal links in IPython Notebooks and Markdown documents** `notebook`_. 

There is a sort of tutorial notebook in this repository: TOC.ipynb. You should clone the repository, run setup.py to install IPythonTOC and try the notebook.

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

As the notebook is developed, put this ``genTOCMarkdownCell`` before starting a new section\:

    +-------------------------------------------------------------------------------------+
    |                                                                                     |
    | with open('TOCMarkdownCell.txt', 'w') as outfile\:                                  |
    |                                                                                     |
    |    outfile.write(toc.genTOCMarkdownCell('Introduction'))                            |
    |                                                                                     |
    | !cat TOCMarkdownCell.txt                                                            |
    |                                                                                     |
    | !rm TOCMarkdownCell.txt                                                             |
    |                                                                                     |
    +-------------------------------------------------------------------------------------+

Move the ``genTOCMarkdownCell`` down to the point in your notebook where you want to start a new section and make the argument to genTOCMarkdownCell the string title for your new section then run it. Add a markdown cell right after it and copy the output from genTOCMarkdownCell into the markdown cell that starts your new section. Then go to the genTOCEntry cell near the top of your notebook and run it. For example, if you make the argument to  ``genTOCMarkdownCell`` as shown above and run it, you get the output:

    <a id='Introduction'></a>
    
    ###Introduction

Then when you go to the top of your notebook and run genTocEntry, you get the output:

    ``[Introduction](#Introduction)``  

Copy this link string and paste it into the ``TOC markdown cell`` as follows\:

    +--------------------------------------------------------------------------------------+
    | <a id='TOC'></a>                                                                     |
    |                                                                                      |
    | #TOC                                                                                 |
    |                                                                                      |
    | [Introduction](#Introduction)                                                        |
    |                                                                                      |
    +--------------------------------------------------------------------------------------+

After you edit the ``TOC cell`` to insert the link string and then you press shift-enter, the link to your new section will appear in your notebook Table of Contents as a web link and clicking it will position the browser to your new section.

One thing I often forget is that clicking a line in the TOC makes the browser jump to that cell but doesn't select it. Whatever cell was active when we clicked on the TOC link is still active, so a down or up arrow or shift-enter refers to still active cell, not the cell we got by clicking on the TOC link. 

This License plus $3 gets you a cup of coffee at Starbucks (inflation not included)
-------

::
    Do whatever you want with it. Hope it works for you but it may not. You've been warned. For technical support, call 800-477-2937.

.. _notebook: http://nbviewer.ipython.org/github/rasbt/python_reference/blob/master/tutorials/table_of_contents_ipython.ipynb
