from lib.actions import BaseAction

__all__ = [
    'ListVMsAction'
]


class ListVMsAction(BaseAction):
    api_type = 'compute'

    def run(self, credentials, extra_kwargs=None):
        extra_kwargs = extra_kwargs or {}
        driver = self._get_driver_for_credentials(credentials=credentials)
        vms = driver.list_nodes(**extra_kwargs)

        return self.resultsets.formatter(vms)
