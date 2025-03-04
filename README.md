# Inception-of-Things Sample Application

This repository contains a **FastAPI** application that renders a dynamic HTML page using **Jinja2** templates. The page displays basic info such as:

* **App Name** and **App Version**
* **Pod ID** and **Node ID** (optional environment variables typically injected in a Kubernetes environment)

We provide multiple Docker images on Docker Hub under [lhutt42](https://hub.docker.com/r/lhutt42), each tagged with different **App/Version** identifiers. The project also includes Kubernetes manifests to demonstrate how to deploy the app onto a cluster.

## Available Docker Images on Docker Hub

We maintain four images for demonstration purposes, each referencing different **apps** or **versions**:

1. **App 1**, version `1.0.0`

```
lhutt42/lhutt-iot-app-one:1.0.0
```

2. **App 1**, version `2.0.0`

```
lhutt42/lhutt-iot-app-one:2.0.0
```

3. **App 2**, version `1.0.0`

```
lhutt42/lhutt-iot-app-two:1.0.0
```

4. **App 3**, version `1.0.0`

```
lhutt42/lhutt-iot-app-three:1.0.0
```

## Pulling and Running from Docker Hub

**Example**: To run **App 1**, version `1.0.0` on your local machine:

```bash
docker pull lhutt42/lhutt-iot-app-one:1.0.0
docker run -d -p 3000:3000 lhutt42/lhutt-iot-app-one:1.0.0
```

Then open http://localhost:3000 in your browser to see the FastAPI-powered page.

---

## Kubernetes Manifests

Within [`./manifest`](./manifests), you’ll find:

1. `deployment.yaml`
   * Creates a Kubernetes `Deployment` named **app** that runs your containerized FastAPI service.
   * Feel free to update the `image:` field to one of your Docker Hub tags:
     ```yaml
     containers:
       - name: app
         image: lhutt42/lhutt-iot-app-one:1.0.0
      ```
2. `service.yaml`
   * Exposes the Deployment internally as a `Service` named **app** on port **3000**.
3. `ingress.yaml`
   * Routes external traffic to the service.
   * By default, it uses `dev.local` as the hostname:
     ```yaml
     host: dev.local
     path: /
     backend:
       service:
         name: app
         port:
           name: web
     ```
   * Update your `/etc/hosts` or DNS to map `dev.local` to the IP where the Kubernetes ingress controller is listening.
