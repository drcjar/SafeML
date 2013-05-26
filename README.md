A project to summarise, explore, and visualise fatal accident inquiry data with a view to learning from it if possible.

Datasource lives here http://www.scotcourts.gov.uk/search-judgments/sheriff-court?type=structured

Initial approach was brute force with wget. Then after thinking for a moment used search to return all incidents, downloaded webpage with this, used beautiful soup to a list of inquiry report links, used wget to fetch list.

Parse html inquiry reports to text and merge using nltk

... do stuff ...
