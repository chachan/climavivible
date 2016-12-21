Citizen's Climate Lobby Panamá
==========

Citizen's Climate Lobby Panamá is a project developed in [HUGO](https://gohugo.io)
- - -
## Installation

Simply download and install the appropriate version for your platform from [Hugo Releases](https://github.com/spf13/hugo/releases).
- - -

## Run the project local

To run the local project follow these steps:

* Clone the repository:

      git clone --recursive https://leonelz@bitbucket.org/mobydev/hugo-demo.git

* Located in the root folder of the project and run

      hugo # Build project

      hugo server # Run project

* Open project on browser

      localhost:1313
- - -

## Deploy project

### Prerequisites

The project is hosted on the **google app engine** service. You must start **gcloud** and have project permissions.

Need to install on your local machine [CLOUD SDK](https://cloud.google.com/sdk/)

In the link you can follow the steps for its installation. You have to install also the plugin for python **google-cloud-sdk-app-engine-python**.

### Deploy

* You can run development server locally and check your static pages by following command

      dev_appserver.py ./

* Deploy the public directory to Google App Engine

      ./deploy.sh

* Open project on browser [https://hugodemostack.appspot.com/](https://hugodemostack.appspot.com/)
