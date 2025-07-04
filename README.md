# python-uv-devcontainer

A Ubuntu-based skeleton devcontainer for python development that uses [UV](https://docs.astral.sh/uv/guides/install-python/#using-existing-python-versions) to manage python installation and dependencies.

## VSCode Integration Options

The options configured in [devcontainer.json](./.devcontainer/devcontainer.json) add some helpful features like VSCode Extensions and local environment mirroring to improve Developer Experience.

### VSCode Extensions

* [Better Comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments)
* [Python Language Support](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
* [Python Intellisense](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
* [Even Better TOML](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml)
* [Auto Docstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)

### Local Environment Mirroring

User-defined aliases and default HISTFILE are mounted to the devcontainer via zsh's and oh-my-zsh. 