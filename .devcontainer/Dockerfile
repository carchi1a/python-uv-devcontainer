# syntax=docker/dockerfile:1

ARG UBUNTU_VERSION=24.04
ARG UV_VERSION=0.8.22
ARG USERNAME=dev
ARG UID=1000
ARG GID=${UID}
ARG PYTHON_VERSION=3.13
ARG VENV_LOCATION=/opt/.venv

FROM ghcr.io/astral-sh/uv:${UV_VERSION} AS uv

FROM ubuntu:${UBUNTU_VERSION}

# Remove default ubuntu user https://askubuntu.com/questions/1513927/ubuntu-24-04-docker-images-now-includes-user-ubuntu-with-uid-gid-1000
RUN userdel -r ubuntu || echo "No ubuntu user to remove"

ARG USERNAME
ARG UID
ARG GID
ARG PYTHON_VERSION
ARG VENV_LOCATION

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && \
    apt install --no-install-recommends -y \
	    software-properties-common \
	    curl \
      git \
      gpg-agent \
      sudo \
      unzip \
      zlib1g \
      zsh \
    && rm -rf /var/lib/apt/lists/* \
    && curl -L https://github.com/jqlang/jq/releases/download/jq-1.7.1/jq-linux-amd64 -o /usr/bin/jq \
    && chmod +x /usr/bin/jq

# Create the user and setup zsh as default shell
RUN groupadd --gid ${GID} ${USERNAME} \
  && useradd --uid ${UID} --gid ${GID} -m -G sudo -s /bin/zsh ${USERNAME} \
  && mkdir -p /etc/sudoers.d \
  && echo "${USERNAME} ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/${USERNAME} \
  && chmod 0440 /etc/sudoers.d/${USERNAME} \
  && mkdir -p ${VENV_LOCATION} \
  && chown -R ${GID}:${UID} ${VENV_LOCATION}

# install & setup oh my zsh
RUN su ${USERNAME} -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" \
  && echo "alias pip='uv pip'" > /home/${USERNAME}/.oh-my-zsh/custom/aliases.zsh

COPY --from=uv /uv /uvx /bin/
  
USER ${USERNAME}

RUN uv venv ${VENV_LOCATION} --python ${PYTHON_VERSION}

ENV PATH=${VENV_LOCATION}/bin:${PATH}
ENV VENV_LOCATION=${VENV_LOCATION}

CMD ["/bin/zsh"]
