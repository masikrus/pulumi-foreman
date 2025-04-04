# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities

import types

__config__ = pulumi.Config('foreman')


class _ExportableConfig(types.ModuleType):
    @property
    def client_auth_negotiate(self) -> Optional[bool]:
        """
        Whether or not the client should try to authenticate through the HTTP negotiate mechanism. Defaults to `false`.
        """
        return __config__.get_bool('clientAuthNegotiate')

    @property
    def client_password(self) -> Optional[str]:
        """
        The username to authenticate against Foreman. This can also be set through the environment variable
        `FOREMAN_CLIENT_PASSWORD`. Defaults to `""`.
        """
        return __config__.get('clientPassword') or _utilities.get_env('FOREMAN_CLIENT_PASSWORD')

    @property
    def client_tls_insecure(self) -> Optional[bool]:
        """
        Whether or not to verify the server's certificate. Defaults to `false`.
        """
        return __config__.get_bool('clientTlsInsecure')

    @property
    def client_username(self) -> Optional[str]:
        """
        The username to authenticate against Foreman. This can also be set through the environment variable
        `FOREMAN_CLIENT_USERNAME`. Defaults to `""`.
        """
        return __config__.get('clientUsername') or _utilities.get_env('FOREMAN_CLIENT_USERNAME')

    @property
    def location_id(self) -> Optional[int]:
        """
        The location for all resources requested and created by the providerDefaults to "0". Set organization_id and location_id
        to a value < 0 if you need to disable Locations and Organizations on Foreman older than 1.21
        """
        return __config__.get_int('locationId') or _utilities.get_env_int('FOREMAN_LOCATION_ID')

    @property
    def organization_id(self) -> Optional[int]:
        """
        The organization for all resource requested and created by the Provider Defaults to "0". Set organization_id and
        location_id to a value < 0 if you need to disable Locations and Organizations on Foreman older than 1.21
        """
        return __config__.get_int('organizationId') or _utilities.get_env_int('FOREMAN_ORGANIZATION_ID')

    @property
    def provider_logfile(self) -> Optional[str]:
        return __config__.get('providerLogfile')

    @property
    def provider_loglevel(self) -> Optional[str]:
        """
        The level of verbosity for the provider's log file. This setting determines which types of log messages are written and
        which are ignored. Possible values (from most verbose to least verbose) include 'DEBUG', 'TRACE', 'INFO', 'WARNING',
        'ERROR', and 'NONE'. The provider's logs will be written to the location specified by `provider_logfile`. This can also
        be set through the environment variable `FOREMAN_PROVIDER_LOGLEVEL`. Defaults to `'INFO'`.
        """
        return __config__.get('providerLoglevel')

    @property
    def server_hostname(self) -> Optional[str]:
        """
        The hostname / IP address of the Foreman REST API server
        """
        return __config__.get('serverHostname') or _utilities.get_env('FOREMAN_SERVER_HOSTNAME')

    @property
    def server_protocol(self) -> Optional[str]:
        """
        The protocol the Foreman REST API server is using for communication. Defaults to `"https"`.
        """
        return __config__.get('serverProtocol') or _utilities.get_env('FOREMAN_PROTOCOL')

