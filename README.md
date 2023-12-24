# Dependency Confusion Demonstration Laboratory

Welcome to the Dependency Confusion Demonstration Laboratory. This lab is designed to showcase the concept of dependency confusion, a security vulnerability that can arise when using package managers like pip.

## Overview

Dependency confusion occurs when a package manager, such as pip, resolves and installs dependencies based on different sources, leading to unintended and potentially insecure installations. In this lab, we will simulate a dependency confusion scenario to illustrate the risks associated with incorrect package resolution.

## Instructions

Follow the steps below to simulate the dependency confusion scenario:

### 1. Setup the Local Package Server

Run the following command in the "packages" folder to start a local package server:

```bash
cd packages
```
```bash
python -m http.server
```

This will create a simple HTTP server to serve package files from the "packages" directory.

### 2. Simulate Dependency Confusion

Now, users are instructed to install the dcvalidator package with version 2.0.0 from the local package server. However, if version 2.0.0 is not present locally, pip may attempt to fetch it from the default Python Package Index (PyPI).

```bash
pip install --extra-index-url http://localhost:8000 dcvalidator
```

Note: If version 2.0.0 is present in the "packages/dcvalidator" directory, it will be installed. Otherwise, pip may fetch a higher version from PyPI, potentially leading to a security vulnerability.

### 3. Observations

Users may notice that pip resolves the dependency to version 1.0.3 from PyPI instead of version 1.0.1 available locally. This is due to pip selecting the highest available version, which may be unintended.

### 4. Security Implications

- If the dcvalidator package is installed locally, it is considered safe. In this case, running validator.py will work as usual without any security risks.

- If the dcvalidator package is installed from PyPI, it may point to an attacker's malicious version. Simulate the risk by running validator.py after the installation. The code in validator.py will run OS commands and return the directory output, illustrating how an attacker can execute malicious actions.

```bash
python validator.py
```

Dependency confusion scenarios can have security implications as they might lead to the installation of unintended or malicious packages. It's crucial to be aware of the package resolution mechanism and ensure that dependencies are resolved from trusted sources.
Disclaimer

This laboratory is designed for educational purposes only. Participants should be cautious when running commands and understand the potential security risks associated with dependency confusion. Do not use these techniques in a production environment.

## License

`DependencyConfusionLab` is made with ♥  by [Wation](https://github.com/TheWation) and it's released under the `Apache License 2.0` license.