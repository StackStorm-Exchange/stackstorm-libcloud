from lib.actions import BaseAction

__all__ = [
    'ListDNSZonesAction'
]


class ListDNSZonesAction(BaseAction):
    api_type = 'dns'

    def run(self, credentials, extra_kwargs=None):
        extra_kwargs = extra_kwargs or {}
        driver = self._get_driver_for_credentials(credentials=credentials)
        zones = driver.list_zones(**extra_kwargs)
        return self.resultsets.formatter(zones)
