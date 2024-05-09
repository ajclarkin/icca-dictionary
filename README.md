## ICCA Dictionary

A quick and simple tool for looking up *dictionaryPropNames* for entries in the Intellispace 
Critical Care & Anaesthesia (ICCA) clinical information system at work.


### The Problem

Database lookups require knowledge of the propName to select the correct rows. These are not
memorable. There may also be a need to filter by document.


### This Tool

This is a simple tool which requires a list of documents, interventions, and their propNames. 
It then filters by string.

Optimised for keyboard use (although not compatibile with Vimium browser plugin). Navigate up
and down the results table using cursor keys and press enter to copy the propName to clipboard 
for pasting into SQL.


### Data Source

Requires a correctly formatted CSV with columns:
 - documentLabel
 - intLabel (take care to ensure wrapped in quotes as may contain commas)
 - attLabel (wrapped)
 - aDPN -> contains attributeDictionaryPropName
 - tablename -> although I've used the DAR patient tables I list the main dbo Pt table here

Philips don't provide a good means of building this so I take a pragmatic approach. I have code to 
extract unique entries from the database and add to the data source.

**Caution** Depending on the version and means used, SSMS may append a status report to the CSV which
won't import correctly. Make sure to check the tail of the file.
