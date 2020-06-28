---
layout: post
title: TrelloExport 1.9.64 with CSV
tags: trello chrome excel markdown html opml twig template csv 
---

## Export to CSV

TrelloExport 1.9.64 introduces the possibility to export cards to CSV.

![TrelloExport_1.9.64]({{ site.baseurl }}/images/TrelloExport_1.9.64.png)

Exporting to CSV works with all options that were already available for Excel, so you can decide whether to export archived cards, comments, checklists, attachments and custom fields, you can opt to have one row per card, checklist item, label or member and you can select the columns you wish to export to your final CSV file.

The data loading process is shared with the Excel export mode, so you should expect to get exactly the same data if you select the same options - what differs is of course the final export to a CSV file.

I built it to export all values as quoted, i.e. with quotes containing the value of each column like:

> "Column1","Column2"
>  
> "value1","value2"

Then all values are "escaped", that is quotes are transformed to apices (a " becomes an ') and CR/LF characters are removed.
This way you can get a proper CSV file in output. Please let me know if this is a suitable solution for your workflows.


## Feedback

Your feedback is always welcome. If you have any problem please open an issue on [GitHub](https://github.com/trapias/trelloExport/issues), I'll do my best to fix it quickly.

## Donate?

If you wish to support the development of this tool, like Richard did (thanks again!), you can [make a donation](https://trapias.github.io/donate/).

## Download

You can now get TrelloExport from the Chrome Web Store at [this URL](https://chrome.google.com/webstore/detail/trelloexport/kmmnaeamjfdnbhljpedgfchjbkbomahp).

If you want the source version, get them on GitHub at [https://github.com/trapias/trelloExport](https://github.com/trapias/trelloExport), and follow the installation instructions in the readme.


