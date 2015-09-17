# -*- coding: utf-8 -*-

from django.conf import settings


if settings.REST_FRAMEWORK['DEFAULT_VERSIONING_CLASS'] == 'rest_framework.versioning.URLPathVersioning':
    default_version = settings.REST_FRAMEWORK['DEFAULT_VERSION']

    def set_default_version(params):
        for param in params:
            if param['name'] == 'version' and 'defaultValue' not in param:
                param['defaultValue'] = default_version

else:
    def set_default_version(params):
        pass
