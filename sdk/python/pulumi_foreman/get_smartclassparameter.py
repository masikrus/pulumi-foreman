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
    'GetSmartclassparameterResult',
    'AwaitableGetSmartclassparameterResult',
    'get_smartclassparameter',
    'get_smartclassparameter_output',
]

@pulumi.output_type
class GetSmartclassparameterResult:
    """
    A collection of values returned by getSmartclassparameter.
    """
    def __init__(__self__, __meta_=None, id=None, parameter=None, puppetclass_id=None):
        if __meta_ and not isinstance(__meta_, bool):
            raise TypeError("Expected argument '__meta_' to be a bool")
        pulumi.set(__self__, "__meta_", __meta_)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if parameter and not isinstance(parameter, str):
            raise TypeError("Expected argument 'parameter' to be a str")
        pulumi.set(__self__, "parameter", parameter)
        if puppetclass_id and not isinstance(puppetclass_id, int):
            raise TypeError("Expected argument 'puppetclass_id' to be a int")
        pulumi.set(__self__, "puppetclass_id", puppetclass_id)

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
    def parameter(self) -> str:
        return pulumi.get(self, "parameter")

    @property
    @pulumi.getter(name="puppetclassId")
    def puppetclass_id(self) -> int:
        return pulumi.get(self, "puppetclass_id")


class AwaitableGetSmartclassparameterResult(GetSmartclassparameterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSmartclassparameterResult(
            __meta_=self.__meta_,
            id=self.id,
            parameter=self.parameter,
            puppetclass_id=self.puppetclass_id)


def get_smartclassparameter(parameter: Optional[str] = None,
                            puppetclass_id: Optional[int] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSmartclassparameterResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['parameter'] = parameter
    __args__['puppetclassId'] = puppetclass_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('foreman:index/getSmartclassparameter:getSmartclassparameter', __args__, opts=opts, typ=GetSmartclassparameterResult).value

    return AwaitableGetSmartclassparameterResult(
        __meta_=pulumi.get(__ret__, '__meta_'),
        id=pulumi.get(__ret__, 'id'),
        parameter=pulumi.get(__ret__, 'parameter'),
        puppetclass_id=pulumi.get(__ret__, 'puppetclass_id'))
def get_smartclassparameter_output(parameter: Optional[pulumi.Input[str]] = None,
                                   puppetclass_id: Optional[pulumi.Input[int]] = None,
                                   opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetSmartclassparameterResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['parameter'] = parameter
    __args__['puppetclassId'] = puppetclass_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('foreman:index/getSmartclassparameter:getSmartclassparameter', __args__, opts=opts, typ=GetSmartclassparameterResult)
    return __ret__.apply(lambda __response__: GetSmartclassparameterResult(
        __meta_=pulumi.get(__response__, '__meta_'),
        id=pulumi.get(__response__, 'id'),
        parameter=pulumi.get(__response__, 'parameter'),
        puppetclass_id=pulumi.get(__response__, 'puppetclass_id')))
