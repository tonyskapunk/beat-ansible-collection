# beat_role

A role to print the Internet Time in beats.

## Input Variables

| Var    | Type |  Value  | Required | Description |
| ------ | ---- | ------- | -------- | ----------- |
| beat_role_centibeats | bool | true | No | Whether to return the beat time using centibeats |

## Examples

- At the play level, with default values

```yaml
- name: Beats
  hosts: localhost
  roles:
     - role: tonyskapunk.beat.beat_role
```

- As a task, without centibeats

```yaml
- name: Print beat time
  ansible.builtin.include_role:
    name: tonyskapunk.beat.beat_role
  vars:
    beat_role_centibeats: false
```

## License

GPL 3.0
