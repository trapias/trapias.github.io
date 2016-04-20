---
layout: post
title: TrelloExport 1.9.19
permalink: /blog/trelloexport-1-9-19
tags: trello chrome excel markdown
---

New features for TrelloExport, a Chrome extension to export data from Trello to Excel. And now to Markdown, too.

## Whatsnew for v. 1.9.19
- refactoring export flow
- updated jQuery Growl to version 1.3.1
- new Markdown export mode

## Refactoring export
I made a partial refactoring: export flow has been rewritten to better handle data into a JSON structure, so to enable different export modes. 

**It is now possible to export to Excel and Markdown**, and more export formats could now more easily be added.

## Updated jQuery Growl
Updated jQuery Growl, the library used to give you notifications about what TrelloExport is doing, to version 1.3.1.

## Markdown export mode
We've got a new export mode: you can now choose to export, as usual, to Excel or to a [Markdown](https://daringfireball.net/projects/markdown/) (.MD) file. 

The export dialog now has a new dropdown to choose the target of your export, Excel or Markdown. Other options are the same as before, meaning **you can decide what and how to export**.

![Exporting to Markdown]({{ site.baseurl }}/images/markdown_export_mode.png)

If you don't know what Markdown is, take a look [here](https://it.wikipedia.org/wiki/Markdown). Basically, we can now export to a formatted text file you can easily convert to HTML or other formats (say, a word processor document) with tools like [Pandoc](http://pandoc.org/).

You can edit Markdown with any text editor, or with dedicated editors like [MacDown](http://macdown.uranusjr.com/) for the Mac.

**This is meant to produce reports**: TrelloExport will export boards, lists, cards, comments, chechlists and attachments information into an .MD file, formatting all of them in a "readable" format. It is then up to you to do whatever you want with the file: print, export, edit it as needed.

Is this feature interesting to you? Let me know!

## Feedback
Your feedback is welcome on all these new features! Also consider some bugs could come out: if so, please open an issue on [GitHub](https://github.com/trapias/trelloExport/issues) or contact me, I'll do my best to fix it quickly.

## Donate?
If you wish to support the development of this tool, you can now [make a donation](http://trapias.github.io/donate/).

## Download
Get TrelloExport on GitHub at [https://github.com/trapias/trelloExport](https://github.com/trapias/trelloExport), and follow the installation instructions in the readme.
