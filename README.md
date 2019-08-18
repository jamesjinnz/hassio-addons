Hass.io add-on experiments
--------------------------

These are some random experiments for Hass.io add-ons.

## How to add repository to Hass.io

[Follow repository installation instructions](https://home-assistant.io/hassio/installing_third_party_addons/) with the url `https://github.com/AndBobsYourUncle/hassio-addons`.


## Build externally
```bash
sudo docker run --rm --privileged -v ~/.docker:/root/.docker homeassistant/amd64-builder --help
```

```bash
sudo docker run -it --rm --privileged \
    -v /var/run/docker.sock:/var/run/docker.sock -v ~/.docker:/root/.docker \
    homeassistant/amd64-builder --armhf -t google-assistant-webserver \
    -r https://github.com/carlba/hassio-addons -b 0.0.5 --docker-login
```

Note mounting the docker socket into the container prevents issues with layers on layers with 
layered filesystem such as overlayfs2.

[How to Publish hassio add-ons](https://developers.home-assistant.io/docs/en/hassio_addon_publishing.html#build-scripts-to-publish-add-ons-to-docker-hub)  

## Build locally
