[![Ansible Collection](https://img.shields.io/badge/dynamic/json?color=orange&style=flat&label=collection&prefix=v&url=https://galaxy.ansible.com/api/v3/collections/tonyskapunk/beat/&query=highest_version.version)](https://galaxy.ansible.com/tonyskapunk/beat)
[![GitHub tag](https://img.shields.io/github/tag/tonyskapunk/beat-ansible-collection.svg)](https://github.com/tonyskapunk/beat-ansible-collection/tags)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/tonyskapunk/beat-ansible-collection)](https://github.com/tonyskapunk/beat-ansible-collection/tags)
[![GitHub Contributors](https://img.shields.io/github/contributors/tonyskapunk/beat-ansible-collection)](https://github.com/tonyskapunk/beat-ansible-collection/tags)

[![Ansible Galaxy](https://github.com/tonyskapunk/beat-ansible-collection/actions/workflows/publish.yml/badge.svg)](https://github.com/tonyskapunk/beat-ansible-collection/actions/workflows/publish.yml)
[![Module Testing](https://github.com/tonyskapunk/beat-ansible-collection/actions/workflows/module-testing.yml/badge.svg)](https://github.com/tonyskapunk/beat-ansible-collection/actions/workflows/module-testing.yml)
[![Role testing](https://github.com/tonyskapunk/beat-ansible-collection/actions/workflows/role-testing.yml/badge.svg)](https://github.com/tonyskapunk/beat-ansible-collection/actions/workflows/role-testing.yml)

# Ansible Collection - tonyskapunk.beat

Based on the [beat](https://github.com/tonyskapunk/beat) project.

Documentation for the collection.

This collection provides a module and a role to exemplify the use of them through collections

## Ansible version compatibility

The collection is tested and supported with: `ansible >= 2.9`

## Installing the collection

```shell
ansible-galaxy collection install tonyskapunk.beat
```

You can also include it in a `requirements.yml` file and install it via ansible-galaxy collection install -r `requirements.yml`, using the format:

```yaml
---
collections:
  - name: tonyskapunk.beat
```

## Using this collection

You can call modules by their Fully Qualified Collection Namespace (FQCN), such as `tonyskapunk.beat.beat`:

```yaml
- name: Using beat
  hosts: localhost
  tasks:
    - name: Get internet time
      tonyskapunk.beat.beat:
        centibeats: true
      register: beats
```

or you can add full namespace and collection name in the `collections` element in your playbook

```yaml
- name: Using grafana collection
  hosts: localhost
  collection:
    - tonyskapunk.beat
  tasks:
    - name: Get internet time
     beat:
        centibeats: true
      register: beats
```

## License

GPL-3.0-or-later
