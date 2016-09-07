---
layout: post
title: TrelloExport 1.9.25
tags: trello chrome excel markdown html opml
---

A quick recap of new features in TrelloExport 1.9.24 and 1.9.25.

## What's TrelloExport?
It's a Chrome extension that allows you to export data from your Trello boards to Excel, Markdown, HTML and OPML files.
Once installed, you will find a new option in Trello right sidebar under More > Print and Export:

## 1.9.24
This release wasn't followed by a post, so just a couple of words: 1.9.24 introduced new flags in the options dialog (checkboxes to enable/disable exporting of comments, checklist items and attachments) and a new option to export checklist items to rows, for Excel only.

![Options]({{ site.baseurl }}/images/TrelloExport__Options.png)


## 1.9.25
Paginating cards loading: cards are now loaded in bunchs, so to be able to progressively load any number of cards, surpassing the Trello API limit of 1000 maximum records returned per query.

Please report if you have any issue with the new loading method.


## Feedback
Your feedback is welcome on all these new features! Also consider some bugs could come out: if so, please open an issue on [GitHub](https://github.com/trapias/trelloExport/issues) or contact me, I'll do my best to fix it quickly.

## Donate?
If you wish to support the development of this tool, you can now [make a donation](http://trapias.github.io/donate/).

## Download
You can now get TrelloExport from the Chrome Web Store at [this URL](https://chrome.google.com/webstore/detail/trelloexport/kmmnaeamjfdnbhljpedgfchjbkbomahp).

If you want the source version, get them on GitHub at [https://github.com/trapias/trelloExport](https://github.com/trapias/trelloExport), and follow the installation instructions in the readme.
