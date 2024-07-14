# Infrastructure
Repository for managing my home infrastructure using Ansible.

**This will not work for you**, as the files are heavily customized for my setup, and you'd be missing the vault as well.
Feel free to use anything here for reference. I'm still learning as well :)

## Specifications
- [QNAP TS-453D](https://www.qnap.com/en/product/ts-453d) (16 GB replaced) running [TrueNAS SCALE](https://www.truenas.com/truenas-scale/) (Bluefin 22.12)\
  2x4 TB CMR (WD Red) in MIRROR as storage, 1 TB SDD as app data, and 500 GB SSD as boot.\
  Cobia (23.10) and Dragonfish (24.04) removed Docker, which is why I'm stuck on Bluefin.
  Electric Eel (24.10) will remove K3s and add Docker back, making it potentially viable to update again.
- [AVM FRITZ!Box 4060](https://en.avm.de/products/fritzbox/fritzbox-4060/), however, I'm thinking about replacing it with a [UniFi Dream Machine SE](https://eu.store.ui.com/eu/en/products/udm-se) soon.

An important thing to note is that running custom software on QNAP devices will cause the exhaust fan to no longer work.\
I learned this the hard way when the CPU overheated once. Since I immediately installed TrueNAS upon getting it, I always thought the fan was just *that* silent.\
Thankfully, [someone](https://github.com/Stonyx) has made a kernel module called [QNAP-EC](https://github.com/Stonyx/QNAP-EC) which allows you to control it via `fancontrol`.

## Backups
The data pool consists of 2 hard drives in a MIRROR setup, ensuring data redundancy if one drive fails.\
The most important volume mounts are backed up nightly at 5:00 AM using TrueNAS Cloud Sync to B2.\
**This setup can still be improved**, since I don't test backup restores yet, nor are any of the PCs backed up.

## Services
These are the services I run and use, which are also setup by this Ansible playbook.
| Name                                                       | Description                                                         |
|------------------------------------------------------------|---------------------------------------------------------------------|
| [Traefik](https://traefik.io/traefik)                      | Application reverse proxy                                           |
| [AdGuard Home](https://github.com/AdguardTeam/AdGuardHome) | Network-wide ads & trackers blocking DNS server                     |
| [Dozzle](https://dozzle.dev)                               | Container inspection with literally the best UI                     |
| [Sonarr](https://sonarr.tv)                                | Automated TV show management                                        |
| [Radarr](https://radarr.video)                             | Automated movie management                                          |
| [Lidarr](https://lidarr.audio)                             | Automated music management                                          |
| [Prowlarr](https://github.com/Prowlarr/Prowlarr)           | Universal indexer management                                        |
| [Recyclarr](https://github.com/recyclarr/recyclarr)        | Automatically sync TRaSH Guides to your Sonarr and Radarr instances |
| [qBittorrent](https://hotio.dev/containers/qbittorrent)    | BitTorrent client with VueTorrent Web UI                            |
| [Gluetun](https://github.com/qdm12/gluetun)                | VPN client in a thin Docker container                               |
| [Jellyseerr](https://github.com/Fallenbagel/jellyseerr)    | Media discovery and request management                              |
| [Jellyfin](https://jellyfin.org)                           | The Free Software Media System                                      |

## Usage
**This playbook expects to be ran on TrueNAS Bluefin 22.12, any other version does not work.**

You must do initial bootstrapping yourself by enabling SSH and adding your SSH key in the web UI.
Make sure to enable the Docker daemon as well using [this hack](https://gist.github.com/tprelog/7988dc6b196775f33929beb19f0090d7).
You might have to add your user account to the `docker` group via the TrueNAS Web UI.
Change the web UI port from `80` to `81` and `443` to `444`. This is what Traefik expects and requires.

**Ensure you have Ansible installed first**, you can find the instructions [here](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html).

1. Install the required roles: `ansible-galaxy install -r requirements.yml --force`
2. Add the vault password to `.vault_password`, you might have to create it.
3. Run the playbook: `ansible-playbook main.yml`

## Development
Install the required roles as mentioned above and run `pnpm install` to install the Git pre-commit hooks.
Make sure to not commit your vault unencrypted :)
