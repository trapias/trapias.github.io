---
layout: post
title: TrelloExport 1.8.9
permalink: /blog/trelloexport-1-8-9
tags: trello
---


Following the publication of [TrelloExport 1.8.8 some days ago](https://blog-trapias.rhcloud.com/trelloexport-trello-to-excel/), I now pushed on Github an update for this Chrome extension.

## What's new in TrelloExport 1.8.9
New data columns:

- added column Card #
- added columns memberCreator, datetimeCreated, datetimeDone and memberDone pulling modifications from https://github.com/bmccormack/export-for-trello/blob/5b2b8b102b98ed2c49241105cb9e00e44d4e1e86/trelloexport.js
- added linq.min.js library to support linq queries for the above modifications

The full list of **Columns** is now:

	columnHeadings = ['List', 'Card #', 'Title', 'Link', 'Description', 'Checklists', 'Comments', 'Attachments', 'Votes', 'Spent', 'Estimate', 'Created', 'CreatedBy', 'Due', 'Done', 'DoneBy', 'Members', 'Labels']

### datetimeDone and memberDone
These fields are calculated intercepting when a card was moved to the Done list. While bmccormack's code only checks for this list, I check for cards being moved to any list whose name starts with "Done" (e.g. using lists named "Done Bugfix", "Done New Feature" and so will work).

Grab TrelloExport from Github at [https://github.com/trapias/trelloExport](https://github.com/trapias/trelloExport)
