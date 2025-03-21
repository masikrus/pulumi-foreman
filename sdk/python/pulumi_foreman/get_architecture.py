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
    'GetArchitectureResult',
    'AwaitableGetArchitectureResult',
    'get_architecture',
    'get_architecture_output',
]

@pulumi.output_type
class GetArchitectureResult:
    """
    A collection of values returned by getArchitecture.
    """
    def __init__(__self__, __meta_=None, id=None, name=None, operatingsystem_ids=None):
        if __meta_ and not isinstance(__meta_, bool):
            raise TypeError("Expected argument '__meta_' to be a bool")
        pulumi.set(__self__, "__meta_", __meta_)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if operatingsystem_ids and not isinstance(operatingsystem_ids, list):
            raise TypeError("Expected argument 'operatingsystem_ids' to be a list")
        pulumi.set(__self__, "operatingsystem_ids", operatingsystem_ids)

    @property
    @pulumi.getter
    def __meta_(self) -> bool:
        return pulumi.get(self, "__meta_")

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

    @property
    @pulumi.getter(name="operatingsystemIds")
    def operatingsystem_ids(self) -> Sequence[int]:
        return pulumi.get(self, "operatingsystem_ids")


class AwaitableGetArchitectureResult(GetArchitectureResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetArchitectureResult(
            __meta_=self.__meta_,
            id=self.id,
            name=self.name,
            operatingsystem_ids=self.operatingsystem_ids)


def get_architecture(name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetArchitectureResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('foreman:index/getArchitecture:getArchitecture', __args__, opts=opts, typ=GetArchitectureResult).value

    return AwaitableGetArchitectureResult(
        __meta_=pulumi.get(__ret__, '__meta_'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        operatingsystem_ids=pulumi.get(__ret__, 'operatingsystem_ids'))
def get_architecture_output(name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetArchitectureResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('foreman:index/getArchitecture:getArchitecture', __args__, opts=opts, typ=GetArchitectureResult)
    return __ret__.apply(lambda __response__: GetArchitectureResult(
        __meta_=pulumi.get(__response__, '__meta_'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        operatingsystem_ids=pulumi.get(__response__, 'operatingsystem_ids')))
