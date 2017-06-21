# Libcloud Integration Pack

This pack allows you to integrate with
[Apache Libcloud](http://libcloud.apache.org/).

## Configuration

Copy the example configuration in [libcloud.yaml.example](./libcloud.yaml.example)
to `/opt/stackstorm/configs/libcloud.yaml` and edit as required.

It must contain a credentials set for the Cloud providers you wish to use.
Actions take a `credentials` parameter to specify which credentials to use.

Example configuration:

```yaml
---
  credentials:
    ec2_prod_us_west_1:
      api_key: "username"
      api_secret: "password"
      type: "compute"
      provider: "ec2_us_east"
      region: "us-west-1"
    rax_dev_iad:
      api_key: "username"
      api_secret: "password"
      type: "compute"
      provider: "rackspace"
      region: "iad"
```

**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`

## Actions

The following actions are supported:

### Virtual Machines / Servers

* Create a new VM - `create_vm`
* Reboot a VM - `reboot_vm`
* Stop a VM - `stop_vm`
* Start a VM - `start_vm`
* Destroy a VM - `destroy_vm`

### Storage

* Upload a file to a container - `upload_file`
* Enable CDN for a container and retrieve container CDN URL -
  `enable_cdn_for_container`
* Retrieve CDN URL of a CDN enabled container - `get_container_cdn_url`
* Retrieve CDN URL for an object which is stored in a CDN enabled container -
  `get_object_cdn_url`

### DNS

* Create a new DNS record - `create_dns_record`
* Delete an existing DNS record - `delete_dns_record`
