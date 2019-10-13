from lib.actions import BaseAction

__all__ = [
    'ListImagesAction'
]


class ListImagesAction(BaseAction):
    api_type = 'compute'

    def run(self, credentials, extra_kwargs=None):
        extra_kwargs = extra_kwargs or {}
        driver = self._get_driver_for_credentials(credentials=credentials)
        images = driver.list_images(**extra_kwargs)
        return self.resultsets.formatter(images)
