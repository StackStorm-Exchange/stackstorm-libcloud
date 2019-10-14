from lib.actions import BaseAction

__all__ = [
    'ListContainerClustersAction'
]


class ListContainerClustersAction(BaseAction):
    api_type = 'container'

    def run(self, credentials, extra_kwargs=None):
        extra_kwargs = extra_kwargs or {}
        driver = self._get_driver_for_credentials(credentials=credentials)
        members = driver.list_clusters(**extra_kwargs)
        return self.resultsets.formatter(members)
