# Just A Route Generator (JARGen)

## Table of Contents
<!-- TOC -->
* [Just A Route Generator (JARGen)](#just-a-route-generator-jargen)
  * [Table of Contents](#table-of-contents)
  * [What does this package do?](#what-does-this-package-do)
  * [Use Cases/Models](#use-casesmodels)
  * [Features](#features)
    * [Supported Platforms](#supported-platforms)
    * [Planned Platforms](#planned-platforms)
    * [Supported Path Attributes](#supported-path-attributes)
    * [Planned Functionality](#planned-functionality)
  * [Some Important Notes](#some-important-notes)
  * [Usage Instructions](#usage-instructions)
    * [Requirements](#requirements)
  * [Configuration Reference](#configuration-reference)
  * [Contributions](#contributions)
<!-- TOC -->

## What does this package do?

JARGen (pronounced jar-jen) is... exactly what it says on the tin - it's just a route generator! Ironic, huh? No jargon here at all!

Tired of creating six million loopbacks every time you need to pump a bunch of routes into a routing protocol for your lab environment? Be tired no more! This package generates an arbitrary number of random routes, alongside random route attributes (subject to any constraints defined in your configuration for this package), and allows you to export those routes using a variety of methods.

To be clear, if you need, like, two routes, don't bother with this package. Use this as the rule of thumb - if you need to create so many routes, your fingers will kill you tomorrow if you try to do so manually, look no further than this package!

Other than that...nope, that's it! My guiding mantra throughout the development of this tool was to make something that you can use for a few minutes and then move out of the way. After all, if you're using this tool, you're trying to lab something interesting...like BGP! A route generator? That's not interesting!

As such, even though there's a lot of customization potential with this tool, I've made sure to strike a balance between being flexible in many use cases and making something that's not overly complicated. At minimum, very little configuration is required to just let JARGen take the wheel and generate some random routes!

## Use Cases/Models

There are a couple of ways you can use this package. Of course, these are all just suggestions and you are free to use it as you wish. 

* Export all generated routes and associated path attributes as configuration commands. From there, you can add those configuration commands to any ol' router in your lab environment that you want to serve as the source of those routes.
* Export a Docker image containing an instance of the BIRD internet routing daemon that is preconfigured with all of the routes and neighbors that you need and import it onto your desired container host using the `docker load -i <file>` command (e.g., for Containerlab/native Docker use cases) or imported into a network emulation platform (e.g., Cisco Modeling Labs or EVE-NG). From there, you can start a new container using this image for any environment where you need a quick and dirty source of random/"internet" routes!

## Features
### Supported Platforms
* Cisco IOS/IOS-XE
* Cisco IOS-XR
* Juniper Junos
* Linux routing (FRR/BIRD)
* BIRD container

### Planned Platforms
* Nokia SR-OS/SR Linux

### Supported Path Attributes
* NEXT-HOP
* AS-PATH
* Communities
* Origin

### Planned Functionality
* Import routes from BGPdump/MRT format
* Allow definition of basic policy inside of config.yml file (e.g., to selectively apply path attributes)

## Some Important Notes
* **Specifically for the container option:** by design, there is a constraint built into the configuration validation that requires all peerings between the bgpbox and the peer router to be eBGP. Put another way, the local ASN and any neighbor ASN(s) defined in the config file **MUST** be different. This restriction solely exists to make things easier, since it means that we don't have to consider any wonky iBGP behaviors, in terms of propagating the generated routes further into the lab network. Also, it means that we can just consider eBGP path attributes (i.e., no local preference).

## Usage Instructions

### Requirements
Before you can use JARGen, there are some prerequisites that need to be satisfied:
* Since JARGen operates as a Python package, a valid Python 3.x interpreter must be installed on the system that will be running JARGen. Given the simple nature of this package, any reasonably modern version of Python 3 will do. For the record, this package was tested on Python 3.12.
* JARGen must be installed from the PyPI using the `pip install jargen` (or the `python -m pip install jargen`) command. It's recommended that you do this inside of a virtual environment. Note that, if you do, you'll need to activate the virtual environment (i.e., by running the `source <venv>/bin/activate` command) before you can execute JARGen
* **Only for container image creation and MRT parsing use cases**: Docker must be installed and accessible by the user executing JARGen. Consider that this may mean you need to run JARGen with `sudo` privileges. When using JARGen for a use case that requires Docker, it's recommended that you run JARGen on a Linux-based machine.

From there, assuming you've satisfied all of the aforementioned prerequisites, it's as simple as running the `jargen` (or `python -m jargen`) command! Note, however, that JARGen requires a YAML configuration file to be referenced during execution. Check out the [configuration reference](#configuration-reference) section below for more details on what options exist inside of the configuration file.

To feed this configuration file to JARGen during execution, it's as easy as including `[-c|--configfile] <path to your YAML config file here>` after `jargen` in the command. That's it! It's not just that you don't need to specify any additional options - there ARE no additional options to be specified! All of the settings the tool needs are inside of the YAML file.

## Configuration Reference

| Syntax | Description |
| ------ | ----------- |

## Contributions

Do you have anything you want to contribute to JARGen to make it better? Awesome! I know that I probably haven't covered EVERY possible inch of ground, so if you want to develop additions, feel free to fork the repo and then open a PR with your changes. I'll try to review them ASAP.