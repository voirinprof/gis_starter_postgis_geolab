# 🗺️ GIS Starter with PostGIS & Python (DevContainer)

This project provides a ready-to-use development environment for working with spatial databases (PostgreSQL/PostGIS) and Python. It is ideal for classes, workshops, or personal geospatial projects using GitHub Codespaces or Visual Studio Code with the Dev Containers extension.

## 🚀 Features

- 📦 Preconfigured **PostgreSQL with PostGIS** for spatial data management.
- 🐍 **Python 3** with common geospatial libraries.
- ⚙️ DevContainer configuration for a reproducible development setup.

## 🧰 Technologies Used

- [PostgreSQL](https://www.postgresql.org/) with [PostGIS](https://postgis.net/)
- [Python 3](https://www.python.org/)
- [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/)
- [Visual Studio Code](https://code.visualstudio.com/) with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- [GitHub Codespaces](https://github.com/features/codespaces) (optional)

## 🛠️ Requirements (local)

> use github codespace instead

- [Docker](https://www.docker.com/) installed on your system.
- [Visual Studio Code](https://code.visualstudio.com/) with the Dev Containers extension.
- A GitHub account to use Codespaces (optional).

## 🚀 Quick Start

### 🔁 Clone the Repository

```bash
git clone https://github.com/voirinprof/gis_starter_postgis_geolab.git
cd gis_starter_postgis_geolab
```

### 🐳 Open in a DevContainer

1. Open the folder in Visual Studio Code.
2. When prompted, click “Reopen in Container.”
3. Wait for the environment to build and initialize.

### 💻 Or Use GitHub Codespaces

1. Click the green **"Code"** button on the GitHub repo.
2. Choose **"Open with Codespaces"** > **"New codespace"**.
3. The environment will be ready in a few minutes.

## 📂 Project Structure

```
gis_starter_postgis_geolab/
├── .devcontainer/
│   ├── devcontainer.json
│   ├── Dockerfile
│   ├── requirements.txt
│   └── docker-compose.yml
├── scripts/
│   └── ... some scripts in python
└── README.md
```

- `.devcontainer/` : Configuration for the development environment.
- `appscripts/` : Folder for your Python code.

## 🧪 pgAdmin4

You have access in a browser to `pgAdmin4`. Go in the tab `foward ports`, click on `Open in browser` for the port `5050`.

## 📚 Useful Resources

- [Official PostGIS Documentation](https://postgis.net/documentation/)
- [VS Code Dev Containers Guide](https://code.visualstudio.com/docs/devcontainers/containers)
- [GitHub Codespaces Intro](https://docs.github.com/en/codespaces)

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request to improve the setup.