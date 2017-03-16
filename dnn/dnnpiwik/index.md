---
layout: default
categories: dnn
title: DNNPiwik
subtitle: Piwik Analytics for DNN
description: DNNPiwik is a module for DotNetNuke that allows you to easily integrate the Piwik analytics tracking script in any page, choosing which roles you don't want to track (tipically Administrators).
---

<h1>{{page.title}}</h1>
<h2>{{ page.subtitle }}</h2>

DNNPiwik is a module for DotNetNuke that allows you to easily integrate the <a href="http://piwik.org/integrate/" target="_blank">Piwik analytics</a> tracking script in any page, choosing which roles you don't want to track (tipically Administrators).

<div class="addthis_native_toolbox"></div>

## Download

DNNPiwik is on Github, fork it at [https://github.com/trapias/DNNPiwik](https://github.com/trapias/DNNPiwik "https://github.com/trapias/DNNPiwik") or download a [release package](https://github.com/trapias/DNNPiwik/releases) for easy installation via Dnn extensions manager.

## Installation

Grab the release package and install DnnPiwik as any other Dnn module, using Dnn extensions manager. Then add a DnnPiwik module instance to any page and open module settings to configure it.

## Setup

Configuration is very easy: type your Piwik Site ID in "Piwik Site ID", and the URL (withour protocol information!) in "Piwik Host". Optionally select roles you do not want to track.

![DNNPiwik Settings]({{site_url}}/images/DNNPiwik_Settings.png)

## Comments

{% include disqus.html disqus_identifier=page.disqus_identifier %}
