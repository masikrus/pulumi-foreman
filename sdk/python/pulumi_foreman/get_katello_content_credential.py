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
from . import _utilities

__all__ = [
    'GetKatelloContentCredentialResult',
    'AwaitableGetKatelloContentCredentialResult',
    'get_katello_content_credential',
    'get_katello_content_credential_output',
]

@pulumi.output_type
class GetKatelloContentCredentialResult:
    """
    A collection of values returned by getKatelloContentCredential.
    """
    def __init__(__self__, content=None, id=None, name=None):
        if content and not isinstance(content, str):
            raise TypeError("Expected argument 'content' to be a str")
        pulumi.set(__self__, "content", content)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def content(self) -> str:
        return pulumi.get(self, "content")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")


class AwaitableGetKatelloContentCredentialResult(GetKatelloContentCredentialResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKatelloContentCredentialResult(
            content=self.content,
            id=self.id,
            name=self.name)


def get_katello_content_credential(name: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKatelloContentCredentialResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('foreman:index/getKatelloContentCredential:getKatelloContentCredential', __args__, opts=opts, typ=GetKatelloContentCredentialResult).value

    return AwaitableGetKatelloContentCredentialResult(
        content=pulumi.get(__ret__, 'content'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'))
def get_katello_content_credential_output(name: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetKatelloContentCredentialResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('foreman:index/getKatelloContentCredential:getKatelloContentCredential', __args__, opts=opts, typ=GetKatelloContentCredentialResult)
    return __ret__.apply(lambda __response__: GetKatelloContentCredentialResult(
        content=pulumi.get(__response__, 'content'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name')))
