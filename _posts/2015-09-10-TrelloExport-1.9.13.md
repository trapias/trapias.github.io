---
layout: post
title: TrelloExport 1.9.13
permalink: /blog/trelloexport-1-9-13
tags: trello
---


New features for TrelloExport, a Chrome extension to export data from Trello to Excel.

## Introducing version 1.9.13
Here's what's new for version 1.9.13:

- new 'DoneTime' column holding card completion time in days, hours, minutes and seconds, formatted as per [ISO8601](https://en.wikipedia.org/wiki/ISO_8601)
- name (prefix) of 'Done' lists is now configurable, default "Done"
- larger options dialog to better show options
- export multiple (selected) boards
- export multiple (selected) cards in a list (i.e. export single cards)

## DoneTime
The exported Excel file has now a new 'DoneTime' column, holding cards' completion time in days, hours, minutes and seconds.
This time is formatted as **PnDTnHnMnS**, a short format for [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) durations, like:

	P2DT5H4M30S

to mean a duration of 2 days, 5 hours, 4 minutes and 30 seconds.

The duration is calculated taking the card creation date as start, and the date of when the card was moved to a "Done" list as the end of the period.

## Done prefix
The "Done" list name is now configurable: this means you can set the name of lists you want to use to calculate cards' completed status, and now completion time (DoneTime).

The name actually acts as a prefix, i.e. "Done" means TrelloExport will consider a card completed when it is moved to a list whose name starts with "Done" (case insensitive, also).

So, if you put completed cards in lists named like "Completed", you can now dynamically set this name and let TrelloExport calculate cards' completion state  exporting the **member** (Trello user) who completed (moved the card to the Done list) the card, date-time of **when** he did so, and the **elapsed time** between card creation and this moment (see DoneTime above).


## Larger Options dialog
The options dialog is larger and holds new options, like the Done prefix and dropdowns for the new kind of exports.

![Improved options dialog]({{ site.baseurl }}/images/TrelloExport_Options_3.png)

## Four options to export
TrelloExport now has four (4) ways to export data:

- Current Board, original functionality exporting all lists and all cards in current board;
- Select Lists in current Board, i.e. export all cards from selected lists only from current board;
- Multiple Boards, i.e. select multiple boards for export;
- Select cards in a list, i.e. select single cards for export.

## Export multiple boards
This new kind of export allows you to choose what boards to export. 

When you select this mode, you're presented a multiple select with the list of all boards in current Organization. You can select one or more of them (cmd+click on Mac, ctrl+click otherwise) and click "Export" to get data from multiple boards in your excel file.

Each board will go to its own sheet in the report, while all archived lists and cards go to a dedicated "Arvhive" sheet.

## Export single cards
This new export method allows you to select what cards, single cards, to export.

When you select this, you're preresented a dropdown with all lists in current board. You then have to select one of them.

When you select a list, a new select multiple is created with the list of all cards in the choosen list. You can now select (again, cmd+click on Mac, ctrl+click otherwise) which cards you want in your report and click "Export" to get your Excel file as usual.

## Feedback!
Your feedback is welcome on all these new features! Also consider some bugs could come out: if so, please open an issue on [GitHub](https://github.com/trapias/trelloExport/issues) or contact me, I'll do my best to fix it quickly.


## Download
Get TrelloExport on GitHub at [https://github.com/trapias/trelloExport](https://github.com/trapias/trelloExport), and follow the installation instructions in the readme.
