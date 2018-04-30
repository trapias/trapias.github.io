---
layout: post
title: TrelloExport 1.9.43
tags: trello chrome excel markdown html opml twig
---

Export HTML with templates!

## Introducing Twig Templates

TrelloExport 1.9.43 is an huge update for HTML export, adopting [Twig Templates](https://twig.symfony.com/) - using the [TwigJS](https://github.com/twigjs/twig.js/wiki) library.

Using a template engine means, in few words, we can export personalized HTML files with data from our Trello boards.

We can customize the output (the resulting HTML file in this case) the way we want. **We can decide what to include in every single exported file**, by checking or unchecking the flags available in TrelloExport options dialog, and **we can customize the output just by selecting a template**. 

And, if we want, we can modify an existing template, or create a completely new one. Put inline styles in it, or link some external CSS, and you can distribute your HTML. Send it via email, publish it on a blog, even - why not? - automatically publish it via some online service. More to come on this.

In an upcoming release, **I'm adding Twig templates for other export formats** too, such as Markdown and more.
And of course if anybody wants to share new templates, I can include them in a next release and/or add them to some shared template-set. 


## Sponsored Feature

Twig templates are the first sponsored feature for TrelloExport: this means the development of this feature was accelerated and prioritized because of a specific business need, and because of a donation.

So please let me say a big THANK YOU (and you all should also do so) to whom made this all possible:

> **Dr Richard Kaplan** of  [www.kaplanlifecareplan.com](http://www.kaplanlifecareplan.com)
> 
> Richard is using Trello and TrelloExport as part of an open-source project to develop software for writing in medicine and other academic fields.
> 
> He welcomes inquiries from those who may be interested in learning more.

## Updated options dialog

The options dialog is now scrollable, so that it can hold more fields and - hopefully - be usable also on smaller screens.

For the HTML export mode we had the possibility to shoose a custom CSS file: now we can also choose a template, and load our templates from a custom URL.

<br>

| **TrelloExport 1.9.43 Mac** | **TrelloExport 1.9.43 Windows**                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![TrelloExport_1.9.43_Options_Mac.png]({{ site.baseurl }}/images/TrelloExport_1.9.43_Options_Mac.png) | ![TrelloExport_1.9.43_Options_Mac.png]({{ site.baseurl }}/images/TrelloExport_1.9.43_Options_Win.png) |

<br>
The "template" dropdown allows us to choose a template, while the "template-set" textbox allows to specify from where we want to load our templates. If we leave it empty, it will use "local" templates, that is templates from the installation folder.

### Update, version 1.9.45

Version 1.9.45 adds an array of labels (jsonLabels) to the exported data, and a new button in dialog to clear localStorage - this should help if some wrong setting has been incorrectly saved and preventing TrelloExport to work properly.


## Template-Sets

TrelloExport loads templates in groups, where a group of templates is defined by a template-set JSON file.
Such file describes a list of templates, where each **template** has:

- a **name**,
- an **URL**,
- a **description**,
- an optional **CSS** file URL (if not specified, the custom stylesheet provided in TrelloExport options dialog will be used, or, if not specified, the default local css will be used).

Because of security, all URLs must be HTTPS - it’s not possible to load templates from HTTP.
A template-set JSON definition file looks like this:

```json
{
    "templates": [
        {
            "name": "html",
            "url": "https://trapias.github.io/assets/TrelloExport/html.twig",
            "description": "Default HTML",
            "css": "https://trapias.github.io/assets/TrelloExport/default.css"
        },
        {
            "name": "bibliography",
            "url": "https://trapias.github.io/assets/TrelloExport/bibliography.twig",
            "description": "Bibliography HTML",
            "css": "https://trapias.github.io/assets/TrelloExport/bibliography.css"
        },
        {
            "name": "newsletter",
            "url": "https://trapias.github.io/assets/TrelloExport/newsletter.twig",
            "description": "Newsletter HTML",
            "css": "https://trapias.github.io/assets/TrelloExport/newsletter.css"
        }
    ]
}
```

Per default TrelloExport loads local templates from its installation folder, containing this same set of templates, but you can override this in the options dialog, and **load a custom template-set from any HTTPS URL**.

## Templates

The above template-set is the online version of standard TrelloExport templates, available at [https://trapias.github.io/assets/TrelloExport/templates.json](https://trapias.github.io/assets/TrelloExport/templates.json). Put this url in the "template-set" input box to use online templates.

The JSON data format provided by TrelloExport to its templates is documented below, and you can find templates on your hard disk or in [this folder at Github](https://github.com/trapias/trapias.github.io/tree/master/assets/TrelloExport).

Here's a brief description of first templates available.

### Default template 

The default template looks very much like the HTML output produced by previous versions of TrelloExport, just a bit improved both in styling and in content: **it is now possible to include any data in template**, including custom fields from the Trello CustomFields PowerUp.
This template uses the default.css with the addition of [Font Awesome icons](https://fontawesome.com/icons?d=gallery).

![TrelloExport_DefaultTemplate]({{ site.baseurl }}/images/TrelloExport_DefaultTemplate.png)

### Bibliography template

This is a template thinked for research tasks: collect links into a Trello Board, and produce a nice bibliography HTML file you can put on a website, or you can share with anybody the way you want (or even automatically push to some online service... more to come!).

In order to use this template you have to properly setup your Trello Board, so that the template can find data it needs to produce the expected result.
You can have any number of lists in your board, but cards within them must have at least:

- a title
- an attachment link, which will become the main bibliography item link.

Cards would also contain a description text, and can then include any data: comments, other attachments, checklists, custom fields.

![TrelloExport_BibliographyTemplate]({{ site.baseurl }}/images/TrelloExport_BibliographyTemplate.png)


### Newsletter template

The Newsletter template is another simple template that could be used for a newsletter, or something like that.


![TrelloExport_NewsletterTemplate]({{ site.baseurl }}/images/TrelloExport_NewsletterTemplate.png)



## Rendering

Here's some technical details for who wants to work on templates.

TrelloExport renders HTML by "sending" the template a custom data object holding two main nodes, **renderSettings** and **cards**.

The renderSettings object only contains two properties, the **CSS** URL and the current **language**.

The cards array is then an array of cards, built with Trello data and some custom calculations.

```json
{
    "renderSettings": {
        "CSS": "https://trapias.github.io/assets/TrelloExport/default.css",
        "language": "it-IT"
    },
    "cards": []
}
```

Cards have the following properties: 

```json
{
            "organizationName": "Trapias",
            "boardName": "TrelloExport",
            "listName": "Feature Requests / Ideas",
            "cardID": 21,
            "title": "Export/Backup + import",
            "shortLink": "https://trello.com/c/cRVWNCtw",
            "cardDescription": "<p>[2014-03-25 04:07:16 - @bluespeed] Could you offer an additional service that would do automatic backups every week and/or night of an entire organizations board. We are using trello so much for project management that if something happened to the information we are putting in it would be a huge problem. I understand we can export .json files, If we were to manually do that every week, would that be able to be reimported intro trello if something happened?</p>",
            "checkLists": "",
            "numberOfComments": 0,
            "comments": "",
            "attachments": "",
            "votes": 2,
            "spent": "",
            "estimate": "",
            "points_estimate": "",
            "points_consumed": "",
            "datetimeCreated": "29/3/2014 10:04:09",
            "memberCreator": "Alberto Velo",
            "LastActivity": "5/1/2016 07:15:20",
            "due": "",
            "datetimeDone": "",
            "memberDone": "",
            "completionTime": "",
            "completionTimeText": "",
            "memberInitials": "",
            "labels": [],
            "isArchived": false,
            "jsonCheckLists": [],
            "jsonComments": [],
            "jsonAttachments": [],
            "dueComplete": false,
            "customFields": []
    },
```

Please note there are some duplicates, due to the different export formats now available and not yet optimized.
For example the "attachments" or "comments" fields are the old fields holding text for all items: the complete JSON arrays are in jsonCheckLists , jsonComments and jsonAttachments.


### CheckLists

```json
"jsonCheckLists": [
        {
            "name": "Elettronica",
            "items": [
                {
                    "name": "Cr2430",
                    "completed": false
                }
            ]
        },
        {
            "name": "Bevande",
            "items": [
                {
                    "name": "Coca cola",
                    "completed": false
                },
            ]
        },
```                

### Comments

```json
"jsonComments": [
            {
                "date": "11/4/2018 10:34:37",
                "text": "<p>@phildalencour_ap can you please open an issue on GitHub? Have to work on this</p>",
                "memberCreator": {
                    "id": "508fe2f791808fea59005084",
                    "avatarHash": "37bc2522dc8664d18c4f65fb5e7672a2",
                    "avatarUrl": "https://trello-avatars.s3.amazonaws.com/37bc2522dc8664d18c4f65fb5e7672a2",
                    "fullName": "Alberto Velo",
                    "initials": "AV",
                    "username": "trapias"
                }
            },
}
```


### Attachments

```json
"jsonAttachments": [
                {
                    "id": "5adbf30d1042f8473a04e568",
                    "bytes": null,
                    "date": "2018-04-22T02:27:25.192Z",
                    "edgeColor": null,
                    "idMember": "5a70aa03ec41ee11db900be1",
                    "isUpload": false,
                    "mimeType": "",
                    "name": "https://www.ncbi.nlm.nih.gov/pubmed/?term=Acceleration+Perturbations+of+Daily+Living+%E2%80%93+A+Comparison+to+Whiplash",
                    "previews": [],
                    "url": "https://www.ncbi.nlm.nih.gov/pubmed/?term=Acceleration+Perturbations+of+Daily+Living+%E2%80%93+A+Comparison+to+Whiplash",
                    "pos": 16384
                },
                {
                    "id": "5adbfc660f6347caaec6203d",
                    "bytes": 5887596,
                    "date": "2018-04-22T03:07:18.574Z",
                    "edgeColor": null,
                    "idMember": "5a70aa03ec41ee11db900be1",
                    "isUpload": true,
                    "mimeType": null,
                    "name": "Allen.pdf",
                    "previews": [],
                    "url": "https://trello-attachments.s3.amazonaws.com/5adbf208893b97fd6379b798/5adbf30c1042f8473a04e563/6e5ccdd1b890ebb58fcd58a27bfed4c1/Allen.pdf",
                    "pos": 32768
                },
            ],
```

### Custom Fields

Custom Fields, from the Trello Custom Fields Power Up, are both exported as an array of name/value couples and as plain fields:

```json
"customFields": [
{
    "name": "campo dropdown",
    "value": "item 2"
},
{
    "name": "campo text",
    "value": "testo2"
},
{
    "name": "campo number",
    "value": "2"
},
{
    "name": "campo data",
    "value": "14/4/2018, 12:00:00"
},
{
    "name": "campo checkbox",
    "value": "true"
}
],
"campo dropdown": "item 2",
"campo text": "testo2",
"campo number": "2",
"campo data": "14/4/2018, 12:00:00",
"campo checkbox": "true"
```          

### Labels

Update: added in version 1.9.45, jsonLabels is an array of all labels (Trello data).

```json
"jsonLabels": [
	{	"id":"545e62d674d650d567b54a34","idBoard":"52f8f8302712d41520ee559a",
	"name":"Enhancement","color":"yellow"
	}
]
```

### Usage

Inside templates, we just reference our data object, for example:

![html_twig_trelloExport.png]({{ site.baseurl }}/images/html_twig_trelloExport.png)


## Further development

I'd like to add more templates, and waiting for your templates - I'm not a Twig expert, let me see what can be done with it!

I'm also adding Twig templates for Markdown and OPML export modes, that currently still use the "old version" code, without templates, and maybe more formats - it should be pretty easy to have Twig templates to build textual output, say a CSV or TXT file.

Please open issues at [GitHub](https://github.com/trapias/trelloExport/issues) if you have questions, suggestions, needs.


## Feedback
Your feedback is always welcome. If you have any problem please open an issue on [GitHub](https://github.com/trapias/trelloExport/issues), I'll do my best to fix it quickly.

## Donate?
If you wish to support the development of this tool, like Richard did (thanks again!), you can [make a donation](http://trapias.github.io/donate/).

## Download
You can now get TrelloExport from the Chrome Web Store at [this URL](https://chrome.google.com/webstore/detail/trelloexport/kmmnaeamjfdnbhljpedgfchjbkbomahp).

If you want the source version, get them on GitHub at [https://github.com/trapias/trelloExport](https://github.com/trapias/trelloExport), and follow the installation instructions in the readme.


