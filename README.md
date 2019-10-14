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
    gce:
      api_key: "service account email"
      api_secret: "path to pem file"
      type: "compute"
      provider: "gce"
      # Arbitrary driver constructor arguments can be passed by utilizing extra_kwargs
      # config option
      extra_kwargs:
        project: "your project id"
        datacenter: "us-central1-a"
```

**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`

## Actions

The following actions are supported:

### Virtual Machines / Servers

* List available VMs - ``list_vms``
* List available VM sizes - ``list_sizes``
* List available VM images - ``list_images``
* Create a new VM - ``create_vm``
* Reboot a VM - ``reboot_vm``
* Stop a VM - ``stop_vm``
* Start a VM - ``start_vm``
* Destroy a VM - ``destroy_vm``
* Import public SSH key - ``import_public_ssh_key``

### Storage

* Upload a file to a container - ``upload_file``
* Enable CDN for a container and retrieve container CDN URL -
  ``enable_cdn_for_container``
* Retrieve CDN URL of a CDN enabled container - ``get_container_cdn_url``
* Retrieve CDN URL for an object which is stored in a CDN enabled container -
  ``get_object_cdn_url``

### DNS

* Create a new DNS record - ``create_dns_record``
* Delete an existing DNS record - ``delete_dns_record``
* List DNS records for a particual zone ``list_dns_records``
* List available DNS zones - ``list_dns_zones``

### LoadBalancer

* Attach member to the loadbalancer - ``balancer_attach_member``
* List load balancer members - ``balancer_list_members``
* Create a new load balancer - ``create_balancer``
* List load balancers - ``list_balancers``

## Container as a Service

* Create new container cluster - ``create_container_cluster``
* Deploy a new container to a cluster - ``deploy_container``
* List available container clusters - ``list_container_clusters``
* List available containers in a cluster - ``list_container_clusters``
* Start a container - ``start_container``
* Stop a container - ``stop_container``
* Restart a container - ``restart_container``

## Passing driver specific arguments to the action

Version ``v0.6.0`` of this pack added support for new ``extra_kwargs`` parameter to all the pack
actions.

With this parameter, user can specify arbitrary dictionary of additional keyword arguments which
are passed to the underlying Libcloud driver method.

For example:

```bash
st2 run libcloud.destroy_vm credentials=gce_dev vm_id=12346, extra_kwargs='{"sync": false}'
```

Keep in mind that most of those custom arguments are driver specific so you should avoid them
and only utilize standard parameters if you care about portability across multiple providers.
