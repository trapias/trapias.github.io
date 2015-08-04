---
layout: post
title: TrelloExport 1.9.11
permalink: /blog/trelloexport-1-9-11
tags: trello
---


TrelloExport is a Chrome extension to export data from Trello to Excel.

## Whatsnew for version 1.9.11

- added a new Options dialog
- export full board or choosen list(s) only
- add who and when item was completed to checklist items as of [issue #5](https://github.com/trapias/trelloExport/issues/5)


## New Options dialog
A new Options dialog gets opened when you click on TrelloExport button:

![Export button]({{ site.baseurl }}/images/trelloexport_1.9.10.png)

![Options dialog]({{ site.baseurl }}/images/TrelloExport_Options_1.png)

You can now set the data-limit, i.e. the max number of items to request to Trello APIs, and the type of export.

The default is to export the full board, as in all previous version. A new options is to export only one or more lists from the current board:

![Options dialog - export choosen list(s)]({{ site.baseurl }}/images/TrelloExport_Options_2.png)

You just have to CMD-Click on the Mac, or Control-Click on PCs, to select one or more lists, and then click "Export" to get your XSLX file as before - just it will hold only data from the specified list(s).

I'd like to extend this Options dialog to allow, for example:

- to export all or selected boards
- to export single cards from a choosen list
- to eventually add other export formats, beyond xlsx

Your feedback is welcome, just comment here, on the dedicated [Trello board](https://trello.com/b/MBnwUMwM/trelloexport) or open new issues in the [Github project page](https://github.com/trapias/trelloExport).


## Checklist items data
A little enhancement as per [issue #5](https://github.com/trapias/trelloExport/issues/5): now completed checklist items are exported with the detail of who and when the item was completed.

## Download
Get TrelloExport on GitHub at [https://github.com/trapias/trelloExport](https://github.com/trapias/trelloExport)

