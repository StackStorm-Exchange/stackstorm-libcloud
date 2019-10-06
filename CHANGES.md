# Changelog

## v0.5.0

- Upgrade to apache-libcloud ``v2.6.0``. #8

- Fix ``reboot_vm``, ``destroy_vm``, ``start_vm`` and other VM actions so they work correctly with
  the Google Compute Engine (GCE) driver. #8

## v0.4.3

- Update pack so it also works with providers such as Vultr which only take a single credential
  argument - either ``api_key`` or ``api_secret``. Previously it only worked with providers which
  took both.

## v0.4.0

- Updated action `runner_type` from `run-python` to `python-script`.

## v0.3.0

* Migrate to `config.schema.yaml`.

## v0.2.0

* Exoscale provider
  [Sebastien Goasguen]

## v0.1.0

* Initial release
