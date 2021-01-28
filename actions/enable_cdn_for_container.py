from lib.actions import BaseAction

__all__ = [
    'EnableContainerCDN'
]


class EnableContainerCDN(BaseAction):
    api_type = 'storage'

    def run(self, credentials, container_name, extra_kwargs=None):
        extra_kwargs = extra_kwargs or {}
        driver = self._get_driver_for_credentials(credentials=credentials)

        container = driver.get_container(container_name=container_name)
        driver.enable_container_cdn(container=container, **extra_kwargs)
        container_cdn_url = driver.get_container_cdn_url(container=container)

        result = {'url': container_cdn_url}
        return result
