from lib.actions import BaseAction

__all__ = [
    'ListBalancersAction'
]


class ListBalancersAction(BaseAction):
    api_type = 'loadbalancer'

    def run(self, credentials, extra_kwargs=None):
        extra_kwargs = extra_kwargs or {}
        driver = self._get_driver_for_credentials(credentials=credentials)
        members = driver.list_balancers(**extra_kwargs)
        return self.resultsets.formatter(members)
