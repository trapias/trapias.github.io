---
layout: post
title: TrelloExport 1.9.14
permalink: /blog/trelloexport-1-9-14
tags: trello
---

Some bugfix and some new features for TrelloExport, a Chrome extension to export data from Trello to Excel.

## Fixes

- fixed card completion calculation when exporting multiple boards (fix getMoveCardAction and getCreateCardAction)
- loading comments with a new function (getCommentCardActions), trying to fix issues with comments reported by some users; please give feedback


## New features

### Dates formatting
Dates are now formatted accordingly to user (browser) locale.

### Multiple 'Done' list name prefixes
We now can set multiple 'Done' list names for the card completion calculation function (see "Done prefix" in [notes for version 1.9.13](http://trapias.github.io/blog/trelloexport-1-9-13/)).


![Multiple done prefix]({{ site.baseurl }}/images/1.9.14.png)


The input box now accepts a comma-separated list of partial list names, i.e. just specify multiple names in the textbox like 'Done,Completed' (without apices). 

Card completion time will be calculated for all cards that were moved to a list whose name starts with one of these prefixes.


### Filter lists when exporting multiple boards
We now can optionally filter the exported lists by name, when exporting multiple boards (see the new "**filter lists by name**" box in figure above).

As per the multiple 'Done list name' prefixes, the 'Filter lists by name' input box accepts a comma-separated list of partial list names, i.e. just specify multiple names in the textbox like 'Done,Completed' (without apices). Lists will then be (case insensitively) matched when their name starts with one of these values.


## Feedback!
Your feedback is welcome on all these new features! Also consider some bugs could come out: if so, please open an issue on [GitHub](https://github.com/trapias/trelloExport/issues) or contact me, I'll do my best to fix it quickly.

## Donate?
If you wish to support the development of this tool, you can now [make a donation](http://trapias.github.io/donate/).

## Download
Get TrelloExport on GitHub at [https://github.com/trapias/trelloExport](https://github.com/trapias/trelloExport), and follow the installation instructions in the readme.
