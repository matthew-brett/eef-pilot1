#########################
Where are the Brexiteers?
#########################

.. code-links:: clear

Every year, the `Hansard Society
<https://www.hansardsociety.org.uk/research/audit-of-political-engagement>`_
sponsors a survey on political engagement in the UK.

They put topical questions in each survey.  For the 2016 / 7 survey, they
asked about how people voted in the Brexit referendum.

Luckily, they make the data freely available online for us to analyze.

You can get the data for yourself from the UK Data Service:
https://discover.ukdataservice.ac.uk/catalogue/?sn=8183. There are data files
in various formats, including:

* SPSS format (for the SPSS statistical package);
* Stata format (for the Stata statistical package);
* tab-delimited (a general data format, that can be used with Excel and other
  packages).

The data is in a standard form, with one row per respondent, and one column
per question.

To save you a tiny bit of work, I've made an unchanged copy of the
tab-delimited version of the data file for you to download directly. I've also
made a copy of the document describing the questions they ask and the way that
they have recorded the answers in the data file.  This is often called the
"data dictionary".  It was originally in Rich Text Format, but I have
converted to PDF for convenience.  It is otherwise identical to the file you
will find at the UK Data Service.

You can download these copies of the files from the following links:

* :download:`tab-delimited data file
  <audit_of_political_engagement_14_2017.tab>`;
* :download:`data dictionary PDF file
  <audit_of_political_engagement_14_2017_ukda_data_dictionary.pdf>`.

In the moment, we are going to try and analyze these data.  We will focus on
two questions labeled ``cut15`` and ``numage``.  ``cut15`` is the question
about Brexit. The data dictionary has the *variable label* "CUT15 - How did
you vote on the question 'Should the United Kingdom remain a member of the
European Union or leave the European Union'?".  The recorded values run from 1
through 6 and have the following labels:

.. code-block:: none

    Value label information for cut15
    Value = 1.0    Label = Remain a member of the European Union
    Value = 2.0    Label = Leave the European Union
    Value = 3.0    Label = Did not vote
    Value = 4.0    Label = Too young
    Value = 5.0    Label = Can't remember
    Value = 6.0    Label = Refused

We also want the variable ``numage``; this is the age of the respondent in
years.

Your task is the following:

* Load the data.
* Check the values for ``cut15`` and ``numage``. Are there any bad values?  If
  there are, remove the respondents (rows) that have invalid values in either
  variable.
* In this clean dataset, find the number of people who admitted to voting
  Remain.  Find the number of people who admitted to voting Leave.  Calculate
  the ratio of Leave voters to (voters who voted either Leave or Remain).
* Write down every step of what you did, so that someone else can reproduce
  it.

Remember, the `final referendum vote percentages
<https://www.electoralcommission.org.uk/find-information-by-subject/elections-and-referendums/past-elections-and-referendums/eu-referendum/electorate-and-count-information>`_
were:

* Remain: 48.1%
* Leave: 51.9%

Did the proportion you find, match the proportion in the referendum?  How far
off was it?  Is it too far off?  Think about what "too far" could mean.

.. include:: links_names.inc
